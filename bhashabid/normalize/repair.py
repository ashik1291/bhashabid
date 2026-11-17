# tools/bn_normalize/repair.py
# Deterministic Autonomous Bengali Linguistic Repair Engine
import re
from typing import Tuple, List, Dict, Optional

from .unicode import canonicalize_unicode
from .punctuation import normalize_punctuation
from .orthography import normalize_orthography
from ..lint.guru_chandali import SADHU_MARKERS, CHOLITO_MARKERS
from ..lint.honorifics import (
    THIRD_PERSON_ORDINARY_TO_HONORIFIC,
    THIRD_PERSON_HONORIFIC_TO_ORDINARY,
    TINI_CLASH_PAT,
    SE_CLASH_PAT,
    TUMI_CLASH_PAT,
    APNI_CLASH_PAT,
    AMI_CLASH_PAT,
    SECOND_PERSON_FIRST_VERB_PAT,
    FORMAL_TO_FAMILIAR_VERBS,
    FAMILIAR_TO_FORMAL_VERBS,
    NON_FIRST_TO_FIRST_VERBS,
    FIRST_TO_SECOND_FAMILIAR_VERBS,
    FIRST_TO_SECOND_FORMAL_VERBS
)

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# Pronoun stems where 'মত' denotes opinion/view rather than comparison
PRONOUN_OPINION_STEMS = {
    "আমার", "আমাদের", "তোমার", "তোমাদের", "তার", "তাদের", "তাঁর", "তাঁদের",
    "কার", "কাদের", "যার", "যাদের", "এর", "এদের", "ওর", "ওদের", "কারও", "কারো"
}

def _fix_similarity_moto(match):
    word = match.group(1)
    if word in PRONOUN_OPINION_STEMS:
        return match.group(0)  # Preserve untouched to prevent opinion ambiguity
    return f"{word} মতো"

# Deterministic canonical calque repairs (replaces unnatural machine translations with standard Bengali)
CANONICAL_CALQUE_REPAIRS = [
    # Causal / passive calques
    (re.compile(B_L + r"দ্বারা\s+সভাপতিত্ব[\u0980-\u09FF]*" + B_R), "সভাপতিত্বে অনুষ্ঠিত"),
    (re.compile(B_L + r"দ্বারা\s+সরবরাহ[\u0980-\u09FF]*" + B_R), "সরবরাহকৃত"),
    (re.compile(B_L + r"দ্বারা\s+অনুমোদিত" + B_R), "অনুমোদিত"),
    (re.compile(B_L + r"দ্বারা\s+চালিত" + B_R), "পরিচালিত"),
    (re.compile(B_L + r"দ্বারা\s+কৃত" + B_R), "সম্পাদিত"),
    # Legal & Judicial calques
    (re.compile(B_L + r"জিজ্ঞেস\s+করে\s+একটি\s+রুল\s+জারি\s+করেছে" + B_R), "রুল নিশি জারি করেছেন"),
    (re.compile(B_L + r"জিজ্ঞেস\s+করে\s+একটি\s+রুল" + B_R), "রুল নিশি"),
    # Academic & Corporate calques
    (re.compile(B_L + r"পেপারটি\s+তর্ক\s+করে" + B_R), "গবেষণাপত্রে যুক্তি উপস্থাপন করা হয়েছে"),
    (re.compile(B_L + r"গেম\s+চেঞ্জার" + B_R), "যুগান্তকারী সমাধান"),
    (re.compile(B_L + r"পেইন\s+পয়েন্ট" + B_R), "প্রধান সংকট"),
    (re.compile(B_L + r"ঝড়\s+বৃদ্ধি" + B_R), "জলোচ্ছ্বাস"),
    (re.compile(B_L + r"বড়\s+বিপদের\s+সংকেত" + B_R), "মহাবিপদ সংকেত"),
    (re.compile(B_L + r"বিক্রির\s+কাগজ" + B_R), "সাফ-কবলা বিক্রয় দলিল"),
    (re.compile(B_L + r"পোকা\s+মারার\s+ওষুধ" + B_R), "বালাইনাশক"),
    (re.compile(B_L + r"পরাজয়\s+স্বীকার\s+করেছে" + B_R), "পরাজিত হয়েছে"),
    # Best practice calque naturalization
    (re.compile(B_L + r"সর্বোত্তম\s+অনুশীলন(?:গুলো|সমূহ|গুলা)?" + B_R), "সর্বোত্তম চর্চা")
]

