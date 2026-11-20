# bhashabid/lint/guru_chandali.py
# Sadhu-Cholito mixing detection (গুরুচণ্ডালী দোষ)
import re
from .models import LintIssue, LintSeverity
from .sadhu_paradigm import SADHU_FORMS, AMBIGUOUS_FORMS, CONTEXT_INFINITIVES

SADHU_MARKERS = {
    "আসিয়া": "এসে",
    "আসিয়াছিলেন": "এসেছিলেন",
    "করিয়াছিল": "করেছিল",
    "করিয়াছিলেন": "করেছিলেন",
    "করিয়া": "করে",
    "যাইয়া": "গিয়ে",
    "বলিয়া": "বলে",
    "বলিয়াছিলেন": "বলেছিলেন",
    "দেখিয়া": "দেখে",
    "দেখিয়াছিলেন": "দেখেছিলেন",
    "খাইয়া": "খেয়ে",
    "লইয়া": "নিয়ে",
    "যাইবে": "যাবে",
    "হইবে": "হবে",
    "তাহারা": "তারা",
    "উহারা": "ওরা",
    "সহিত": "সাথে / সঙ্গে",
    "বসিয়া": "বসে",
    "গিয়াছিল": "গিয়েছিল",
    "গিয়াছিলেন": "গিয়েছিলেন",
    "পড়িয়া": "পড়ে",
    "লিখিয়া": "লিখে",
    "বলিতেছেন": "বলছেন",
    "করিলেন": "করলেন",
    "রহিয়াছে": "রয়েছে",
    "করিতে": "করতে",
    "হইয়াছে": "হয়েছে",
    "হইয়া": "হয়ে",
    "হইতে": "হতে / থেকে",
    "ইহাতে": "এতে",
    "তাহা": "তা",
    "যাহা": "যা",
    "পারিবে": "পারবে",
    "পারিবেন": "পারবেন",
    "হইল": "হলো",
    "হউক": "হোক",
    "হইলেন": "হলেন",
    "তাহাদিগকে": "তাদেরকে",
    "তাহাদিগের": "তাদের",
    "যদ্দারা": "যার দ্বারা / যাতে",
    "চালাইয়া": "চালিয়ে",
    "থাকিতে": "থাকতে",
    "দর্শাইতে": "দর্শাতে",
    "করিলে": "করলে",
    "হইলে": "হলে",
    # Sadhu pronouns
    "তাহার": "তার",
    "তাহাকে": "তাকে",
    "তাহাদের": "তাদের",
    "যাহার": "যার",
    "যাহারা": "যারা",
    "যাহাকে": "যাকে",
    "ইহার": "এর",
    "ইহারা": "এরা",
    "ইহাকে": "একে",
    "উহার": "ওর",
    "কাহার": "কার",
    "কাহারও": "কারও",
    "কেহ": "কেউ",
    "তাঁহার": "তাঁর",
    "তাঁহারা": "তাঁরা",
    "তাঁহাকে": "তাঁকে",
    "যাঁহারা": "যাঁরা",
    "যাঁহার": "যাঁর",
    # Sadhu finite verbs
    "করিব": "করব",
    "করিবে": "করবে",
    "করিবেন": "করবেন",
    "করিল": "করল",
    "করিলাম": "করলাম",
    "করিত": "করত",
    "করিতেছে": "করছে",
    "করিতেছেন": "করছেন",
    "করিতেছি": "করছি",
    "করিয়াছে": "করেছে",
    "করিয়াছেন": "করেছেন",
    "করিয়াছি": "করেছি",
    "যাইতেছে": "যাচ্ছে",
    "যাইতেছেন": "যাচ্ছেন",
    "যাইতেছি": "যাচ্ছি",
    "হইতেছে": "হচ্ছে",
    "হইত": "হতো",
    "গিয়াছে": "গিয়েছে",
    "গিয়াছেন": "গিয়েছেন",
    "দিয়াছে": "দিয়েছে",
    "দিয়াছেন": "দিয়েছেন",
    "বলিল": "বলল",
    "বলিলেন": "বললেন",
    "দেখিল": "দেখল",
    "দেখিলেন": "দেখলেন",
    "আসিল": "এল",
    "আসিলেন": "এলেন",
    "আসিলাম": "এলাম",
    "পাইলেন": "পেলেন",
    "ফিরিয়া": "ফিরে",
    "শুনিয়া": "শুনে",
    "চলিয়া": "চলে",
    "উঠিয়া": "উঠে",
    "থাকিয়া": "থেকে",
    "রাখিয়া": "রেখে",
    "জানিয়া": "জেনে",
    "পাইয়া": "পেয়ে",
    "গিয়া": "গিয়ে",
}

