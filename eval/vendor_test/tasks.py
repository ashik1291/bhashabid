"""Frozen task set for manual multi-vendor testing.

Checks were written BEFORE any vendor output was collected. Do not edit a check after
results exist; add a new task instead. Tasks with check=None are human-rating only.
convention=True marks checks that encode a Bhashabid/Bangladesh-standard convention
(not a universal truth); they are reported separately so they cannot inflate the headline.
"""
import os
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import bhashabid as b
from bhashabid.normalize.unicode import canonicalize_unicode as canon
from bhashabid.lint.guru_chandali import find_style_tokens

BN = r"[ঀ-৿]"


def has(t, *pats):
    return all(re.search(canon(p), t) for p in pats)


def lacks(t, *pats):
    return not any(re.search(canon(p), t) for p in pats)


def word(w):
    return r"(?<!" + BN + r")" + w + r"(?!" + BN + r")"


def payar_ok(t):
    lines = [l.strip() for l in t.splitlines() if re.search(BN, l)]
    return len(lines) >= 2 and all(
        b.verify_payar(re.sub(r"[।,;!?\-—]", " ", l)).is_valid_payar for l in lines[:2]
    )


def T(id, cat, sector, prompt, check=None, convention=False):
    return dict(id=id, cat=cat, sector=sector, prompt=prompt, check=check, convention=convention)


