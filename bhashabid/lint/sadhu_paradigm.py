# bhashabid/lint/sadhu_paradigm.py
# Sadhu -> Cholito verb paradigms and lexical forms (Bangla Academy প্রমিত চলিত).
# Full-form tables are generated from known roots only, so look-alike words
# (মোবাইল, লিখিত, চলিত, মরিয়া) are never matched.

from ..normalize.unicode import canonicalize_unicode

# Consonant-final roots: Sadhu stem + suffix. Roots whose vowel is আ (রাখ, আস) mutate to এ
# in the participle and perfect (রাখিয়া -> রেখে, আসিয়া -> এসে).
CONSONANT_ROOTS = [
    "কর", "বল", "চল", "ধর", "পড়", "লিখ", "শুন", "দেখ", "ফির", "উঠ", "বস", "বুঝ", "খুঁজ",
    "ছুট", "পৌঁছ", "গড়", "ভর", "নড়", "সর", "মিল", "জ্বল", "ঘুর", "ফেল", "তুল", "খুল", "ভুল",
    "শিখ", "জিত", "দৌড়", "ফুট", "উড়", "লড়", "মুছ", "ঢুক", "কিন", "চিন", "খেল", "বেচ", "মিশ",
    "রাখ", "জান", "পার", "মার", "থাক", "ডাক", "হাস", "কাঁদ", "বাঁচ", "নাচ", "মান", "থাম", "কাট",
    "হাঁট", "আস", "আন", "জাগ", "ছাড়", "বাড়", "ভাঙ", "লাগ", "নাম", "চাপ", "হার", "ফাট", "ভাব",
    "পাল", "সাজ", "ভাস",
]

# Causative / -আ stems: Sadhu stem (as written before ই-suffixes) -> (Cholito participle base, Cholito finite stem).
CAUSATIVE_STEMS = {
    "পাঠা": ("পাঠ", "পাঠা"), "জানা": ("জান", "জানা"), "চালা": ("চাল", "চালা"), "ঘুমা": ("ঘুম", "ঘুমা"),
    "দাঁড়া": ("দাঁড়", "দাঁড়া"), "হারা": ("হার", "হারা"), "বসা": ("বস", "বসা"), "লাগা": ("লাগ", "লাগা"),
    "তাকা": ("তাক", "তাকা"), "পালা": ("পাল", "পালা"), "নামা": ("নাম", "নামা"), "থামা": ("থাম", "থামা"),
    "জাগা": ("জাগ", "জাগা"), "ভাসা": ("ভাস", "ভাসা"), "সাজা": ("সাজ", "সাজা"), "কাটা": ("কাট", "কাটা"),
    "দেখা": ("দেখ", "দেখা"), "শুনা": ("শুন", "শোনা"), "বুঝা": ("বুঝ", "বোঝা"), "উঠা": ("উঠ", "ওঠা"),
    "ফিরা": ("ফির", "ফেরা"), "শিখা": ("শিখ", "শেখা"), "পড়া": ("পড়", "পড়া"), "করা": ("কর", "করা"),
    "চালাই": ("চাল", "চালা"),
}

