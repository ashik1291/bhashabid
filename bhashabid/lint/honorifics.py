# tools/bn_lint/honorifics.py
# Honorific Concordance Linter (আপনি / তুমি / তুই) with Bidirectional Repair
import re
from .models import LintIssue, LintSeverity

# Boundary helper for Bengali tokens
B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# Verb transformation dictionaries
FORMAL_TO_FAMILIAR_VERBS = {
    "করেন": "করো", "যান": "যাও", "বলেন": "বলো", "খান": "খাও",
    "দেখেন": "দেখো", "নেন": "নাও", "দেন": "দাও", "হোন": "হও",
    "আসেন": "এসো", "করবেন": "করবে", "যাবেন": "যাবে"
}

FAMILIAR_TO_FORMAL_VERBS = {
    "করো": "করেন", "যাও": "যান", "বলো": "বলেন", "খাও": "খান",
    "দেখো": "দেখেন", "নাও": "নেন", "দাও": "দেন", "হও": "হোন",
    "এসো": "আসেন", "করবে": "করবেন", "যাবে": "যাবেন"
}

FORMAL_TO_INTIMATE_VERBS = {
    "করেন": "করিস", "যান": "যাস", "বলেন": "বলিস", "খান": "খাস", "দেখেন": "দেখিস",
    "নেন": "নিস", "দেন": "দিস", "আসেন": "আসিস", "করবেন": "করবি", "যাবেন": "যাবি"
}

INTIMATE_TO_FAMILIAR_VERBS = {
    "করিস": "করো", "যাবি": "যাবে", "বলিস": "বলো", "খাস": "খাও",
    "দেখিস": "দেখো", "নিস": "নাও", "দিস": "দাও", "করবি": "করবে"
}

# Third-person verb mappings (তিনি vs সে)
THIRD_PERSON_ORDINARY_TO_HONORIFIC = {
    "বলল": "বললেন", "করল": "করলেন", "গেল": "গেলেন", "খেল": "খেলেন",
    "দেখল": "দেখলেন", "নিল": "নিলেন", "দিল": "দিলেন", "বলে": "বলেন",
    "করে": "করেন", "যায়": "যান", "খায়": "খান", "দেখে": "দেখেন",
    "দেয়": "দেন", "নেয়": "নেন",
    "হলো": "হলেন", "বলবে": "বলবেন", "করবে": "করবেন", "যাবে": "যাবেন",
    "ছিল": "ছিলেন", "আসে": "আসেন", "এলো": "এলেন", "আসলো": "আসলেন",
    "আসবে": "আসবেন", "থাকে": "থাকেন", "থাকবে": "থাকবেন", "হয়েছে": "হয়েছেন",
    "গিয়েছিল": "গিয়েছিলেন", "করেছিল": "করেছিলেন", "বলেছিল": "বলেছিলেন",
    "এসেছিল": "এসেছিলেন", "হয়েছিল": "হয়েছিলেন", "দেখেছিল": "দেখেছিলেন",
    "খেয়েছিল": "খেয়েছিলেন", "দিয়েছিল": "দিয়েছিলেন", "নিয়েছিল": "নিয়েছিলেন",
    "করত": "করতেন", "যেত": "যেতেন", "বলত": "বলতেন", "থাকত": "থাকতেন",
    "ফিরল": "ফিরলেন", "বসল": "বসলেন", "উঠল": "উঠলেন", "লিখল": "লিখলেন",
    "পড়ল": "পড়লেন", "ডাকল": "ডাকলেন", "হাসল": "হাসলেন", "শুনল": "শুনলেন",
    "আনল": "আনলেন", "পাঠাল": "পাঠালেন", "জানাল": "জানালেন", "চাইল": "চাইলেন"
}

THIRD_PERSON_HONORIFIC_TO_ORDINARY = {
    v: k for k, v in THIRD_PERSON_ORDINARY_TO_HONORIFIC.items()
}

