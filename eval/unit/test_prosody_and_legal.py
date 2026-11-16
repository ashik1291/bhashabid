# eval/unit/test_prosody_and_legal.py
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_prosody import scan_line, verify_payar, verify_rhyme
from tools.bn_legal import determine_writ_type, generate_writ_prayer, WritType
from tools.verify_provenance import audit_provenance

class TestProsodyAndLegal(unittest.TestCase):

    def test_payar_validity(self):
        line = "কাশীদাস কহে সাধু শুনে পুণ্যবান"
        res = verify_payar(line)
        self.assertTrue(res.is_valid_payar)
        self.assertEqual(res.part1_morae, 8)
        self.assertEqual(res.part2_morae, 6)
        self.assertEqual(res.total_morae, 14)

    def test_broken_payar(self):
        broken_line = "কাশীদাস বলিতেছেন কথা তোমরা শোনো"
        res = verify_payar(broken_line)
        self.assertFalse(res.is_valid_payar)

    def test_rhyme_verification(self):
        line1 = "কাশীদাস কহে সাধু শুনে পুণ্যবান"
        line2 = "মহাভারত কথা অমৃত সমান"
        self.assertTrue(verify_rhyme(line1, line2))

    def test_dalabritta_scansion(self):
        line = "বৃষ্টি পড়ে টাপুর টুপুর"
        res = scan_line(line, metre_system="dalabritta")
        self.assertGreater(res.total_morae, 0)
        self.assertEqual(res.total_morae, res.total_syllables)

    def test_writ_type_determination(self):
        self.assertEqual(determine_writ_type("illegal detention in custody"), WritType.HABEAS_CORPUS)
        self.assertEqual(determine_writ_type("quash unlawful order"), WritType.CERTIORARI)
        self.assertEqual(determine_writ_type("compel statutory officer to perform duty"), WritType.MANDAMUS)
        self.assertEqual(determine_writ_type("dispute qualification to hold public office"), WritType.QUO_WARRANTO)

    def test_writ_prayer_generation(self):
        prayers = generate_writ_prayer(
            writ_type=WritType.CERTIORARI,
            subject="অবৈধ বহিষ্কার আদেশ",
            authority_name="রেজিস্ট্রার"
        )
        self.assertGreaterEqual(len(prayers), 2)
        self.assertTrue(any("আইনগত কর্তৃত্ববহির্ভূত" in p for p in prayers))

    def test_civil_conveyancing_deeds(self):
        from tools.bn_legal import DeedType, DeedSchedule, format_deed_schedule, generate_encumbrance_free_clause, generate_saf_kabala_clause
        sch = DeedSchedule(
            district="ঢাকা",
            subregistry="তেজগাঁও",
            mouza="বাড্ডা",
            jl_number="১২",
            khatian_type="আরএস",
            khatian_number="৪৫৬",
            dag_number="৭৮৯",
            land_class="নাল",
            area="৫ শতাংশ",
            boundaries={"north": "রহিমের জমি", "south": "সরকারি রাস্তা", "east": "করিমের বাড়ি", "west": "খাল"}
        )
        formatted = format_deed_schedule(sch)
        self.assertIn("তফশিল সম্পত্তি পরিচয়", formatted)
        self.assertIn("খতিয়ান (আরএস): ৪৫৬", formatted)
        self.assertIn("দাগ নম্বর: ৭৮৯", formatted)

        encumbrance = generate_encumbrance_free_clause("১ম পক্ষ বিক্রেতা")
        self.assertIn("দায়মুক্ত", encumbrance)
        self.assertIn("ঋণভার", encumbrance)

        clause = generate_saf_kabala_clause("১ম পক্ষ বিক্রেতা", "২য় পক্ষ ক্রেতা", "বিশ লাখ টাকা", sch)
        self.assertIn("সাফ-কবলা", clause)
        self.assertIn("মৌজা বাড্ডা", clause)
        self.assertIn("বিশ লাখ টাকা", clause)

    def test_p2_provenance_audit(self):
        stats = audit_provenance()
        self.assertEqual(len(stats["p2_violations"]), 0)
        self.assertGreater(stats["total_cards"], 20)

if __name__ == "__main__":
    unittest.main()
