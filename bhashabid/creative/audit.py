# bhashabid/creative/audit.py
# Deterministic Literary & Poetic Quality Auditor
import re
from typing import List, Dict, Any, Optional
from .lapidary import check_transliteration_surrenders
try:
    from ..lint import lint_text
except ImportError:
    try:
        from ..bn_lint import lint_text
    except ImportError:
        from bhashabid.lint import lint_text

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# Specific literary hallucination rules
LITERARY_HALLUCINATION_PATTERNS = [
    # Biological realism: Jellyfish do not have wings
    (
        re.compile(B_L + r"জেলি[-]?ফিশ[\u0980-\u09FF]*\s+.*ডানা" + B_R, re.IGNORECASE),
        "শারীরবৃত্তীয় বিভ্রান্তি: জেলিফিশের ডানা থাকে না; প্রাণীটির ছাতার মতো অংশকে 'ছত্র' বলা হয় এবং এর চলন হলো 'সংকোচন-প্রসারণ (খোলে ও বুজে যায়)'।"
    ),
    (
        re.compile(B_L + r"ডানা\s+মে[\u0980-\u09FF]*\s+.*জেলি[-]?ফিশ" + B_R, re.IGNORECASE),
        "শারীরবৃত্তীয় বিভ্রান্তি: জেলিফিশের ক্ষেত্রে 'ডানা মেলা' বৈজ্ঞানিকভাবে ত্রুটিপূর্ণ। 'খোলে ও বুজে যায়' বা 'স্পন্দিত ছত্র' বাঞ্ছনীয়।"
    ),
    # Metaphor drift: Intent/resolve into romantic passion
    (
        re.compile(B_L + r"(?:অভিপ্রায়|সংকল্প|সিদ্ধান্ত)[\u0980-\u09FF]*\s+(?:ত্যাগ|বর্জন)[\u0980-\u09FF]*\s+.*বাসনা" + B_R),
        "শব্দার্থিক বিচ্যুতি: সচেতন সংকল্প বা বৈজ্ঞানিক ইচ্ছাকে 'বাসনা' (রোমান্টিক ব্যাকুলতা) রূপান্তর করলে রচনার গাম্ভীর্য ক্ষুণ্ণ হয়; 'অভিপ্রায়' বা 'সংকল্প' ব্যবহার করুন।"
    ),
]

PADDING_PARTICLES_PATTERN = re.compile(
    B_L + r"(?:কখনো\s+কখনো|তুমিও|যেন\s+যেন|একটি\s+একটি)" + B_R
)

def audit_literary_text(text: str, archetype: str = "general") -> Dict[str, Any]:
    """
    Performs a deterministic multi-pass audit on literary Bengali text:
    1. Grammatical & Guru-chandali purity (via core linter).
    2. Transliteration surrender detection (gemstones & nature).
    3. Biological & anatomical hallucination detection.
    4. Minimalist padding particle detection (for Archetype A).
    """
    results: Dict[str, Any] = {
        "status": "PASS",
        "archetype": archetype,
        "score": 100,
        "issues": [],
        "suggestions": []
    }
    
    # 1. Core Grammar & Calque Linting
    lint_issues = lint_text(text)
    for issue in lint_issues:
        results["issues"].append({
            "type": "LINT",
            "message": f"[{issue.severity.value}] {issue.message}",
            "suggestion": issue.suggestion,
            "line": issue.line
        })
        results["score"] -= 10
        
    # 2. Transliteration Surrenders (Gemstones, Minerals)
    surrenders = check_transliteration_surrenders(text)
    for s in surrenders:
        results["issues"].append({
            "type": "TRANSLITERATION_SURRENDER",
            "message": f"অপ্রয়োজনীয় ইংরেজি লিপ্যন্তর: '{s['term']}'। {s['reason']}।",
            "suggestion": s["suggestion"]
        })
        results["score"] -= 15

    # 3. Biological & Anatomical Hallucinations
    for pat, explanation in LITERARY_HALLUCINATION_PATTERNS:
        if pat.search(text):
            results["issues"].append({
                "type": "ANATOMICAL_HALLUCINATION",
                "message": explanation,
                "suggestion": "মূল পাঠের শারীরবৃত্তীয় সত্যতা বজায় রাখুন।"
            })
            results["score"] -= 20

    # 4. Archetype A (Minimalist/Imagist) Padding Particles
    if archetype.lower() in ("a", "imagist", "minimalist"):
        padding_matches = PADDING_PARTICLES_PATTERN.findall(text)
        if padding_matches:
            results["issues"].append({
                "type": "METRIC_PADDING",
                "message": f"চিত্রকল্পবাদী বা সংযত কবিতায় অনাহূত অলংকরণ পদ শনাক্ত হয়েছে: {padding_matches}",
                "suggestion": "বাক্যের মিতব্যয়িতা বজায় রেখে অনাবশ্যক পদ ছাঁটাই করুন।"
            })
            results["score"] -= 10

    if results["score"] < 70:
        results["status"] = "FAIL"
    elif results["score"] < 95:
        results["status"] = "WARNING"
        
    return results
