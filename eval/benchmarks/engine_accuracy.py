# eval/benchmarks/engine_accuracy.py
# Measures the deterministic linter/repair engine against the labelled gold set (no LLM involved).
import argparse
import io
import json
import os
import sys
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from bhashabid.lint import lint_text
from bhashabid.normalize.repair import repair_text
from bhashabid.normalize.unicode import canonicalize_unicode
from bhashabid.normalize.punctuation import normalize_punctuation

GOLD_PATH = os.path.join(REPO_ROOT, "eval", "gold", "engine_gold.jsonl")

RULE_FAMILIES = {
    "guru_chandali": ("RULE-LINT-GURU-CHANDALI",),
    "honorific": ("RULE-LINT-HONORIFIC-", "RULE-LINT-PERSON-"),
    "calque": ("RULE-LINT-CALQUE",),
}


def load_gold(path: str = GOLD_PATH) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def evaluate(items: list[dict]) -> dict:
    per_label = defaultdict(lambda: {"total": 0, "hit": 0, "misses": [], "repaired": 0})
    clean = {"total": 0, "lint_false_positives": [], "repair_alterations": []}
    per_sector = defaultdict(lambda: {"total": 0, "correct": 0})

    for it in items:
        text, label = it["text"], it["label"]
        rule_ids = [i.rule_id for i in lint_text(text)]
        if label == "clean":
            clean["total"] += 1
            repaired, _ = repair_text(text)
            ok = not rule_ids
            if not ok:
                clean["lint_false_positives"].append({"id": it["id"], "rules": rule_ids})
            # Intended punctuation normalization (curly quotes, Dari) is not counted as an alteration.
            if repaired != normalize_punctuation(canonicalize_unicode(text)):
                ok = False
                clean["repair_alterations"].append({"id": it["id"], "repaired": repaired})
        else:
            prefixes = RULE_FAMILIES[label]
            ok = any(r.startswith(prefixes) for r in rule_ids)
            stats = per_label[label]
            stats["total"] += 1
            stats["hit"] += ok
            repaired, _ = repair_text(text)
            stats["repaired"] += not any(i.rule_id.startswith(prefixes) for i in lint_text(repaired))
            if not ok:
                stats["misses"].append(it["id"])
        per_sector[it["sector"]]["total"] += 1
        per_sector[it["sector"]]["correct"] += ok

    return {
        "recall": {
            k: {**v, "recall": round(v["hit"] / v["total"], 3), "repair_rate": round(v["repaired"] / v["total"], 3)}
            for k, v in per_label.items()
        },
        "clean": {
            **clean,
            "lint_fp_rate": round(len(clean["lint_false_positives"]) / clean["total"], 3),
            "repair_alteration_rate": round(len(clean["repair_alterations"]) / clean["total"], 3),
        },
        "per_sector": {k: {**v, "accuracy": round(v["correct"] / v["total"], 3)} for k, v in sorted(per_sector.items())},
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic engine accuracy on eval/gold/engine_gold.jsonl")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    res = evaluate(load_gold())
    out = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8") if hasattr(sys.stdout, "buffer") else sys.stdout
    if args.json:
        out.write(json.dumps(res, ensure_ascii=False, indent=2) + "\n")
    else:
        out.write("| Rule family | Detected | Recall | Auto-repaired |\n|---|---|---|---|\n")
        for k, v in res["recall"].items():
            out.write(f"| {k} | {v['hit']}/{v['total']} | {v['recall']:.0%} | {v['repaired']}/{v['total']} ({v['repair_rate']:.0%}) |\n")
        c = res["clean"]
        out.write(f"| clean: lint false positives | {len(c['lint_false_positives'])}/{c['total']} | FP rate {c['lint_fp_rate']:.0%} | |\n")
        out.write(f"| clean: repair altered text | {len(c['repair_alterations'])}/{c['total']} | {c['repair_alteration_rate']:.0%} | |\n")
        out.write("\n| Sector | Correct | Accuracy |\n|---|---|---|\n")
        for k, v in res["per_sector"].items():
            out.write(f"| {k} | {v['correct']}/{v['total']} | {v['accuracy']:.0%} |\n")
        for k, v in res["recall"].items():
            if v["misses"]:
                out.write(f"\nMissed {k}: {', '.join(v['misses'])}")
        for fp in c["lint_false_positives"]:
            out.write(f"\nFP {fp['id']}: {fp['rules']}")
        for ra in c["repair_alterations"]:
            out.write(f"\nRepair altered {ra['id']}: {ra['repaired']}")
        out.write("\n")
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
