# bhashabid/skill_installer.py
# One-Click Global Skill & Reference Installer for AI IDEs & Agents
import os
import sys
import shutil
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

PACKAGE_DIR = Path(__file__).parent
REPO_ROOT = PACKAGE_DIR.parent

def get_source_skill_dir() -> Path:
    # 1. Check packaged assets directory (for pip installs)
    p_pkg = PACKAGE_DIR / "assets" / "skills" / "bangla-expert"
    if p_pkg.exists() and (p_pkg / "SKILL.md").exists():
        return p_pkg
    # 2. Check repo root (for dev environments)
    p_repo = REPO_ROOT / "skills" / "bangla-expert"
    if p_repo.exists() and (p_repo / "SKILL.md").exists():
        return p_repo
    p_tools = REPO_ROOT / "tools" / "assets" / "skills" / "bangla-expert"
    if p_tools.exists() and (p_tools / "SKILL.md").exists():
        return p_tools
    raise FileNotFoundError("Could not locate source 'skills/bangla-expert' directory in package assets or repository.")

def get_cursorrules_path() -> Path:
    p_pkg = PACKAGE_DIR / "assets" / "adapters" / "cursor" / ".cursorrules"
    if p_pkg.exists():
        return p_pkg
    p_repo = REPO_ROOT / "adapters" / "cursor" / ".cursorrules"
    if p_repo.exists():
        return p_repo
    p_tools = REPO_ROOT / "tools" / "assets" / "adapters" / "cursor" / ".cursorrules"
    if p_tools.exists():
        return p_tools
    raise FileNotFoundError("Could not locate source '.cursorrules' in package assets or repository.")

def detect_environments() -> Dict[str, Dict[str, Any]]:
    """
    Auto-detects which AI IDEs / Agent environments exist on this machine.
    """
    home = Path.home()
    appdata = Path(os.environ.get("APPDATA", "")) if os.environ.get("APPDATA") else None

    # 1. Cursor
    cursor_found = False
    cursor_hint = ""
    if (home / ".cursor").exists():
        cursor_found = True
        cursor_hint = str(home / ".cursor")
    elif appdata and (appdata / "Cursor").exists():
        cursor_found = True
        cursor_hint = str(appdata / "Cursor")
    elif shutil.which("cursor") is not None:
        cursor_found = True
        cursor_hint = "cursor on PATH"

    # 2. Antigravity
    ag_found = False
    ag_hint = ""
    if (home / ".gemini").exists():
        ag_found = True
        ag_hint = str(home / ".gemini")
    elif shutil.which("agy") is not None or shutil.which("antigravity") is not None:
        ag_found = True
        ag_hint = "agy CLI on PATH"

    # 3. Claude (Desktop / Code)
    claude_found = False
    claude_hint = ""
    claude_cfg = get_claude_desktop_config_path()
    if (home / ".claude").exists() or (home / ".claude.json").exists():
        claude_found = True
        claude_hint = str(home / ".claude")
    elif claude_cfg and claude_cfg.exists():
        claude_found = True
        claude_hint = str(claude_cfg)
    elif shutil.which("claude") is not None:
        claude_found = True
        claude_hint = "claude CLI on PATH"

    return {
        "cursor": {"detected": cursor_found, "hint": cursor_hint},
        "antigravity": {"detected": ag_found, "hint": ag_hint},
        "claude": {"detected": claude_found, "hint": claude_hint}
    }

def get_claude_desktop_config_path() -> Optional[Path]:
    home = Path.home()
    appdata = Path(os.environ.get("APPDATA", "")) if os.environ.get("APPDATA") else None
    if sys.platform == "win32" and appdata:
        return appdata / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "darwin":
        return home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    else:
        return home / ".config" / "Claude" / "claude_desktop_config.json"

