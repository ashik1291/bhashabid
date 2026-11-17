# CLI Integration Unit Tests
import unittest
import subprocess
import sys
import os
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestCLI(unittest.TestCase):

    def run_cli(self, args: list[str], module: str = "bhashabid.cli") -> tuple[int, str, str]:
        cmd = [sys.executable, "-m", module] + args
        p = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()

    def test_cli_number_words(self):
        code, out, _ = self.run_cli(["number", "99"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "নিরানব্বই")

    def test_cli_number_grouped(self):
        code, out, _ = self.run_cli(["number", "1234567", "--format", "grouped"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "১২,৩৪,৫৬৭")

    def test_cli_number_direct_flags(self):
        code, out, _ = self.run_cli(["number", "105.5", "--fraction"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "সাড়ে এক শত পাঁচ")

        code, out, _ = self.run_cli(["number", "50.25", "--currency"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "পঞ্চাশ টাকা পঁচিশ পয়সা")

        code, out, _ = self.run_cli(["number", "32", "--date-ordinal"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "৩২ই")

        code, out, _ = self.run_cli(["number", "25", "--ordinal"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "পঞ্চবিংশ")

        code, out, _ = self.run_cli(["number", "1234567", "--grouped"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "১২,৩৪,৫৬৭")

    def test_cli_normalize(self):
        code, out, _ = self.run_cli(["normalize", "তিনি রেলষ্টেশনে গেলেন."])
        self.assertEqual(code, 0)
        self.assertEqual(out, "তিনি রেলস্টেশনে গেলেন।")

    def test_cli_lint_json(self):
        code, out, _ = self.run_cli(["lint", "তুমি সিদ্ধান্ত নেন", "--json"])
        self.assertEqual(code, 1) # Has error
        data = json.loads(out)
        self.assertGreater(len(data), 0)
        self.assertEqual(data[0]["rule_id"], "RULE-LINT-HONORIFIC-TUMI")
        self.assertIn("তুমি সিদ্ধান্ত নাও", data[0]["suggestion"])

    def test_cli_lint_clean(self):
        code, out, _ = self.run_cli(["lint", "আপনি কাল সকালে আসুন।"])
        self.assertEqual(code, 0)
        self.assertIn("কোনো ব্যাকরণগত বা বানানজনিত ত্রুটি পাওয়া যায়নি", out)

    def test_cli_lint_with_spelling(self):
        code, out, _ = self.run_cli(["lint", "তিনি শ্রদ্ধাঞ্জলী জানালেন।", "--spelling", "--json"])
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertTrue(any(item["rule_id"] == "RULE-LINT-SPELLING" for item in data))
        self.assertTrue(any(item["matched"] == "শ্রদ্ধাঞ্জলী" for item in data))

    def test_cli_install_and_uninstall(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            # Test CLI install-skill
            code, out, _ = self.run_cli(["install-skill", "--target", "cursor", "--workspace", tmpdir])
            self.assertEqual(code, 0)
            self.assertIn("successfully installed", out)

            # Test CLI uninstall-skill
            code, out, _ = self.run_cli(["uninstall-skill", "--target", "cursor", "--workspace", tmpdir])
            self.assertEqual(code, 0)
            self.assertIn("successfully removed", out)

    def test_cli_deed_generation(self):
        code_saf, out_saf, _ = self.run_cli([
            "deed", "--type", "saf-kabala",
            "--vendor", "করিম উদ্দিন",
            "--purchaser", "রহিম মিয়া",
            "--taka", "500000"
        ])
        self.assertEqual(code_saf, 0)
        self.assertIn("সাফ-কবলা হস্তান্তর", out_saf)
        self.assertIn("করিম উদ্দিন", out_saf)
        self.assertIn("পাঁচ লাখ টাকা", out_saf)

        code_enc, out_enc, _ = self.run_cli(["deed", "--type", "encumbrance"])
        self.assertEqual(code_enc, 0)
        self.assertIn("দায়মুক্তি ও নির্ভেজাল ঘোষণা", out_enc)

        code_sch, out_sch, _ = self.run_cli([
            "deed", "--type", "schedule",
            "--district", "ঢাকা",
            "--mouza", "বাড্ডা"
        ])
        self.assertEqual(code_sch, 0)
        self.assertIn("তফশিল", out_sch)
        self.assertIn("বাড্ডা", out_sch)

    def test_cli_writ_respondent_flag(self):
        code, out, _ = self.run_cli([
            "writ", "--remedy", "detention", "--subject", "করিম",
            "--respondent", "স্বরাষ্ট্র মন্ত্রণালয়"
        ])
        self.assertEqual(code, 0)
        self.assertIn("হেবিয়াস কর্পাস", out)
        self.assertIn("স্বরাষ্ট্র মন্ত্রণালয়", out)

    def test_cli_review_list_and_ledger(self):
        code_rev, out_rev, _ = self.run_cli(["review", "--list"])
        self.assertEqual(code_rev, 0)
        self.assertIn("PENDING HUMAN REVIEW QUEUE", out_rev)

        code_led, out_led, _ = self.run_cli(["ledger"])
        self.assertEqual(code_led, 0)
        self.assertIn("BHASHABID EMPIRICAL LEARNING BENCHMARK LEDGER", out_led)

    def test_cli_tools_package_parity(self):
        # Verify bhashabid.cli and tools.cli produce identical number word conversions
        code1, out1, _ = self.run_cli(["number", "99"], module="bhashabid.cli")
        code2, out2, _ = self.run_cli(["number", "99"], module="tools.cli")
        self.assertEqual(code1, code2)
        self.assertEqual(out1, out2)

    def test_cli_date_formatting(self):
        code1, out1, _ = self.run_cli(["date", "2026-03-26"])
        self.assertEqual(code1, 0)
        self.assertEqual(out1, "২৬শে মার্চ, ২০২৬")

        code2, out2, _ = self.run_cli(["date", "2026-04-14", "--bongabdo"])
        self.assertEqual(code2, 0)
        self.assertEqual(out2, "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ")

        # Test CLI parity across bhashabid.cli and tools.cli
        code_p1, out_p1, _ = self.run_cli(["date", "2026-04-14", "--bongabdo"], module="tools.cli")
        self.assertEqual(code2, code_p1)
        self.assertEqual(out2, out_p1)

if __name__ == "__main__":
    unittest.main()