# First-person verbal concordances
NON_FIRST_TO_FIRST_VERBS = {
    # 2nd/3rd honorific -> 1st person
    "করবেন": "করব", "বলবেন": "বলব", "যাবেন": "যাব", "খাবেন": "খাব", "দেখবেন": "দেখব",
    "করলেন": "করলাম", "বললেন": "বললাম", "গেলেন": "গেলাম", "খেলেন": "খেলাম", "দেখলেন": "দেখলাম",
    "করেন": "করি", "বলেন": "বলি", "যান": "যাই", "খান": "খাই", "দেখেন": "দেখি",
    "হলেন": "হলাম", "হবেন": "হব", "হোন": "হই",
    "লিখবেন": "লিখব", "পড়বেন": "পড়ব", "ফিরবেন": "ফিরব", "বসবেন": "বসব", "উঠবেন": "উঠব",
    "ডাকবেন": "ডাকব", "হাসবেন": "হাসব", "শুনবেন": "শুনব", "আনবেন": "আনব", "পাঠাবেন": "পাঠাব", "জানাবেন": "জানাব", "চাইবেন": "চাইব",
    "লিখলেন": "লিখলাম", "পড়লেন": "পড়লাম", "ফিরলেন": "ফিরলাম", "বসলেন": "বসলাম", "উঠলেন": "উঠলাম",
    "ডাকলেন": "ডাকলাম", "হাসলেন": "হাসলাম", "শুনলেন": "শুনলাম", "আনলেন": "আনলাম", "পাঠালেন": "পাঠালাম", "জানালেন": "জানালাম", "চাইলেন": "চাইলাম",
    "লিখেন": "লিখি", "পড়েন": "পড়ি", "ফিরেন": "ফিরি", "বসেন": "বসি", "উঠেন": "উঠি",
    "ডাকেন": "ডাকি", "হাসেন": "হাসি", "শুনেন": "শুনি", "আনেন": "আনি", "পাঠান": "পাঠাই", "জানান": "জানাই", "চান": "চাই",
    # 3rd ordinary -> 1st person
    "করল": "করলাম", "বলল": "বললাম", "গেল": "গেলাম", "খেল": "খেলাম", "দেখল": "দেখলাম",
    "করে": "করি", "বলে": "বলি", "যায়": "যাই", "খায়": "খাই", "দেখে": "দেখি",
    "করবে": "করব", "বলবে": "বলব", "যাবে": "যাব", "খাবে": "খাব", "দেখবে": "দেখব",
    "হলো": "হলাম", "হবে": "হব",
    "লিখল": "লিখলাম", "পড়ল": "পড়লাম", "ফিরল": "ফিরলাম", "বসল": "বসলাম", "উঠল": "উঠলাম",
    "ডাকল": "ডাকলাম", "হাসল": "হাসলাম", "শুনল": "শুনলাম", "আনল": "আনলাম", "পাঠাল": "পাঠালাম", "জানাল": "জানালাম", "চাইল": "চাইলাম",
    "লিখবে": "লিখব", "পড়বে": "পড়ব", "ফিরবে": "ফিরব", "বসবে": "বসব", "উঠবে": "উঠব",
    "ডাকবে": "ডাকব", "হাসবে": "হাসব", "শুনবে": "শুনব", "আনবে": "আনব", "পাঠাবে": "পাঠাব", "জানাবে": "জানাব", "চাইবে": "চাইব",
    "লেখে": "লিখি", "পড়ে": "পড়ি"
}

FIRST_TO_SECOND_FAMILIAR_VERBS = {
    "করলাম": "করলে", "বললাম": "বললে", "গেলাম": "গেলে", "খেলাম": "খেলে", "দেখলাম": "দেখলে",
    "করব": "করবে", "বলব": "বলবে", "যাব": "যাবে", "খাব": "খাবে", "দেখব": "দেখবে",
    "করি": "করো", "বলি": "বলো", "যাই": "যাও", "খাই": "খাও", "দেখি": "দেখো",
    "লিখলাম": "লিখলে", "পড়লাম": "পড়লে", "ফিরলাম": "ফিরলে", "বসলাম": "বসলে", "উঠলাম": "উঠলে",
    "ডাকলাম": "ডাকলে", "হাসলাম": "হাসলে", "শুনলাম": "শুনলে", "আনলাম": "আনলে", "পাঠালাম": "পাঠালে",
    "জানালাম": "জানালে", "চাইলাম": "চাইলে",
    "লিখব": "লিখবে", "পড়ব": "পড়বে", "ফিরব": "ফিরবে", "বসব": "বসবে", "উঠব": "উঠবে",
    "ডাকব": "ডাকবে", "হাসব": "হাসবে", "শুনব": "শুনবে", "আনব": "আনবে", "পাঠাব": "পাঠাবে",
    "জানাব": "জানাবে", "চাইব": "চাইবে",
    "লিখি": "লেখো", "পড়ি": "পড়ো"
}

