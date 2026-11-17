# tools/bn_lint/grammar.py
# Grammatical Defect & Pleonasm Linter (দ্বৈত বহুবচন, বাহুল্য প্রত্যয়, প্রত্যয়ঘটিত অপপ্রয়োগ)
import re
from .models import LintIssue, LintSeverity

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# 1. Double plural patterns (সব/সকল + গণ/বৃন্দ/সমূহ)
DOUBLE_PLURAL_PATS = [
    (re.compile(B_L + r"(সব|সকল)\s+([\u0980-\u09FF]+)(গণ|বৃন্দ|সমূহ)" + B_R),
     "দ্বৈত বহুবচনজনিত বাহুল্য দোষ: বহুবচনবাচক পদের সাথে অতিরিক্ত বহুবচন প্রত্যয় বর্জনীয়।")
]

# 2. Pleonasms
PLEONASM_PATS = [
    (re.compile(B_L + r"প্রায়শই" + B_R),
     "বাহুল্য প্রত্যয়জনিত অপপ্রয়োগ: 'প্রায়শ' শব্দের সাথে অতিরিক্ত 'ই' প্রত্যয় বর্জনীয়।",
     "'প্রায়শ' অথবা 'প্রায়ই'")
]

# 3. Affix defects
AFFIX_DEFECT_PATS = [
    (re.compile(B_L + r"একত্রিত\s+(করে|হয়ে|হওয়ার)" + B_R),
     "প্রত্যয়ঘটিত অপপ্রয়োগ: 'একত্র' স্বয়ংসম্পূর্ণ বিশেষণ, অতিরিক্ত 'ইত' প্রত্যয় যোগ অশুদ্ধ।",
     "একত্র \\1"),
    (re.compile(B_L + r"একত্রিতভাবে" + B_R),
     "প্রত্যয়ঘটিত অপপ্রয়োগ: 'একত্রিতভাবে' এর পরিবর্তে 'একত্রে' ব্যবহার্য।",
     "একত্রে")
]

# 4. Sandhi & Orthographic grammar defects
SANDHI_DEFECT_PATS = [
    (re.compile(B_L + r"উপরোক্ত" + B_R),
     "সন্ধিঘটিত অপপ্রয়োগ: ব্যাকরণসিদ্ধ রূপ 'উপরি-উক্ত' বা 'উপরিউক্ত'।",
     "উপরি-উক্ত"),
    (re.compile(B_L + r"ইতোপূর্বে" + B_R),
     "সন্ধিঘটিত অপপ্রয়োগ: শুদ্ধ রূপ 'ইতিপূর্বে'।",
     "ইতিপূর্বে")
]

# 5. Relative-correlative number concordance
CONCORDANCE_PATS = [
    (re.compile(B_L + r"যেসব\s+([\u0980-\u09FF\s,]+?)\s+তার\s+সমাধান(?=(?:ের|ে)?" + B_R + ")"),
     "বচন সংগতিহীনতা: 'যেসব' বহুবচন সাপেক্ষ সর্বনামের সাথে 'তার' এর বদলে বহুবচন রূপ বাঞ্ছনীয়।",
     "যেসব \\1 সেগুলোর সমাধান")
]

def check_grammar_defects(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        # 1. Double plural
        for pat, msg in DOUBLE_PLURAL_PATS:
            for m in pat.finditer(line):
                determiner = m.group(1)
                noun = m.group(2)
                suffix = m.group(3)
                matched = m.group(0)
                opt1 = f"{determiner} {noun}"
                opt2 = f"{noun}{suffix}"
                issues.append(LintIssue(
                    rule_id="RULE-GRAMMAR-DOUBLE-PLURAL",
                    message=msg,
                    line=line_idx,
                    col=m.start() + 1,
                    severity=LintSeverity.WARNING,
                    matched_text=matched,
                    suggestion=f"বিকল্প ১: '{opt1}' অথবা বিকল্প ২: '{opt2}'"
                ))

        # 2. Pleonasm
        for pat, msg, sugg in PLEONASM_PATS:
            for m in pat.finditer(line):
                issues.append(LintIssue(
                    rule_id="RULE-GRAMMAR-PLEONASM",
                    message=msg,
                    line=line_idx,
                    col=m.start() + 1,
                    severity=LintSeverity.WARNING,
                    matched_text=m.group(0),
                    suggestion=sugg
                ))

        # 3. Affix defects
        for pat, msg, sugg in AFFIX_DEFECT_PATS:
            for m in pat.finditer(line):
                matched = m.group(0)
                if "\\1" in sugg and m.groups():
                    fixed = m.expand(sugg)
                else:
                    fixed = sugg
                issues.append(LintIssue(
                    rule_id="RULE-GRAMMAR-AFFIX",
                    message=msg,
                    line=line_idx,
                    col=m.start() + 1,
                    severity=LintSeverity.WARNING,
                    matched_text=matched,
                    suggestion=f"প্রমিত রূপ: '{fixed}'"
                ))

        # 4. Sandhi defects
        for pat, msg, sugg in SANDHI_DEFECT_PATS:
            for m in pat.finditer(line):
                issues.append(LintIssue(
                    rule_id="RULE-GRAMMAR-SANDHI",
                    message=msg,
                    line=line_idx,
                    col=m.start() + 1,
                    severity=LintSeverity.WARNING,
                    matched_text=m.group(0),
                    suggestion=f"শুদ্ধ রূপ: '{sugg}'"
                ))

        # 5. Concordance
        for pat, msg, sugg in CONCORDANCE_PATS:
            for m in pat.finditer(line):
                fixed = m.expand(sugg)
                issues.append(LintIssue(
                    rule_id="RULE-GRAMMAR-CONCORDANCE",
                    message=msg,
                    line=line_idx,
                    col=m.start() + 1,
                    severity=LintSeverity.INFO,
                    matched_text=m.group(0),
                    suggestion=f"বচন সংগতিশীল রূপ: '{fixed}'"
                ))

    return issues
