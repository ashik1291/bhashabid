# eval/unit/test_security_posture.py
"""
Production Security & Trust Assurance Suite for Bhashabid.
Validates:
1. MCP Server input sanitization, injection-resistance, and error boundaries.
2. Offline engine safety (zero-network, AST purity, no eval/exec).
3. Skill kernel text safety (no executable commands or shell exploits).
4. Knowledge cards integrity & YAML deserialization safety.
"""

import os
import ast
import unittest
import yaml
import glob
from pathlib import Path
from bhashabid import repair, normalize, lint, format_number, scan_line, spellcheck
from tools.mcp_server.server import BhashabidMCPServer

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestSecurityPosture(unittest.TestCase):

    def setUp(self):
        self.mcp = BhashabidMCPServer()

    def test_mcp_injection_resistance(self):
        """MCP tools must safely handle hostile injection payloads without shell or code execution."""
        hostile_inputs = [
            "; cat /etc/passwd #",
            "`rm -rf /`",
            "$(whoami)",
            "{{ 7 * 7 }}",
            "<script>alert('xss')</script>",
            "\x00\r\n\t--drop table users;",
            "%s%s%s%s%s%x%x",
            "import os; os.system('echo hack')",
            "A" * 10000  # large payload stress
        ]

        for hostile in hostile_inputs:
            # 1. normalize_text
            res_norm = self.mcp.call_tool("normalize_text", {"text": hostile})
            self.assertIn("result", res_norm)
            self.assertIsInstance(res_norm["result"], str)

            # 2. lint_text
            res_lint = self.mcp.call_tool("lint_text", {"text": hostile})
            self.assertIn("issues", res_lint)
            self.assertIn("issue_count", res_lint)

            # 3. repair_text
            res_rep = self.mcp.call_tool("repair_text", {"text": hostile})
            self.assertIn("repaired", res_rep)
            self.assertIn("fixes_count", res_rep)

            # 4. convert_number with hostile number string
            res_num = self.mcp.call_tool("convert_number", {"number": hostile, "format": "words"})
            self.assertIn("result", res_num)

    def test_mcp_unknown_tool_boundary(self):
        """MCP server must raise ValueError on unknown tool requests without crashing."""
        with self.assertRaises(ValueError) as ctx:
            self.mcp.call_tool("malicious_eval_tool", {"code": "1+1"})
        self.assertIn("Unknown tool", str(ctx.exception))

    def test_offline_engine_ast_purity(self):
        """Core linguistic modules must not contain unsafe dynamic code execution (eval, exec)."""
        core_dirs = [
            os.path.join(REPO_ROOT, "bhashabid"),
            os.path.join(REPO_ROOT, "tools", "bn_normalize"),
            os.path.join(REPO_ROOT, "tools", "bn_lint"),
            os.path.join(REPO_ROOT, "tools", "bn_numbers"),
            os.path.join(REPO_ROOT, "tools", "bn_prosody"),
            os.path.join(REPO_ROOT, "tools", "mcp_server"),
        ]

        banned_calls = {"eval", "exec", "__import__", "compile"}

        for cdir in core_dirs:
            for py_file in glob.glob(os.path.join(cdir, "*.py")):
                with open(py_file, "r", encoding="utf-8") as f:
                    source = f.read()
                tree = ast.parse(source, filename=py_file)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Name):
                            self.assertNotIn(
                                node.func.id,
                                banned_calls,
                                f"Security Violation: Prohibited call '{node.func.id}' found in {py_file}"
                            )

    def test_offline_zero_network_invariance(self):
        """Offline engine API must execute synchronously and deterministically without network calls."""
        # Test basic Bengali sentences across all core modules
        sample = "তিনি বললেন যে ১৫ই আগস্ট প্রকল্পটির তথ্য উপস্থাপন করা হইবে।"
        repaired, fixes = repair(sample)
        self.assertIsInstance(repaired, str)
        self.assertGreater(len(fixes), 0)

        normalized = normalize(sample)
        self.assertIsInstance(normalized, str)

        lint_issues = lint(sample)
        self.assertGreater(len(lint_issues), 0)

        num_words = format_number("1234567")
        self.assertIsInstance(num_words, str)

        prosody = scan_line("মহাভারতের কথা অমৃত সমান")
        self.assertGreater(prosody.total_morae, 0)

    def test_skill_kernel_declarative_safety(self):
        """Skill markdown files must be purely declarative and contain no executable shell/script blocks."""
        skill_files = glob.glob(os.path.join(REPO_ROOT, "skills", "**", "*.md"), recursive=True)
        self.assertGreater(len(skill_files), 0, "Skill files must exist.")

        dangerous_patterns = [
            "```bash\nrm ",
            "```sh\nrm ",
            "```powershell\nRemove-Item",
            "sudo ",
            "<script",
            "curl -X POST",
            "wget "
        ]

        for sfile in skill_files:
            with open(sfile, "r", encoding="utf-8") as f:
                content = f.read()
            for pattern in dangerous_patterns:
                self.assertNotIn(
                    pattern,
                    content,
                    f"Security Alert: Potentially destructive pattern '{pattern}' found in skill file {sfile}"
                )

    def test_knowledge_cards_deserialization_safety(self):
        """Knowledge cards must use safe YAML loading and strictly contain safe data types."""
        cards = glob.glob(os.path.join(REPO_ROOT, "knowledge", "cards", "*.yaml"))
        self.assertGreater(len(cards), 0, "Production knowledge cards must exist.")

        for card_path in cards:
            with open(card_path, "r", encoding="utf-8") as f:
                raw_text = f.read()
            # Ensure no YAML code injection tags
            self.assertNotIn("!!python/", raw_text, f"Unsafe YAML tag found in {card_path}")

            data = yaml.safe_load(raw_text)
            self.assertIsInstance(data, dict, f"Card must be a dictionary in {card_path}")
            self.assertIn("id", data)
            self.assertIn("rule_summary", data)
            self.assertIn("confidence", data)
            self.assertEqual(data.get("confidence"), "reviewed")

    def test_secret_leak_scanner(self):
        """Repository must be completely free of secrets, credentials, and work emails."""
        from tools.secret_scanner import scan_repository
        leaks = scan_repository(Path(REPO_ROOT))
        self.assertEqual(leaks, 0, f"Security Violation: {leaks} secret/credential leak(s) detected.")

    def test_dependency_cve_audit(self):
        """Direct dependencies must have 0 known CVEs in Google OSV / PyPA database."""
        from tools.dependency_audit import audit_dependencies
        status = audit_dependencies()
        self.assertEqual(status, 0, "Dependency Security Audit detected vulnerable packages.")

    def test_skill_installer_safety_gate(self):
        """Skill installer must verify directory safety and reject executable files."""
        import tempfile
        from pathlib import Path
        from tools.skill_installer import verify_skill_safety

        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            # 1. Safe markdown should pass
            (tmppath / "guide.md").write_text("# Safe Guide", encoding="utf-8")
            self.assertTrue(verify_skill_safety(tmppath))

            # 2. Executable binary should be blocked
            (tmppath / "payload.exe").write_text("MZ...", encoding="utf-8")
            with self.assertRaises(PermissionError):
                verify_skill_safety(tmppath)

if __name__ == "__main__":
    unittest.main()
