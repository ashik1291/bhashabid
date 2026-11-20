# bhashabid/lint/learned.py
# Human-approved word/phrase replacements from the learning loop (assets/learned/replacements.json).
import json
import os
import re
from functools import lru_cache

from .models import LintIssue, LintSeverity
from ..normalize.unicode import canonicalize_unicode

_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "learned", "replacements.json")
_B_L = r"(?<![ঀ-৿\w])"
_B_R = r"(?![ঀ-৿\w])"


@lru_cache(maxsize=1)
def learned_replacements():
    """[(compiled pattern, wrong, right)] longest first; empty when no replacement has been approved."""
    try:
        with open(_PATH, encoding="utf-8") as f:
            items = json.load(f)
    except (OSError, ValueError):
        return []
    out = []
    for it in items:
        wrong, right = canonicalize_unicode(it.get("wrong", "")).strip(), canonicalize_unicode(it.get("right", "")).strip()
        if wrong and right and wrong != right:
            pat = re.compile(_B_L + r"\s+".join(re.escape(w) for w in wrong.split()) + _B_R)
            out.append((pat, wrong, right))
    return sorted(out, key=lambda x: -len(x[1]))


def check_learned(text: str) -> list:
    issues = []
    for line_idx, line in enumerate(text.splitlines(), start=1):
        for pat, wrong, right in learned_replacements():
            for m in pat.finditer(line):
                issues.append(LintIssue(
                    rule_id="RULE-LINT-LEARNED",
                    message=f"শিখে নেওয়া সংশোধন: '{wrong}' এর বদলে '{right}' ব্যবহার করুন।",
                    line=line_idx, col=m.start() + 1, severity=LintSeverity.WARNING,
                    matched_text=m.group(0), suggestion=right,
                ))
    return issues


def apply_learned(text: str):
    """Returns (text, [(wrong, right)]) after applying approved replacements."""
    applied = []
    for pat, wrong, right in learned_replacements():
        if pat.search(text):
            text = pat.sub(right, text)
            applied.append((wrong, right))
    return text, applied
