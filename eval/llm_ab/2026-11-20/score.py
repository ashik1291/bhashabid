# Scores with-skill vs without-skill LLM outputs using deterministic checks only.
import io, json, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(D, "..", "..", "..")))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import bhashabid as b
from bhashabid.normalize.unicode import canonicalize_unicode as canon
from bhashabid.normalize.punctuation import normalize_punctuation
from bhashabid.normalize.orthography import normalize_orthography
from bhashabid.lint.guru_chandali import find_style_tokens

TASKS = {t["id"]: t for t in json.load(open(os.path.join(D, "tasks.json"), encoding="utf-8"))}
BN = r"[ঀ-৿]"


def has(t, *pats):
    return all(re.search(canon(p), t) for p in pats)


def payar_ok(t):
    lines = [l.strip() for l in t.splitlines() if re.search(BN, l)]
    return len(lines) >= 2 and all(b.verify_payar(re.sub(r"[।,;!?\-—]", " ", l)).is_valid_payar for l in lines[:2])


# Task-level correctness checks (fixed before scoring; T06/T07 widened after a scorer bug, see README).
CHECKS = {
    "T01": lambda t: has(t, r"(১,২৩,৪৫,৬৭,৮৯০|1,23,45,67,890|কোটি)", r"(১০\.৮৭|10\.87)"),
    "T02": lambda t: has(t, r"১২,৩৪,৫৬৭\.৫০", r"বারো লাখ", r"চৌত্রিশ হাজার", r"পাঁচ\s?(শত|শো)", r"সাতষট্টি", r"পঞ্চাশ পয়সা"),
    "T03": lambda t: canon("দ্বারা") not in t,
    "T04": lambda t: has(t, r"বরাবর", r"বিষয়") and canon("প্রিয়") not in t,
    "T05": lambda t: "TCK-942" in t and not re.search(r"(?<!" + BN + r")তুমি(?!" + BN + r")", t),
    "T06": lambda t: has(t, r"তুমি") and has(t, r"(তুই|তোর|িস(?!" + BN + r")|লি(?!" + BN + r"))"),
    "T07": lambda t: has(t, r"(১|১লা|পহেলা)\s*বৈশাখ", r"১৪৩৩", r"(?<![০-৯])(১|১লা)\s*পৌষ", r"১৪৩২"),
    "T08": lambda t: has(t, r"দেড়", r"আড়াই"),
    "T09": lambda t: has(t, r"রুল", r"(আইনগত কর্তৃত্ব|আইনানুগ কর্তৃত্ব)"),
    "T10": payar_ok,
    "T11": lambda t: True,
    "T12": lambda t: not find_style_tokens(t)[0] and canon("পড়ছিল") in t,
}
KEYS = ["ascii_period", "guru", "honorific", "calque", "grammar", "orthography", "western_grouping", "percent_sign"]


def metrics(t):
    issues = b.lint(t)
    fam = lambda pre: sum(1 for i in issues if i.rule_id.startswith(pre))
    return {
        "ascii_period": max(0, normalize_punctuation(t).count("।") - t.count("।")),
        "guru": fam("RULE-LINT-GURU"),
        "honorific": fam("RULE-LINT-HONORIFIC") + fam("RULE-LINT-PERSON"),
        "calque": fam("RULE-LINT-CALQUE"),
        "grammar": fam("RULE-GRAMMAR"),
        "orthography": sum(1 for a, c in zip(t.split(), normalize_orthography(t).split()) if a != c),
        "western_grouping": len(re.findall(r"[0-9০-৯]{1,3}(?:,[0-9০-৯]{3}){2,}", t)),
        "percent_sign": t.count("%"),
    }


def score(outputs, apply_repair):
    tot, passed = dict.fromkeys(KEYS, 0), {}
    for tid, text in outputs.items():
        text = canon(b.repair(text)[0] if apply_repair else text)
        for k, v in metrics(text).items():
            tot[k] += v
        passed[tid] = bool(CHECKS[tid](text))
    return tot, passed


rows = []
for model in ("haiku", "sonnet"):
    for cond in ("base", "skill"):
        outs = json.load(open(os.path.join(D, f"out_{model}_{cond}.json"), encoding="utf-8"))
        for rep in (False, True):
            rows.append((model, cond + ("+repair" if rep else ""), *score(outs, rep)))

print("| model | condition | task checks passed | engine-flagged defects | " + " | ".join(KEYS) + " |")
print("|---|---|---|---|" + "---|" * len(KEYS))
for m, c, tot, tp in rows:
    print(f"| {m} | {c} | {sum(tp.values())}/12 | {sum(tot.values())} | " + " | ".join(str(tot[k]) for k in KEYS) + " |")
print("\n| task | sector | " + " | ".join(f"{m}:{c}" for m, c, _, _ in rows) + " |")
print("|---|---|" + "---|" * len(rows))
for tid in TASKS:
    print(f"| {tid} | {TASKS[tid]['sector']} | " + " | ".join("✓" if tp[tid] else "✗" for *_, tp in rows) + " |")
