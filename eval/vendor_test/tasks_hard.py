"""Hard set V31-V37: long output, many numbers, Bangabda dates, tool-dependent metre, long register conversion.
Checks frozen before any result exists (see CHECK_LOG.md for later changes).
"""
import re

import bhashabid as b
from bhashabid.lint.guru_chandali import find_style_tokens
from tasks import BN, T, has, lacks, word


def nwords(t):
    return len(re.findall(r"[ঀ-৿]+", t))


def payar_all(t, n):
    lines = [l.strip() for l in t.splitlines() if re.search(BN, l)]
    return len(lines) == n and all(
        b.verify_payar(re.sub(r"[।,;!?\-—]", " ", l)).is_valid_payar for l in lines
    )


SADHU_INPUT = (
    "একদা এক গ্রামে এক বৃদ্ধ কৃষক বাস করিত। প্রত্যহ প্রভাতে সে ক্ষেত্রে গমন করিয়া হলকর্ষণ করিত এবং সন্ধ্যায় গৃহে "
    "ফিরিয়া আসিত। তাহার পুত্র নগরে বিদ্যাশিক্ষা করিতেছিল। একদিন বৃদ্ধ শুনিল যে তাহার পুত্র পরীক্ষায় উত্তীর্ণ হইয়াছে। "
    "আনন্দে সে মিষ্টান্ন ক্রয় করিয়া প্রতিবেশীদিগকে বিতরণ করিল। প্রতিবেশীগণ বলিল, \"তোমার পুত্র একদিন বড় মানুষ হইবে।\" "
    "বৃদ্ধ হাসিয়া কহিল, \"আমি কেবল চাহি, সে যেন সৎ থাকে।\""
)

SADHU_FORMS = [r"করিয়া", r"করিত", r"হইয়া", r"হইবে", r"বলিল", r"কহিল", r"তাহার", r"হাসিয়া", r"শুনিল", r"ফিরিয়া"]
CHOLITO_FORMS = [word(w) for w in (
    "করে", "করেছে", "গিয়ে", "দিয়ে", "নিয়ে", "হয়েছে", "হয়েছিল", "বলল", "দেখল", "শুনল", "তার", "তাকে", "তারা", "তাদের",
)]

TASKS_HARD = [
    T("V31", "long_news", "Macroeconomics & Banking",
      "Write a Bengali news report of 200-250 words for a Bangladeshi daily using these facts: "
      "(1) Bangladesh Bank raised the policy rate by 50 basis points to 10 percent. "
      "(2) Inflation was 10.87 percent in October, up from 9.92 percent in September. "
      "(3) Total loan disbursement this quarter was 1234567890 taka. "
      "(4) On Tuesday 17 November 2026 the Executive Committee of the National Economic Council (ECNEC), chaired by the Chief Adviser, "
      "approved 10 projects costing 8425.51 crore taka. "
      "Use Bengali digits, lakh/crore comma grouping for full amounts, the word শতাংশ instead of the % sign, and standard newspaper Cholito. "
      "Output only the report.",
      lambda t: has(t, r"১০\.৮৭\s*শতাংশ", r"৯\.৯২\s*শতাংশ", r"(৮,৪২৫\.৫১|৮৪২৫\.৫১)\s*কোটি", r"(১,২৩,৪৫,৬৭,৮৯০|১২৩\s*কোটি)", r"১৭\s*নভেম্বর")
      and lacks(t, r"%", r"দ্বারা", r"[0-9]", r"[০-৯]{1,3}(?:,[০-৯]{3}){2,}") and 150 <= nwords(t) <= 330),
    T("V32", "bangabda", "Citizen Digital Services & Smart Governance",
      "Convert each Gregorian date to the Bangladesh Bengali-calendar (Bangabda) date, written with Bengali digits and the Bengali month name, one per line: "
      "14 April 2026; 21 February 2026; 15 November 2026; 17 November 2026; 16 December 2026.",
      lambda t: has(t, r"১(লা)?\s*বৈশাখ,?\s*১৪৩৩", r"৮(ই)?\s*ফাল্গুন,?\s*১৪৩২", r"৩০(শে)?\s*কার্তিক,?\s*১৪৩৩",
                    r"২(রা)?\s*অগ্রহায়ণ,?\s*১৪৩৩", r"১(লা)?\s*পৌষ,?\s*১৪৩৩")),
    T("V33", "amounts", "Macroeconomics & Banking",
      "For each amount, write it in Bengali digits with lakh/crore grouping, then in Bengali words followed by টাকা, one per line: "
      "1050; 100000; 2500000; 10000000; 123456789.50; 7005003.",
      lambda t: has(t, r"১,০৫০", r"১,০০,০০০", r"২৫,০০,০০০", r"১,০০,০০,০০০", r"১২,৩৪,৫৬,৭৮৯\.৫০", r"৭০,০৫,০০৩",
                    r"এক হাজার পঞ্চাশ", r"এক (লাখ|লক্ষ)", r"এক কোটি", r"সত্তর (লাখ|লক্ষ) পাঁচ হাজার তিন",
                    r"ছাপ্পান্ন হাজার", r"পঞ্চাশ পয়সা")),
    T("V34", "sadhu_long", "Literary & Language",
      "Write a Bengali short story of at least 150 words about an old ferryman on the river Padma, entirely in consistent Sadhu bhasha "
      "(সাধু ভাষা). Use no Cholito verb or pronoun forms anywhere. Output only the story.",
      lambda t: nwords(t) >= 100 and has(t, r"(করিয়া|হইয়া|করিল|তাহার)") and lacks(t, *CHOLITO_FORMS)),
    T("V35", "payar4", "Classical Poetry & Prosody",
      "Write exactly 4 lines of Bengali verse about the monsoon in Payar metre: every line has 14 akshar split 8+6, rhyming in couplets (AABB). "
      "Output only the four lines.",
      lambda t: payar_all(t, 4)),
    T("V36", "legal_long", "Constitutional Law & Writs",
      "Draft in Bengali the operative prayer of an Article 102 writ petition asking the High Court Division to declare a municipal "
      "demolition order illegal, with separate prayer clauses (ক), (খ), (গ) and (ঘ), following Bangladesh writ practice.",
      lambda t: has(t, r"রুল", r"কেন", r"কর্তৃত্ব", r"\(?ক\)", r"\(?খ\)", r"\(?গ\)", r"\(?ঘ\)")),
    T("V37", "sadhu2cholito_long", "Literary & Language",
      "Rewrite the following passage entirely in standard modern Cholito Bengali, keeping the meaning and the quoted dialogue. "
      "Output only the rewritten passage.\n\n" + SADHU_INPUT,
      lambda t: not find_style_tokens(t)[0] and lacks(t, *SADHU_FORMS) and has(t, r"কৃষক")),
]
