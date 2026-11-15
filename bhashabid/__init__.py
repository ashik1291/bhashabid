"""
Bhashabid (ভাষাবিদ) — Deterministic Bengali Linguistic Coprocessor Engine
Pure-Python, Zero-LLM, High-Throughput Bengali Natural Language Processor.
"""

from tools.bn_normalize.repair import repair_text as repair
from tools.bn_normalize.normalizer import normalize, normalize_text
from tools.bn_normalize.unicode import canonicalize_unicode, is_nfc_normalized
from tools.bn_lint.linter import lint_text as lint
from tools.bn_normalize.lexicon import get_default_lexicon, bengali_edit_distance
from tools.bn_numbers import format_lakh_crore as format_number, number_to_bangla_words, format_currency_words
from tools.bn_prosody import scan_line, verify_payar

__version__ = "1.0.0"

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
    "lint",
    "spellcheck",
    "format_number",
    "number_to_bangla_words",
    "format_currency_words",
    "scan_line",
    "verify_payar",
    "get_default_lexicon",
    "bengali_edit_distance",
    "__version__"
]