# Distinctively Cholito markers (excluding common/neutral verbs like 'ছিল', 'ছিলেন', 'হয়' that exist in Sadhu as well)
CHOLITO_MARKERS = {
    "করেছিল", "করেছিলেন", "এসে", "করে", "গিয়ে", "বলে", "দেখে",
    "খেয়ে", "নিয়ে", "যাবে", "হবে", "তারা", "ওরা",
    "সাথে", "বসে", "গিয়েছিল", "গিয়েছিলেন", "গেল", "গেলেন",
    "করল", "করলেন", "বলল", "বললেন", "খেল", "খেলেন",
    "এলো", "এলেন", "হলো", "হলেন",
    "পড়ে", "লিখে", "বলছেন", "রয়েছে", "করতে", "হয়েছে",
    "হয়ে", "থেকে", "এতে", "পারবে", "পারবেন",
    "দাও", "করো", "বলুন", "হোক", "পারেন", "পারে",
    "দেওয়া",
    "যাব", "যাবো", "খাব", "খাবো", "পাব", "পাবো", "দেব", "দেবো", "নেব", "নেবো",
    "যাবেন", "খাবেন", "পাবেন", "দেবেন", "নেবেন", "তার", "তাকে", "তাদের", "কেউ",
}

_BN_WORD = re.compile(r"[ঀ-৿]+")

# Sadhu finite verb morphology (perfect -িয়াছ-, progressive -িতেছ-) is not used in Cholito.
_SADHU_SUFFIX_PAT = re.compile(r"(?:ি|ই)(?:য়াছ|তেছ)(?:ে|েন|ি|িল|িলেন|িলাম|িস)$")

# Cholito finite verb morphology: perfect -েছ-, progressive -চ্ছ-/-ছ-, consonant-stem past -লেন/-লো, consonant-stem future -বো/-বেন.
_CONSONANT = r"[ক-হড়ঢ়য়]"
_CHOLITO_SUFFIX_PAT = re.compile(
    r"(?:েছ(?:ে|েন|ি|িল|িলেন|িলাম|িস|ো)"
    r"|চ্ছ(?:ে|েন|ি|িল|িলেন|িলাম|িস|ো)"
    rf"|{_CONSONANT}ছ(?:ে|েন|ি|িস|ো|িল|িলেন|িলাম)"
    rf"|{_CONSONANT}ল(?:েন|ো)"
    rf"|{_CONSONANT}ব(?:ো|েন))$"
)
_CHOLITO_SUFFIX_EXCLUSIONS = {"গুচ্ছে", "গুচ্ছো"}


# Productive Sadhu -> Cholito verb conversions (stem + Sadhu suffix + tense tail).
_SADHU_TO_CHOLITO_RULES = [
    (re.compile(r"^(.+)াইতেছ(.*)$"), r"\1াচ্ছ\2"),   # খাইতেছে -> খাচ্ছে
    (re.compile(r"^(.+)িতেছ(.*)$"), r"\1ছ\2"),      # করিতেছে -> করছে, লিখিতেছিল -> লিখছিল
]
# Perfect -িয়াছ- -> -েছ- is regular only when the stem has no আ-kar (পারিয়াছে -> পেরেছে mutates).
_SADHU_PERFECT_PAT = re.compile(r"^([^\u09BE]+)িয়াছ(.*)$")


# Sadhu forms that also occur in formal or Bangladeshi Cholito: converted only on explicit request,
# never reported as Guru-chandali.
# অদ্য and ঐ survive in legal/official Cholito formulas ("এই চুক্তিপত্র অদ্য ... সম্পাদিত হলো").
_NOT_REPORTED = AMBIGUOUS_FORMS | CONTEXT_INFINITIVES | {"নিমিত্ত", "এরূপ", "সেরূপ", "যেরূপ", "কিরূপ", "অদ্য", "ঐ"}
# 'হইতে' is the infinitive 'হতে' before these verbs, otherwise the postposition 'থেকে'.
_HOITE_INFINITIVE_NEXT = ("পার", "লাগ", "চা", "হই", "হব", "হবে", "দাও", "দিন", "দে", "থাক")
# Motion verbs (গেল, যাই) are left out: "বাড়িতে গেল" is "went home", not an infinitive.
_INFINITIVE_NEXT = _HOITE_INFINITIVE_NEXT + ("শুরু", "আরম্ভ")


