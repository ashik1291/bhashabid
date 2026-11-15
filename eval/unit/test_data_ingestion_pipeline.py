# eval/unit/test_data_ingestion_pipeline.py
# Verification of 17-Sector Ingestion Pipeline & 4-Tier Fallback Cascade
import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.domain_taxonomy import CANONICAL_SECTORS, canonicalize_sector, get_sector_number
from tools.mistake_synthesizer import MistakeLearningSynthesizer
from tools.autonomous_scraper import AutonomousScraper


class TestDataIngestionPipeline(unittest.TestCase):
    def setUp(self):
        self.synth = MistakeLearningSynthesizer()
        self.scraper = AutonomousScraper()

    def test_domain_taxonomy_completeness(self):
        """Verifies exactly 17 canonical sectors are defined and numbered 1..17."""
        self.assertEqual(len(CANONICAL_SECTORS), 17)
        for idx, sec in enumerate(CANONICAL_SECTORS, start=1):
            self.assertEqual(canonicalize_sector(sec), sec)
            self.assertEqual(get_sector_number(sec), idx)

    def test_alias_normalization(self):
        """Verifies historical corpus and practice aliases map to canonical designations."""
        aliases = [
            ("Banking & Macroeconomics", "Macroeconomics & Banking"),
            ("Tax & Customs", "Macroeconomics & Banking"),
            ("Macroeconomic & Finance", "Macroeconomics & Banking"),
            ("Official Administrative", "Administrative Governance & Memos"),
            ("Administrative Governance", "Administrative Governance & Memos"),
            ("Land Conveyancing & Deeds", "Land Registry & Deeds"),
            ("Judicial & High Court", "Constitutional Law & Writs"),
            ("Sports Vernacular", "Mass Media & Digital Journalism"),
            ("Corporate & Tech", "ICT & Software Engineering"),
            ("Disaster Early Warning", "Agronomy & Disaster Management"),
            ("Agronomy & Crop Protection", "Agronomy & Disaster Management"),
            ("Education & Pedagogy", "Education & NCTB Pedagogy"),
            ("Science & Encyclopedic", "Academic Research & Methodology"),
            ("Poetic Prosody", "Classical Poetry & Prosody"),
            ("Healthcare & Medicine", "Healthcare & Epidemiology"),
            ("Customer Support & Conversational Chat", "Customer Support & Omnichannel Messaging"),
            ("Translation, Calque De-Naturalization & Idioms", "Translation & Calque Naturalization"),
        ]
        for alias, expected in aliases:
            self.assertEqual(canonicalize_sector(alias), expected)

    def test_mistake_synthesizer_all_17_sectors(self):
        """Verifies mistake learning synthesizer yields valid challenge items for all 17 sectors."""
        for sec in CANONICAL_SECTORS:
            items = self.synth.synthesize_sector_batch(sec, count=2)
            self.assertEqual(len(items), 2, f"Failed for sector: {sec}")
            for itm in items:
                self.assertTrue(len(itm["text"]) > 15)
                self.assertIn("MISTAKE-LEARN-", itm["id"])

    def test_offline_fallback_cascade(self):
        """Verifies scraper falls back to local corpora and mistake synthesis when feeds are offline."""
        offline_scraper = AutonomousScraper(feeds=[{"name": "Dummy", "url": "http://127.0.0.1:9999/null", "domain": "General"}])
        items = offline_scraper.scrape_targeted_sector_data(["Banking & Macroeconomics"], max_items_per_sector=2)
        self.assertEqual(len(items), 2)
        for itm in items:
            self.assertEqual(itm["domain"], "Banking & Macroeconomics")
            self.assertTrue(len(itm["text"]) > 15)

    def test_stratified_deficit_balanced_mixing(self):
        """Verifies multi-source sectors harvest both RSS and Open API feeds or gracefully spill over."""
        items = self.scraper.scrape_targeted_sector_data(["Macroeconomics & Banking"], max_items_per_sector=4)
        self.assertEqual(len(items), 4)
        for itm in items:
            self.assertTrue(len(itm["text"]) > 15)
            self.assertEqual(itm["domain"], "Macroeconomics & Banking")


if __name__ == "__main__":
    unittest.main()
