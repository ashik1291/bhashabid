# eval/unit/test_public_api.py
# Verification of top-level 'import bhashabid' Public Python API
import unittest
import bhashabid

class TestBhashabidPublicAPI(unittest.TestCase):
    def test_top_level_repair(self):
        text = "পানির মত সহজ ও পুরষ্কার বিতরণী।"
        repaired, fixes = bhashabid.repair(text)
        self.assertIn("পানির মতো সহজ", repaired)
        self.assertIn("পুরস্কার বিতরণী", repaired)

    def test_top_level_number_formatting(self):
        formatted = bhashabid.format_number("1234567.50")
        self.assertEqual(formatted, "১২,৩৪,৫৬৭.৫০")

        words = bhashabid.format_currency_words(1234567.50)
        self.assertIn("বারো লাখ", words)
        self.assertIn("পয়সা", words)

    def test_top_level_spellcheck(self):
        # Single word typo
        suggs = bhashabid.spellcheck("মনযোগ")
        self.assertIn("মনোযোগ", suggs)

        # Full sentence audit
        issues = bhashabid.spellcheck("তিনি মনযোগ দিয়ে পড়ছেন")
        self.assertIsInstance(issues, list)

    def test_top_level_prosody(self):
        res = bhashabid.verify_payar("মহাভারতের কথা অমৃত সমান।")
        self.assertTrue(res.is_valid_payar)

if __name__ == "__main__":
    unittest.main()
