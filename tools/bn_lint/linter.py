from .models import LintIssue, LintSeverity
from .guru_chandali import check_guru_chandali
from .honorifics import check_honorific_clash
from .calques import check_calques
from .spelling import check_spelling
from ..bn_normalize.unicode import canonicalize_unicode

def lint_text(
    text: str,
    profile: str = "bd_standard",
    include_spelling: bool = False
) -> list[LintIssue]:
    """
    Scans Bengali text for linguistic errors:
    1. Sadhu-Cholito mixing (Guru-chandali dosh).
    2. Pronoun-verb honorific clashes (আপনি/তুমি/তুই/তিনি/সে).
    3. English literal calques and awkward passive voice.
    4. Optional offline phonetic spelling mistakes (if include_spelling=True).
    Respects dialect profile ('bd_standard' or 'wb_standard').
    """
    if not text:
        return []

    text = canonicalize_unicode(text)
    issues = []
    issues.extend(check_guru_chandali(text))
    issues.extend(check_honorific_clash(text))
    issues.extend(check_calques(text, profile=profile))

    if include_spelling:
        issues.extend(check_spelling(text))

    return issues