# Deterministic grammatical pleonasms and ungrammatical affix repairs (অপপ্রয়োগ ও বাহুল্য বর্জন)
CANONICAL_GRAMMAR_DEFECT_REPAIRS = [
    # Pleonasm: প্রায়শই -> প্রায়শ / প্রায়ই
    (re.compile(B_L + r"প্রায়শই" + B_R), "প্রায়শ", "বাহুল্য প্রত্যয় বর্জন: 'প্রায়শই' -> 'প্রায়শ'"),
    # Suffix defect: একত্রিত -> একত্র
    (re.compile(B_L + r"একত্রিত\s+করে" + B_R), "একত্র করে", "প্রত্যয়ঘটিত অপপ্রয়োগ নিবারণ: 'একত্রিত করে' -> 'একত্র করে'"),
    (re.compile(B_L + r"একত্রিত\s+হয়ে" + B_R), "একত্র হয়ে", "প্রত্যয়ঘটিত অপপ্রয়োগ নিবারণ: 'একত্রিত হয়ে' -> 'একত্র হয়ে'"),
    (re.compile(B_L + r"একত্রিতভাবে" + B_R), "একত্রে", "প্রত্যয়ঘটিত অপপ্রয়োগ নিবারণ: 'একত্রিতভাবে' -> 'একত্রে'"),
    # Relative-correlative number concordance: যেসব ... তার সমাধান -> যেসব ... সেগুলোর সমাধান
    (re.compile(B_L + r"যেসব\s+([\u0980-\u09FF\s,]+?)\s+তার\s+সমাধান(?=(?:ের|ে)?" + B_R + ")"), r"যেসব \1 সেগুলোর সমাধান", "বচন সংগতি: 'যেসব ... তার সমাধান' -> 'যেসব ... সেগুলোর সমাধান'"),
    # Journalistic & Bangla Academy standard: রবিবার -> রোববার
    (re.compile(B_L + r"রবিবার" + B_R), "রোববার", "গণমাধ্যম ও প্রমিত চলিত রীতি: 'রবিবার' -> 'রোববার'"),
    # Bangla Academy orthography: কারো কারো -> কারও কারও
    (re.compile(B_L + r"কারো\s+কারো" + B_R), "কারও কারও", "বাংলা একাডেমি প্রমিত বানানরীতি: 'কারো কারো' -> 'কারও কারও'"),
    # Word boundary separation: এছাড়া -> এ ছাড়া
    (re.compile(B_L + r"এছাড়া" + B_R), "এ ছাড়া", "বাংলা একাডেমি পদ পৃথকীকরণ: 'এছাড়া' -> 'এ ছাড়া'"),
    # Sandhi and ungrammatical forms
    (re.compile(B_L + r"উপরোক্ত" + B_R), "উপরি-উক্ত", "সন্ধিঘটিত অপপ্রয়োগ নিবারণ: 'উপরোক্ত' -> 'উপরি-উক্ত'"),
    (re.compile(B_L + r"ইতোপূর্বে" + B_R), "ইতিপূর্বে", "সন্ধিঘটিত অপপ্রয়োগ নিবারণ: 'ইতোপূর্বে' -> 'ইতিপূর্বে'"),
    # Double plural pleonasms (দ্বৈত বহুবচন)
    (re.compile(B_L + r"সব\s+([\u0980-\u09FF]+)গণ" + B_R), r"সব \1", "দ্বৈত বহুবচনজনিত বাহুল্য দোষ নিবারণ: 'সব ... গণ' -> 'সব ...'"),
    (re.compile(B_L + r"সকল\s+([\u0980-\u09FF]+)বৃন্দ" + B_R), r"সকল \1", "দ্বৈত বহুবচনজনিত বাহুল্য দোষ নিবারণ: 'সকল ... বৃন্দ' -> 'সকল ...'"),
]


