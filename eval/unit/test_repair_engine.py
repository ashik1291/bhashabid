# eval/unit/test_repair_engine.py
# Comprehensive Unit Tests for Deterministic Bengali Linguistic Repair Engine
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.repair import repair_text
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

        # Pleonasm
        repaired_pl, _ = repair_text("তিনি প্রায়শই বিলম্ব করেন।")
        self.assertEqual(repaired_pl, "তিনি প্রায়শ বিলম্ব করেন।")
        self.assertEqual(len(lint_text(repaired_pl)), 0)

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
            ("আমি প্রায়শই সিস্টেম ডিজাইন বিষয়ক আলোচনা দেখি।", "আমি প্রায়শ সিস্টেম ডিজাইন বিষয়ক আলোচনা দেখি।"),
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

    def test_mcp_server_repair_tool(self):
        server = BhashabidMCPServer()
        res = server.call_tool(
            "repair_text",
            {"text": "আদালত জিজ্ঞেস করে একটি রুল জারি করেছে."}
        )
        self.assertIn("repaired", res)
        self.assertIn("রুল নিশি জারি করেছেন।", res["repaired"])
        self.assertGreater(res["fixes_count"], 0)

if __name__ == "__main__":
    unittest.main()
