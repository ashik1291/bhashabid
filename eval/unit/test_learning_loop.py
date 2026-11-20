import json
import os
import sys
import tempfile
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools import learning_loop as L

DOC = (
    "নতুন প্রকল্পে ফ্লুরিক্সান প্রযুক্তি ব্যবহার করা হয়েছে। ফ্লুরিক্সান খুব দ্রুত কাজ করে।\n"
    "সার্ভারে deployment শেষ হয়েছে।\n"
    "সে গুনিয়াছিল এবং খাতায় লিখে রেখেছে।\n"
)


class TestLearningLoop(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = self.tmp.name
        self.paths = L.LoopPaths(
            drafts_dir=os.path.join(t, "drafts"), learned_dir=os.path.join(t, "learned"),
            rejected_dir=os.path.join(t, "rejected"), lexicon_additions=os.path.join(t, "lex.txt"),
            sadhu_roots=os.path.join(t, "roots.json"), idioms_json=[os.path.join(t, "idioms.json")],
            terms_md=os.path.join(t, "terms.md"), cases_jsonl=os.path.join(t, "cases.jsonl"),
            rebuild_bundle=False, stop_file=os.path.join(t, "STOP"),
        )
        with open(os.path.join(t, "idioms.json"), "w", encoding="utf-8") as f:
            json.dump([{"id": "IDM-001", "english": "x", "flawed_calque": "ক খ", "calque_pattern": "ক\\s+খ",
                        "natural_bengali": "গ", "category": "PROVERB"}], f, ensure_ascii=False)
        self.inbox = os.path.join(t, "inbox")
        os.makedirs(self.inbox)
        with open(os.path.join(self.inbox, "llm_output.txt"), "w", encoding="utf-8") as f:
            f.write(DOC)

    def tearDown(self):
        self.tmp.cleanup()

    def _cards(self):
        return {c["kind"]: c for c in L.list_pending(self.paths)}

    def test_scan_detects_undecidable_cases_and_dedupes(self):
        stats = L.scan([self.inbox], paths=self.paths)
        self.assertGreater(stats["new_cards"], 0)
        cards = self._cards()
        self.assertEqual(cards["lexicon"]["candidate"], "ফ্লুরিক্সান")
        self.assertEqual(cards["lexicon"]["evidence"]["count"], 2)
        self.assertEqual(cards["term"]["candidate"], "deployment")
        self.assertEqual(cards["sadhu_root"]["decision"]["root"], "গুন")
        self.assertTrue(all(c["review"]["status"] == "PENDING_HUMAN_REVIEW" for c in cards.values()))
        self.assertEqual(L.scan([self.inbox], paths=self.paths)["new_cards"], 0)

    def test_approval_requires_reviewer_and_fields(self):
        L.scan([self.inbox], paths=self.paths)
        term = self._cards()["term"]["id"]
        with self.assertRaises(ValueError):
            L.approve(term, "", {"bengali": "ডিপ্লয়মেন্ট"}, paths=self.paths)
        with self.assertRaises(ValueError):
            L.approve(term, "Reviewer", {}, paths=self.paths)  # bengali missing

    def test_apply_distills_only_approved_cards(self):
        L.scan([self.inbox], paths=self.paths)
        cards = self._cards()
        L.approve(cards["lexicon"]["id"], "Reviewer", paths=self.paths)
        L.approve(cards["term"]["id"], "Reviewer", {"bengali": "ডিপ্লয়মেন্ট"}, paths=self.paths)
        L.approve(cards["sadhu_root"]["id"], "Reviewer", paths=self.paths)
        idiom_src = next(c for k, c in cards.items() if k not in ("lexicon", "term", "sadhu_root")) if len(cards) > 3 else None

        report = L.apply_approved(self.paths)
        self.assertEqual(len(report["applied"]), 3)
        self.assertIn("ফ্লুরিক্সান", L._read_text(self.paths.lexicon_additions))
        self.assertIn("- deployment → ডিপ্লয়মেন্ট", L._read_text(self.paths.terms_md))
        self.assertEqual(L._read_json(self.paths.sadhu_roots), ["গুন"])
        cases = [json.loads(line) for line in L._read_text(self.paths.cases_jsonl).splitlines()]
        self.assertEqual(len(cases), 3)
        self.assertEqual(len(os.listdir(self.paths.learned_dir)), 3)
        # Unapproved cards stay pending and untouched.
        self.assertTrue(all(c["review"]["status"] == "PENDING_HUMAN_REVIEW" for c in L.list_pending(self.paths)))
        if idiom_src:
            self.assertIn(idiom_src["id"], report["pending"] + report["manual"])

    def test_idiom_and_reject(self):
        L.scan([self.inbox], paths=self.paths)
        term = self._cards()["term"]["id"]
        L.approve(term, "Reviewer", {"action": "add_idiom", "english": "At the end of the day",
                                     "flawed_calque": "দিনের শেষে বলতে গেলে", "natural_bengali": "চূড়ান্ত বিচারে"},
                  paths=self.paths)
        L.apply_approved(self.paths)
        items = L._read_json(self.paths.idioms_json[0])
        self.assertEqual(items[-1]["id"], "IDM-002")
        self.assertEqual(items[-1]["calque_pattern"], "দিনের\\s+শেষে\\s+বলতে\\s+গেলে")

        lex = self._cards()["lexicon"]["id"]
        L.reject(lex, "Reviewer", "brand name", paths=self.paths)
        self.assertTrue(os.path.exists(os.path.join(self.paths.rejected_dir, f"{lex}.yaml")))
        L.scan([self.inbox], paths=self.paths)
        self.assertNotIn(lex, [c["id"] for c in L.list_pending(self.paths)])

    def test_agent_suggestion_then_human_accepts(self):
        L.scan([self.inbox], paths=self.paths)
        term = self._cards()["term"]["id"]
        L.suggest(term, "gemini-2.5-pro", {"bengali": "ডিপ্লয়মেন্ট"}, "standard loanword", "high", paths=self.paths)
        card = self._cards()["term"]
        self.assertEqual(card["review"]["status"], "PENDING_HUMAN_REVIEW")  # suggestion never approves
        self.assertEqual(card["llm_suggestion"]["by"], "gemini-2.5-pro")
        L.approve(term, "Ashikur Rahman Bhuiyan", accept_suggestion=True, paths=self.paths)
        self.assertTrue(self._cards()["term"]["review"]["accepted_llm_suggestion"])
        self.assertEqual(L.status(self.paths)["approved_not_applied"], 1)

    def test_models_cannot_approve_or_reject(self):
        L.scan([self.inbox], paths=self.paths)
        lex = self._cards()["lexicon"]["id"]
        for name in ("Claude Opus", "gemini-2.5-pro", "GPT-4o", "AI reviewer", "assistant"):
            with self.assertRaises(ValueError):
                L.approve(lex, name, paths=self.paths)
            with self.assertRaises(ValueError):
                L.reject(lex, name, paths=self.paths)

    def test_suggestion_must_be_complete_and_reject_suggestion_not_auto_approved(self):
        L.scan([self.inbox], paths=self.paths)
        term = self._cards()["term"]["id"]
        with self.assertRaises(ValueError):
            L.suggest(term, "claude", {}, paths=self.paths)  # bengali missing
        L.suggest(term, "claude", {"action": "reject"}, "brand name", paths=self.paths)
        with self.assertRaises(ValueError):
            L.approve(term, "Ashikur Rahman Bhuiyan", accept_suggestion=True, paths=self.paths)

    def test_kill_switch(self):
        open(self.paths.stop_file, "w").close()
        with self.assertRaises(RuntimeError):
            L.scan([self.inbox], paths=self.paths)
        with self.assertRaises(RuntimeError):
            L.apply_approved(self.paths)


if __name__ == "__main__":
    unittest.main()
