# eval/unit/test_self_improving_pipeline.py
# Unit Tests for Closed-Loop Knowledge Card Synthesizer & Skill Distiller
import unittest
import os
import tempfile
import yaml
from pathlib import Path

from tools.card_synthesizer import CardSynthesizer
from tools.skill_distiller import SkillDistiller, MAX_CORE_TOKEN_BUDGET

class TestSelfImprovingPipeline(unittest.TestCase):

    def test_card_synthesizer_draft_creation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            synth = CardSynthesizer(drafts_dir=tmpdir)
            out_path = synth.synthesize_draft_from_anomaly(
                title="Test Proverb Rule",
                domain="translation",
                register="formal",
                rule_summary="Map English proverb to Bengali idiom.",
                bad_examples=["ঘেউ ঘেউ করা কুকুর"],
                good_examples=["যত গর্জে তত বর্ষে না"],
                common_llm_error="Literal machine calque.",
                sources=["Test Source"],
                draft_id="CRD-DFT-999"
            )

            self.assertTrue(os.path.exists(out_path))
            with open(out_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            self.assertEqual(data["id"], "CRD-DFT-999")
            self.assertEqual(data["confidence"], "candidate")
            self.assertEqual(data["review"]["status"], "PENDING_HUMAN_REVIEW")
            self.assertIn("যত গর্জে তত বর্ষে না", data["good_examples"])

    def test_card_synthesizer_anti_deception_exemplar_gate(self):
        """Principle P2 & Anti-Deception: Anomalies lacking authentic positive exemplars or consisting of raw-English tokens must be auto-rejected into negative learning memory."""
        with tempfile.TemporaryDirectory() as tmpdir, tempfile.TemporaryDirectory() as rej_dir:
            synth = CardSynthesizer(drafts_dir=tmpdir, rejected_dir=rej_dir)
            
            # Anomaly 1: Raw English token anomaly (auto-rejected to negative memory)
            raw_eng_anomaly = [{
                "rule_id": "RULE-ANOMALY-RAW-ENGLISH",
                "matched": "NovelRawTokenXYZ",
                "raw_text": "ভারতের প্রাচীনতম চিকিৎসা পদ্ধতি আয়ুর্বেদ NovelRawTokenXYZ সম্পর্কে সচেতন করা",
                "suggestion": "Foreign terminology requires standard Bengali terminology.",
                "domain": "Healthcare & Medicine"
            }]
            created_eng = synth.cluster_and_synthesize_anomalies(raw_eng_anomaly)
            self.assertEqual(len(created_eng), 0, "Raw English token anomaly must not be queued as draft")
            
            # Verify it was archived in negative memory (rejected directory)
            import glob
            rej_cards = glob.glob(os.path.join(rej_dir, "*.yaml"))
            self.assertEqual(len(rej_cards), 1, "Must be archived in negative learning memory")
            with open(rej_cards[0], "r", encoding="utf-8") as rf:
                rej_data = yaml.safe_load(rf)
            self.assertEqual(rej_data["confidence"], "rejected")
            self.assertEqual(rej_data["review"]["status"], "REJECTED")

            # Anomaly 2: Anomaly where suggestion is a meta-instruction without positive exemplars
            meta_inst_anomaly = [{
                "rule_id": "RULE-ANOMALY-CALQUE",
                "matched": "কাল্পনিক অপরীক্ষিত ক্যাল্ক",
                "raw_text": "প্রকল্পটি বৈদেশিক কাল্পনিক অপরীক্ষিত ক্যাল্ক।",
                "suggestion": "প্রমিত বাংলায় স্বাভাবিকভাবে পুনর্লিখন করুন।",
                "domain": "translation"
            }]
            created_meta = synth.cluster_and_synthesize_anomalies(meta_inst_anomaly)
            self.assertEqual(len(created_meta), 0, "Anomaly lacking positive exemplars must not be queued as draft")
            
            # Anomaly 3: Valid anomaly with concrete paired Bengali exemplar (queued for human review)
            valid_anomaly = [{
                "rule_id": "RULE-ANOMALY-CALQUE",
                "matched": "অযৌক্তিক কৃত্রিম ক্যাল্ক",
                "raw_text": "এটি একটি অযৌক্তিক কৃত্রিম ক্যাল্ক বাক্য।",
                "suggestion": "'এটি একটি সাবলীল প্রমিত বাংলা বাক্য।'",
                "domain": "translation"
            }]
            created_valid = synth.cluster_and_synthesize_anomalies(valid_anomaly)
            self.assertEqual(len(created_valid), 1, "Anomaly with authentic positive exemplar must be drafted")

    def test_skill_distiller_token_budget_verification(self):
        distiller = SkillDistiller()
        self.assertGreater(len(distiller.approved_cards), 0)

        # Test valid text under budget
        valid_text = "This is a short rule prompt with few tokens."
        is_valid, tok = distiller.verify_token_budget(valid_text, max_tokens=100)
        self.assertTrue(is_valid)
        self.assertLess(tok, 100)

        # Test oversize text
        huge_text = "শব্দ " * 500
        is_valid_huge, tok_huge = distiller.verify_token_budget(huge_text, max_tokens=MAX_CORE_TOKEN_BUDGET)
        self.assertFalse(is_valid_huge)
        self.assertGreater(tok_huge, MAX_CORE_TOKEN_BUDGET)

    def test_skill_distiller_live_distillation(self):
        distiller = SkillDistiller()
        stats = distiller.distill_all(auto_install=False)
        self.assertGreaterEqual(stats["approved_cards_loaded"], 28)
        self.assertTrue(stats["token_budget_compliant"])
        self.assertLessEqual(stats["core_rules_token_count"], MAX_CORE_TOKEN_BUDGET)

if __name__ == "__main__":
    unittest.main()
