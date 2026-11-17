# Unit Tests for Bhashabid MCP Server
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.mcp_server import BhashabidMCPServer

class TestMCPServer(unittest.TestCase):

    def setUp(self):
        self.server = BhashabidMCPServer()

    def test_list_tools(self):
        tools = self.server.list_tools()
        names = [t["name"] for t in tools]
        self.assertIn("convert_number", names)
        self.assertIn("normalize_text", names)
        self.assertIn("lint_text", names)

    def test_call_convert_number(self):
        res = self.server.call_tool("convert_number", {"number": 99, "format": "words"})
        self.assertEqual(res["result"], "নিরানব্বই")

        res_grouped = self.server.call_tool("convert_number", {"number": 1234567, "format": "grouped"})
        self.assertEqual(res_grouped["result"], "১২,৩৪,৫৬৭")

        # Test floating-point and string decimal handling
        res_dec = self.server.call_tool("convert_number", {"number": "89079490.7890", "format": "words"})
        self.assertEqual(
            res_dec["result"],
            "আট কোটি নব্বই লাখ ঊনআশি হাজার চার শত নব্বই দশমিক সাত আট নয় শূন্য"
        )

        res_dec_float = self.server.call_tool("convert_number", {"number": 3.14, "format": "words"})
        self.assertEqual(res_dec_float["result"], "তিন দশমিক এক চার")

        res_dec_grouped = self.server.call_tool("convert_number", {"number": "89079490.7890", "format": "grouped"})
        self.assertEqual(res_dec_grouped["result"], "৮,৯০,৭৯,৪৯০.৭৮৯০")

        res_curr = self.server.call_tool("convert_number", {"number": "50.25", "format": "currency"})
        self.assertEqual(res_curr["result"], "পঞ্চাশ টাকা পঁচিশ পয়সা")

        res_frac = self.server.call_tool("convert_number", {"number": 2.5, "format": "fraction"})
        self.assertEqual(res_frac["result"], "আড়াই")

        res_ord = self.server.call_tool("convert_number", {"number": 35, "format": "ordinal"})
        self.assertEqual(res_ord["result"], "৩৫-তম")

        res_date_ord = self.server.call_tool("convert_number", {"number": 26, "format": "date_ordinal"})
        self.assertEqual(res_date_ord["result"], "২৬শে")

    def test_call_normalize_text(self):
        res = self.server.call_tool("normalize_text", {"text": "তিনি রেলষ্টেশনে গেলেন."})
        self.assertEqual(res["result"], "তিনি রেলস্টেশনে গেলেন।")

    def test_call_lint_text(self):
        res = self.server.call_tool("lint_text", {"text": "আপনি কি কাজটি করো?"})
        self.assertGreater(res["issue_count"], 0)
        self.assertEqual(res["issues"][0]["rule_id"], "RULE-LINT-HONORIFIC-APNI")

    def test_call_generate_deed_clause(self):
        res_saf = self.server.call_tool("generate_deed_clause", {
            "deed_type": "saf_kabala",
            "vendor_name": "করিম উদ্দিন",
            "purchaser_name": "রহিম মিয়া",
            "consideration_taka": 500000
        })
        self.assertEqual(res_saf["deed_type"], "saf_kabala")
        self.assertIn("করিম উদ্দিন", res_saf["clause"])
        self.assertIn("রহিম মিয়া", res_saf["clause"])
        self.assertIn("পাঁচ লাখ টাকা", res_saf["clause"])

        res_enc = self.server.call_tool("generate_deed_clause", {
            "deed_type": "encumbrance_free"
        })
        self.assertEqual(res_enc["deed_type"], "encumbrance_free")
        self.assertIn("দায়মুক্ত ও নির্ভেজাল", res_enc["clause"])

        res_sch = self.server.call_tool("generate_deed_clause", {
            "deed_type": "schedule",
            "district": "ঢাকা",
            "thana": "গুলশান",
            "mouza": "বাড্ডা",
            "jl_no": "১২",
            "dag_no": "৪৫০",
            "land_area": "১০ শতাংশ"
        })
        self.assertEqual(res_sch["deed_type"], "schedule")
        self.assertIn("তফশিল", res_sch["schedule_text"])
        self.assertIn("মৌজা: বাড্ডা", res_sch["schedule_text"])

    def test_call_format_date(self):
        res_greg = self.server.call_tool("format_date", {"date": "2026-03-26"})
        self.assertEqual(res_greg["formatted"], "২৬শে মার্চ, ২০২৬")
        self.assertEqual(res_greg["calendar"], "gregorian")

        res_bong = self.server.call_tool("format_date", {"date": "2026-04-14", "calendar": "bongabdo"})
        self.assertEqual(res_bong["formatted"], "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ")
        self.assertEqual(res_bong["calendar"], "bongabdo")
        self.assertEqual(res_bong["bongabdo_year"], 1433)

if __name__ == "__main__":
    unittest.main()
