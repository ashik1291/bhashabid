"""Score manual vendor results.

python eval/vendor_test/score.py            # writes results/REPORT.md
python eval/vendor_test/score.py --blind    # writes blind/blind_sheet.md + blind/key.json for native raters
"""
import io
import json
import math
import os
import random
import re
import sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import bhashabid as b
from bhashabid.normalize.orthography import normalize_orthography
from bhashabid.normalize.punctuation import normalize_punctuation
from bhashabid.normalize.unicode import canonicalize_unicode as canon
from tasks import TASKS, TASKS_BY_ID

RES = os.path.join(D, "results")
KEYS = ["ascii_period", "guru", "honorific", "calque", "grammar", "orthography", "western_grouping", "percent_sign"]
SECTION = re.compile(r"^## (V\d+)[ \t]*\n(.*?)(?=^## V\d+|\Z)", re.S | re.M)


def parse(path):
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    return {m.group(1): canon(m.group(2).strip()) for m in SECTION.finditer(text) if m.group(2).strip()}


def bengali_lines(t):
    """Engine defect metrics only make sense on Bengali prose; drop lines dominated by Latin text (explanations, transliterations)."""
    keep = []
    for line in t.splitlines():
        bn = len(re.findall(r"[ঀ-৿]", line))
        la = len(re.findall(r"[A-Za-z]", line))
        if bn and bn >= la:
            keep.append(line)
    return "\n".join(keep)


def metrics(t):
    t = bengali_lines(t)
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


def run_check(task, text):
    if task["check"] is None:
        return None
    try:
        return bool(task["check"](text))
    except Exception:
        return False


def score(outs, repair):
    core = conv = ncore = nconv = 0
    defects = dict.fromkeys(KEYS, 0)
    per = {}
    for tid, text in outs.items():
        if tid not in TASKS_BY_ID:
            continue
        t = canon(b.repair(text)[0]) if repair else text
        for k, v in metrics(t).items():
            defects[k] += v
        task = TASKS_BY_ID[tid]
        ok = run_check(task, t)
        per[tid] = ok
        if ok is None:
            continue
        if task["convention"]:
            nconv += 1
            conv += ok
        else:
            ncore += 1
            core += ok
    return dict(core=core, ncore=ncore, conv=conv, nconv=nconv, defects=defects, per=per, answered=len(outs))


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def mcnemar_exact(a_only, b_only):
    """Two-sided exact McNemar p from discordant pairs (a passes/b fails vs the reverse)."""
    n = a_only + b_only
    if n == 0:
        return 1.0
    k = min(a_only, b_only)
    p = 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, p)


def paired(x, y):
    """x, y: {task: True/False/None}. Missing counts as fail. Returns (x_only, y_only, n_tasks)."""
    xo = yo = n = 0
    for t in TASKS:
        if t["check"] is None or t["convention"]:
            continue
        n += 1
        a, b_ = bool(x.get(t["id"])), bool(y.get(t["id"]))
        xo += a and not b_
        yo += b_ and not a
    return xo, yo, n


