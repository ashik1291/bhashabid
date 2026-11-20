"""Builds the skill bundles:
  bhashabid-skill.zip / bhashabid.skill  claude.ai and API Agent Skill (rules + references + bundled engine)
  bhashabid-skill-text.zip               text-only (SKILL.md + references) for Gemini Gems, ChatGPT and
                                         claude.ai without code execution; no Python code or binary files

Layout: SKILL.md at the ZIP root, the format verified to upload on both claude.ai (Customize > Skills)
and Gemini (Customize > Skills):
  SKILL.md
  references/...
  scripts/bn.py            # bhashabid-skill.zip only: runner, python scripts/bn.py <command> ...
  scripts/bhashabid/...    # bhashabid-skill.zip only: pure-stdlib engine (no MCP server needed)
"""
import json
import os
import sys
import zipfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL_DIR = os.path.join(REPO, "skills", "bangla-expert")
PKG_DIR = os.path.join(REPO, "bhashabid")
SKILL_NAME = "bangla-expert"
OUTPUTS = ("bhashabid-skill.zip", "bhashabid.skill")
TEXT_OUTPUT = "bhashabid-skill-text.zip"
IDIOMS_JSON = os.path.join(PKG_DIR, "assets", "idioms", "bilingual_idioms.json")  # engine source of truth
# Generated into the skill and its packaged mirrors (installers copy these).
IDIOMS_MD_PATHS = [
    os.path.join(SKILL_DIR, "references", "idioms.md"),
    os.path.join(PKG_DIR, "assets", "skills", SKILL_NAME, "references", "idioms.md"),
    os.path.join(REPO, "tools", "assets", "skills", SKILL_NAME, "references", "idioms.md"),
]
CATEGORY_TITLES = {
    "PROVERB": "Proverbs", "COLLOQUIAL": "Everyday idioms", "BUSINESS": "Business",
    "ADMINISTRATIVE": "Administrative", "JOURNALISM": "Journalism", "LEGAL": "Legal",
    "CIVIC": "Civic services", "LITERARY": "Literary", "ACADEMIC": "Academic",
}

# Engine parts not needed inside the skill sandbox (MCP server, IDE installers, duplicated skill copies).
PKG_EXCLUDE_DIRS = {"__pycache__", "mcp", os.path.join("assets", "skills"), os.path.join("assets", "adapters")}
PKG_EXCLUDE_FILES = {"skill_installer.py", "py.typed"}

RUNNER = '''"""Bhashabid engine runner for sandboxes without the MCP server.
Usage: python scripts/bn.py <command> [args]   (same commands as the `bhashabid` CLI)
Examples:
  python scripts/bn.py date 2025-12-16 --bongabdo
  python scripts/bn.py number 1234567.50 --currency
  python scripts/bn.py prosody "পদ্মার ঢেউ ..." --verify-payar
  python scripts/bn.py lint "আপনার বাংলা লেখা"
  python scripts/bn.py repair "আপনার বাংলা লেখা"
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bhashabid.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
'''


def _skill_files():
    for root, dirs, files in os.walk(SKILL_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == "STANDALONE_ALL_IN_ONE.md":  # human copy-paste manual, not part of the skill
                continue
            full = os.path.join(root, f)
            yield full, os.path.relpath(full, SKILL_DIR)


def _engine_files():
    for root, dirs, files in os.walk(PKG_DIR):
        rel_root = os.path.relpath(root, PKG_DIR)
        dirs[:] = [d for d in dirs if d not in PKG_EXCLUDE_DIRS and os.path.join(rel_root, d).lstrip(".\\/") not in PKG_EXCLUDE_DIRS]
        for f in files:
            if f in PKG_EXCLUDE_FILES or f.endswith(".pyc"):
                continue
            full = os.path.join(root, f)
            yield full, os.path.join("scripts", "bhashabid", os.path.relpath(full, PKG_DIR))


def render_idioms_md() -> str:
    """Compact model-facing idiom list generated from the engine's JSON (no regex, ids or JSON syntax)."""
    with open(IDIOMS_JSON, encoding="utf-8") as f:
        items = json.load(f)
    lines = [
        "# English Idioms → Natural Bengali",
        "",
        "Translate idioms by meaning, never word for word. Format: English → natural Bengali (✗ literal calque to avoid).",
        "Apply only to figurative use; literal mentions stay literal (\"I ate a piece of cake\" → এক টুকরো কেক খেলাম).",
        "Generated from the engine's idiom table; the `lint`/`repair` tools detect and fix these calques.",
    ]
    order = list(CATEGORY_TITLES) + sorted({i["category"] for i in items} - set(CATEGORY_TITLES))
    for cat in order:
        group = sorted((i for i in items if i["category"] == cat), key=lambda i: i["english"].lower())
        if not group:
            continue
        lines += ["", f"## {CATEGORY_TITLES.get(cat, cat.title())}"]
        lines += [f"- {i['english']} → {i.get('gloss', i['natural_bengali'])} (✗ {i['flawed_calque']})" for i in group]
    return "\n".join(lines) + "\n"


def write_idioms_md() -> list:
    text = render_idioms_md()
    for path in IDIOMS_MD_PATHS:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    return IDIOMS_MD_PATHS


def build() -> list:
    write_idioms_md()
    entries = sorted(set(_skill_files()) | set(_engine_files()), key=lambda e: e[1])
    written = []
    for out in OUTPUTS:
        path = os.path.join(REPO, out)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for src, arc in entries:
                z.write(src, arc.replace(os.sep, "/"))
            z.writestr("scripts/bn.py", RUNNER)
        written.append(path)
    text_path = os.path.join(REPO, TEXT_OUTPUT)
    with zipfile.ZipFile(text_path, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in sorted(_skill_files(), key=lambda e: e[1]):
            z.write(src, arc.replace(os.sep, "/"))
    written.append(text_path)
    return written


if __name__ == "__main__":
    for p in build():
        print(f"{p} ({os.path.getsize(p) // 1024} KB)")
    sys.exit(0)