def repair_text(text: str, profile: str = "bd_standard") -> Tuple[str, List[Dict]]:
    """
    Deterministic Bengali linguistic repair engine.
    Automatically repairs:
    1. Unicode decomposition and stray nuktas.
    2. Bangla Academy orthography & loanword standards.
    3. Punctuation standardization (Dari replacement outside URLs/numbers).
    4. Guru-chandali mixtures (harmonizes isolated Sadhu forms into Cholito).
    5. Unnatural English translation calques & machine proverbs.
    6. Honorific concordance mismatches.

    Returns:
        (repaired_text, applied_fixes)
    """
    if not text:
        return "", []

    # If text contains no Bengali characters, leave completely intact
    if not re.search(r"[\u0980-\u09FF]", text):
        return text, []

    applied_fixes = []
    current_text = canonicalize_unicode(text)

    # 1. Orthography loanword corrections
    norm_orth = normalize_orthography(current_text, profile=profile)
    if norm_orth != current_text:
        applied_fixes.append({
            "category": "ORTHOGRAPHY",
            "before": current_text,
            "after": norm_orth,
            "description": "Standardized Bangla Academy loanword orthography"
        })
        current_text = norm_orth

    # 2. Punctuation normalization
    norm_punc = normalize_punctuation(current_text)
    if norm_punc != current_text:
        applied_fixes.append({
            "category": "PUNCTUATION",
            "before": current_text,
            "after": norm_punc,
            "description": "Standardized Bengali Dari (।) and quotes"
        })
        current_text = norm_punc

    # 3. Canonical Calque Naturalization
    for pat, replacement in CANONICAL_CALQUE_REPAIRS:
        if pat.search(current_text):
            old = current_text
            current_text = pat.sub(replacement, current_text)
            applied_fixes.append({
                "category": "CALQUE_NATURALIZATION",
                "pattern": pat.pattern,
                "replacement": replacement,
                "description": f"Naturalized literal calque to '{replacement}'"
            })

    # 3b. Canonical Grammar Defect Repairs (Pleonasm, Affixes & Concordance)
    for pat, replacement, desc in CANONICAL_GRAMMAR_DEFECT_REPAIRS:
        if pat.search(current_text):
            current_text = pat.sub(replacement, current_text)
            applied_fixes.append({
                "category": "GRAMMATICAL_INVARIANT",
                "pattern": pat.pattern,
                "replacement": replacement,
                "description": desc
            })

    # 3c. Context-aware similarity 'মত' -> 'মতো' (leaves pronoun opinion stems 'আমার মত' untouched)
    sim_moto_pat = re.compile(r"(?<![\u0980-\u09FF])([\u0980-\u09FF]+(?:ের|র))\s+মত(?![\u0980-\u09FF])")
    if sim_moto_pat.search(current_text):
        new_text = sim_moto_pat.sub(_fix_similarity_moto, current_text)
        if new_text != current_text:
            applied_fixes.append({
                "category": "GRAMMATICAL_INVARIANT",
                "pattern": r"-র/-এর মত",
                "replacement": "-র/-এর মতো",
                "description": "সাদৃশ্যবাচক প্রত্যয় প্রমিতকরণ: '-র মত' -> '-র মতো'"
            })
            current_text = new_text

    # 3d. Safe High-Confidence Lexicon Typo Repairs (Homophone single candidate repairs)
    try:
        from .lexicon import get_default_lexicon
        lex = get_default_lexicon()
        typo_tokens = set(re.findall(r"[\u0980-\u09FF]{4,}", current_text))
        for token in typo_tokens:
            fixed_lemma = lex.find_high_confidence_repair(token)
            if fixed_lemma and fixed_lemma != token:
                token_pat = re.compile(B_L + re.escape(token) + B_R)
                if token_pat.search(current_text):
                    current_text = token_pat.sub(fixed_lemma, current_text)
                    applied_fixes.append({
                        "category": "ORTHOGRAPHY_PHONETIC",
                        "pattern": token,
                        "replacement": fixed_lemma,
                        "description": f"অফলাইন লেক্সিকন প্রমিত রূপ: '{token}' -> '{fixed_lemma}'"
                    })
    except Exception:
        pass

    # 4. Guru-Chandali Harmonization (Archaic Sadhu verbs in Cholito text)
    tokens = set(re.findall(r"[\u0980-\u09FF]+", current_text))
    has_cholito = bool(tokens.intersection(CHOLITO_MARKERS))
    has_sadhu = bool(tokens.intersection(set(SADHU_MARKERS.keys())))

    # In modern standard prose, if Cholito markers exist or default standard is requested, harmonise Sadhu
    if has_sadhu and (has_cholito or profile == "bd_standard"):
        for s_verb, c_verb in SADHU_MARKERS.items():
            # Only use strict single canonical Cholito verb (skip multi-suggestions with '/')
            c_target = c_verb.split("/")[0].strip()
            pattern = re.compile(B_L + re.escape(s_verb) + B_R)
            if pattern.search(current_text):
                current_text = pattern.sub(c_target, current_text)
                applied_fixes.append({
                    "category": "GURU_CHANDALI_HARMONIZATION",
                    "sadhu": s_verb,
                    "cholito": c_target,
                    "description": f"Harmonized Sadhu form '{s_verb}' to Promito Cholito '{c_target}'"
                })

    # 5. Honorific Concordance Repair
    # (a) TINI + ordinary verb -> TINI + honorific verb
    for m in list(TINI_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        hon_verb = THIRD_PERSON_ORDINARY_TO_HONORIFIC.get(verb, f"{verb}েন")
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{hon_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 3rd-person honorific '{subj}' with verb '{hon_verb}'"
        })

    # (b) SE + honorific verb -> SE + ordinary verb
    for m in list(SE_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        ord_verb = THIRD_PERSON_HONORIFIC_TO_ORDINARY.get(verb, verb)
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{ord_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 3rd-person ordinary '{subj}' with verb '{ord_verb}'"
        })

    # (c) APNI + informal verb -> APNI + formal verb
    for m in list(APNI_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        formal_verb = FAMILIAR_TO_FORMAL_VERBS.get(verb, f"{verb}েন")
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{formal_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 2nd-person formal '{subj}' with verb '{formal_verb}'"
        })

    # (d) TUMI + formal or intimate verb -> TUMI + familiar verb
    for m in list(TUMI_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        fam_verb = FORMAL_TO_FAMILIAR_VERBS.get(verb, verb)
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{fam_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 2nd-person familiar '{subj}' with verb '{fam_verb}'"
        })

    # (e) AMI / AMRA + non-first-person verb -> AMI / AMRA + first-person verb
    for m in list(AMI_CLASH_PAT.finditer(current_text)):
        middle = m.group(2)
        if re.search(r"(?<![\u0980-\u09FF])(?:আপনি|আপনারা|তুমি|তোমরা|তুই|তোরা|তিনি|তাঁরা|সে|তারা|কে|কারা)(?![\u0980-\u09FF])", middle):
            continue
        subj = m.group(1)
        verb = m.group(3)
        first_verb = NON_FIRST_TO_FIRST_VERBS.get(verb)
        if first_verb:
            old_clause = m.group(0)
            new_clause = f"{subj}{middle}{first_verb}"
            current_text = current_text.replace(old_clause, new_clause, 1)
            applied_fixes.append({
                "category": "PERSON_CONCORDANCE",
                "before": old_clause,
                "after": new_clause,
                "description": f"Concorded 1st-person '{subj}' with verb '{first_verb}'"
            })

    # (f) TUMI / APNI + first-person verb -> TUMI / APNI + 2nd-person verb
    for m in list(SECOND_PERSON_FIRST_VERB_PAT.finditer(current_text)):
        middle = m.group(2)
        if re.search(r"(?<![\u0980-\u09FF])(?:আমি|আমরা)(?![\u0980-\u09FF])", middle):
            continue
        subj = m.group(1)
        verb = m.group(3)
        if subj in ("তুমি", "তোমরা"):
            target_verb = FIRST_TO_SECOND_FAMILIAR_VERBS.get(verb)
        elif subj in ("আপনি", "আপনারা"):
            target_verb = FIRST_TO_SECOND_FORMAL_VERBS.get(verb)
        else:
            target_verb = None
        if target_verb:
            old_clause = m.group(0)
            new_clause = f"{subj}{middle}{target_verb}"
            current_text = current_text.replace(old_clause, new_clause, 1)
            applied_fixes.append({
                "category": "PERSON_CONCORDANCE",
                "before": old_clause,
                "after": new_clause,
                "description": f"Concorded 2nd-person '{subj}' with verb '{target_verb}'"
            })

    return current_text, applied_fixes