def report():
    files = sorted(f for f in os.listdir(RES) if f.endswith(".md") and f not in ("TEMPLATE.md", "REPORT.md"))
    if not files:
        print("no result files in", RES)
        return
    total_core = sum(1 for t in TASKS if t["check"] and not t["convention"])
    total_conv = sum(1 for t in TASKS if t["check"] and t["convention"])
    rows, grid = [], {}
    for fn in files:
        name = fn[:-3]
        outs = parse(os.path.join(RES, fn))
        for rep in (False, True):
            s = score(outs, rep)
            label = name + ("+repair" if rep else "")
            grid[label] = s["per"]
            rows.append((label, s))
    lines = [
        "# Vendor test report\n",
        f"Core checks: {total_core} tasks. Convention checks (Bhashabid/BD-standard, reported separately): {total_conv}. "
        f"Human-only tasks: {sum(1 for t in TASKS if t['check'] is None)}.\n",
        "Unanswered tasks count as failures in the denominators. `+repair` = same text after offline `bhashabid.repair` (no LLM).\n",
        "| run | answered | core pass | convention pass | engine defects | " + " | ".join(KEYS) + " |",
        "|---|---|---|---|---|" + "---|" * len(KEYS),
    ]
    for label, s in rows:
        lines.append(
            f"| {label} | {s['answered']}/{len(TASKS)} | {s['core']}/{total_core} | {s['conv']}/{total_conv} | "
            f"{sum(s['defects'].values())} | " + " | ".join(str(s["defects"][k]) for k in KEYS) + " |"
        )
    lines += ["", "## Pass rate with 95% Wilson CI (core checks; unanswered = fail)", "", "| run | pass | rate | 95% CI |", "|---|---|---|---|"]
    for label, s_ in rows:
        lo, hi = wilson(s_["core"], total_core)
        lines.append(f"| {label} | {s_['core']}/{total_core} | {s_['core'] / max(1, total_core):.0%} | {lo:.0%}-{hi:.0%} |")
    lines += ["", "## Paired comparisons (exact McNemar, two-sided; discordant tasks only)", "",
              "| comparison | only first passes | only second passes | p |", "|---|---|---|---|"]
    names = {l for l, _ in rows}
    pairs = []
    for l in sorted(names):
        v, _, c = l.partition("__")
        if c.startswith("base") and not c.endswith("+repair"):
            for other in ("skill", "tools"):
                if f"{v}__{other}" in names:
                    pairs.append((f"{v}__{other}", l))
        if not l.endswith("+repair") and f"{l}+repair" in names:
            pairs.append((f"{l}+repair", l))
    for a, b_ in pairs:
        xo, yo, _n = paired(grid[a], grid[b_])
        lines.append(f"| {a} vs {b_} | {xo} | {yo} | {mcnemar_exact(xo, yo):.3f} |")
    lines += ["", "With ~27 paired tasks only large effects reach p<0.05; report CIs and effect sizes, not just p.", ""]
    labels = [l for l, _ in rows]
    lines += ["", "| task | cat | " + " | ".join(labels) + " |", "|---|---|" + "---|" * len(labels)]
    for t in TASKS:
        cells = []
        for l in labels:
            v = grid[l].get(t["id"], "missing")
            cells.append("n/a" if v is None else "·" if v == "missing" else "✓" if v else "✗")
        lines.append(f"| {t['id']} | {t['cat']} | " + " | ".join(cells) + " |")
    md = "\n".join(lines) + "\n"
    with io.open(os.path.join(RES, "REPORT.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(md)
    print(md)


def blind():
    files = sorted(f for f in os.listdir(RES) if f.endswith(".md") and f not in ("TEMPLATE.md", "REPORT.md"))
    items = []
    for fn in files:
        for tid, text in parse(os.path.join(RES, fn)).items():
            items.append((tid, fn[:-3], text))
    random.Random(20261121).shuffle(items)
    os.makedirs(os.path.join(D, "blind"), exist_ok=True)
    key, out = {}, ["# Blind rating sheet. Rate each item 1-5 on: fluency, naturalness, register/honorific correctness, factual/number correctness.",
                    "# Do not look at key.json until all items are rated.\n"]
    for i, (tid, run, text) in enumerate(items, 1):
        code = f"B{i:04d}"
        key[code] = {"task": tid, "run": run}
        out.append(f"## {code} (task prompt: {TASKS_BY_ID[tid]['prompt']})\n\n{text}\n\nfluency=  naturalness=  register=  correctness=\n")
    with io.open(os.path.join(D, "blind", "blind_sheet.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    with io.open(os.path.join(D, "blind", "key.json"), "w", encoding="utf-8") as f:
        json.dump(key, f, ensure_ascii=False, indent=1)
    print(f"{len(items)} items -> blind/blind_sheet.md (+ key.json)")


if __name__ == "__main__":
    blind() if "--blind" in sys.argv else report()