FIRST_TO_SECOND_FORMAL_VERBS = {
    "করলাম": "করলেন", "বললাম": "বললেন", "গেলাম": "গেলেন", "খেলাম": "খেলেন", "দেখলাম": "দেখলেন",
    "করব": "করবেন", "বলব": "বলবেন", "যাব": "যাবেন", "খাব": "খাবেন", "দেখব": "দেখবেন",
    "করি": "করেন", "বলি": "বলেন", "যাই": "যান", "খাই": "খান", "দেখি": "দেখেন",
    "লিখলাম": "লিখলেন", "পড়লাম": "পড়লেন", "ফিরলাম": "ফিরলেন", "বসলাম": "বসলেন", "উঠলাম": "উঠলেন",
    "ডাকলেন": "ডাকলেন", "হাসলাম": "হাসলেন", "শুনলাম": "শুনলেন", "আনলাম": "আনলেন", "পাঠালাম": "পাঠালেন",
    "জানালাম": "জানালেন", "চাইলাম": "চাইলেন",
    "লিখব": "লিখবেন", "পড়ব": "পড়বেন", "ফিরব": "ফিরবেন", "বসব": "বসবেন", "উঠব": "উঠবেন",
    "ডাকব": "ডাকবেন", "হাসব": "হাসবেন", "শুনব": "শুনবেন", "আনব": "আনবেন", "পাঠাব": "পাঠাবেন",
    "জানাব": "জানাবেন", "চাইব": "চাইবেন",
    "লিখি": "লিখেন", "পড়ি": "পড়েন"
}

FIRST_TO_THIRD_ORDINARY_VERBS = {
    "করলাম": "করল", "বললাম": "বলল", "গেলাম": "গেল", "খেলাম": "খেল", "দেখলাম": "দেখল",
    "নিলাম": "নিল", "দিলাম": "দিল", "হলাম": "হলো", "থাকলাম": "থাকল",
    "লিখলাম": "লিখল", "পড়লাম": "পড়ল", "ফিরলাম": "ফিরল", "বসলাম": "বসল", "উঠলাম": "উঠল",
    "ডাকলাম": "ডাকল", "হাসলাম": "হাসল", "শুনলাম": "শুনল", "আনলাম": "আনল", "পাঠালাম": "পাঠাল",
    "জানালাম": "জানাল", "চাইলাম": "চাইল",
    "করব": "করবে", "বলব": "বলবে", "যাব": "যাবে", "খাব": "খাবে", "দেখব": "দেখবে",
    "নেব": "নেবে", "দেব": "দেবে", "হব": "হবে", "থাকব": "থাকবে",
    "লিখব": "লিখবে", "পড়ব": "পড়বে", "ফিরব": "ফিরবে", "বসব": "বসবে", "উঠব": "উঠবে",
    "ডাকব": "ডাকবে", "হাসব": "হাসবে", "শুনব": "শুনবে", "আনব": "আনবে", "পাঠাব": "পাঠাবে",
    "জানাব": "জানাবে", "চাইব": "চাইবে",
    "করি": "করে", "বলি": "বলে", "যাই": "যায়", "খাই": "খায়", "দেখি": "দেখে",
    "লিখি": "লেখে", "পড়ি": "পড়ে"
}

# Regular productive Bengali honorific inflectional verbal suffixes
HONORIFIC_FINITE_VERB_PAT = re.compile(
    r"(?<![\u0980-\u09FF])[\u0980-\u09FF]+?(?:লেন|তেন|বেন|েন|ছেন|ছিলেন|েছেন)(?![\u0980-\u09FF])"
)

# Productive finite-verb morphology (whole-token alternatives appended to the closed verb lists below)
_W = r"[ঀ-৿]+?"
FORMAL_VERB_MORPH = r"আছেন|" + _W + r"(?:ছেন|ছিলেন|লেন|বেন|তেন)"
_C = r"[\u0995-\u09B9\u09DC\u09DD\u09DF]"
FAMILIAR_VERB_MORPH = r"আছো|আছ|" + _W + r"(?:ছো|ছিলে|েছ|চ্ছ|" + _C + r"ছ)"
ORDINARY_3P_VERB_MORPH = _W + r"(?:চ্ছে|েছে|ছিল|" + _C + r"ছে)"
_NOT_VERB_TOKENS = {"স্বচ্ছ", "তুচ্ছ", "গুচ্ছ", "কেন", "যেন"}