TASKS = [
    T("V01", "numerals", "Macroeconomics & Banking",
      "Write the amount 2500000 taka in Bengali digits using South Asian lakh/crore comma grouping, then in Bengali words.",
      lambda t: has(t, r"২৫,০০,০০০", r"পঁচিশ (লাখ|লক্ষ)")),
    T("V02", "numerals", "Macroeconomics & Banking",
      "Write the number 123456789 in Bengali digits using South Asian lakh/crore comma grouping, then in Bengali words.",
      lambda t: has(t, r"১২,৩৪,৫৬,৭৮৯", r"বারো কোটি", r"ছাপ্পান্ন হাজার")),
    T("V03", "numerals", "Education & NCTB Pedagogy",
      "Give the Bengali ordinal words (as full words, not digits) for 1st, 2nd, 3rd, 4th, 5th and 10th.",
      lambda t: has(t, r"প্রথম", r"দ্বিতীয়", r"তৃতীয়", r"চতুর্থ", r"পঞ্চম", r"দশম")),
    T("V04", "numerals", "Education & NCTB Pedagogy",
      "Write the decimal 3.75 in Bengali words, as it would be read aloud.",
      lambda t: has(t, r"তিন দশমিক (সাত পাঁচ|পঁচাত্তর)") and lacks(t, r"সাড়ে\s*তিন দশমিক")),
    T("V05", "numerals", "Culinary & Daily Life",
      "Write in Bengali: \"Add 3.5 cups of rice and cook for 4.5 hours.\" Use natural Bengali words for the fractional amounts.",
      lambda t: has(t, r"সাড়ে তিন", r"সাড়ে চার")),
    T("V06", "dates", "Mass Media & Digital Journalism",
      "In Bengali, write the date 21 February 2026 (Gregorian; Bengali digits, Bengali month name) and say it is International Mother Language Day.",
      lambda t: has(t, r"২১\s*ফেব্রুয়ারি,?\s*২০২৬", r"মাতৃভাষা")),
    T("V07", "dates", "Citizen Digital Services & Smart Governance",
      "Pohela Boishakh 1433 falls on 14 April 2026. In Bengali, state the Bengali-calendar date of 15 April 2026, using Bengali digits.",
      lambda t: has(t, r"২\s*বৈশাখ", r"১৪৩৩")),
    T("V08", "dates", "Customer Support & Conversational Chat",
      "Write the times 3:45 PM and 2:30 PM the way they are spoken in natural Bengali.",
      lambda t: has(t, r"পৌনে\s*চার", r"আড়াই")),
    T("V09", "dates", "Mass Media & Digital Journalism",
      "Write the date 16 December 2026 in Bengali (Bengali digits, Bengali month name) and say it is Victory Day (Bijoy Dibosh).",
      lambda t: has(t, r"১৬\s*ডিসেম্বর", r"বিজয় দিবস")),
    T("V10", "calque", "Translation & Calque Naturalization",
      "Translate into natural Bengali newspaper prose: \"The report was prepared by the committee and is characterised by delays.\"",
      lambda t: lacks(t, r"দ্বারা")),
    T("V11", "calque", "Translation & Calque Naturalization",
      "Translate into natural Bengali: \"It was raining cats and dogs, so the match was called off.\"",
      lambda t: lacks(t, r"বিড়াল", r"কুকুর")),
    T("V12", "calque", "Translation & Calque Naturalization",
      "Translate into natural Bengali: \"He kicked the bucket last year.\"",
      lambda t: lacks(t, r"বালতি") and has(t, r"(মারা|প্রয়াত|মৃত্যু|গত হয়েছেন)")),
    T("V13", "calque", "Sports Journalism",
      "Write a 2-sentence Bengali cricket report: Bangladesh lost to India by 5 wickets. Use Bengali digits.",
      lambda t: has(t, r"৫\s*উইকেটে", r"(হেরে|হেরেছে|হার)") and lacks(t, r"পরাজিত করা হয়")),
    T("V14", "calque", "Macroeconomics & Banking",
      "Write a 2-sentence Bengali news line: inflation rose to 9.5 percent in October, mainly driven by food prices. Use Bengali digits.",
      lambda t: has(t, r"৯\.৫\s*শতাংশ") and lacks(t, r"%", r"দ্বারা")),
    T("V15", "sadhu_cholito", "Literary & Language",
      "Rewrite in standard modern Cholito Bengali: \"সে গৃহে গমন করিয়া ভোজন করিল এবং নিদ্রা গেল।\"",
      lambda t: not find_style_tokens(t)[0] and lacks(t, r"করিয়া", r"করিল", r"গমন")),
    T("V16", "sadhu_cholito", "Literary & Language",
      "Rewrite in standard modern Cholito Bengali: \"তিনি বলিলেন যে আমি আসিব না।\"",
      lambda t: has(t, r"(বললেন|বলেছেন)", r"আসব না") and lacks(t, r"বলিলেন", r"আসিব")),
    T("V17", "sadhu_cholito", "Literary & Language",
      "Rewrite in consistent Sadhu bhasha (no Cholito forms): \"সে বাড়ি গিয়ে ভাত খেল এবং ঘুমাল।\"",
      lambda t: has(t, r"(গিয়া|গমন করিয়া)", r"(খাইল|ভোজন করিল|আহার করিল)") and lacks(t, r"গিয়ে", word("খেল"))),
    T("V18", "register", "Customer Support & Conversational Chat",
      "Write 2 Bengali sentences to a customer (address them as আপনি) saying refund REF-7781 will arrive within 3 working days. Use Bengali digits for the number of days.",
      lambda t: "REF-7781" in t and lacks(t, word("তুমি"), word("তোমার"))),
    T("V19", "register", "Creative Fiction & Dialogue",
      "Write a 4-line Bengali dialogue: a 14-year-old boy first talks to his best friend using তুই, then to his headmaster using আপনি.",
      lambda t: has(t, word("তুই")) and has(t, word("আপনি"))),
    T("V20", "register", "Education & NCTB Pedagogy",
      "Write 4 Bengali sentences about a respected teacher who retired after 30 years, referring to the teacher with the honorific তিনি throughout (never সে).",
      lambda t: has(t, word("তিনি")) and lacks(t, word("সে"))),
    T("V21", "official", "Administrative Governance & Memos",
      "Write a short formal Bengali leave application to a school headmaster for 3 days of sick leave, in standard Bangladeshi application format.",
      lambda t: has(t, r"(বরাবর|সবিনয়)", r"বিষয়") and lacks(t, r"প্রিয় মহাশয়")),
    T("V22", "official", "Administrative Governance & Memos",
      "Write the opening two lines of an official Bangladesh government memo conveying approval of a development project. Use standard Bangladeshi secretariat wording.",
      None),
    T("V23", "official", "Constitutional Law & Writs",
      "In Bengali, write how a High Court Division bench issues a Rule Nisi asking why a government order should not be declared illegal.",
      lambda t: has(t, r"রুল", r"কেন", r"(জানতে চেয়ে|কারণ দর্শা)")),
    T("V24", "official", "Land Conveyancing & Deeds",
      "Write in Bengali the standard operative clause of a sale deed stating that the seller transfers a plot of land to the buyer for 500000 taka. Use Bengali digits with lakh grouping.",
      lambda t: has(t, r"(বিক্রয়|কবলা)", r"(৫,০০,০০০|পাঁচ (লাখ|লক্ষ))")),
    T("V25", "official", "Healthcare & Epidemiology",
      "Write Bengali patient instructions: take 1 tablet of 250 mg three times a day after meals for 5 days. Use Bengali digits.",
      lambda t: has(t, r"(দিনে|প্রতিদিন)\s*(তিন|৩)\s*বার", r"(খাওয়ার|খাবারের|আহারের)\s*পর", r"২৫০")),
    T("V26", "orthography", "Education & NCTB Pedagogy",
      "Write one natural Bengali sentence that contains the words: station, post office and bird.",
      lambda t: has(t, r"স্টেশন", r"পোস্ট", r"পাখি") and lacks(t, r"ষ্টেশন", r"পোষ্ট", r"পাখী")),
    T("V27", "orthography", "Mass Media & Digital Journalism",
      "Write 3 Bengali sentences about the monsoon in Bangladesh.",
      lambda t: "।" in t and not re.search(r"(?<![0-9০-৯])\.(?:\s|$)", t)),
    T("V28", "convention", "Technology & Corporate",
      "Explain in 3 Bengali sentences what a database and machine learning are.",
      lambda t: has(t, r"ডেটাবেস", r"মেশিন লার্নিং") and lacks(t, r"ডাটা"), convention=True),
    T("V29", "convention", "Citizen Digital Services & Smart Governance",
      "In Bangladeshi standard Bengali, politely ask a stranger for a glass of water.",
      lambda t: has(t, r"পানি") and lacks(t, word("জল")), convention=True),
    T("V30", "poetry", "Classical Poetry & Prosody",
      "Write 2 Bengali lines about the Meghna river in Payar metre: exactly 14 akshar (syllables) per line, split 8+6. Output only the two lines.",
      payar_ok),
]

from tasks_hard import TASKS_HARD  # noqa: E402

TASKS += TASKS_HARD
TASKS_BY_ID = {t["id"]: t for t in TASKS}