# Vowel-final and irregular roots: tense -> (Sadhu prefix, Cholito prefix).
IRREGULAR_PREFIXES = [
    # খা
    ("PART", "খাইয়া", "খেয়ে"), ("PERF", "খাইয়াছ", "খেয়েছ"), ("PROG", "খাইতেছ", "খাচ্ছ"),
    ("PAST", "খাইল", "খেল"), ("FUT", "খাইব", "খাব"), ("HAB", "খাইত", "খেত"), ("INF", "খাইতে", "খেতে"),
    # পা
    ("PART", "পাইয়া", "পেয়ে"), ("PERF", "পাইয়াছ", "পেয়েছ"), ("PROG", "পাইতেছ", "পাচ্ছ"),
    ("PAST", "পাইল", "পেল"), ("FUT", "পাইব", "পাব"), ("HAB", "পাইত", "পেত"), ("INF", "পাইতে", "পেতে"),
    # যা
    ("PART", "যাইয়া", "গিয়ে"), ("PART", "গিয়া", "গিয়ে"), ("PERF", "গিয়াছ", "গিয়েছ"), ("PROG", "যাইতেছ", "যাচ্ছ"),
    ("FUT", "যাইব", "যাব"), ("HAB", "যাইত", "যেত"), ("INF", "যাইতে", "যেতে"),
    # হ
    ("PART", "হইয়া", "হয়ে"), ("PERF", "হইয়াছ", "হয়েছ"), ("PROG", "হইতেছ", "হচ্ছ"),
    ("PAST", "হইল", "হল"), ("FUT", "হইব", "হব"), ("HAB", "হইত", "হত"),
    # দি / নি / লই
    ("PART", "দিয়া", "দিয়ে"), ("PERF", "দিয়াছ", "দিয়েছ"), ("PROG", "দিতেছ", "দিচ্ছ"), ("FUT", "দিব", "দেব"),
    ("PART", "নিয়া", "নিয়ে"), ("PERF", "নিয়াছ", "নিয়েছ"), ("PROG", "নিতেছ", "নিচ্ছ"), ("FUT", "নিব", "নেব"),
    ("PART", "লইয়া", "নিয়ে"), ("PERF", "লইয়াছ", "নিয়েছ"), ("PROG", "লইতেছ", "নিচ্ছ"),
    ("PAST", "লইল", "নিল"), ("FUT", "লইব", "নেব"), ("HAB", "লইত", "নিত"), ("INF", "লইতে", "নিতে"),
    # চাহ / গাহ / রহ / শু / ধু
    ("PART", "চাহিয়া", "চেয়ে"), ("PERF", "চাহিয়াছ", "চেয়েছ"), ("PROG", "চাহিতেছ", "চাইছ"),
    ("PAST", "চাহিল", "চাইল"), ("FUT", "চাহিব", "চাইব"), ("HAB", "চাহিত", "চাইত"), ("INF", "চাহিতে", "চাইতে"),
    ("PART", "গাহিয়া", "গেয়ে"), ("PERF", "গাহিয়াছ", "গেয়েছ"), ("PROG", "গাহিতেছ", "গাইছ"),
    ("PAST", "গাহিল", "গাইল"), ("FUT", "গাহিব", "গাইব"), ("HAB", "গাহিত", "গাইত"), ("INF", "গাহিতে", "গাইতে"),
    ("PART", "রহিয়া", "রয়ে"), ("PERF", "রহিয়াছ", "রয়েছ"), ("PAST", "রহিল", "রইল"), ("FUT", "রহিব", "রইব"),
    ("PART", "শুইয়া", "শুয়ে"), ("PERF", "শুইয়াছ", "শুয়েছ"), ("PAST", "শুইল", "শুল"), ("INF", "শুইতে", "শুতে"),
    ("PART", "ধুইয়া", "ধুয়ে"), ("PERF", "ধুইয়াছ", "ধুয়েছ"), ("PAST", "ধুইল", "ধুল"), ("INF", "ধুইতে", "ধুতে"),
]

# Person/number endings allowed after each tense prefix (Sadhu ending == Cholito ending).
TAILS = {
    "PART": [""],
    "PERF": ["", "ে", "েন", "ি", "িস", "িল", "িলেন", "িলাম", "িলে", "িলি"],
    "PROG": ["", "ে", "েন", "ি", "িস", "িল", "িলেন", "িলাম", "িলে", "িলি"],
    "PAST": ["", "েন", "াম", "ে", "ি"],
    "FUT": ["", "ে", "েন", "ি"],
    "HAB": ["েন", "াম", "ে", "িস"],
    "INF": [""],
}
# Bare habitual 3rd person (করিত) collides with Tatsama adjectives (লিখিত, চলিত, মিলিত);
# allow it only for these roots.
BARE_HABITUAL_ROOTS = {"কর", "বল", "থাক", "দেখ", "আস", "রাখ", "পার", "জান", "ডাক", "শুন"}

# Forms that are common in Bangladeshi Cholito too (দিবে, নিবে): converted on explicit request only,
# never reported as Guru-chandali.
AMBIGUOUS_FORMS = {"দিব", "দিবে", "দিবেন", "দিবি", "নিব", "নিবে", "নিবেন", "নিবি"}

