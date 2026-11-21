"""Generate TEST_CASES.md, results/TEMPLATE.md and ready/ paste files from tasks.py.
Run: python eval/vendor_test/build_pack.py
"""
import io
import os
import sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from tasks import TASKS

SKILL_DIR = os.path.join(D, "..", "..", "skills", "bangla-expert")
REFS = {
    "numerals": ["numerals.md"], "dates": ["numerals.md"], "calque": ["idioms.md"],
    "sadhu_cholito": ["grammar_registers.md"], "register": ["grammar_registers.md"],
    "orthography": ["orthography.md"], "convention": ["technical_terms.md", "orthography.md"],
    "poetry": ["creative_writing.md", "numerals.md"],
    "long_news": ["journalism_domains.md", "numerals.md"], "bangabda": ["numerals.md"], "amounts": ["numerals.md"],
    "sadhu_long": ["grammar_registers.md"], "payar4": ["numerals.md", "creative_writing.md"],
    "legal_long": ["constitutional_writs.md"], "sadhu2cholito_long": ["grammar_registers.md"],
}
SECTOR_REFS = {
    "Administrative Governance & Memos": ["official_letters.md"],
    "Constitutional Law & Writs": ["constitutional_writs.md"],
    "Land Conveyancing & Deeds": ["academic_legal_medical.md"],
    "Healthcare & Epidemiology": ["academic_legal_medical.md"],
}
NO_TOOLS = (
    "[Context: you have NO tools and NO code execution in this chat. "
    "Where the skill says to use a tool, use its rules and tables instead.]\n\n"
)


def _read(rel):
    with io.open(os.path.join(SKILL_DIR, rel), encoding="utf-8") as f:
        return f.read()


def ready_files():
    """One paste-ready file per task and condition. The skill condition pre-selects the reference the
    skill's routing table would pick (a small advantage over letting the model choose; noted in the report)."""
    out = os.path.join(D, "ready")
    os.makedirs(out, exist_ok=True)
    skill = _read("SKILL.md")
    for t in TASKS:
        refs = SECTOR_REFS.get(t["sector"], []) if t["cat"] == "official" else REFS.get(t["cat"], [])
        ref_txt = "\n\n".join(f"=== references/{r} ===\n" + _read("references/" + r) for r in refs)
        bodies = {
            "base": t["prompt"] + "\n",
            "skillcore": NO_TOOLS + "=== SKILL.md ===\n" + skill + "\n\n=== TASK ===\n" + t["prompt"] + "\n",
            "skill": NO_TOOLS + "=== SKILL.md ===\n" + skill + "\n\n" + ref_txt + "\n\n=== TASK ===\n" + t["prompt"] + "\n",
        }
        for name, body in bodies.items():
            with io.open(os.path.join(out, f"{t['id']}__{name}.txt"), "w", encoding="utf-8", newline="\n") as f:
                f.write(body)


def main():
    ready_files()
    out = [
        "# Bhashabid manual multi-vendor test pack\n",
        f"{len(TASKS)} frozen tasks. Checks are fixed in `tasks.py` before any result exists.\n",
        "## How to run\n",
        "1. Pick vendors (e.g. ChatGPT, Gemini). Same model tier for every condition of a vendor; write the exact model name down.",
        "2. Each task in a **fresh chat**, two conditions:",
        "   - `base`: paste `ready/Vxx__base.txt`.",
        "   - `skill`: paste `ready/Vxx__skill.txt` (skill + the reference the routing table selects + the task).",
        "   - `skillcore` (only if `skill` is too long to paste): `ready/Vxx__skillcore.txt` = SKILL.md + task, no reference. Record it as `<vendor>__skillcore.md`; never mix it with `skill` runs.",
        "3. Copy only the model's final Bengali answer. Do not edit it.",
        "4. Send the answer back in chat (or save `results/<vendor>__<condition>.md`, one `## Vxx` heading per task).",
        "5. Do not tune the skill or rules while testing.\n",
        "Tasks marked *(human only)* have no automatic check; they are for the native-speaker blind rating.\n",
        "## Tasks\n",
    ]
    tmpl = ["# Paste each model answer under its heading. Keep the `## Vxx` lines exactly.\n"]
    for t in TASKS:
        tag = " *(human only)*" if t["check"] is None else (" *(project convention)*" if t["convention"] else "")
        out.append(f"### {t['id']} · {t['cat']} · {t['sector']}{tag}\n")
        out.append("```text\n" + t["prompt"] + "\n```\n")
        tmpl.append(f"## {t['id']}\n\n\n")
    with io.open(os.path.join(D, "TEST_CASES.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    with io.open(os.path.join(D, "results", "TEMPLATE.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(tmpl))
    print("wrote TEST_CASES.md, results/TEMPLATE.md, ready/*.txt")


if __name__ == "__main__":
    main()