PERSONAL_PRONOUN_PAT = re.compile(
    B_L + r"(?:আমি|আমরা|আপনি|আপনারা|তুমি|তোমরা|তুই|তোরা|তিনি|তাঁরা|সে|তারা|উনি|ওনারা|ও|ওরা)" + B_R
)

_SUFFIX_RULES = {
    "formal_2p": [("ছিলে", "ছিলেন"), ("ছো", "ছেন"), ("চ্ছ", "চ্ছেন"), ("েছ", "েছেন"), ("আছ", "আছেন"), ("ছ", "ছেন")],
    "familiar_2p": [("ছিলেন", "ছিলে"), ("ছেন", "ছো"), ("লেন", "লে"), ("বেন", "বে"), ("তেন", "তে")],
    "intimate_2p": [("আছেন", "আছিস"), ("আছো", "আছিস"), ("েছেন", "েছিস"), ("চ্ছেন", "চ্ছিস"), ("ছেন", "ছিস"),
                    ("েছো", "েছিস"), ("চ্ছো", "চ্ছিস"), ("ছো", "ছিস"), ("লেন", "লি"), ("বেন", "বি"), ("তেন", "তিস")],
    "honorific_3p": [("চ্ছে", "চ্ছেন"), ("েছে", "েছেন"), ("ছিল", "ছিলেন"), ("ছে", "ছেন")],
    "ordinary_3p": [("ছিলেন", "ছিল"), ("ছেন", "ছে"), ("লেন", "ল"), ("বেন", "বে"), ("তেন", "ত")],
}


COORDINATOR_PAT = re.compile(B_L + r"(?:এবং|ও|আর)" + B_R)


def inflect_verb(verb: str, table: dict, target: str):
    """Maps a finite verb to the target register via the closed table, else by productive suffix; None if unknown."""
    if verb in table:
        return table[verb]
    if verb in _NOT_VERB_TOKENS:
        return None
    for old, new in _SUFFIX_RULES[target]:
        if verb.endswith(old):
            return verb[: -len(old)] + new
    return None


def is_guarded_middle(middle: str) -> bool:
    """True when the span between subject and verb crosses a clause or contains another subject pronoun."""
    return bool(CLAUSE_BOUNDARY_PAT.search(middle) or PERSONAL_PRONOUN_PAT.search(middle))


# 1. আপনি + informal verbs
APNI_CLASH_PAT = re.compile(
    B_L + r"(আপনি|আপনারা)" + B_R +
    r"((?:(?!(?:আপনি|আপনারা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(করো|যাও|বলো|খাও|দেখো|নাও|দাও|হও|এসো|করিস|যাবি|বলিস|খাস|দেখিস|আসিস|" + FAMILIAR_VERB_MORPH + r")" + B_R
)

# 2. তুমি + formal or intimate verbs
TUMI_CLASH_PAT = re.compile(
    B_L + r"(তুমি|তোমরা)" + B_R +
    r"((?:(?!(?:তুমি|তোমরা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(আসেন|করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন|করিস|যাবি|বলিস|খাস|দেখিস|" + FORMAL_VERB_MORPH + r")" + B_R
)

# 3. তুই + formal verbs
TUI_CLASH_PAT = re.compile(
    B_L + r"(তুই|তোরা)" + B_R +
    r"((?:(?!(?:তুই|তোরা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(আসেন|করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন|" + FORMAL_VERB_MORPH + r"|" + FAMILIAR_VERB_MORPH + r")" + B_R
)

# 4. তিনি / তাঁরা + ordinary verbs (e.g. তিনি বলল -> তিনি বললেন OR সে বলল)
TINI_CLASH_PAT = re.compile(
    B_L + r"(তিনি|তাঁরা)" + B_R +
    r"((?:(?!(?:তিনি|তাঁরা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(ছিল|বলল|করল|গেল|খেল|দেখল|নিল|দিল|বলে|করে|যায়|খায়|দেখে|হলো|বলবে|করবে|যাবে|আসে|এলো|আসলো|আসবে|থাকে|থাকবে|হয়েছে|গিয়েছিল|করেছিল|বলেছিল|এসেছিল|হয়েছিল|দেখেছিল|খেয়েছিল|দিয়েছিল|নিয়েছিল|করত|যেত|বলত|থাকত|ফিরল|বসল|উঠল|লিখল|পড়ল|ডাকল|হাসল|শুনল|আনল|পাঠাল|জানাল|চাইল|" + ORDINARY_3P_VERB_MORPH + r")" + B_R
)