# Generated forms that are also real words (Arabic হাসিল, English pile, names মারিয়া/সাজিয়া, place নড়িয়া).
BLOCKED_FORMS = {"হাসিল", "পাইল", "মারিয়া", "সাজিয়া", "নড়িয়া"}

# Roots whose ই-form is a common noun, so root+িতে also reads as noun+locative
# (বাড়িতে 'at home', ছুটিতে 'on holiday', চিনিতে 'in sugar'). Converted only in infinitive context.
NOUN_COLLISION_ROOTS = {"বাড়", "চিন", "ছুট", "হাস", "তুল", "খুল", "ভর", "ভাব", "সাজ", "পাল"}

# Irregular finite forms that override the generated tables.
OVERRIDES = {
    "হইল": "হলো", "হইত": "হতো",
    "আসিল": "এল", "আসিলেন": "এলেন", "আসিলাম": "এলাম", "আসিলে": "এলে", "আসিলি": "এলি",
    "আনিল": "আনল",
}

# Sadhu pronouns, adverbs and function words.
LEXICAL = {
    "ইহা": "এটি", "উহা": "ওটি", "ঐ": "ওই", "অদ্য": "আজ", "কল্য": "কাল", "এক্ষণে": "এখন",
    "তথায়": "সেখানে", "যথায়": "যেখানে", "নিমিত্ত": "জন্য", "এরূপ": "এমন", "সেরূপ": "তেমন",
    "যেরূপ": "যেমন", "কিরূপ": "কেমন", "অদ্যাপি": "আজও",
}


def _learned_roots() -> list:
    """Consonant roots added through the human-approved learning loop (assets/learned/sadhu_roots.json)."""
    import json
    import os
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "learned", "sadhu_roots.json")
    try:
        with open(path, encoding="utf-8") as f:
            return [r for r in json.load(f) if isinstance(r, str) and r and r not in CONSONANT_ROOTS]
    except (OSError, ValueError):
        return []


def _mutate(stem: str) -> str:
    """আ-vowel roots take এ in the Cholito participle/perfect: রাখ -> রেখ, আস -> এস, কাঁদ -> কেঁদ."""
    if stem.startswith("আ"):
        return "এ" + stem[1:]
    i = stem.rfind("া")
    return stem[:i] + "ে" + stem[i + 1:] if i != -1 else stem


def build_forms() -> dict:
    forms = {}

    def add(prefix_s, prefix_c, tense):
        for t in TAILS[tense]:
            forms.setdefault(prefix_s + t, prefix_c + t)

    for s_prefix, c_prefix, tense in [(p, c, t) for t, p, c in IRREGULAR_PREFIXES]:
        add(s_prefix, c_prefix, tense)

    for r in CONSONANT_ROOTS + _learned_roots():
        m = _mutate(r)
        add(r + "িয়া", m + "ে", "PART")
        add(r + "িয়াছ", m + "েছ", "PERF")
        add(r + "িতেছ", r + "ছ", "PROG")
        add(r + "িল", r + "ল", "PAST")
        add(r + "িব", r + "ব", "FUT")
        add(r + "িত", r + "ত", "HAB")
        add(r + "িতে", r + "তে", "INF")
        if r in BARE_HABITUAL_ROOTS:
            forms.setdefault(r + "িত", r + "ত")

    for s, (part, fin) in CAUSATIVE_STEMS.items():
        base = s if s.endswith("ই") else s + "ই"
        add(base + "য়া", part + "িয়ে", "PART")
        add(base + "য়াছ", part + "িয়েছ", "PERF")
        add(base + "তেছ", fin + "চ্ছ", "PROG")
        add(base + "ল", fin + "ল", "PAST")
        add(base + "ব", fin + "ব", "FUT")
        add(base + "ত", fin + "ত", "HAB")
        add(base + "তে", fin + "তে", "INF")

    forms.update(OVERRIDES)
    forms.update(LEXICAL)
    for b in BLOCKED_FORMS:
        forms.pop(b, None)
    # Linted text is canonical (precomposed য়/ড়/ঢ়); store keys and values the same way.
    return {canonicalize_unicode(s): canonicalize_unicode(c) for s, c in forms.items() if s != c}


SADHU_FORMS = build_forms()
CONTEXT_INFINITIVES = {canonicalize_unicode(r + "িতে") for r in NOUN_COLLISION_ROOTS}