def sadhu_to_cholito(token: str, next_token: str = ""):
    """Cholito form of a Sadhu token (paradigm table, dictionary, then suffix rule); None when not derivable."""
    if token == "হইতে":
        return "হতে" if next_token.startswith(_HOITE_INFINITIVE_NEXT) else "থেকে"
    if token in CONTEXT_INFINITIVES and not next_token.startswith(_INFINITIVE_NEXT):
        return None
    if token in SADHU_FORMS:
        return SADHU_FORMS[token]
    if token in SADHU_MARKERS:
        return SADHU_MARKERS[token].split("/")[0].strip()
    for pat, repl in _SADHU_TO_CHOLITO_RULES:
        if pat.match(token):
            return pat.sub(repl, token)
    if _SADHU_PERFECT_PAT.match(token):
        return _SADHU_PERFECT_PAT.sub(r"\1েছ\2", token)
    return None


def convert_to_cholito(text: str) -> tuple[str, list[dict], list[str]]:
    """Converts every recognised Sadhu form in text to Promito Cholito.
    Returns (converted_text, changes, unresolved_sadhu_tokens)."""
    matches = list(_BN_WORD.finditer(text))
    out, changes, unresolved, last = [], [], [], 0
    for idx, m in enumerate(matches):
        tok = m.group(0)
        if not (is_sadhu_token(tok) or tok in SADHU_FORMS):
            continue
        nxt = matches[idx + 1].group(0) if idx + 1 < len(matches) else ""
        new = sadhu_to_cholito(tok, nxt)
        if not new:
            if is_sadhu_token(tok):
                unresolved.append(tok)
            continue
        out.append(text[last:m.start()])
        out.append(new)
        last = m.end()
        changes.append({"sadhu": tok, "cholito": new})
    out.append(text[last:])
    return "".join(out), changes, list(dict.fromkeys(unresolved))


def is_word_in_text(word: str, text: str) -> bool:
    pattern = r"(?<![ঀ-৿])" + re.escape(word) + r"(?![ঀ-৿])"
    return bool(re.search(pattern, text))


def is_sadhu_token(token: str) -> bool:
    if token in _NOT_REPORTED:
        return False
    return token in SADHU_MARKERS or token in SADHU_FORMS or bool(_SADHU_SUFFIX_PAT.search(token))


def is_cholito_token(token: str) -> bool:
    if token in CHOLITO_MARKERS:
        return True
    return token not in _CHOLITO_SUFFIX_EXCLUSIONS and bool(_CHOLITO_SUFFIX_PAT.search(token))


def find_style_tokens(text: str) -> tuple[list[str], list[str]]:
    """Returns (sadhu_tokens, cholito_tokens) in order of appearance."""
    tokens = _BN_WORD.findall(text)
    return [t for t in tokens if is_sadhu_token(t)], [t for t in tokens if is_cholito_token(t)]


def check_guru_chandali(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        found_sadhu, found_cholito = find_style_tokens(line)

        # If both Sadhu and Cholito markers co-occur in the same line/sentence
        if found_sadhu and found_cholito:
            for s in dict.fromkeys(found_sadhu):
                col = line.find(s) + 1
                suggestion = SADHU_MARKERS.get(s)
                issues.append(LintIssue(
                    rule_id="RULE-LINT-GURU-CHANDALI",
                    message=f"গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('{s}') ও চলিত রীতির মিশ্রণ ঘটেছে।",
                    line=line_idx,
                    col=col,
                    severity=LintSeverity.ERROR,
                    matched_text=s,
                    suggestion=f"চলিত রূপে '{suggestion}' ব্যবহার করুন।" if suggestion else "এই সাধু ক্রিয়াপদটির চলিত রূপ ব্যবহার করুন।"
                ))

    return issues