# 5. সে / তারা + honorific verbs (e.g. সে বললেন -> সে বলল OR তিনি বললেন)
SE_CLASH_PAT = re.compile(
    B_L + r"(সে|তারা)" + B_R +
    r"((?:(?!(?:সে|তারা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(ছিলেন|বললেন|করলেন|গেলেন|খেলেন|দেখলেন|নিলেন|দিলেন|বলেন|করেন|খান|দেখেন|হলেন|বলবেন|করবেন|যাবেন|আসেন|এলেন|আসলেন|আসবেন|থাকেন|থাকবেন|হয়েছেন|গিয়েছিলেন|করেছিলেন|বলেছিলেন|এসেছিলেন|হয়েছিলেন|দেখেছিলেন|খেয়েছিলেন|দিয়েছিলেন|নিয়েছিলেন|করতেন|যেতেন|বলতেন|থাকতেন|ফিরলেন|বসলেন|উঠলেন|লিখলেন|পড়লেন|ডাকলেন|হাসলেন|শুনলেন|আনলেন|পাঠালেন|জানালেন|চাইলেন|" + FORMAL_VERB_MORPH + r")" + B_R
)

# 6. আমি / আমরা + non-first-person verbs (e.g. আমি করবেন না -> আমি করব না)
AMI_CLASH_PAT = re.compile(
    B_L + r"(আমি|আমরা)" + B_R +
    r"((?:(?!(?:আমি|আমরা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(করবেন|বলবেন|যাবেন|খাবেন|দেখবেন|নেবেন|দেবেন|আসবেন|থাকবেন|হবেন|"
          r"লিখবেন|পড়বেন|ফিরবেন|বসবেন|উঠবেন|ডাকবেন|হাসবেন|শুনবেন|আনবেন|পাঠাবেন|জানাবেন|চাইবেন|"
          r"করলেন|বললেন|গেলেন|খেলেন|দেখলেন|নিলেন|দিলেন|এলেন|আসলেন|থাকলেন|হলেন|"
          r"লিখলেন|পড়লেন|ফিরলেন|বসলেন|উঠলেন|ডাকলেন|হাসলেন|শুনলেন|আনলেন|পাঠালেন|জানালেন|চাইলেন|"
          r"করেন|বলেন|যান|খান|দেখেন|নেন|দেন|আসেন|থাকেন|হোন|"
          r"লিখেন|পড়েন|ফিরেন|বসেন|উঠেন|ডাকেন|হাসেন|শুনেন|আনেন|পাঠান|জানান|চান|"
          r"করতেন|বলতেন|যেতেন|খেতেন|দেখতেন|থাকতেন|লিখতেন|পড়তেন|"
          r"করল|বলল|গেল|খেল|দেখল|নিল|দিল|এলো|আসলো|হলো|থাকল|"
          r"লিখল|পড়ল|ফিরল|বসল|উঠল|ডাকল|হাসল|শুনল|আনল|পাঠাল|জানাল|চাইল|"
          r"করবে|বলবে|যাবে|খাবে|দেখবে|নেবে|দেবে|আসবে|থাকবে|হবে|"
          r"লিখবে|পড়বে|ফিরবে|বসবে|উঠবে|ডাকবে|হাসবে|শুনবে|আনবে|পাঠাবে|জানাবে|চাইবে|"
          r"করিস|বলিস|যাবি|খাস|দেখিস|নিস|দিস|আসিস|লিখিস|পড়িস)" + B_R
)

