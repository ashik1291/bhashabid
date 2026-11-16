#!/usr/bin/env bash
# Bhashabid (ভাষাবিদ) — Zero-Dependency Universal Skill & IDE Installer (macOS & Linux)
# Works 100% out of the box with or without Python installed!
set -euo pipefail

TARGET="${1:-all}"
WORKSPACE="${2:-}"

echo "================================================================="
echo "BHASHABID (ভাষাবিদ) — UNIVERSAL SKILL & IDE INSTALLER"
echo "================================================================="

HOME_DIR="${HOME}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_ROOT="$(dirname "${SCRIPT_DIR}")"
GITHUB_RAW="https://raw.githubusercontent.com/ashik1291/bhashabid/main"

TEMP_DIR=""
cleanup() {
  if [ -n "${TEMP_DIR}" ] && [ -d "${TEMP_DIR}" ]; then
    rm -rf "${TEMP_DIR}"
  fi
}
trap cleanup EXIT

if [ -f "${REPO_ROOT}/skills/bangla-expert/SKILL.md" ]; then
  echo "→ Using local Bhashabid repository source..."
  SOURCE_SKILL_DIR="${REPO_ROOT}/skills/bangla-expert"
  SOURCE_CURSOR_RULE="${REPO_ROOT}/adapters/cursor/.cursorrules"
else
  echo "→ Fetching latest Bhashabid skill files from GitHub..."
  TEMP_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t 'bhashabid')"
  mkdir -p "${TEMP_DIR}/references"

  curl -fsSL "${GITHUB_RAW}/skills/bangla-expert/SKILL.md" -o "${TEMP_DIR}/SKILL.md"
  curl -fsSL "${GITHUB_RAW}/adapters/cursor/.cursorrules" -o "${TEMP_DIR}/.cursorrules"

  for ref in academic_legal_medical.md constitutional_writs.md creative_writing.md ecommerce_fintech_civic.md grammar_registers.md journalism_domains.md numerals.md official_letters.md orthography.md; do
    curl -fsSL "${GITHUB_RAW}/skills/bangla-expert/references/${ref}" -o "${TEMP_DIR}/references/${ref}"
  done

  SOURCE_SKILL_DIR="${TEMP_DIR}"
  SOURCE_CURSOR_RULE="${TEMP_DIR}/.cursorrules"
fi

# 1. Cursor IDE
if [ "${TARGET}" = "cursor" ] || [ "${TARGET}" = "all" ]; then
  mkdir -p "${HOME_DIR}/.cursor/rules" "${HOME_DIR}/.cursor/bangla-references"
  cp -f "${SOURCE_CURSOR_RULE}" "${HOME_DIR}/.cursor/rules/bangla-expert.mdc"
  cp -rf "${SOURCE_SKILL_DIR}/references/"* "${HOME_DIR}/.cursor/bangla-references/"
  echo "[✓] Cursor IDE:"
  echo "    • Global Rule: ${HOME_DIR}/.cursor/rules/bangla-expert.mdc"
  echo "    • References:  ${HOME_DIR}/.cursor/bangla-references (9 domain guides)"
fi

# 2. Antigravity IDE / CLI
if [ "${TARGET}" = "antigravity" ] || [ "${TARGET}" = "all" ]; then
  AG_DEST1="${HOME_DIR}/.gemini/config/skills/bhashabid"
  AG_DEST2="${HOME_DIR}/.gemini/antigravity/skills/bangla-expert"
  mkdir -p "${AG_DEST1}/references" "${AG_DEST2}/references"

  cp -f "${SOURCE_SKILL_DIR}/SKILL.md" "${AG_DEST1}/SKILL.md"
  cp -rf "${SOURCE_SKILL_DIR}/references/"* "${AG_DEST1}/references/"

  cp -f "${SOURCE_SKILL_DIR}/SKILL.md" "${AG_DEST2}/SKILL.md"
  cp -rf "${SOURCE_SKILL_DIR}/references/"* "${AG_DEST2}/references/"

  echo "[✓] Google Antigravity:"
  echo "    • Global Skill: ${AG_DEST1}"
  echo "    • Legacy Path:  ${AG_DEST2}"
fi

# 3. Claude Desktop / Code
if [ "${TARGET}" = "claude" ] || [ "${TARGET}" = "all" ]; then
  CL_DEST="${HOME_DIR}/.claude/skills/bangla-expert"
  mkdir -p "${CL_DEST}/references"
  cp -f "${SOURCE_SKILL_DIR}/SKILL.md" "${CL_DEST}/SKILL.md"
  cp -rf "${SOURCE_SKILL_DIR}/references/"* "${CL_DEST}/references/"
  echo "[✓] Claude Desktop / Code:"
  echo "    • Global Skill: ${CL_DEST}"
fi

# 4. Optional Workspace
if [ -n "${WORKSPACE}" ]; then
  mkdir -p "${WORKSPACE}/.cursor/rules" "${WORKSPACE}/.cursor/bangla-references"
  cp -f "${SOURCE_CURSOR_RULE}" "${WORKSPACE}/.cursorrules"
  cp -f "${SOURCE_CURSOR_RULE}" "${WORKSPACE}/.cursor/rules/bangla-expert.mdc"
  cp -rf "${SOURCE_SKILL_DIR}/references/"* "${WORKSPACE}/.cursor/bangla-references/"
  echo "[✓] Workspace Target (${WORKSPACE}):"
  echo "    • Local Rule: ${WORKSPACE}/.cursorrules"
fi

# 5. Environment & Tool Capability Check
echo ""
echo "--- Environment & Tool Capability Status ---"
if command -v python3 &>/dev/null || command -v python &>/dev/null; then
  PY_BIN="$(command -v python3 || command -v python)"
  echo "[✓] Python Detected: ${PY_BIN}"

  # Configure MCP servers if python is present
  "${PY_BIN}" -c "
import json, os, sys
from pathlib import Path

home = Path.home()
entry = {'command': sys.executable, 'args': ['-m', 'bhashabid.mcp']}

targets = [
    home / '.cursor' / 'mcp.json',
    home / '.gemini' / 'config' / 'mcp_config.json',
    home / '.gemini' / 'antigravity' / 'mcp_servers.json',
    home / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json',
    home / '.config' / 'Claude' / 'claude_desktop_config.json'
]

for p in targets:
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        data = {'mcpServers': {}}
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding='utf-8-sig'))
            except Exception:
                pass
        if 'mcpServers' not in data or not isinstance(data['mcpServers'], dict):
            data['mcpServers'] = {}
        data['mcpServers']['bhashabid'] = entry
        p.write_text(json.dumps(data, indent=2), encoding='utf-8')
        print(f'    • MCP configured: {p}')
    except Exception as e:
        pass
" 2>/dev/null || true
else
  echo "[!] Python Not Detected on this machine."
  echo "    • Skill Mode: FULLY ACTIVE ✓ (AI directly applies Bangla Academy standards,"
  echo "      active voice, numeral words, and legal/deed templates inside your IDE)."
  echo "    • If you later want zero-token local CLI tools (e.g. bhashabid number), simply"
  echo "      install Python 3.10+ and run: pip install bhashabid"
fi

echo ""
echo "================================================================="
echo "✓ BHASHABID INSTALLATION COMPLETE! READY TO USE."
echo "================================================================="
