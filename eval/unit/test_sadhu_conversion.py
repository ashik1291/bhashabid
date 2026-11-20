import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from bhashabid.normalize.repair import repair_text
from bhashabid.normalize.unicode import canonicalize_unicode as canon

# (Sadhu input, expected Promito Cholito) — REQ-026 / REQ-027
CONVERSIONS = [
    ("তিনি বাজারে গিয়াছিলেন এবং মাছ কিনিয়া বাড়ি ফিরিলেন। তাহার পুত্র তখন পড়িতেছিল।",
     "তিনি বাজারে গিয়েছিলেন এবং মাছ কিনে বাড়ি ফিরলেন। তার পুত্র তখন পড়ছিল।"),
    ("তিনি বাজারে গিয়াছিলেন এবং সন্ধ্যায় ফিরিয়া আসিলেন।", "তিনি বাজারে গিয়েছিলেন এবং সন্ধ্যায় ফিরে এলেন।"),
    ("তাহার কথা শুনিয়া সকলে বিস্মিত হইল।", "তার কথা শুনে সকলে বিস্মিত হলো।"),
    ("রাজা ইহা দেখিয়া অত্যন্ত প্রীত হইলেন।", "রাজা এটি দেখে অত্যন্ত প্রীত হলেন।"),
    ("সে বলিল যে সে কাল আসিবে।", "সে বলল যে সে কাল আসবে।"),
    ("তিনি ঢাকা হইতে চট্টগ্রাম গেলেন।", "তিনি ঢাকা থেকে চট্টগ্রাম গেলেন।"),
    ("ইহা সত্য হইতে পারে।", "এটি সত্য হতে পারে।"),
    ("পুলিশ ঘটনাস্থলে পৌঁছিয়াছে।", "পুলিশ ঘটনাস্থলে পৌঁছেছে।"),
    ("তিনি চিঠি পাঠাইলেন।", "তিনি চিঠি পাঠালেন।"),
    ("সে ছবিটি দেখাইয়া বলিল।", "সে ছবিটি দেখিয়ে বলল।"),
    ("আমি ভাত খাইতেছি।", "আমি ভাত খাচ্ছি।"),
    ("তাহারা গান গাহিতেছিল।", "তারা গান গাইছিল।"),
    ("বৃদ্ধ লোকটি লাঠি লইয়া ধীরে ধীরে হাঁটিতে লাগিলেন।", "বৃদ্ধ লোকটি লাঠি নিয়ে ধীরে ধীরে হাঁটতে লাগলেন।"),
    ("সে রাখিয়া দিয়াছে।", "সে রেখে দিয়েছে।"),
    ("শিশুটি হাসিতে লাগিল।", "শিশুটি হাসতে লাগল।"),
]

# Words that look like Sadhu verb forms but are not; must survive conversion untouched.
LOOK_ALIKES = [
    "মোবাইল ফাইলের স্টাইল চলিত রীতিতে লিখিত পরীক্ষা।",
    "সে ছুটিতে বাড়িতে গেল।",
    "চায়ে চিনিতে মিষ্টি বেশি।",
    "তারা কাজ হাসিল করল।",
    "মারিয়া স্কুলে গেল।",
    "ছেলেটি মরিয়া হয়ে চেষ্টা করছে।",
]


class TestSadhuToCholito(unittest.TestCase):

    def test_explicit_conversion(self):
        for src, expected in CONVERSIONS:
            out, fixes = repair_text(src, target_style="cholito")
            self.assertEqual(out, canon(expected), src)
            self.assertFalse(any(f["category"] == "SADHU_UNRESOLVED" for f in fixes), src)

    def test_look_alikes_untouched(self):
        for text in LOOK_ALIKES:
            self.assertEqual(repair_text(text, target_style="cholito")[0], canon(text), text)
            self.assertEqual(repair_text(text)[0], canon(text), text)

    def test_default_preserves_consistent_sadhu(self):
        src = "তাহার কথা শুনিয়া সকলে বিস্মিত হইল।"
        self.assertEqual(repair_text(src)[0], canon(src))


if __name__ == "__main__":
    unittest.main()
