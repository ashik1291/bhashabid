# Bengali Punctuation Normalization
import re

DARI = "\u0964"  # । (Bengali Dari)
DOUBLE_DARI = "\u0965" # ॥ (Bengali Double Dari)

# Regex to safely protect URLs, web domains, and email addresses from Dari conversion
URL_OR_EMAIL_PATTERN = re.compile(
    r"(?:https?://[^\s।]+|ftp://[^\s।]+|www\.[^\s।]+|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)"
)

def normalize_punctuation(text: str, convert_period_to_dari: bool = True) -> str:
    """
    Normalizes punctuation in Bengali text:
    1. Converts ASCII sentence-ending period (.) and ASCII pipe (|) to Bengali Dari (।) while strictly preserving:
       - Decimals (e.g. 3.14 or ৩.১৪)
       - Web URLs (e.g. https://www.tbsnews.net)
       - Email addresses (e.g. info@bangladesh.gov.bd)
       - Alphanumeric domain names and abbreviations (e.g. e.g., i.e., test.com)
       - Markdown table rows (| col1 | col2 |) and non-Bengali shell/bitwise pipes
    2. Collapses repeated consecutive Dari characters (।। -> ।).
    3. Enforces standard typographic spacing:
       - Removes redundant whitespace before punctuation (ভাত খাই । -> ভাত খাই।)
       - Enforces single whitespace after sentence terminators (।, ॥, !, ?) when followed by words
    4. Standardizes quotation marks to typographical curved quotes.
    """
    if not text:
        return ""

    # Protect URLs and email addresses using temporary token masking
    masked_items = []
    def _mask_url_or_email(match):
        raw = match.group(0)
        trailing_period = ""
        # If URL ends with a sentence-terminating dot (e.g. 'visit site.com.'), don't swallow the dot
        if raw.endswith("."):
            raw = raw[:-1]
            trailing_period = "."
        idx = len(masked_items)
        masked_items.append(raw)
        return f"__BHASHABID_URL_MASK_{idx}__{trailing_period}"

    text = URL_OR_EMAIL_PATTERN.sub(_mask_url_or_email, text)

    # 1. Convert ASCII pipe (|) used as Dari in Bengali text (protecting markdown tables and shell/code pipes)
    if re.search(r"[\u0980-\u09FF]", text):
        lines = text.split("\n")
        norm_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
                norm_lines.append(line)
            else:
                if re.search(r"[\u0980-\u09FF]", line):
                    line = re.sub(r"(?<=[\u0980-\u09FF])\s*\|+(?=[\s\u0980-\u09FF\n]|$)", DARI, line)
                    line = re.sub(r"(?<=[\u0980-\u09FF\s])\|+(?=[\s\u0980-\u09FF\n]|$)", DARI, line)
                norm_lines.append(line)
        text = "\n".join(norm_lines)

    # 2. Collapse multiple consecutive Daris (।। -> ।)
    text = re.sub(r"[\u0964]{2,}", DARI, text)

    # 3. Convert ASCII period (.) to Bengali Dari (।) where appropriate
    if convert_period_to_dari and re.search(r"[\u0980-\u09FF]", text):
        # 1. Do not convert if followed by ASCII/Bengali digit (decimals like 3.14, ৩.১৪)
        # 2. Do not convert if between ASCII alphanumeric characters (like site.com, node.js, e.g.)
        # 3. Only convert when preceded by Bengali word or at true sentence terminator
        def _replace_period(m):
            span_start = m.start()
            span_end = m.end()
            # Lookahead check for decimal
            after_char = text[span_end:span_end+1]
            if after_char and (after_char.isdigit() or "\u09E6" <= after_char <= "\u09EF"):
                return "."
            # Lookbehind and lookahead for ASCII domain/abbr (e.g. name.ext)
            before_char = text[span_start-1:span_start] if span_start > 0 else ""
            if before_char and after_char and before_char.isalnum() and after_char.isalpha():
                return "."
            return DARI

        text = re.sub(r"\.", _replace_period, text)

    # Restore protected URLs and email addresses
    for idx, original in enumerate(masked_items):
        text = text.replace(f"__BHASHABID_URL_MASK_{idx}__", original)

    # Clean space before sentence ending marks
    text = re.sub(r"\s+([\u0964\u0965!?,;:])", r"\1", text)

    # Enforce standard space after sentence terminators (।, ॥, !, ?) when directly followed by word characters
    terminators = r"[\u0964\u0965!?]"
    closer_chars = r"[\"'”’\)\}\]]"
    text = re.sub(f"({terminators})(?!\\s|{terminators}|{closer_chars}|$)", r"\1 ", text)
    text = re.sub(f"({terminators}{closer_chars}+)(?!\\s|{terminators}|{closer_chars}|$)", r"\1 ", text)

    # Standardize ASCII quotes to curved Bengali quotes
    # Opening double quote (preceded by start/space/dash/punctuation, followed by letter)
    text = re.sub(r'(^|[\s—,;:])"([\u0980-\u09FFA-Za-z\'])', r'\1“\2', text)
    # Closing double quote (preceded by letter/punctuation, followed by end/space/dash/punctuation)
    text = re.sub(r'([\u0980-\u09FFA-Za-z\u0964!?,.;\'])\"($|[\s—\u0964!?,.;])', r'\1”\2', text)

    return text
