# eval/unit/test_repair_engine.py
# Comprehensive Unit Tests for Deterministic Bengali Linguistic Repair Engine
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.repair import repair_text
from tools.bn_normalize.unicode import canonicalize_unicode
from tools.bn_lint import lint_text
from tools.mcp_server.server import BhashabidMCPServer

class TestRepairEngine(unittest.TestCase):

    def test_calque_naturalization(self):
        cases = [
            ("সৌরবিদ্যুৎ দ্বারা চালিত পাম্প", "সৌরবিদ্যুৎ পরিচালিত পাম্প"),
            ("আদালত জিজ্ঞেস করে একটি রুল জারি করেছে", "আদালত রুল নিশি জারি করেছেন"),
            ("পেপারটি তর্ক করে যে উন্নয়ন আবশ্যক।", "গবেষণাপত্রে যুক্তি উপস্থাপন করা হয়েছে যে উন্নয়ন আবশ্যক।"),
            ("উপকূলে ১০ নম্বর বড় বিপদের সংকেত দেখানো হয়েছে।", "উপকূলে ১০ নম্বর মহাবিপদ সংকেত দেখানো হয়েছে।"),
            ("জমির বিক্রির কাগজ হস্তান্তর করা হলো।", "জমির সাফ-কবলা বিক্রয় দলিল হস্তান্তর করা হলো।"),
            ("ফসলে ক্ষতিকর পোকা মারার ওষুধ দেওয়া হয়েছে।", "ফসলে ক্ষতিকর বালাইনাশক দেওয়া হয়েছে।")
        ]
        for raw, expected in cases:
            repaired, fixes = repair_text(raw)
            self.assertIn(expected, repaired)
            self.assertGreater(len(fixes), 0)
            # Ensure post-repair lint issues are 0
            issues = lint_text(repaired)
            self.assertEqual(len(issues), 0, f"Residual defects found in repaired text: {repaired}")

    def test_guru_chandali_harmonization(self):
        raw = "উদ্দীপকটি পড়িয়া নিচের প্রশ্নগুলোর উত্তর দাও।"
        repaired, fixes = repair_text(raw)
        self.assertIn("উদ্দীপকটি পড়ে নিচের প্রশ্নগুলোর উত্তর দাও", repaired)
        self.assertTrue(any(f["category"] == "GURU_CHANDALI_HARMONIZATION" for f in fixes))
        issues = lint_text(repaired)
        self.assertEqual(len(issues), 0)

    def test_honorific_concordance_repair(self):
        # Tini (honorific) + ordinary verb
        raw_tini = "তিনি কাল ঢাকা গেল।"
        repaired_tini, fixes_tini = repair_text(raw_tini)
        self.assertIn("তিনি কাল ঢাকা গেলেন", repaired_tini)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_tini))
        self.assertEqual(len(lint_text(repaired_tini)), 0)

        # Se (ordinary) + honorific verb
        raw_se = "সে বললেন যে কাল আসবে।"
        repaired_se, fixes_se = repair_text(raw_se)
        self.assertIn("সে বলল যে কাল আসবে", repaired_se)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_se))
        self.assertEqual(len(lint_text(repaired_se)), 0)

        # Apni (formal) + familiar verb
        raw_apni = "আপনি কাজটি করো।"
        repaired_apni, fixes_apni = repair_text(raw_apni)
        self.assertIn("আপনি কাজটি করেন", repaired_apni)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_apni))

        # Tumi (familiar) + formal verb
        raw_tumi = "তুমি সিদ্ধান্ত নেন।"
        repaired_tumi, fixes_tumi = repair_text(raw_tumi)
        self.assertIn("তুমি সিদ্ধান্ত নাও", repaired_tumi)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_tumi))

    def test_first_person_concordance_repair(self):
        # Ami (1st person) + honorific verb -> Ami + 1st person verb
        raw_ami = "আমি কাজটি করবেন না।"
        repaired_ami, fixes_ami = repair_text(raw_ami)
        self.assertIn("আমি কাজটি করব না।", repaired_ami)
        self.assertTrue(any(f["category"] == "PERSON_CONCORDANCE" for f in fixes_ami))
        self.assertEqual(len(lint_text(repaired_ami)), 0)

        # Tumi + 1st person verb -> Tumi + 2nd person verb
        raw_tumi = "তুমি কাজটি করলাম।"
        repaired_tumi, fixes_tumi = repair_text(raw_tumi)
        self.assertIn("তুমি কাজটি করলে।", repaired_tumi)
        self.assertTrue(any(f["category"] == "PERSON_CONCORDANCE" for f in fixes_tumi))
        self.assertEqual(len(lint_text(repaired_tumi)), 0)

        # Apni + 1st person verb -> Apni + formal verb
        raw_apni = "আপনি চিঠি লিখলাম।"
        repaired_apni, fixes_apni = repair_text(raw_apni)
        self.assertIn("আপনি চিঠি লিখলেন।", repaired_apni)
        self.assertTrue(any(f["category"] == "PERSON_CONCORDANCE" for f in fixes_apni))
        self.assertEqual(len(lint_text(repaired_apni)), 0)

        # Se / Tara + 1st person verb -> Se / Tara + ordinary verb
        raw_se = "সে কাজটি করলাম।"
        repaired_se, fixes_se = repair_text(raw_se)
        self.assertIn("সে কাজটি করল।", repaired_se)
        self.assertTrue(any(f["category"] == "PERSON_CONCORDANCE" for f in fixes_se))
        self.assertEqual(len(lint_text(repaired_se)), 0)

        # Tini + 1st person verb -> Tini + honorific verb
        raw_tini = "তিনি কাজটি করলাম।"
        repaired_tini, fixes_tini = repair_text(raw_tini)
        self.assertIn("তিনি কাজটি করলেন।", repaired_tini)
        self.assertTrue(any(f["category"] == "PERSON_CONCORDANCE" for f in fixes_tini))
        self.assertEqual(len(lint_text(repaired_tini)), 0)

    def test_grammar_defect_repairs(self):
        # Double plurals
        repaired_dp, _ = repair_text("সব ছাত্রগণ ক্লাসে উপস্থিত ছিল।")
        self.assertEqual(repaired_dp, "সব ছাত্র ক্লাসে উপস্থিত ছিল।")
        self.assertEqual(len(lint_text(repaired_dp)), 0)

        repaired_dp2, _ = repair_text("সকল শিক্ষকগণ উপস্থিত ছিলেন।")
        self.assertEqual(repaired_dp2, "সকল শিক্ষক উপস্থিত ছিলেন।")
        self.assertEqual(len(lint_text(repaired_dp2)), 0)

        repaired_dp3, _ = repair_text("সব বইসমূহ লাইব্রেরিতে আছে।")
        self.assertEqual(repaired_dp3, "সব বই লাইব্রেরিতে আছে।")
        self.assertEqual(len(lint_text(repaired_dp3)), 0)

        # Pleonasm
        repaired_pl, _ = repair_text("তিনি প্রায়শই বিলম্ব করেন।")
        # প্রায়শই is widely accepted; the lint rule is advisory and repair must not rewrite it
        from bhashabid.normalize.unicode import canonicalize_unicode as _canon
        self.assertEqual(_canon(repaired_pl), _canon("তিনি প্রায়শই বিলম্ব করেন।"))
        self.assertTrue(any(x.rule_id == "RULE-GRAMMAR-PLEONASM" for x in lint_text(repaired_pl)))

        repaired_km, _ = repair_text("তিনি কেবলমাত্র সত্য বলতেন।")
        self.assertEqual(repaired_km, "তিনি কেবল সত্য বলতেন।")
        self.assertEqual(len(lint_text(repaired_km)), 0)

        # Affix defect
        repaired_affix, _ = repair_text("তারা একত্রিত হয়ে সিদ্ধান্ত নিল।")
        self.assertEqual(repaired_affix, "তারা একত্র হয়ে সিদ্ধান্ত নিল।")
        self.assertEqual(len(lint_text(repaired_affix)), 0)

        # Day name, word boundary, pronoun
        repaired_rob, _ = repair_text("আগামী রবিবার ব্যাংক বন্ধ থাকবে।")
        self.assertEqual(repaired_rob, "আগামী রোববার ব্যাংক বন্ধ থাকবে।")
        self.assertEqual(len(lint_text(repaired_rob)), 0)

        repaired_ech, _ = repair_text("এছাড়া অন্যান্য সিদ্ধান্ত বাস্তবায়িত হবে।")
        self.assertEqual(repaired_ech, "এ ছাড়া অন্যান্য সিদ্ধান্ত বাস্তবায়িত হবে।")
        self.assertEqual(len(lint_text(repaired_ech)), 0)

    def test_idempotence_and_clean_text(self):
        clean_text = "তিনি প্রতিদিন সকালে বিদ্যালয়ে যান এবং পাঠদান করেন।"
        repaired, fixes = repair_text(clean_text)
        self.assertEqual(repaired, clean_text)
        self.assertEqual(len(fixes), 0)

    def test_grammar_defect_and_pleonasm_repairs(self):
        cases = [
            ("বিভিন্ন সার্ভিসকে একত্রিত করে একটি কাঠামো গড়ে তোলা।", "বিভিন্ন সার্ভিসকে একত্র করে একটি কাঠামো গড়ে তোলা।"),
            ("প্রকৌশলীরা যেসব সমস্যার মুখোমুখি হন, তার সমাধানের জন্য এটি উপযোগী।", "প্রকৌশলীরা যেসব সমস্যার মুখোমুখি হন, সেগুলোর সমাধানের জন্য এটি উপযোগী।"),
            ("রবিবার তারা মিছিল করে। এছাড়া কারো কারো মাথায় হেলমেট ছিল।", "রোববার তারা মিছিল করে। এ ছাড়া কারও কারও মাথায় হেলমেট ছিল।"),
            ("উপরোক্ত বিষয়ে সকল সদস্যবৃন্দ অবগত আছেন।", "উপরি-উক্ত বিষয়ে সকল সদস্য অবগত আছেন।"),
            ("নিরাপত্তার সর্বোত্তম অনুশীলনগুলো মেনে চলা আবশ্যক।", "নিরাপত্তার সর্বোত্তম চর্চা মেনে চলা আবশ্যক।")
        ]
        for raw, expected in cases:
            repaired, fixes = repair_text(raw)
            self.assertIn(expected, repaired)
            self.assertTrue(len(fixes) > 0)

    def test_orthography_reph_and_affix_repairs(self):
        cases = [
            ("ধর্ম্ম ও কার্য্যক্ষেত্রে তাঁর অবদান অপরিসীম।", "ধর্ম ও কার্যক্ষেত্রে তাঁর অবদান অপরিসীম।"),
            ("এযাবৎ বিভিন্ন প্রতিযোগীতা ও সহযোগীতামূলক কর্মসূচি হয়েছে।", "এ যাবৎ বিভিন্ন প্রতিযোগিতা ও সহযোগিতামূলক কর্মসূচি হয়েছে।"),
            ("তিনি প্রথম পুরষ্কার পেয়ে মনযোগ দিয়ে পড়ছেন।", "তিনি প্রথম পুরস্কার পেয়ে মনোযোগ দিয়ে পড়ছেন।")
        ]
        for raw, expected in cases:
            repaired, fixes = repair_text(raw)
            self.assertIn(expected, repaired)
            self.assertTrue(len(fixes) > 0)

    def test_context_aware_moto_and_lexicon_repairs(self):
        # 1. Similarity 'মত' should become 'মতো'
        sim_text = "পানির মত সহজ ও ফুলের মত সুন্দর।"
        repaired_sim, fixes_sim = repair_text(sim_text)
        self.assertIn("পানির মতো সহজ ও ফুলের মতো সুন্দর", repaired_sim)

        # 2. Opinion 'মত' should stay intact
        op_text = "আমার মত হলো এই সিদ্ধান্ত সঠিক নয়।"
        repaired_op, fixes_op = repair_text(op_text)
        self.assertIn("আমার মত হলো", repaired_op)

        # 3. Offline lexicon high-confidence repair
        lex_typo_text = "সেখানে কোনো দূর্ঘটনা ঘটেনি।"
        repaired_lex, fixes_lex = repair_text(lex_typo_text)
        self.assertIn("কোনো দুর্ঘটনা ঘটেনি", repaired_lex)
        self.assertTrue(any(f["category"] == "ORTHOGRAPHY_PHONETIC" for f in fixes_lex))

    def test_ambiguous_proverbs_preserved_literally(self):
        # Literal contexts must NOT be mutated by repair()
        literal_cake = "টেবিলে একটি কেকের টুকরো আছে।"
        repaired_cake, fixes_cake = repair_text(literal_cake)
        self.assertEqual(repaired_cake, literal_cake)
        self.assertEqual(len(fixes_cake), 0)

        literal_hunter = "শিকারি ঝোপের চারপাশে পেটাচ্ছিলেন।"
        repaired_hunter, fixes_hunter = repair_text(literal_hunter)
        self.assertEqual(repaired_hunter, literal_hunter)
        self.assertEqual(len(fixes_hunter), 0)

        # But linter MUST flag them as potential calques
        issues = lint_text(literal_cake)
        self.assertTrue(any("কেকের টুকরো" in i.matched_text for i in issues))

    def test_contextual_idiom_calque_repairs(self):
        # 1. Non-literal context repaired
        raw_idiom = "এই কাজটা কোনো কেকের টুকরো নয়।"
        repaired, _ = repair_text(raw_idiom)
        self.assertEqual(repaired, "এই কাজটা কোনো সহজ কাজ নয়।")
        self.assertEqual(len(lint_text(repaired)), 0)

        # 2. Literal food preserved untouched
        raw_literal = "টেবিলে একটি কেকের টুকরো আছে।"
        repaired_lit, _ = repair_text(raw_literal)
        self.assertEqual(repaired_lit, raw_literal)

        # 3. Bad workman proverb repaired
        raw_workman = "দিনের শেষে, একজন খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়।"
        repaired_wm, _ = repair_text(raw_workman)
        self.assertIn("নাচতে না জানলে উঠান বাঁকা", repaired_wm)
        self.assertEqual(len(lint_text(repaired_wm)), 0)

    def test_mcp_server_repair_tool(self):
        server = BhashabidMCPServer()
        res = server.call_tool(
            "repair_text",
            {"text": "আদালত জিজ্ঞেস করে একটি রুল জারি করেছে."}
        )
        self.assertIn("repaired", res)
        self.assertIn("রুল নিশি জারি করেছেন।", res["repaired"])
        self.assertGreater(res["fixes_count"], 0)

    def test_markdown_code_block_preservation(self):
        raw_markdown = (
            "# ডেভেলপার নির্দেশিকা\n\n"
            "নিচের ফাংশনটি দেখুন:\n"
            "```python\n"
            "def compute_mask():\n"
            '    # এই কাজটা কোনো কেকের টুকরো নয়\n'
            '    flag = "টেস্ট" | 0x01\n'
            "    return flag\n"
            "```\n\n"
            'বাহিরের বাংলা লেখা: এই কাজটা কোনো কেকের টুকরো নয়। এছাড়াও `user_name = "করিম"` ভেরিয়েবল দেখুন।'
        )
        repaired, fixes = repair_text(raw_markdown)
        # 1. Code block internal syntax must remain 100% byte-for-byte identical
        self.assertIn('def compute_mask():\n    # এই কাজটা কোনো কেকের টুকরো নয়\n    flag = "টেস্ট" | 0x01\n    return flag', repaired)
        # 2. Inline code span must remain identical
        self.assertIn('`user_name = "করিম"`', repaired)
        # 3. Outer prose must be properly naturalized
        self.assertIn("বাহিরের বাংলা লেখা: এই কাজটা কোনো সহজ কাজ নয়।", repaired)

    def test_mcp_server_markdown_code_safety(self):
        server = BhashabidMCPServer()
        raw = "```python\nval = 1 | 2\n```\nএই কাজটা কোনো কেকের টুকরো নয়."
        res = server.call_tool("repair_text", {"text": raw})
        self.assertIn("val = 1 | 2", res["repaired"])
        self.assertIn("সহজ কাজ নয়।", res["repaired"])

    def test_expanded_bilingual_idioms_repair(self):
        cases = [
            ("তিনি বললেন সততা হলো সেরা নীতি।", "সততাই সর্বোত্তম পন্থা"),
            ("কাজ শব্দের চেয়ে জোরে কথা বলে।", "কথার চেয়ে কাজের মূল্য বেশি"),
            ("খালি পাত্র বেশি শব্দ করে।", "খালি কলসি বাজে বেশি"),
            ("হীরা হীরাকে কাটে।", "সেয়ানে সেয়ানে কোলাকুলি"),
        ]
        for raw, expected in cases:
            repaired, fixes = repair_text(raw)
            self.assertIn(expected, repaired)
            self.assertGreater(len(fixes), 0)
            self.assertEqual(len(lint_text(repaired)), 0, f"Residual defects in repaired idiom: {repaired}")

    def test_natural_bengali_proverbs_not_flagged(self):
        # Natural or fully naturalised Bengali sayings must not be treated as calques.
        for text in ["যা চকচক করে সবই সোনা নয়।", "রোম একদিনে তৈরি হয়নি।", "খবরের দিকে চোখ রাখুন।",
                     "ডুবন্ত মানুষ খড়কুটো আঁকড়ে ধরে।", "চায়ের কাপে ঝড় তুলেছে বিষয়টি।"]:
            self.assertEqual(repair_text(text)[0], canonicalize_unicode(text), text)
            self.assertFalse(any(i.rule_id == "RULE-LINT-CALQUE" for i in lint_text(text)), text)

    def test_skill_idioms_md_in_sync_with_engine(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "build_skill_bundle", os.path.join(REPO_ROOT, "scripts", "build_skill_bundle.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        expected = mod.render_idioms_md()
        for path in mod.IDIOMS_MD_PATHS:
            with open(path, encoding="utf-8") as f:
                self.assertEqual(f.read(), expected, f"{path} is stale; run scripts/build_skill_bundle.py")

    def test_abbreviation_and_reph_end_to_end(self):
        raw = "ড. মুহাম্মদ ইউনূস ও ডা. এ. কে. খান সাহেবকে (পৃ. ৩০-৩৫) স্মরণ করা হলো."
        repaired, fixes = repair_text(raw)
        self.assertEqual(repaired, "ড. মুহাম্মদ ইউনূস ও ডা. এ. কে. খান সাহেবকে (পৃ. ৩০-৩৫) স্মরণ করা হলো।")

        raw_reph = "বর্ত্তমান যুগে কর্ত্তব্য পালন আবশ্যক."
        repaired_reph, _ = repair_text(raw_reph)
        self.assertEqual(repaired_reph, "বর্তমান যুগে কর্তব্য পালন আবশ্যক।")

if __name__ == "__main__":
    unittest.main()


class TestAutoRepairSafety(unittest.TestCase):
    """Regression cases from the Wikipedia false-positive audit (2026-11-21)."""

    def _canon(self, t):
        from bhashabid.normalize.unicode import canonicalize_unicode
        return canonicalize_unicode(t)

    def test_lexical_identity_words_and_names_untouched(self):
        for text in ["চারা রোপণের জন্য গর্ত খোড়া হয়।", "নেত্রকোণা জেলা।", "তৌকির আহমেদ এলেন।"]:
            self.assertEqual(self._canon(repair_text(text)[0]), self._canon(text))

    def test_short_vowel_and_known_typo_still_repaired(self):
        self.assertEqual(self._canon(repair_text("সে খুশী হল।")[0]), self._canon("সে খুশি হল।"))
        self.assertEqual(self._canon(repair_text("আবিস্কৃত")[0]), self._canon("আবিষ্কৃত"))

    def test_no_devanagari_in_output(self):
        import re
        self.assertEqual(self._canon(repair_text("আবিস্কার")[0]), self._canon("আবিষ্কার"))
        self.assertIsNone(re.search("[ऀ-ॿ]", repair_text("আবিস্কার")[0]))

    def test_valid_long_initial_vowel_numerals_untouched(self):
        for w in ["ঊননব্বই", "ঊনপঞ্চাশ", "ঊনিশ"]:
            self.assertEqual(self._canon(repair_text(w)[0]), self._canon(w))