# 7. Non-first-person pronouns + first-person verbs (e.g. আপনি চিঠি লিখলাম -> আপনি চিঠি লিখলেন)
NON_FIRST_PERSON_FIRST_VERB_PAT = re.compile(
    B_L + r"(আপনি|আপনারা|তুমি|তোমরা|তুই|তোরা|তিনি|তাঁরা|সে|তারা)" + B_R +
    r"((?:(?!(?:আপনি|আপনারা|তুমি|তোমরা|তুই|তোরা|তিনি|তাঁরা|সে|তারা)" + B_R + r")[^।?!,;:\n\"“”'‘’])*?)" +
    B_L + r"(করলাম|বললাম|গেলাম|খেলাম|দেখলাম|নিলাম|দিলাম|হলাম|থাকলাম|"
          r"লিখলাম|পড়লাম|ফিরলাম|বসলাম|উঠলাম|ডাকলাম|হাসলাম|শুনলাম|আনলাম|পাঠালাম|জানালাম|চাইলাম|"
          r"করব|বলব|যাব|খাব|দেখব|নেব|দেব|হব|থাকব|"
          r"লিখব|পড়ব|ফিরব|বসব|উঠব|ডাকব|হাসব|শুনব|আনব|পাঠাব|জানাব|চাইব|"
          r"করতাম|বলতাম|যেতাম|খেতাম|দেখতাম|থাকতাম|লিখতাম|পড়তাম)" + B_R
)

# Universal clause boundary marker: subordinate and coordinate conjunctions
CLAUSE_BOUNDARY_PAT = re.compile(
    B_L + r"(যে|যেন|কারণ|যেহেতু|সেহেতু|যখন|তখন|যদি|তবে|তাহলে|কিন্তু|অথবা|বা|যাতে|নইলে|যা|তাই|যত|যেমন|যেখানে)" + B_R
)

