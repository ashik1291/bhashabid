# eval/benchmarks/fp_audit.py
# False-positive audit: run lint + repair on text that is presumed clean native Bengali
# (e.g. Bengali Wikipedia) and report how often the engine objects.
# A flag is only a *candidate* false positive: a human must triage the sample file.
#
#   python eval/benchmarks/fp_audit.py corpus.jsonl [more.txt ...] [--out triage.md] [--sample 40]
import argparse
import io
import json
import os
import random
import sys
from collections import Counter

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from bhashabid.lint import lint_text
from bhashabid.normalize.punctuation import normalize_punctuation
from bhashabid.normalize.repair import repair_text
from bhashabid.normalize.unicode import canonicalize_unicode


def load_sentences(paths):
    out = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if p.endswith(".jsonl"):
                    try:
                        line = json.loads(line).get("text", "").strip()
                    except ValueError:
                        continue
                if line:
                    out.append(line)
    return out


def audit(sentences):
    flagged, altered, rules = [], [], Counter()
    for s in sentences:
        ids = [i.rule_id for i in lint_text(s)]
        if ids:
            flagged.append((s, ids))
            rules.update(set(ids))
        repaired, _ = repair_text(s)
        if repaired != normalize_punctuation(canonicalize_unicode(s)):
            altered.append((s, repaired))
    n = max(1, len(sentences))
    return {
        "n": len(sentences),
        "flag_rate": len(flagged) / n,
        "alter_rate": len(altered) / n,
        "rules": rules,
        "flagged": flagged,
        "altered": altered,
    }


def render(res, sample, seed=7):
    rnd = random.Random(seed)
    L = [
        "# False-positive audit (candidate FPs need human triage)",
        "",
        f"- sentences: **{res['n']}**",
        f"- lint flag rate: **{res['flag_rate']:.1%}** ({len(res['flagged'])})",
        f"- repair alteration rate (beyond Unicode/punctuation): **{res['alter_rate']:.1%}** ({len(res['altered'])})",
        "- Presumed-clean text may contain real errors; confirm each sample before counting it as a false positive.",
        "",
        "## Flags by rule",
        "",
    ]
    L += [f"- `{r}`: {c}" for r, c in res["rules"].most_common()] or ["- none"]
    L += ["", "## Flagged sample (mark each TP / FP)", ""]
    for s, ids in rnd.sample(res["flagged"], min(sample, len(res["flagged"]))):
        L.append(f"- [ ] `{', '.join(ids)}` — {s}")
    L += ["", "## Repair-altered sample (mark each OK / WRONG)", ""]
    for s, r in rnd.sample(res["altered"], min(sample, len(res["altered"]))):
        L.append(f"- [ ] {s}\n  - → {r}")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--out", default=None)
    ap.add_argument("--sample", type=int, default=40)
    a = ap.parse_args()
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    md = render(audit(load_sentences(a.paths)), a.sample)
    if a.out:
        with open(a.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(md)
    print(md)


if __name__ == "__main__":
    main()
