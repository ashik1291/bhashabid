import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import bhashabid
from bhashabid.normalize.lexicon import get_default_lexicon
from bhashabid.normalize.repair import repair_text
from bhashabid.normalize.unicode import canonicalize_unicode as canon

NEWS = ("শুক্রবার সংবাদমাধ্যমকে ইরাওলা বলেন, প্রস্তুতির জন্য আমাদের হাতে কোনো তথ্য নেই। "
        "চলতি সপ্তাহে ম্যানচেস্টারে পৌঁছানোর পর খেলোয়াড়দের নিয়ে কাজ করার সামান্য সময়ই পেয়েছেন চেলসির সাবেক এই কোচ। "
        "২০২৩ সালের পর ঘরের মাঠে তাদের হারাতে পারেনি লিভারপুল। এখানে থাকতে পেরে আমি নিজেকে ভাগ্যবান মনে করি।")


class TestLexiconInflection(unittest.TestCase):
    """Real-world regression (sports news translation, 2026-11-20): inflected words were flagged as
    misspellings and repair rewrote the valid participle পেরে (পারা) into পেড়ে."""

    def test_inflected_forms_are_known(self):
        lex = get_default_lexicon()
        for w in ["বলেন", "হয়েছেন", "ছেড়ে", "পেরে", "প্রস্তুতির", "চেলসির", "পারলে", "পারেনি", "মানিয়ে", "শুনে", "রেখেছেন"]:
            self.assertTrue(lex.is_known(canon(w)), w)

    def test_real_typos_still_flagged(self):
        lex = get_default_lexicon()
        for w in ["পাখী", "আবিস্কার", "দূর্ঘটনা"]:
            self.assertFalse(lex.is_known(canon(w)), w)

    def test_news_paragraph_has_no_spelling_flags_and_repair_keeps_it(self):
        self.assertEqual(bhashabid.spellcheck(NEWS), [])
        self.assertEqual(repair_text(canon(NEWS))[0], canon(NEWS))


if __name__ == "__main__":
    unittest.main()
