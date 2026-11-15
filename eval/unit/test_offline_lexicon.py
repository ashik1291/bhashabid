# eval/unit/test_offline_lexicon.py
# Unit Tests for Offline Deterministic Bengali Lexicon and Spellchecking Engine
import unittest
from tools.bn_normalize.lexicon import (
    BengaliOfflineLexicon,
    get_default_lexicon,
    bengali_edit_distance
)
from tools.mcp_server.server import BhashabidMCPServer

class TestBengaliOfflineLexicon(unittest.TestCase):
    def setUp(self):
        self.lex = get_default_lexicon()

    def test_phonetic_weighted_distance(self):
        # Homophonic pair (স vs ষ) should have lower distance than completely unrelated consonants (স vs ক)
        dist_homophonic = bengali_edit_distance("আবিস্কার", "\u0986\u09ac\u09bf\u09b7\u09cd\u0995\u09be\u09b0")
        dist_unrelated = bengali_edit_distance("আবিস্কার", "আবিক্কার")
        self.assertLess(dist_homophonic, dist_unrelated)

        # ি vs ী should have lower distance than ি vs া
        dist_vowel_homophone = bengali_edit_distance("পাখী", "পাখি")
        dist_vowel_different = bengali_edit_distance("পাখা", "পাখি")
        self.assertLessEqual(dist_vowel_homophone, dist_vowel_different)

    def test_known_and_unknown_words(self):
        self.assertTrue(self.lex.is_known("বাংলাদেশ"))
        self.assertTrue(self.lex.is_known("মনোযোগ"))
        self.assertTrue(self.lex.is_known("পুরস্কার"))
        self.assertFalse(self.lex.is_known("মনযোগ"))
        self.assertFalse(self.lex.is_known("পুরষ্কার"))

    def test_compound_and_affix_recognition(self):
        # Productive compounds and affixes must be recognized as valid words
        compounds = [
            "পরিবেশবান্ধব",
            "তথ্যপ্রযুক্তি",
            "বেআইনি",
            "অপ্রয়োজনীয়"
        ]
        for c in compounds:
            self.assertTrue(self.lex.is_known(c), f"Expected '{c}' to be recognized as a valid compound/affixed word")

    def test_phonetic_spelling_suggestions(self):
        test_cases = [
            ("মনযোগ", "মনোযোগ"),
            ("পুরষ্কার", "পুরস্কার"),
            ("শারীরীক", "শারীরিক"),
            ("আবিস্কার", "\u0986\u09ac\u09bf\u09b7\u09cd\u0995\u09be\u09b0"),
            ("দুরবস্থা", "দুরবস্থা")
        ]
        for typo, expected in test_cases:
            suggs = self.lex.suggest_corrections(typo, max_suggestions=2)
            self.assertTrue(len(suggs) > 0, f"Expected suggestion for {typo}")
            self.assertIn(expected, suggs, f"Expected {expected} in suggestions for {typo}")

    def test_audit_text(self):
        text = "তিনি পুরষ্কার পেয়ে মনযোগ দিয়ে পড়ছেন।"
        issues = self.lex.audit_text(text)
        flagged_words = [i["word"] for i in issues]
        self.assertIn("পুরষ্কার", flagged_words)
        self.assertIn("মনযোগ", flagged_words)

        for issue in issues:
            if issue["word"] == "পুরষ্কার":
                self.assertIn("পুরস্কার", issue["suggestions"])
            if issue["word"] == "মনযোগ":
                self.assertIn("মনোযোগ", issue["suggestions"])

    def test_mcp_spellcheck_tool(self):
        server = BhashabidMCPServer()
        res = server.call_tool("spellcheck_text", {"text": "ছাত্রটি পুরষ্কার পেল।"})
        self.assertIn("issues_count", res)
        self.assertGreater(res["issues_count"], 0)
        self.assertEqual(res["issues"][0]["word"], "পুরষ্কার")
        self.assertIn("পুরস্কার", res["issues"][0]["suggestions"])

if __name__ == "__main__":
    unittest.main()
