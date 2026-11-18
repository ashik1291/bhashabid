# eval/unit/test_creative_framework.py
# Unit Tests for Bhashabid Pioneer Literary & Poetic Translation Framework

import unittest
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

class TestCreativeFramework(unittest.TestCase):

    def setUp(self):
        self.ref_file = REPO_ROOT / "skills" / "bangla-expert" / "references" / "creative_writing.md"
        self.standalone_file = REPO_ROOT / "skills" / "bangla-expert" / "STANDALONE_ALL_IN_ONE.md"
        self.assertTrue(self.ref_file.exists(), f"Missing {self.ref_file}")
        self.assertTrue(self.standalone_file.exists(), f"Missing {self.standalone_file}")

    def test_authorial_register_archetypes_present(self):
        content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("Archetype A: Imagist / Minimalist / Scientific", content)
        self.assertIn("Archetype B: Romantic / Symbolist / Classical", content)
        self.assertIn("Archetype C: Realist Fiction / Living Dialogue", content)
        self.assertIn("Marianne Moore", content)
        self.assertIn("Jibanananda", content)

    def test_lapidary_gemstone_equivalents(self):
        content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("পিঙ্গল-আভ", content)
        self.assertIn("রক্তনীলমণি", content)
        self.assertIn("বৈদূর্যমণি", content)
        self.assertIn("ফিরোজা", content)
        self.assertIn("শঙ্খশুভ্র", content)
        self.assertIn("নির্মোক", content)

    def test_biological_anatomical_integrity_invariants(self):
        content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("Rule of Anatomical Realism", content)
        self.assertIn("ছত্র", content)
        self.assertIn("বুজে যায়", content)
        self.assertIn("কর্ষিকা", content)
        self.assertIn("ডানা মেলা", content)  # Listed under strictly forbidden

    def test_cognitive_volition_and_negative_invariants(self):
        content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("Rule of Cognitive Intent vs. Romantic Longing", content)
        self.assertIn("অভিপ্রায়", content)
        self.assertIn("সংকল্প", content)
        self.assertIn("বাসনা", content)  # Listed under forbidden drift
        self.assertIn("Rule of Zero Uninvited Particles", content)

    def test_three_pass_cognitive_process(self):
        content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("The 3-Pass Cognitive Guided Process", content)
        self.assertIn("Pass 1: Register & Anatomical Audit", content)
        self.assertIn("Pass 2: Aesthetic Naturalization", content)
        self.assertIn("Pass 3: Negative Invariant Purge", content)

    def test_standalone_prompt_literary_invariants(self):
        content = self.standalone_file.read_text(encoding="utf-8")
        self.assertIn("রক্তনীলমণি", content)
        self.assertIn("পিঙ্গল-আভ", content)
        self.assertIn("অভিপ্রায় / সংকল্প", content)
        self.assertIn("NEVER wings/ডানা", content)

    def test_semantic_conservation_and_pop_culture_rules(self):
        ref_content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("Rule of Semantic Conservation & Scale Integrity", ref_content)
        self.assertIn("Rule of Modern Pop-Culture Entity Exemption", ref_content)
        self.assertIn("Rule of Dignified Cognitive Metaphor Mapping", ref_content)
        self.assertIn("গিটার হিরো", ref_content)
        self.assertIn("তলিয়ে দেখা", ref_content)

        standalone_content = self.standalone_file.read_text(encoding="utf-8")
        self.assertIn("Modern Pop-Culture & Entity Exemption", standalone_content)
        self.assertIn("Semantic Conservation & Factual Scale Invariant", standalone_content)
        self.assertIn("Cognitive & Investigative Metaphors", standalone_content)
        self.assertIn("গিটার-নায়ক", standalone_content)

    def test_python_lapidary_engine(self):
        from bhashabid.creative import lookup_lapidary
        res = lookup_lapidary("amethyst")
        self.assertIsNotNone(res)
        self.assertIn("রক্তনীলমণি", res)
        res_amber = lookup_lapidary("amber")
        self.assertIn("পিঙ্গল-আভ", res_amber)

    def test_python_literary_audit_catches_anatomical_hallucination(self):
        from bhashabid.creative import audit_literary_text
        flawed = "জেলিফিশটি তার ডানা মেলে উড়ে গেল এবং এর রঙ ছিল অ্যাম্বার-রঙা অ্যামেথিস্ট।"
        report = audit_literary_text(flawed)
        self.assertEqual(report["status"], "FAIL")
        types = [iss["type"] for iss in report["issues"]]
        self.assertIn("ANATOMICAL_HALLUCINATION", types)
        self.assertIn("TRANSLITERATION_SURRENDER", types)

    def test_python_prompt_engine_generates_5_laws(self):
        from bhashabid.creative import generate_literary_prompt
        prompt = generate_literary_prompt(
            "An amber-colored amethyst Inhabits it",
            author="Marianne Moore",
            genre_or_archetype="imagist"
        )
        self.assertIn("THE 5 UNIVERSAL META-LAWS", prompt)
        self.assertIn("Law 1: The Three Dimensions of Transduction", prompt)
        self.assertIn("Law 3: Biological Realism & Lapidary Equivalence", prompt)
        self.assertIn("Marianne Moore", prompt)

    def test_mcp_creative_tools(self):
        from bhashabid.mcp.server import BhashabidMCPServer
        server = BhashabidMCPServer()
        lap_res = server.call_tool("lookup_lapidary", {"term": "turquoise"})
        self.assertIn("ফিরোজা", lap_res["equivalents"])
        audit_res = server.call_tool("audit_literary_text", {"text": "জেলিফিশের ডানা"})
        self.assertEqual(audit_res["result"]["status"], "WARNING")

    def test_all_five_universal_meta_laws_codified(self):
        ref_content = self.ref_file.read_text(encoding="utf-8")
        self.assertIn("Law 1: The Three Dimensions of Transduction", ref_content)
        self.assertIn("Law 2: Authorial Tone-Matrix Alignment", ref_content)
        self.assertIn("Law 3: Biological Realism & Lapidary Equivalence", ref_content)
        self.assertIn("Law 4: Anti-Calque Syntactic Re-Ordering", ref_content)
        self.assertIn("Law 5: Prosody, Rhythm & Cadence Lock", ref_content)

        standalone_content = self.standalone_file.read_text(encoding="utf-8")
        self.assertIn("Law 1 (Transduction)", standalone_content)
        self.assertIn("Law 2 (Tone-Matrix)", standalone_content)
        self.assertIn("Law 3 (Anatomical & Lapidary Realism)", standalone_content)
        self.assertIn("Law 4 (Anti-Calque Syntax)", standalone_content)
        self.assertIn("Law 5 (Prosodic Cadence)", standalone_content)

if __name__ == "__main__":
    unittest.main()
