# tools/bn_normalize/orthography.py
# Deterministic Bengali Orthographic & Morphological Normalizer
# Strictly follows Bangla Academy Prashita Bangla Banan-Riti (প্রমিত বাংলা বানানের নিয়ম)
import re

# 1. Foreign loanword S replacements (Bangla Academy Rule 1.01 & 1.04)
# Foreign words with /s/ or /st/ should use 'স্ট' or 'স', never 'ষ্ট' or 'ষ'
LOANWORD_S_ROOTS = [
    ("রেজিষ্ট্রেশন", "রেজিস্ট্রেশন"),
    ("রেজিষ্ট্রি", "রেজিস্ট্রি"),
    ("ষ্টেশন", "স্টেশন"),
    ("মাষ্টার", "মাস্টার"),
    ("পোষ্টার", "পোস্টার"),
    ("পোষ্ট", "পোস্ট"),
    ("ষ্টুডিও", "স্টুডিও"),
    ("ষ্ট্যান্ড", "স্ট্যান্ড"),
    ("ষ্টোর", "স্টোর"),
    ("কাষ্টমার", "কাস্টমার"),
    ("ট্যাক্সী", "ট্যাক্সি"),
    ("ক্লাষ", "ক্লাস"),
    ("ইনষ্টিটিউট", "ইনস্টিটিউট"),
    ("ইনষ্টিটিউশন", "ইনস্টিটিউশন"),
    ("কনষ্টেবল", "কনস্টেবল"),
    ("ডাষ্টবিন", "ডাস্টবিন"),
    ("ব্যারিষ্টার", "ব্যারিস্টার"),
    ("অফিষার", "অফিসার"),
]

# 2. Natva-Shatva Vidhan & Visarga Sandhi (ণত্ব-ষত্ব বিধান ও বিসর্গ সন্ধি জনিত প্রমিত রূপ)
NATVA_SHATVA_ROOTS = [
    ("পুরষ্কার", "পুরস্কার"),
    ("আবিস্কার", "আবিष्कार"),
    ("নিস্কাশন", "নিষ্কাশন"),
    ("নিস্পত্তি", "নিষ্পত্তি"),
    ("দুস্কৃতি", "দুষ্কৃতি"),
    ("মনোকষ্ট", "মনঃকষ্ট"),
    ("শিরচ্ছেদ", "শিরশ্ছেদ"),
    ("অধোপতন", "অধঃপতন"),
    ("পুনঃরূপ", "পুনরূপ"),
]

# 3. Tatsama Dual-Vowel Invariants (Bangla Academy Rule 1.01: যেসব তৎসম শব্দে ই/ঈ বা উ/ঊ উভয়ই প্রযোজ্য, সে ক্ষেত্রে হ্রস্বস্বর)
TATSAMA_DUAL_VOWEL_ROOTS = [
    ("শ্রেণী", "শ্রেণি"),
    ("পদবী", "পদবি"),
    ("পল্লী", "পল্লি"),
    ("সূচী", "সূচি"),
    ("ধূলী", "ধূলি"),
    ("উর্ণা", "উর্না"),
    ("কিংবদন্তী", "কিংবদন্তি"),
]

# 4. Tatbhava / Desi / Foreign words that must take short-vowel 'ি' (হ্রস্ব-ইকার) under modern orthography
TATBHAVA_SHORT_VOWEL_ROOTS = [
    ("পাখী", "পাখি"),
    ("হাতী", "হাতি"),
    ("দাদী", "দাদি"),
    ("নানী", "নানি"),
    ("চাচী", "চাচি"),
    ("মামী", "মামি"),
    ("শাড়ী", "শাড়ি"),
    ("বাড়ী", "বাড়ি"),
    ("গাড়ী", "গাড়ি"),
    ("তরকারী", "তরকারি"),
    ("সরকারী", "সরকারি"),
    ("ফার্সী", "ফারসি"),
    ("আরবী", "আরবি"),
    ("ইংরেজী", "ইংরেজি"),
    ("বাঙালী", "বাঙালি"),
    ("কেরানী", "কেরানি"),
    ("ফেব্রুয়ারী", "ফেব্রুয়ারি"),
    ("জানুয়ারী", "জানুয়ারি"),
    ("ডিগ্রী", "ডিগ্রি"),
    ("লটারী", "লটারি"),
    ("ডায়েরী", "ডায়েরি"),
    ("পার্টী", "পার্টি"),
    ("একাডেমী", "একাডেমি"),
    ("রেশমী", "রেশমি"),
    ("আসামী", "আসামি"),
    ("ছুরী", "ছুরি"),
    ("দাবী", "দাবি"),
]

