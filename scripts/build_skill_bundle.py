"""Builds the claude.ai / API Agent Skill bundle: bhashabid-skill.zip and bhashabid.skill.

Layout (claude.ai requires the skill folder at the ZIP root, named like the skill):
  bangla-expert/SKILL.md
  bangla-expert/references/...
  bangla-expert/scripts/bn.py            # runner: python scripts/bn.py <command> ...
  bangla-expert/scripts/bhashabid/...    # pure-stdlib engine (no MCP server needed)
"""
import os
import sys
import zipfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL_DIR = os.path.join(REPO, "skills", "bangla-expert")
PKG_DIR = os.path.join(REPO, "bhashabid")
SKILL_NAME = "bangla-expert"
OUTPUTS = ("bhashabid-skill.zip", "bhashabid.skill")

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
            yield full, os.path.join(SKILL_NAME, os.path.relpath(full, SKILL_DIR))


def _engine_files():
    for root, dirs, files in os.walk(PKG_DIR):
        rel_root = os.path.relpath(root, PKG_DIR)
        dirs[:] = [d for d in dirs if d not in PKG_EXCLUDE_DIRS and os.path.join(rel_root, d).lstrip(".\\/") not in PKG_EXCLUDE_DIRS]
        for f in files:
            if f in PKG_EXCLUDE_FILES or f.endswith(".pyc"):
                continue
            full = os.path.join(root, f)
            yield full, os.path.join(SKILL_NAME, "scripts", "bhashabid", os.path.relpath(full, PKG_DIR))


def build() -> list:
    entries = sorted(set(_skill_files()) | set(_engine_files()), key=lambda e: e[1])
    written = []
    for out in OUTPUTS:
        path = os.path.join(REPO, out)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for src, arc in entries:
                z.write(src, arc.replace(os.sep, "/"))
            z.writestr(f"{SKILL_NAME}/scripts/bn.py", RUNNER)
        written.append(path)
    return written


if __name__ == "__main__":
    for p in build():
        print(f"{p} ({os.path.getsize(p) // 1024} KB)")
    sys.exit(0)