def check_honorific_clash(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        # 1. Check তুমি clash
        for m_tumi in TUMI_CLASH_PAT.finditer(line):
            subj = m_tumi.group(1)
            middle = m_tumi.group(2)
            verb = m_tumi.group(3)
            matched = m_tumi.group(0)

            # Linguistic Guard: Cross-clause boundary
            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            # Guard: another subject pronoun intervenes, or the token is not a verb
            if PERSONAL_PRONOUN_PAT.search(middle) or verb in _NOT_VERB_TOKENS:
                continue

            if verb in FORMAL_TO_FAMILIAR_VERBS:
                correct_familiar_verb = FORMAL_TO_FAMILIAR_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_familiar_verb}"
                formal_subj = "আপনি" if subj == "তুমি" else "আপনারা"
                opt2 = f"{formal_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১ (ক্রিয়াপদ পরিবর্তন): '{opt1}' অথবা বিকল্প ২ (সর্বনাম পরিবর্তন): '{opt2}'"
            elif verb in INTIMATE_TO_FAMILIAR_VERBS:
                correct_familiar_verb = INTIMATE_TO_FAMILIAR_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_familiar_verb}"
                intimate_subj = "তুই" if subj == "তুমি" else "তোরা"
                opt2 = f"{intimate_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১: '{opt1}' অথবা বিকল্প ২: '{opt2}'"
            else:
                suggestion = f"ক্রিয়াপদে যথাযথ বিভক্তি প্রয়োগ করুন।"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TUMI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সাধারণ) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tumi.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 2. Check আপনি clash
        for m_apni in APNI_CLASH_PAT.finditer(line):
            subj = m_apni.group(1)
            middle = m_apni.group(2)
            verb = m_apni.group(3)
            matched = m_apni.group(0)

            # Linguistic Guard: Cross-clause boundary
            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            # Guard: another subject pronoun intervenes, or the token is not a verb
            if PERSONAL_PRONOUN_PAT.search(middle) or verb in _NOT_VERB_TOKENS:
                continue

            if verb in FAMILIAR_TO_FORMAL_VERBS:
                correct_formal_verb = FAMILIAR_TO_FORMAL_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_formal_verb}"
                familiar_subj = "তুমি" if subj == "আপনি" else "তোমরা"
                opt2 = f"{familiar_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১ (ক্রিয়াপদ পরিবর্তন): '{opt1}' অথবা বিকল্প ২ (সর্বনাম পরিবর্তন): '{opt2}'"
            else:
                suggestion = f"ক্রিয়াপদে যথাযথ সম্ভ্রমাত্মক বিভক্তি (-েন) প্রয়োগ করুন।"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-APNI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সম্ভ্রমাত্মক) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_apni.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 3. Check তুই clash
        for m_tui in TUI_CLASH_PAT.finditer(line):
            subj = m_tui.group(1)
            middle = m_tui.group(2)
            verb = m_tui.group(3)
            matched = m_tui.group(0)
            if CLAUSE_BOUNDARY_PAT.search(middle) or PERSONAL_PRONOUN_PAT.search(middle) or verb in _NOT_VERB_TOKENS:
                continue
            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TUI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (ঘনিষ্ঠ/তুচ্ছার্থ) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tui.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion="ঘনিষ্ঠ রূপে -িস/-বি (যেমন: করিস, যাবি) ব্যবহার করুন।"
            ))

        # 4. Check তিনি / তাঁরা clash (3rd person honorific pronoun + non-honorific verb)
        for m_tini in TINI_CLASH_PAT.finditer(line):
            subj = m_tini.group(1)
            middle = m_tini.group(2)
            verb = m_tini.group(3)
            matched = m_tini.group(0)

            # Linguistic Guard 1: Cross-clause boundary
            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            # Linguistic Guard 2: Prior honorific verb already exists in middle
            # e.g. 'তিনি পদ ছাড়েন বলে' -> 'ছাড়েন' is already the main verb matching 'তিনি'.
            has_prior_hon_verb = any(
                re.search(rf"(?<![\u0980-\u09FF]){hv}(?![\u0980-\u09FF])", middle)
                for hv in THIRD_PERSON_HONORIFIC_TO_ORDINARY.keys()
            ) or bool(HONORIFIC_FINITE_VERB_PAT.search(COORDINATOR_PAT.split(middle)[-1]))
            if has_prior_hon_verb or PERSONAL_PRONOUN_PAT.search(middle):
                continue

            # Linguistic Guard 3: Non-finite participle in compound or serial verb construction
            # e.g. 'তিনি বাতিল করে দেন' or 'তিনি বাতিল করে ... বলেন' or 'তিনি কাজটি শেষ করে বাড়ি ফিরলেন'
            rest_of_clause = line[m_tini.end():]
            if verb in ("করে", "হয়ে", "গিয়ে", "এসে", "দেখে", "বলে"):
                # Check if an honorific finite verb follows in the same clause (dictionary or inflectional suffix)
                has_hon_verb = any(
                    re.search(rf"(?<![\u0980-\u09FF]){hv}(?![\u0980-\u09FF])", rest_of_clause)
                    for hv in THIRD_PERSON_HONORIFIC_TO_ORDINARY.keys()
                ) or bool(HONORIFIC_FINITE_VERB_PAT.search(rest_of_clause))
                if has_hon_verb:
                    continue

            # Linguistic Guard 4: Quotative complementizer 'বলে' followed by reporting predicate
            # e.g. 'বলে জানা গেছে', 'বলে মনে করা হয়', 'বলে দাবি করা হয়'
            if verb == "বলে" and re.search(r"^\s*(?:জানা গেছে|মনে করা|দাবি করা|উল্লেখ করা|প্রকাশ|জানানো)", rest_of_clause):
                continue

            hon_verb = THIRD_PERSON_ORDINARY_TO_HONORIFIC.get(verb, f"{verb}েন")
            ord_subj = "সে" if subj == "তিনি" else "তারা"
            suggestion = f"বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): '{subj}{middle}{hon_verb}' অথবা বিকল্প ২ (সাধারণ সর্বনাম): '{ord_subj}{middle}{verb}'"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TINI",
                message=f"তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tini.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 5. Check সে / তারা clash (3rd person ordinary pronoun + honorific verb)
        for m_se in SE_CLASH_PAT.finditer(line):
            subj = m_se.group(1)
            middle = m_se.group(2)
            verb = m_se.group(3)
            matched = m_se.group(0)

            # Linguistic Guard: Cross-clause boundary
            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            # Linguistic Guard 5: Demonstrative determiner 'সে' modifying a noun
            # e.g. 'সে কথা ভাবা দরকার', 'সে সময়', 'সে বিষয়'
            if subj == "সে" and re.match(r"^\s*(?:কথা|বিষয়|সময়|দিন|বছর|ঘটনা|মুহূর্ত|স্থান|জায়গা|কারণে|ফলে|লোক|ব্যক্তি)(?![\u0980-\u09FF])", middle):
                continue

            # Linguistic Guard 6: Another honorific subject intervenes in middle
            # e.g. 'সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন' -> subject of 'করেন' is 'তিনি', not 'সে'.
            if subj == "সে" and re.search(r"(?<![\u0980-\u09FF])(তিনি|তাঁরা|আপনারা)(?![\u0980-\u09FF])", middle):
                continue

            ord_verb = THIRD_PERSON_HONORIFIC_TO_ORDINARY.get(verb, verb)
            hon_subj = "তিনি" if subj == "সে" else "তাঁরা"
            suggestion = f"বিকল্প ১ (সাধারণ ক্রিয়াপদ): '{subj}{middle}{ord_verb}' অথবা বিকল্প ২ (সম্ভ্রমাত্মক সর্বনাম): '{hon_subj}{middle}{verb}'"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-SE",
                message=f"তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_se.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 6. Check আমি / আমরা clash (1st person pronoun + 2nd/3rd person verb)
        for m_ami in AMI_CLASH_PAT.finditer(line):
            subj = m_ami.group(1)
            middle = m_ami.group(2)
            verb = m_ami.group(3)
            matched = m_ami.group(0)

            # Linguistic Guard: Cross-clause boundary
            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            # Guard: Intervening subject pronoun (e.g. আমি জানি আপনি আসবেন)
            if re.search(r"(?<![\u0980-\u09FF])(?:আপনি|আপনারা|তুমি|তোমরা|তুই|তোরা|তিনি|তাঁরা|সে|তারা|কে|কারা)(?![\u0980-\u09FF])", middle):
                continue

            first_verb = NON_FIRST_TO_FIRST_VERBS.get(verb)
            if first_verb:
                suggestion = f"উত্তম পুরুষের ক্রিয়াপদ প্রয়োগ করুন: '{subj}{middle}{first_verb}'"
            else:
                suggestion = "উত্তম পুরুষের সঙ্গতিপূর্ণ ক্রিয়াপদ প্রয়োগ করুন।"

            issues.append(LintIssue(
                rule_id="RULE-LINT-PERSON-AMI",
                message=f"পুরুষ ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (উত্তম পুরুষ) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_ami.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 7. Check non-first-person pronouns + 1st person verb (e.g. আপনি চিঠি লিখলাম -> আপনি চিঠি লিখলেন)
        for m_sec in NON_FIRST_PERSON_FIRST_VERB_PAT.finditer(line):
            subj = m_sec.group(1)
            middle = m_sec.group(2)
            verb = m_sec.group(3)
            matched = m_sec.group(0)

            if CLAUSE_BOUNDARY_PAT.search(middle):
                continue

            if re.search(r"(?<![\u0980-\u09FF])(?:আমি|আমরা)(?![\u0980-\u09FF])", middle):
                continue

            if subj in ("তুমি", "তোমরা"):
                rule_id = "RULE-LINT-PERSON-TUMI"
                cor_verb = FIRST_TO_SECOND_FAMILIAR_VERBS.get(verb, "করবে/করলে")
                person_desc = "মধ্যম পুরুষ (সাধারণ)"
            elif subj in ("আপনি", "আপনারা"):
                rule_id = "RULE-LINT-PERSON-APNI"
                cor_verb = FIRST_TO_SECOND_FORMAL_VERBS.get(verb, "করবেন/করলেন")
                person_desc = "মধ্যম পুরুষ (সম্ভ্রমাত্মক)"
            elif subj in ("তুই", "তোরা"):
                rule_id = "RULE-LINT-PERSON-TUI"
                cor_verb = "করবি/করলি"
                person_desc = "মধ্যম পুরুষ (তুচ্ছ/অন্তরঙ্গ)"
            elif subj in ("তিনি", "তাঁরা"):
                rule_id = "RULE-LINT-PERSON-TINI"
                cor_verb = FIRST_TO_SECOND_FORMAL_VERBS.get(verb, "করলেন/করবেন")
                person_desc = "নাম পুরুষ (সম্ভ্রমাত্মক)"
            else:  # সে, তারা
                rule_id = "RULE-LINT-PERSON-SE"
                cor_verb = FIRST_TO_THIRD_ORDINARY_VERBS.get(verb, "করল/করবে")
                person_desc = "নাম পুরুষ (সাধারণ)"

            suggestion = f"{person_desc} ক্রিয়াপদ প্রয়োগ করুন: '{subj}{middle}{cor_verb}'"

            issues.append(LintIssue(
                rule_id=rule_id,
                message=f"পুরুষ ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' ({person_desc}) এর সাথে উত্তম পুরুষের ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_sec.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

    return issues
