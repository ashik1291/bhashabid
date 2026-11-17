"""
Bhashabid (ভাষাবিদ) — Deterministic Bengali Linguistic Coprocessor Engine
Pure-Python, Zero-LLM, High-Throughput Bengali Natural Language Processor.
"""

from .normalize.repair import repair_text as repair
from .normalize.normalizer import normalize, normalize_text
from .normalize.unicode import canonicalize_unicode, is_nfc_normalized
from .normalize.punctuation import normalize_punctuation
from .normalize.orthography import normalize_orthography
from .lint.linter import lint_text as lint
from .lint.spelling import check_spelling
from .normalize.lexicon import get_default_lexicon, bengali_edit_distance
from .numbers import (
    format_lakh_crore as format_number,
    number_to_bangla_words,
    format_currency_words,
    decimal_to_bangla_words,
    fraction_to_bangla_words,
    to_classical_ordinal,
    to_date_ordinal,
    to_bangla_digits,
    to_ascii_digits,
    format_date_bangla,
    format_date_bongabdo,
    gregorian_to_bongabdo,
    BENGALI_MONTHS
)
from .prosody import scan_line, verify_payar
from .legal import (
    WritType,
    determine_writ_type,
    generate_writ_prayer,
    DeedType,
    DeedSchedule,
    format_deed_schedule,
    generate_encumbrance_free_clause,
    generate_saf_kabala_clause
)

__version__ = "1.0.1"

def spellcheck(text_or_word: str):
    """
    Offline phonetic spellchecker.
    If a single word is provided, returns list of top correction suggestions.
    If a sentence/text is provided, returns list of flagged issue dictionaries.
    """
    lex = get_default_lexicon()
    text_or_word = text_or_word.strip()
    if " " in text_or_word:
        return lex.audit_text(text_or_word)
    return lex.suggest_corrections(text_or_word)

__all__ = [
    "repair",
    "normalize",
    "normalize_text",
    "canonicalize_unicode",
    "is_nfc_normalized",
    "normalize_punctuation",
    "normalize_orthography",
    "lint",
    "check_spelling",
    "spellcheck",
    "format_number",
    "number_to_bangla_words",
    "format_currency_words",
    "decimal_to_bangla_words",
    "fraction_to_bangla_words",
    "to_classical_ordinal",
    "to_date_ordinal",
    "to_bangla_digits",
    "to_ascii_digits",
    "format_date_bangla",
    "format_date_bongabdo",
    "gregorian_to_bongabdo",
    "BENGALI_MONTHS",
    "scan_line",
    "verify_payar",
    "get_default_lexicon",
    "bengali_edit_distance",
    "WritType",
    "determine_writ_type",
    "generate_writ_prayer",
    "DeedType",
    "DeedSchedule",
    "format_deed_schedule",
    "generate_encumbrance_free_clause",
    "generate_saf_kabala_clause",
    "__version__"
]
