# tools/bn_lint/spelling.py
# Offline Phonetic Spellcheck Integration for Bhashabid Linter
from typing import List, Tuple
from .models import LintIssue, LintSeverity
from ..bn_normalize.lexicon import get_default_lexicon

def _offset_to_line_col(text: str, offset: int) -> Tuple[int, int]:
    lines = text[:offset].split("\n")
    line = len(lines)
    col = len(lines[-1]) + 1
    return line, col

def check_spelling(text: str) -> List[LintIssue]:
    """
    Scans text with the 78k offline phonetic lexicon and generates LintIssue
    warnings for unrecognized or misspelled Bengali words with closest corrections.
    """
    if not text:
        return []

    lex = get_default_lexicon()
    spelling_errors = lex.audit_text(text)
    issues = []

    for err in spelling_errors:
        start_idx = err["span"][0]
        line, col = _offset_to_line_col(text, start_idx)
        suggestions = err.get("suggestions", [])
        primary_fix = err.get("primary_fix", suggestions[0] if suggestions else None)
        suggestions_str = ", ".join(suggestions[:3]) if suggestions else "কোনো প্রস্তাবনা পাওয়া যায়নি"

        issues.append(
            LintIssue(
                rule_id="RULE-LINT-SPELLING",
                message=f"সম্ভাব্য বানান ভুল: '{err['word']}'. প্রস্তাবিত শুদ্ধ রূপ: {suggestions_str}",
                line=line,
                col=col,
                severity=LintSeverity.WARNING,
                matched_text=err["word"],
                suggestion=primary_fix
            )
        )

    return issues
