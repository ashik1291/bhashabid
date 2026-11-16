# Unit Test for bhashabid package structure and exports
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import bhashabid
from bhashabid.normalize import normalize, canonicalize_unicode, is_nfc_normalized, normalize_punctuation
from bhashabid.lint import lint_text, check_spelling
from bhashabid.numbers import format_lakh_crore, number_to_bangla_words, format_currency_words
from bhashabid.prosody import scan_line, verify_payar
from bhashabid.legal import generate_writ_prayer

class TestPackageIntegrity(unittest.TestCase):

    def test_top_level_exports(self):
        self.assertTrue(hasattr(bhashabid, "repair"))
        self.assertTrue(hasattr(bhashabid, "normalize"))
        self.assertTrue(hasattr(bhashabid, "lint"))
        self.assertTrue(hasattr(bhashabid, "spellcheck"))
        self.assertTrue(hasattr(bhashabid, "format_number"))
        self.assertTrue(hasattr(bhashabid, "scan_line"))
        self.assertTrue(hasattr(bhashabid, "verify_payar"))

    def test_normalize_execution(self):
        res = bhashabid.normalize("তিনি রেলষ্টেশনে গেলেন |")
        self.assertEqual(res, "তিনি রেলস্টেশনে গেলেন।")

    def test_lint_with_spelling(self):
        issues = bhashabid.lint("তিনি শ্রদ্ধাঞ্জলী জানালেন।", include_spelling=True)
        self.assertTrue(any(i.rule_id == "RULE-LINT-SPELLING" for i in issues))

    def test_numbers_execution(self):
        words = bhashabid.number_to_bangla_words(10050)
        self.assertIn("দশ হাজার", words)
        grouped = bhashabid.format_number(10000000)
        self.assertEqual(grouped, "১,০০,০০,০০০")

    def test_prosody_execution(self):
        line = "মহাভারতের কথা অমৃত সমান"
        analysis = bhashabid.scan_line(line)
        self.assertEqual(analysis.total_morae, 14)

if __name__ == "__main__":
    unittest.main()