# 4. Affix, Sandhi & Morphology Invariant Standardizations (প্রত্যয় ও সন্ধিঘটিত প্রমিত রূপ)
AFFIX_AND_SANDHI_ROOTS = [
    ("প্রতিযোগীতা", "প্রতিযোগিতা"),
    ("সহযোগীতা", "সহযোগিতা"),
    ("সহযোগীতামূলক", "সহযোগিতামূলক"),
    ("প্রতিদ্বন্দীতা", "প্রতিদ্বন্দ্বিতা"),
    ("প্রতিদ্বন্দী", "প্রতিদ্বন্দ্বী"),
    ("প্রতিদ্বন্দ্বীতা", "প্রতিদ্বন্দ্বিতা"),
    ("দায়ীত্ব", "দায়িত্ব"),
    ("স্থায়ীত্ব", "স্থায়িত্ব"),
    ("মনযোগ", "মনোযোগ"),
    ("অনূসন্ধান", "অনুসন্ধান"),
    ("শারীরীক", "শারীরিক"),
    ("দূরবস্থা", "দুরবস্থা"),
    ("মুহুর্ত", "মুহূর্ত"),
    ("মুমুর্ষু", "মুমূর্ষু"),
    ("নীরবচ্ছিন্ন", "নিরবচ্ছিন্ন"),
    ("অধ্যাবসায়", "অধ্যবসায়"),
    ("প্রাণীবিদ্যা", "প্রাণিবিদ্যা"),
    ("প্রাণীজগত", "প্রাণিজগৎ"),
    ("মন্ত্রীসভা", "মন্ত্রিসভা"),
]

# 5. Reph Gemination (রেফের পর ব্যঞ্জনবর্ণের দ্বিত্ব বর্জন - বাংলা একাডেমি নিয়ম ১.০২)
REPH_GEMINATION_ROOTS = [
    ("ধর্ম্ম", "ধর্ম"),
    ("কর্ম্ম", "কর্ম"),
    ("মর্ম্ম", "মর্ম"),
    ("কার্য্য", "কার্য"),
    ("সূর্য্য", "সূর্য"),
    ("ধৈর্য্য", "ধৈর্য"),
    ("বার্দ্ধক্য", "বার্ধক্য"),
    ("পূর্ব্বক", "পূর্বক"),
    ("অনিবার্য্য", "অনিবার্য"),
    ("অর্দ্ধেক", "অর্ধেক"),
    ("অর্দ্ধ", "অর্ধ"),
]

# 6. Word Boundary Separations (পদ পৃথকীকরণ - বাংলা একাডেমি প্রমিত রূপ)
WORD_BOUNDARY_ROOTS = [
    ("এযাবৎ", "এ যাবৎ"),
    ("যতদূর", "যত দূর"),
    ("যেপর্যন্ত", "যে পর্যন্ত"),
    ("সেপর্যন্ত", "সে পর্যন্ত"),
]

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

COMPILED_WORD_BOUNDARIES = [
    (re.compile(B_L + re.escape(bad) + B_R), good)
    for bad, good in WORD_BOUNDARY_ROOTS
]

def normalize_orthography(text: str, profile: str = "bd_standard") -> str:
    """
    Enforces standardized orthographic rules based on the selected profile.
    Default profile 'bd_standard' enforces modern Bangla Academy rules:
    - Foreign loanwords use 'স'/'স্ট', not 'ষ'/'ষ্ট'.
    - Tatbhava/desi/foreign words use short-vowel 'ি', not 'ী'.
    - Natva-Shatva Vidhan (পুরস্কার, আবিষ্কার, ইত্যাদি).
    - Gemination after Reph is eliminated (ধর্ম্ম -> ধর্ম, কার্য্য -> কার্য).
    - Affix (-তা, -ত্ব, -সভা) vowel shortening (প্রতিযোগিতা, দায়িত্ব).
    - Word boundary separations (এ যাবৎ, যে পর্যন্ত).
    """
    if not text:
        return ""

    if profile == "bd_standard":
        # 1. Loanword S replacements (stem-aware)
        for bad_stem, good_stem in LOANWORD_S_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # Handle 'বাষ' (bus) strictly at word boundaries to avoid altering 'বাষট্টি' (62), 'সুভাষ', or 'বাষ্প' (vapor)
        text = re.sub(r"(?<![\u0980-\u09FF])বাষ(?=(?:ে|ের|টা|টি|গুলো|গুলা)?(?![\u0980-\u09FF]))", "বাস", text)

        # 2. Natva-Shatva Vidhan replacements
        for bad_stem, good_stem in NATVA_SHATVA_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # 3. Tatsama dual-vowel short vowel replacements (Rule 1.01)
        for bad_stem, good_stem in TATSAMA_DUAL_VOWEL_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # 4. Tatbhava short-vowel replacements
        for bad_stem, good_stem in TATBHAVA_SHORT_VOWEL_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # 5. Affix, Sandhi & Invariants replacements
        for bad_stem, good_stem in AFFIX_AND_SANDHI_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # 6. Reph gemination elimination
        for bad_stem, good_stem in REPH_GEMINATION_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # 7. Word boundary separations
        for pat, good in COMPILED_WORD_BOUNDARIES:
            text = pat.sub(good, text)

    return text
