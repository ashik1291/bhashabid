# eval/benchmarks/heldout_curve.py
# Learning-curve logger. Evaluates the engine on a FROZEN held-out set and appends one row per run
# (git revision, approved-learning artefact counts, recall/FP) to eval/reports/heldout_curve.jsonl.
# Run it before and after each batch of human-approved learn-apply changes; the held-out set must never be
# used to author rules (see eval/heldout/README.md). Without that, a rising curve is overfitting, not learning.
#
#   python eval/benchmarks/heldout_curve.py [--heldout eval/heldout/heldout.jsonl] [--label "after batch 3"]
import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, HERE)
from engine_accuracy import evaluate, load_gold  # noqa: E402

LEARNED = os.path.join(REPO_ROOT, "bhashabid", "assets", "learned")
LOG = os.path.join(REPO_ROOT, "eval", "reports", "heldout_curve.jsonl")


def _lines(path):
    try:
        with open(path, encoding="utf-8") as f:
            return sum(1 for l in f if l.strip() and not l.startswith("#"))
    except OSError:
        return 0


def _git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heldout", default=os.path.join(REPO_ROOT, "eval", "heldout", "heldout.jsonl"))
    ap.add_argument("--label", default="")
    a = ap.parse_args()
    if not os.path.isfile(a.heldout):
        sys.exit(f"held-out set not found: {a.heldout} (see eval/heldout/README.md)")
    with open(a.heldout, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()[:16]
    res = evaluate(load_gold(a.heldout))
    row = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "label": a.label,
        "git": _git("rev-parse", "--short", "HEAD"),
        "dirty": bool(_git("status", "--porcelain", "--", "bhashabid")),
        "heldout_sha256_16": digest,
        "learned": {
            "lexicon_additions": _lines(os.path.join(LEARNED, "lexicon_additions.txt")),
            "replacements": len(json.load(open(os.path.join(LEARNED, "replacements.json"), encoding="utf-8")))
            if os.path.isfile(os.path.join(LEARNED, "replacements.json")) else 0,
        },
        "recall": {k: {"hit": v["hit"], "total": v["total"], "recall": v["recall"]} for k, v in res["recall"].items()},
        "clean": {
            "total": res["clean"]["total"],
            "lint_fp_rate": res["clean"]["lint_fp_rate"],
            "repair_alteration_rate": res["clean"]["repair_alteration_rate"],
        },
    }
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps(row, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
