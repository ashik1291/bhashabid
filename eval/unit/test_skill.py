# Skill Token Budget and Reference Integrity Test
import unittest
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestSkillIntegrity(unittest.TestCase):

    def test_skill_token_budget(self):
        skill_path = os.path.join(REPO_ROOT, "skills", "bangla-expert", "SKILL.md")
        self.assertTrue(os.path.exists(skill_path), "SKILL.md must exist")

        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            import tiktoken
            tokens = len(tiktoken.get_encoding("cl100k_base").encode(content))
        except ImportError:
            tokens = int(len(content.split()) * 2.2)  # conservative fallback for Bengali-heavy text

        # REQ-036 requires SKILL.md not to exceed 1000 cl100k tokens
        self.assertLess(tokens, 1000, f"SKILL.md exceeds token budget: {tokens} tokens")

    def test_skill_references_exist(self):
        ref_dir = os.path.join(REPO_ROOT, "skills", "bangla-expert", "references")
        expected_refs = ["numerals.md", "orthography.md", "grammar_registers.md"]
        for ref in expected_refs:
            full_ref_path = os.path.join(ref_dir, ref)
            self.assertTrue(os.path.exists(full_ref_path), f"Reference file {ref} must exist")
            self.assertGreater(os.path.getsize(full_ref_path), 50, f"Reference file {ref} should not be empty")

    def test_skill_installer_tool(self):
        from tools.skill_installer import get_source_skill_dir
        src = get_source_skill_dir()
        self.assertTrue((src / "SKILL.md").exists())
        self.assertTrue((src / "references").exists())
        self.assertTrue((src / "STANDALONE_ALL_IN_ONE.md").exists())

if __name__ == "__main__":
    unittest.main()