def install_mcp(target: str = "all", workspace_dir: str = None) -> str:
    """
    Installs Bhashabid MCP server configuration globally for detected environments.
    """
    home = Path.home()
    python_exe = sys.executable.replace("\\", "/")
    env_info = detect_environments()

    # Portable MCP entrypoint using installed package module
    mcp_entry = {
        "command": python_exe,
        "args": ["-m", "bhashabid.mcp"]
    }

    configured = []
    skipped = []

    # 1. Cursor Global MCP (~/.cursor/mcp.json)
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            mcp_file = home / ".cursor" / "mcp.json"
            os.makedirs(mcp_file.parent, exist_ok=True)
            data = {"mcpServers": {}}
            if mcp_file.exists():
                try:
                    with open(mcp_file, "r", encoding="utf-8-sig") as f:
                        data = json.load(f)
                except Exception:
                    data = {"mcpServers": {}}
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            data["mcpServers"]["bhashabid"] = mcp_entry
            with open(mcp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            configured.append(f"Cursor: {mcp_file}")
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity Global MCP (Sync to ~/.gemini/config/mcp_config.json AND ~/.gemini/antigravity/mcp_servers.json)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_mcp_paths = [
                home / ".gemini" / "config" / "mcp_config.json",
                home / ".gemini" / "antigravity" / "mcp_servers.json"
            ]
            for ag_mcp in ag_mcp_paths:
                os.makedirs(ag_mcp.parent, exist_ok=True)
                ag_data = {"mcpServers": {}}
                if ag_mcp.exists():
                    try:
                        with open(ag_mcp, "r", encoding="utf-8-sig") as f:
                            ag_data = json.load(f)
                    except Exception:
                        ag_data = {"mcpServers": {}}
                if "mcpServers" not in ag_data:
                    ag_data["mcpServers"] = {}
                ag_data["mcpServers"]["bhashabid"] = mcp_entry
                with open(ag_mcp, "w", encoding="utf-8") as f:
                    json.dump(ag_data, f, indent=2, ensure_ascii=False)
                configured.append(f"Antigravity: {ag_mcp}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude Desktop & Claude Code MCP
    if target in ["claude", "all"]:
        # 3a. Claude Code CLI (~/.claude.json)
        claude_code_cfg = home / ".claude.json"
        if claude_code_cfg.exists() or shutil.which("claude") is not None:
            code_data = {"mcpServers": {}}
            if claude_code_cfg.exists():
                try:
                    with open(claude_code_cfg, "r", encoding="utf-8-sig") as f:
                        code_data = json.load(f)
                except Exception:
                    code_data = {"mcpServers": {}}
            if "mcpServers" not in code_data:
                code_data["mcpServers"] = {}
            code_data["mcpServers"]["bhashabid"] = {
                "type": "stdio",
                "command": python_exe,
                "args": ["-m", "bhashabid.mcp"]
            }
            with open(claude_code_cfg, "w", encoding="utf-8") as f:
                json.dump(code_data, f, indent=2, ensure_ascii=False)
            configured.append(f"Claude Code: {claude_code_cfg}")

        # 3b. Claude Desktop
        claude_cfg = get_claude_desktop_config_path()
        if target == "claude" or (claude_cfg and claude_cfg.parent.exists()) or env_info["claude"]["detected"]:
            if claude_cfg:
                os.makedirs(claude_cfg.parent, exist_ok=True)
                data = {"mcpServers": {}}
                if claude_cfg.exists():
                    try:
                        with open(claude_cfg, "r", encoding="utf-8-sig") as f:
                            data = json.load(f)
                    except Exception:
                        data = {"mcpServers": {}}
                if "mcpServers" not in data:
                    data["mcpServers"] = {}
                data["mcpServers"]["bhashabid"] = mcp_entry
                with open(claude_cfg, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                configured.append(f"Claude Desktop: {claude_cfg}")
        else:
            skipped.append("Claude Desktop (Not detected)")

    # Workspace MCP (only if explicitly requested)
    if workspace_dir:
        ws_path = Path(workspace_dir)
        ws_mcp = ws_path / ".cursor" / "mcp.json"
        os.makedirs(ws_mcp.parent, exist_ok=True)
        data = {"mcpServers": {}}
        if ws_mcp.exists():
            try:
                with open(ws_mcp, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"mcpServers": {}}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["bhashabid"] = mcp_entry
        with open(ws_mcp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        configured.append(f"Workspace: {ws_mcp}")

    msg = "✓ Bhashabid MCP server configuration successfully installed to:\n"
    for c in configured:
        msg += f"  - {c}\n"
    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"
    return msg

def verify_skill_safety(src_dir: Path) -> bool:
    banned_extensions = {".exe", ".dll", ".so", ".sh", ".bat", ".cmd", ".ps1", ".vbs", ".bin"}
    for f in src_dir.rglob("*"):
        if f.is_file():
            if f.suffix.lower() in banned_extensions:
                raise PermissionError(f"Security Alert: Executable binary or script '{f.name}' blocked from skill installation.")
            if f.suffix.lower() in {".md", ".mdc", ".txt"}:
                try:
                    text = f.read_text(encoding="utf-8", errors="ignore")
                    if "rm -rf" in text or "format c:" in text.lower():
                        raise PermissionError(f"Security Alert: Destructive command pattern detected in '{f.name}'.")
                except Exception as ex:
                    if isinstance(ex, PermissionError):
                        raise ex
    return True

def install_skill(target: str = "all", workspace_dir: str = None, with_mcp: bool = True) -> str:
    """
    Installs Bhashabid skill files and reference guides globally for detected environments.
    """
    src_dir = get_source_skill_dir()
    verify_skill_safety(src_dir)
    home = Path.home()
    env_info = detect_environments()
    dest_paths = []
    skipped = []

    # 1. Cursor Global Rules (~/.cursor/rules/bangla-expert.mdc and ~/.cursor/bangla-references)
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            cur_global_rules = home / ".cursor" / "rules"
            os.makedirs(cur_global_rules, exist_ok=True)
            try:
                src_rule = get_cursorrules_path()
                shutil.copy(src_rule, cur_global_rules / "bangla-expert.mdc")
            except Exception:
                pass

            cur_global_refs = home / ".cursor" / "bangla-references"
            os.makedirs(cur_global_refs, exist_ok=True)
            if (src_dir / "references").exists():
                shutil.copytree(src_dir / "references", cur_global_refs, dirs_exist_ok=True)

            dest_paths.append(f"Cursor (Global Rule): {cur_global_rules / 'bangla-expert.mdc'}")
            dest_paths.append(f"Cursor (References):  {cur_global_refs}")
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity Global Skills (Install to ~/.gemini/config/skills/bhashabid AND ~/.gemini/antigravity/skills/bangla-expert)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_paths = [
                home / ".gemini" / "config" / "skills" / "bhashabid",
                home / ".gemini" / "antigravity" / "skills" / "bangla-expert"
            ]
            for ag_dest in ag_paths:
                os.makedirs(ag_dest, exist_ok=True)
                shutil.copytree(src_dir, ag_dest, dirs_exist_ok=True)
                dest_paths.append(f"Antigravity (Global Skill): {ag_dest}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude Global Skills (~/.claude/skills/bangla-expert)
    if target in ["claude", "all"]:
        if target == "claude" or env_info["claude"]["detected"]:
            cl_global = home / ".claude" / "skills" / "bangla-expert"
            os.makedirs(cl_global, exist_ok=True)
            shutil.copytree(src_dir, cl_global, dirs_exist_ok=True)
            dest_paths.append(f"Claude (Global Skill): {cl_global}")
        else:
            skipped.append("Claude (Not detected)")

    # 4. Optional Workspace Directory
    if workspace_dir:
        ws = Path(workspace_dir)
        cur_rules = ws / ".cursor" / "rules"
        os.makedirs(cur_rules, exist_ok=True)
        try:
            src_rule = get_cursorrules_path()
            shutil.copy(src_rule, ws / ".cursorrules")
            shutil.copy(src_rule, cur_rules / "bangla-expert.mdc")
        except Exception:
            pass
        if (src_dir / "references").exists():
            shutil.copytree(src_dir / "references", ws / ".cursor" / "bangla-references", dirs_exist_ok=True)
        dest_paths.append(f"Workspace ({ws.name}): {cur_rules / 'bangla-expert.mdc'}")
        dest_paths.append(f"Workspace ({ws.name}): {ws / '.cursorrules'}")

    msg = f"✓ Bhashabid skill successfully installed to:\n"
    for dp in dest_paths:
        msg += f"  - {dp}\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    if with_mcp:
        mcp_msg = install_mcp(target=target, workspace_dir=workspace_dir)
        msg += f"\n{mcp_msg}"

    return msg

def uninstall_mcp(target: str = "all", workspace_dir: str = None) -> str:
    home = Path.home()
    env_info = detect_environments()
    removed_from = []
    skipped = []

    # 1. Cursor Global MCP
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            targets = [home / ".cursor" / "mcp.json"]
            if workspace_dir:
                targets.append(Path(workspace_dir) / ".cursor" / "mcp.json")
            for mcp_file in targets:
                if mcp_file.exists():
                    try:
                        with open(mcp_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                            del data["mcpServers"]["bhashabid"]
                            with open(mcp_file, "w", encoding="utf-8") as f:
                                json.dump(data, f, indent=2, ensure_ascii=False)
                            removed_from.append(f"Cursor MCP: {mcp_file}")
                    except Exception:
                        pass
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Claude Desktop & Claude Code config
    if target in ["claude", "all"]:
        # 2a. Claude Code (~/.claude.json)
        claude_code_cfg = home / ".claude.json"
        if claude_code_cfg.exists():
            try:
                with open(claude_code_cfg, "r", encoding="utf-8") as f:
                    code_data = json.load(f)
                if "mcpServers" in code_data and "bhashabid" in code_data["mcpServers"]:
                    del code_data["mcpServers"]["bhashabid"]
                    with open(claude_code_cfg, "w", encoding="utf-8") as f:
                        json.dump(code_data, f, indent=2, ensure_ascii=False)
                    removed_from.append(f"Claude Code MCP: {claude_code_cfg}")
            except Exception:
                pass

        # 2b. Claude Desktop
        claude_cfg = get_claude_desktop_config_path()
        if target == "claude" or (claude_cfg and claude_cfg.exists()) or env_info["claude"]["detected"]:
            if claude_cfg and claude_cfg.exists():
                try:
                    with open(claude_cfg, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                        del data["mcpServers"]["bhashabid"]
                        with open(claude_cfg, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2, ensure_ascii=False)
                        removed_from.append(f"Claude Desktop MCP: {claude_cfg}")
                except Exception:
                    pass
        else:
            skipped.append("Claude Desktop (Not detected)")

    # 3. Antigravity MCP (Clean both config/mcp_config.json and antigravity/mcp_servers.json)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_mcp_paths = [
                home / ".gemini" / "config" / "mcp_config.json",
                home / ".gemini" / "antigravity" / "mcp_servers.json"
            ]
            for ag_mcp in ag_mcp_paths:
                if ag_mcp.exists():
                    try:
                        with open(ag_mcp, "r", encoding="utf-8") as f:
                            ag_data = json.load(f)
                        if "mcpServers" in ag_data and "bhashabid" in ag_data["mcpServers"]:
                            del ag_data["mcpServers"]["bhashabid"]
                            with open(ag_mcp, "w", encoding="utf-8") as f:
                                json.dump(ag_data, f, indent=2, ensure_ascii=False)
                            removed_from.append(f"Antigravity MCP: {ag_mcp}")
                    except Exception:
                        pass
        else:
            skipped.append("Antigravity (Not detected)")

    msg = ""
    if removed_from:
        msg += "✓ Bhashabid MCP server configuration successfully removed from:\n"
        for rf in removed_from:
            msg += f"  - {rf}\n"
    else:
        msg += "Notice: No active Bhashabid MCP server entries found for the specified target.\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    return msg

def uninstall_skill(target: str = "all", workspace_dir: str = None, with_mcp: bool = True) -> str:
    home = Path.home()
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()
    env_info = detect_environments()
    removed_paths = []
    skipped = []

    # 1. Cursor
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            cur_global_mdc = home / ".cursor" / "rules" / "bangla-expert.mdc"
            if cur_global_mdc.exists():
                cur_global_mdc.unlink(missing_ok=True)
                removed_paths.append(f"Cursor (Global Rule): {cur_global_mdc}")

            cur_global_refs = home / ".cursor" / "bangla-references"
            if cur_global_refs.exists():
                shutil.rmtree(cur_global_refs, ignore_errors=True)
                removed_paths.append(f"Cursor (References):  {cur_global_refs}")
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            for ag_dir in [home / ".gemini" / "config" / "skills" / "bhashabid", home / ".gemini" / "antigravity" / "skills" / "bangla-expert"]:
                if ag_dir.exists():
                    shutil.rmtree(ag_dir, ignore_errors=True)
                    removed_paths.append(f"Antigravity (Global Skill): {ag_dir}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude
    if target in ["claude", "all"]:
        if target == "claude" or env_info["claude"]["detected"]:
            cl_global = home / ".claude" / "skills" / "bangla-expert"
            if cl_global.exists():
                shutil.rmtree(cl_global, ignore_errors=True)
                removed_paths.append(f"Claude (Global Skill): {cl_global}")
        else:
            skipped.append("Claude (Not detected)")

    # 4. Workspace Cleanups (Safe signature-checked unlink to protect user configuration)
    ws_expert_mdc = workspace / ".cursor" / "rules" / "bangla-expert.mdc"
    if ws_expert_mdc.exists():
        try:
            ws_expert_mdc.unlink(missing_ok=True)
            removed_paths.append(f"Workspace Rule: {ws_expert_mdc}")
        except Exception:
            pass

    ws_cursorrules = workspace / ".cursorrules"
    if ws_cursorrules.exists():
        should_remove = False
        # Strictly verify signature to protect pre-existing project .cursorrules from accidental deletion
        try:
            content = ws_cursorrules.read_text(encoding="utf-8-sig", errors="ignore")
            if "bhashabid" in content.lower() or "bangla-expert" in content.lower():
                should_remove = True
        except Exception:
            pass
        if should_remove:
            try:
                ws_cursorrules.unlink(missing_ok=True)
                removed_paths.append(f"Workspace Rule: {ws_cursorrules}")
            except Exception:
                pass

    target_cursor_refs = (workspace / ".cursor" / "bangla-references").resolve()
    # Guard: Ensure we only delete the isolated references folder, never the workspace root
    if target_cursor_refs.exists() and target_cursor_refs.name == "bangla-references":
        shutil.rmtree(target_cursor_refs, ignore_errors=True)
        removed_paths.append(f"Workspace References: {target_cursor_refs}")

    msg = ""
    if removed_paths:
        msg = f"✓ Bhashabid skill and references successfully removed from:\n"
        for rp in removed_paths:
            msg += f"  - {rp}\n"
    else:
        msg = "Notice: No installed Bhashabid skill files were found for the specified target.\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    if with_mcp:
        mcp_msg = uninstall_mcp(target=target, workspace_dir=str(workspace))
        msg += f"\n{mcp_msg}"

    return msg

def verify_installation() -> Dict[str, Any]:
    home = Path.home()
    env_info = detect_environments()
    status = {}

    # Cursor
    cursor_active = False
    cursor_details = []
    if env_info["cursor"]["detected"]:
        cur_rule = home / ".cursor" / "rules" / "bangla-expert.mdc"
        cur_refs = home / ".cursor" / "bangla-references"
        cur_mcp = home / ".cursor" / "mcp.json"

        has_rule = cur_rule.exists()
        has_refs = cur_refs.exists() and len(list(cur_refs.glob("*.md"))) > 0
        has_mcp = False
        if cur_mcp.exists():
            try:
                data = json.load(open(cur_mcp, "r", encoding="utf-8-sig"))
                has_mcp = "bhashabid" in data.get("mcpServers", {})
            except Exception:
                pass

        cursor_active = has_rule and has_refs
        cur_ref_count = len(list(cur_refs.glob("*.*"))) if has_refs else 0
        cursor_details.append(f"Global Rules: {'✓' if has_rule else '✗'}")
        cursor_details.append(f"References ({cur_ref_count} guides & datasets): {'✓' if has_refs else '✗'}")
        cursor_details.append(f"MCP Server: {'✓' if has_mcp else '✗'}")

    status["cursor"] = {
        "detected": env_info["cursor"]["detected"],
        "active": cursor_active,
        "details": cursor_details
    }

    # Antigravity
    ag_active = False
    ag_details = []
    if env_info["antigravity"]["detected"]:
        ag_skill1 = home / ".gemini" / "antigravity" / "skills" / "bangla-expert" / "SKILL.md"
        ag_skill2 = home / ".gemini" / "config" / "skills" / "bhashabid" / "SKILL.md"
        has_skill = ag_skill1.exists() or ag_skill2.exists()

        ag_refs1 = home / ".gemini" / "antigravity" / "skills" / "bangla-expert" / "references"
        ag_refs2 = home / ".gemini" / "config" / "skills" / "bhashabid" / "references"
        ag_refs = ag_refs2 if ag_refs2.exists() else ag_refs1
        ag_ref_count = len(list(ag_refs.glob("*.*"))) if ag_refs.exists() else 0

        ag_mcp1 = home / ".gemini" / "antigravity" / "mcp_servers.json"
        ag_mcp2 = home / ".gemini" / "config" / "mcp_config.json"
        has_mcp = False
        for ag_mcp in [ag_mcp1, ag_mcp2]:
            if ag_mcp.exists():
                try:
                    data = json.load(open(ag_mcp, "r", encoding="utf-8-sig"))
                    if "bhashabid" in data.get("mcpServers", {}):
                        has_mcp = True
                        break
                except Exception:
                    pass

        ag_active = has_skill
        ag_details.append(f"Global Skill: {'✓' if has_skill else '✗'}")
        ag_details.append(f"References ({ag_ref_count} guides & datasets): {'✓' if ag_ref_count > 0 else '✗'}")
        ag_details.append(f"MCP Server: {'✓' if has_mcp else '✗'}")

    status["antigravity"] = {
        "detected": env_info["antigravity"]["detected"],
        "active": ag_active,
        "details": ag_details
    }

    # Claude
    claude_active = False
    claude_details = []
    if env_info["claude"]["detected"]:
        cl_skill = home / ".claude" / "skills" / "bangla-expert" / "SKILL.md"
        cl_refs = home / ".claude" / "skills" / "bangla-expert" / "references"
        cl_ref_count = len(list(cl_refs.glob("*.*"))) if cl_refs.exists() else 0

        claude_cfg = get_claude_desktop_config_path()
        claude_code_cfg = home / ".claude.json"
        has_skill = cl_skill.exists()
        has_desktop_mcp = False
        has_code_mcp = False
        if claude_cfg and claude_cfg.exists():
            try:
                data = json.load(open(claude_cfg, "r", encoding="utf-8-sig"))
                has_desktop_mcp = "bhashabid" in data.get("mcpServers", {})
            except Exception:
                pass
        if claude_code_cfg.exists():
            try:
                code_data = json.load(open(claude_code_cfg, "r", encoding="utf-8-sig"))
                has_code_mcp = "bhashabid" in code_data.get("mcpServers", {})
            except Exception:
                pass

        claude_active = has_skill
        claude_details.append(f"Global Skill: {'✓' if has_skill else '✗'}")
        claude_details.append(f"References ({cl_ref_count} guides & datasets): {'✓' if cl_ref_count > 0 else '✗'}")
        claude_details.append(f"Claude Code MCP: {'✓' if has_code_mcp else '✗'}")
        claude_details.append(f"Desktop MCP: {'✓' if has_desktop_mcp else '✗'}")

    status["claude"] = {
        "detected": env_info["claude"]["detected"],
        "active": claude_active,
        "details": claude_details
    }

    return status

def format_status_report() -> str:
    st = verify_installation()
    lines = ["=" * 65, "BHASHABID SYSTEM INSTALLATION & HEALTH STATUS", "=" * 65]
    for env, data in st.items():
        name = env.capitalize()
        if not data["detected"]:
            lines.append(f"[-] {name:15} : Not detected on this machine")
        else:
            state = "ACTIVE (Verified)" if data["active"] else "INACTIVE / NOT INSTALLED"
            icon = "[✓]" if data["active"] else "[!]"
            lines.append(f"{icon} {name:15} : {state}")
            for d in data["details"]:
                lines.append(f"     • {d}")
    lines.append("=" * 65)
    return "\n".join(lines)
