import json
import os
import sys
import tempfile
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools import learning_loop as L
from tools import sector_sources as S

CATEGORY_HTML = """<div id="mw-pages"><div class="mw-content-ltr"><ul>
<li><a href="/wiki/%E0%A6%AC%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%82%E0%A6%95" title="x">ব্যাংক</a></li>
<li><a href="/wiki/%E0%A6%AC%E0%A6%BF%E0%A6%B7%E0%A6%AF%E0%A6%BC%E0%A6%B6%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%A3%E0%A7%80:X">sub</a></li>
<li><a href="/wiki/%E0%A6%B0%E0%A6%9A%E0%A6%A8%E0%A6%BE:Y">ns</a></li>
</ul></div></div>"""
ARTICLE_HTML = """<div id="mw-content-text"><p>বাংলাদেশ ব্যাংক দেশের কেন্দ্রীয় ব্যাংক।<sup>[১]</sup> এটি ১৯৭১ সালে প্রতিষ্ঠিত হয়।</p>
<p>ছোট।</p><p>English only paragraph that should be ignored entirely.</p></div>"""


class TestSectorSourceParsing(unittest.TestCase):

    def test_category_links_skip_namespaces(self):
        self.assertEqual(S._article_links(CATEGORY_HTML, is_category=True), ["ব্যাংক"])

    def test_sentences_strip_refs_and_noise(self):
        sents = S._sentences(ARTICLE_HTML, 10)
        self.assertEqual(sents, ["বাংলাদেশ ব্যাংক দেশের কেন্দ্রীয় ব্যাংক।", "এটি ১৯৭১ সালে প্রতিষ্ঠিত হয়।"])

    def test_every_sector_source_host_is_registered(self):
        from tools.autonomous_scraper import load_approved_hosts
        hosts = load_approved_hosts()
        for pages in S.SECTOR_SOURCES.values():
            for site, _ in pages:
                self.assertIn(f"bn.{site}.org", hosts)


class TestLearningCycle(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = self.tmp.name
        self.paths = L.LoopPaths(
            drafts_dir=os.path.join(t, "drafts"), learned_dir=os.path.join(t, "learned"),
            rejected_dir=os.path.join(t, "rejected"), lexicon_additions=os.path.join(t, "lex.txt"),
            sadhu_roots=os.path.join(t, "roots.json"), idioms_json=[], terms_md=os.path.join(t, "terms.md"),
            cases_jsonl=os.path.join(t, "cases.jsonl"), rebuild_bundle=False, stop_file=os.path.join(t, "STOP"))
        self.inbox = os.path.join(t, "inbox")
        os.makedirs(self.inbox)
        self.state = os.path.join(t, "scanned.json")
        self.reports = os.path.join(t, "reports")

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, name, rows):
        with open(os.path.join(self.inbox, name), "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    def _cycle(self):
        return L.cycle(input_dirs=[self.inbox], paths=self.paths, state_path=self.state, report_dir=self.reports)

    def test_cycle_tags_sectors_reports_and_scans_only_new_files(self):
        self._write("a.jsonl", [{"text": "ফ্লুরিক্সান প্রযুক্তি ভালো। ফ্লুরিক্সান দ্রুত।", "source": "s1", "sector": "ICT & Software Engineering"}])
        res = self._cycle()
        self.assertEqual(res["new_cards"], 1)
        self.assertEqual(res["new_cards_by_sector"], {"ICT & Software Engineering": 1})
        self.assertTrue(os.path.exists(res["report"]))
        self.assertIn("ICT & Software Engineering", L._read_text(res["report"]))
        self.assertEqual(self._cycle()["files_scanned"], 0)  # unchanged file is not rescanned

    def test_repeat_evidence_merges_into_pending_card(self):
        self._write("a.jsonl", [{"text": "ফ্লুরিক্সান ভালো। ফ্লুরিক্সান দ্রুত।", "source": "s1", "domain": "Macroeconomics & Banking"}])
        self._cycle()
        self._write("b.jsonl", [{"text": "ফ্লুরিক্সান আবার এল। ফ্লুরিক্সান সবখানে।", "source": "s2", "sector": "Healthcare & Epidemiology"}])
        res = self._cycle()
        self.assertEqual(res["new_cards"], 0)
        card = L.list_pending(self.paths)[0]
        self.assertEqual(card["evidence"]["count"], 4)
        self.assertEqual(card["evidence"]["sectors"], ["Healthcare & Epidemiology", "Macroeconomics & Banking"])
        self.assertEqual(card["evidence"]["sources"], ["s1", "s2"])

    def test_prompt_bank_ids_give_sectors(self):
        with open(os.path.join(self.inbox, "claude_run.json"), "w", encoding="utf-8") as f:
            json.dump({"LP19": "ডকার ফ্লুরিক্সান কনটেইনার। ফ্লুরিক্সান চালু হয়।"}, f, ensure_ascii=False)
        res = self._cycle()
        self.assertIn("ICT & Software Engineering", res["new_cards_by_sector"])


if __name__ == "__main__":
    unittest.main()
