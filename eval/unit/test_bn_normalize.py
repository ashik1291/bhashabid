# Exhaustive Unit Tests for bn_normalize
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize import (
    normalize,
    canonicalize_unicode,
    is_nfc_normalized,
    normalize_punctuation,
    normalize_orthography
)

class TestBnNormalize(unittest.TestCase):

    def test_unicode_canonicalization(self):
        # Decomposed য় (য + ়) -> precomposed য় (U+09DF)
        decomposed_yo = "\u09AF\u09BC"
        canonical_yo = "\u09DF"
        self.assertEqual(canonicalize_unicode(decomposed_yo), canonical_yo)

        # Decomposed ড় (ড + ়) -> U+09DC
        decomposed_rra = "\u09A1\u09BC"
        self.assertEqual(canonicalize_unicode(decomposed_rra), "\u09DC")

        # Decomposed ঢ় (ঢ + ়) -> U+09DD
        decomposed_rhha = "\u09A2\u09BC"
        self.assertEqual(canonicalize_unicode(decomposed_rhha), "\u09DD")

        # Mixed sentence
        text = "বইটি ভালো হ" + decomposed_yo + "েছে"
        result = canonicalize_unicode(text)
        self.assertEqual(result, canonicalize_unicode("বইটি ভালো হয়েছে"))
        self.assertIn("\u09DF", result)
        self.assertNotIn(decomposed_yo, result)
        self.assertTrue(is_nfc_normalized(result))

    def test_stray_post_vowel_nukta_reordering(self):
        # ড + া + ় (Nukta typed after vowel sign) must reorder and precompose to ড়া (U+09DC + U+09BE)
        post_vowel_rra = "\u09A1\u09BE\u09BC"
        expected = "\u09DC\u09BE"
        self.assertEqual(canonicalize_unicode(post_vowel_rra), expected)

        # য + ো + ় (Nukta typed after vowel sign ও-কার) -> য়ো (U+09DF + U+09CB)
        post_vowel_yo = "\u09AF\u09CB\u09BC"
        expected_yo = "\u09DF\u09CB"
        self.assertEqual(canonicalize_unicode(post_vowel_yo), expected_yo)

    def test_dari_punctuation_and_decimals(self):
        # ASCII period at end of sentence to Dari
        self.assertEqual(normalize_punctuation("তিনি বাড়ি গেলেন."), "তিনি বাড়ি গেলেন।")
        
        # Decimal numbers must be preserved without replacing period with Dari
        self.assertEqual(normalize_punctuation("পাই এর মান ৩.১৪ প্রায়."), "পাই এর মান ৩.১৪ প্রায়।")
        self.assertEqual(normalize_punctuation("দাম 50.25 টাকা."), "দাম 50.25 টাকা।")

        # Collapse duplicate Daris
        self.assertEqual(normalize_punctuation("তিনি বললেন।।"), "তিনি বললেন।")

    def test_ascii_pipe_and_spacing_normalization(self):
        # Avro/Bijoy ASCII pipe typing normalized to Dari
        self.assertEqual(normalize_punctuation("আমি আজ সচিবালয়ে যাব |"), "আমি আজ সচিবালয়ে যাব।")
        self.assertEqual(normalize_punctuation("তিনি গেলেন|তিনি ফিরলেন"), "তিনি গেলেন। তিনি ফিরলেন")
        self.assertEqual(normalize_punctuation("আজ কি বৃষ্টি হবে?না, হবে না."), "আজ কি বৃষ্টি হবে? না, হবে না।")
        
        # Space after Dari followed by closing quote
        self.assertEqual(
            normalize_punctuation('তিনি বললেন, "ভাত খাব।"তারপরে ঘুমালেন.'),
            'তিনি বললেন, “ভাত খাব।” তারপরে ঘুমালেন।'
        )

        # Markdown tables must be preserved without pipe-to-dari mutation
        table = "| নাম | পদবি |\n| করিম | সচিব |"
        self.assertEqual(normalize_punctuation(table), table)

        # Non-Bengali shell pipes or bitwise operators preserved
        self.assertEqual(normalize_punctuation("cat file.txt | grep foo"), "cat file.txt | grep foo")
        self.assertEqual(normalize_punctuation("flags = a | b"), "flags = a | b")

    def test_url_and_email_preservation_in_punctuation(self):
        url_text = "ওয়েবসাইট ভিজিট করুন https://www.tbsnews.net সাইটে."
        expected_url = "ওয়েবসাইট ভিজিট করুন https://www.tbsnews.net সাইটে।"
        self.assertEqual(normalize_punctuation(url_text), expected_url)

        email_text = "যোগাযোগ: info@bangladesh.gov.bd অথবা help@test.com."
        expected_email = "যোগাযোগ: info@bangladesh.gov.bd অথবা help@test.com।"
        self.assertEqual(normalize_punctuation(email_text), expected_email)

    def test_legacy_opentype_khanda_ta(self):
        # Legacy OpenType Bijoy/Avro ZWJ: ত + ্ + ZWJ (\u09a4\u09cd\u200d)
        legacy_zwj = "\u09a4\u09cd\u200d"
        # Standard decomposed ZWNJ: ত + ্ + ZWNJ (\u09a4\u09cd\u200c)
        legacy_zwnj = "\u09a4\u09cd\u200c"
        self.assertEqual(canonicalize_unicode(legacy_zwj), "ৎ")
        self.assertEqual(canonicalize_unicode(legacy_zwnj), "ৎ")

    def test_bangla_academy_loanword_s(self):
        # Foreign loanwords with S
        text = "তিনি রেলষ্টেশনে গিয়ে ডাকঘরে চিঠি পোষ্ট করলেন এবং মাষ্টারমশাইয়ের সাথে দেখা করলেন।"
        expected = "তিনি রেলস্টেশনে গিয়ে ডাকঘরে চিঠি পোস্ট করলেন এবং মাস্টারমশাইয়ের সাথে দেখা করলেন।"
        self.assertEqual(normalize_orthography(text), expected)

        # Cardinal number 62 (বাষট্টি) must NEVER be altered to বাসট্টি
        self.assertEqual(normalize_orthography("বাষট্টি"), "বাষট্টি")
        self.assertEqual(normalize_orthography("সুভাষ বাষে উঠলেন"), "সুভাষ বাসে উঠলেন")

    def test_tatbhava_short_vowels(self):
        text = "গাছের ডালে পাখী গান গায় এবং বনে হাতী হাঁটে।"
        expected = "গাছের ডালে পাখি গান গায় এবং বনে হাতি হাঁটে।"
        self.assertEqual(normalize_orthography(text), expected)

    def test_tatsama_dual_vowel_standardization(self):
        # Bangla Academy Rule 1.01: Dual-valid Tatsama words must take short-vowel 'ি'
        text = "প্রথম শ্রেণীর কর্মকর্তার পদবী পরিবর্তন করে পল্লী উন্নয়ন বোর্ডের কার্যসূচী নির্ধারণ করা হলো।"
        expected = "প্রথম শ্রেণির কর্মকর্তার পদবি পরিবর্তন করে পল্লি উন্নয়ন বোর্ডের কার্যসূচি নির্ধারণ করা হলো।"
        self.assertEqual(normalize_orthography(text), expected)

    def test_whitespace_compaction(self):
        text = "তিনি    বাড়ি   গেলেন।\n\nনতুন   দিন   শুরু   হলো।"
        expected = canonicalize_unicode("তিনি বাড়ি গেলেন।\n\nনতুন দিন শুরু হলো।")
        self.assertEqual(normalize(text), expected)

    def test_normalize_preserves_markdown_code_blocks(self):
        text = (
            "# হেডার\n\n"
            "এখানে কোড:\n"
            "```python\n"
            "def test():\n"
            '    x = "মান" | 1\n'
            "    return x\n"
            "```\n\n"
            'বাইরের টেক্সট: তিনি   রেলষ্টেশনে   গেলেন. `code_val = "টেস্ট"` ভেরিয়েবল।'
        )
        res = normalize(text)
        # Internal code indentation and symbols must remain untouched
        self.assertIn('def test():\n    x = "মান" | 1\n    return x', res)
        # Inline code must remain untouched
        self.assertIn('`code_val = "টেস্ট"`', res)
        # Outside Bengali should be normalized
        self.assertIn("রেলস্টেশনে", res)
        self.assertIn("গেলেন।", res)

    def test_abbreviation_and_initials_preservation(self):
        cases = [
            ("তিনি ড. মুহাম্মদ ইউনূস.", "তিনি ড. মুহাম্মদ ইউনূস।"),
            ("ডা. এ. কে. খান সাহেব এসেছেন.", "ডা. এ. কে. খান সাহেব এসেছেন।"),
            ("এস. এ. আয়ার এবং টি. এস. এলিয়ট.", "এস. এ. আয়ার এবং টি. এস. এলিয়ট।"),
            ("বইটি (পৃ. ৩৫) দ্রষ্টব্য.", "বইটি (পৃ. ৩৫) দ্রষ্টব্য।"),
            ("শর্তগুলো হলো: ১. প্রথম শর্ত ২. দ্বিতীয় শর্ত.", "শর্তগুলো হলো: ১. প্রথম শর্ত ২. দ্বিতীয় শর্ত।"),
            ("তিনি এম.বি.বি.এস. পাস করেছেন.", "তিনি এম.বি.বি.এস. পাস করেছেন।"),
            ("সার্ভার আইপি ১৯২.১৬৮.১.১ এবং সংস্করণ v1.1.0 প্রস্তুত.", "সার্ভার আইপি ১৯২.১৬৮.১.১ এবং সংস্করণ v1.1.0 প্রস্তুত।")
        ]
        for inp, exp in cases:
            self.assertEqual(normalize_punctuation(inp), exp)

    def test_reph_gemination_and_loanword_generalization(self):
        # Universal Reph gemination elimination
        text_reph = "বর্ত্তমান যুগে কর্ত্তব্য পালন ও কীর্ত্তি অর্জনই সর্ব্বপ্রধান লক্ষ্য। অর্দ্ধেক কাজ শেষ করে মূর্চ্ছা যাওয়া উচিত নয়।"
        exp_reph = "বর্তমান যুগে কর্তব্য পালন ও কীর্তি অর্জনই সর্বপ্রধান লক্ষ্য। অর্ধেক কাজ শেষ করে মূর্ছা যাওয়া উচিত নয়।"
        self.assertEqual(normalize_orthography(text_reph), exp_reph)

        # Initial /æ/ loanword standard
        text_ae = "এ্যাসিড ও এ্যাম্বুলেন্স নিয়ে এ্যাকশন নেওয়া হলো।"
        exp_ae = "অ্যাসিড ও অ্যাম্বুলেন্স নিয়ে অ্যাকশন নেওয়া হলো।"
        self.assertEqual(normalize_orthography(text_ae), exp_ae)

        # Suffix -আবলি
        text_aboli = "নতুন নিয়মাবলী ও শর্তাবলীর আলোকে তথ্যাবলী সংগ্রহ করা হয়েছে।"
        exp_aboli = "নতুন নিয়মাবলি ও শর্তাবলির আলোকে তথ্যাবলি সংগ্রহ করা হয়েছে।"
        self.assertEqual(normalize_orthography(text_aboli), exp_aboli)

if __name__ == "__main__":
    unittest.main()
