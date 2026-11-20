# Lightweight MCP Server for Bhashabid tools
import json
from ..numbers import (
    number_to_bangla_words,
    decimal_to_bangla_words,
    format_lakh_crore,
    format_currency_words,
    to_ascii_digits
)
from ..normalize import normalize
from ..lint import lint_text

class BhashabidMCPServer:
    """
    Model Context Protocol (MCP) compatible server exposing Bhashabid deterministic tools:
    - convert_number: Converts digits to Bengali words and South Asian comma formats.
    - normalize_text: Canonicalizes Bengali text to NFC and standard orthography.
    - lint_text: Detects Guru-chandali, honorific clashes, and calques.
    """

    def __init__(self):
        self.tools = [
            {
                "name": "convert_number",
                "description": "Convert integers, floating-point decimals, fractions, ordinals, and currencies into standard Bengali words, fractions, ordinals, or South Asian lakh/crore comma grouping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {"description": "The number to convert (integer, float, or string like '89079490.7890' or '৮৯০৭৯৪৯০.৭৮৯০')."},
                        "format": {"type": "string", "enum": ["words", "grouped", "currency", "fraction", "ordinal", "date_ordinal"], "default": "words"}
                    },
                    "required": ["number"]
                }
            },
            {
                "name": "normalize_text",
                "description": "Normalize Bengali text: Unicode NFC, Dari punctuation, and Bangla Academy orthography.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The raw Bengali text to normalize."},
                        "profile": {"type": "string", "default": "bd_standard"}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "lint_text",
                "description": "Lint Bengali text for Guru-chandali (Sadhu-Cholito mixing), honorific clashes, calques, and optional spelling mistakes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali text to lint."},
                        "check_spelling": {"type": "boolean", "default": False, "description": "Whether to include offline phonetic spelling error checks."}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "repair_text",
                "description": "Automatically repair and normalize Bengali text flaws: Unicode, orthography, punctuation, Guru-chandali, English translation calques, and honorific concordance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali text to repair and normalize."},
                        "profile": {"type": "string", "default": "bd_standard"}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "prosody_scan",
                "description": "Scan Bengali verse for poetic metre (Payar, Matrabritta, Dalabritta) and verify caesura and rhyme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali verse line."},
                        "metre": {"type": "string", "enum": ["aksharbritta", "matrabritta", "dalabritta"], "default": "aksharbritta"},
                        "verify_payar": {"type": "boolean", "default": False}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "generate_writ_prayer",
                "description": "Generate Article 102 High Court constitutional writ prayers in statutory Bengali.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remedy": {"type": "string", "description": "Core remedy (e.g. detention, illegal order, public office)."},
                        "subject": {"type": "string", "description": "Subject matter of the grievance."},
                        "authority": {"type": "string", "description": "Respondent authority name."}
                    },
                    "required": ["remedy", "subject", "authority"]
                }
            },
            {
                "name": "spellcheck_text",
                "description": "Offline deterministic Bengali spellchecker: detects unrecognized words and suggests closest phonetic corrections.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali text to spellcheck."}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "generate_deed_clause",
                "description": "Generate standard statutory Bengali civil conveyancing clauses (Saf-Kabala, Encumbrance-Free, Deed Schedule).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "deed_type": {"type": "string", "enum": ["saf_kabala", "encumbrance_free", "schedule"], "description": "Type of deed clause to generate."},
                        "vendor_name": {"type": "string", "description": "Vendor / transferor name (বিক্রেতা)."},
                        "purchaser_name": {"type": "string", "description": "Purchaser / transferee name (ক্রেতা)."},
                        "consideration_taka": {"type": "number", "description": "Total consideration amount in BDT (পণমূল্য)."},
                        "district": {"type": "string", "description": "District name (জেলা)."},
                        "thana": {"type": "string", "description": "Police Station / Upazila (থানা)."},
                        "mouza": {"type": "string", "description": "Mouza name (মৌজা)."},
                        "jl_no": {"type": "string", "description": "J.L. Number (জে. এল. নং)."},
                        "khatian_no": {"type": "string", "description": "Khatian Number (খতিয়ান নং)."},
                        "dag_no": {"type": "string", "description": "Plot / Dag Number (দাগ নং)."},
                        "land_area": {"type": "string", "description": "Land area and class (জমির শ্রেণি ও পরিমাণ)."},
                        "boundaries": {"type": "object", "description": "Boundaries dictionary (চৌহদ্দি): north, south, east, west."}
                    },
                    "required": ["deed_type"]
                }
            },
            {
                "name": "format_date",
                "description": "Format Gregorian calendar dates into standard Bengali date strings or convert to official Bangabda (বঙ্গাব্দ) calendar (Bangla Academy 2019 revision).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "ISO date string ('YYYY-MM-DD') or Bengali date string."},
                        "calendar": {"type": "string", "enum": ["gregorian", "gregorian_bangla", "bongabdo"], "default": "gregorian", "description": "Target calendar: 'gregorian' (২৬শে মার্চ, ২০২৬) or 'bongabdo' (১৪৩৩ বঙ্গাব্দ)."},
                        "ordinal_suffix": {"type": "boolean", "default": True, "description": "Gregorian only. false gives modern news/official style without day suffix (২৬ মার্চ, ২০২৬)."}
                    },
                    "required": ["date"]
                }
            },
            {
                "name": "audit_literary_text",
                "description": "Deterministic literary, poetic, and creative translation quality audit. Detects biological/anatomical hallucinations (e.g. invented wings on marine life), gemstone transliteration surrenders, and metric padding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The literary Bengali text to audit."},
                        "archetype": {"type": "string", "enum": ["general", "imagist", "romantic", "realist"], "default": "general", "description": "Authorial style archetype."}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "lookup_lapidary",
                "description": "Look up authentic classical Bengali literary equivalents for precious gems, minerals, and anatomical nature terms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "term": {"type": "string", "description": "English mineral, gem, or anatomical term (e.g. 'amethyst', 'amber', 'slough', 'jellyfish bell')."}
                    },
                    "required": ["term"]
                }
            },
            {
                "name": "generate_literary_prompt",
                "description": "Generate a self-sufficient, 5-laws literary translation prompt for any world poet or author.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_text": {"type": "string", "description": "The source literary text to translate."},
                        "author": {"type": "string", "description": "Author or poet name."},
                        "archetype": {"type": "string", "default": "auto", "description": "Authorial style archetype."},
                        "rhymed": {"type": "boolean", "default": False, "description": "Whether to enforce Bengali classical metrical rhyme."}
                    },
                    "required": ["source_text"]
                }
            }
        ]

    def list_tools(self) -> list[dict]:
        return self.tools

    def call_tool(self, name: str, arguments: dict) -> dict:
        if name == "convert_number":
            raw_val = str(arguments.get("number", 0)).strip()
            fmt = arguments.get("format", "words")
            val_ascii = to_ascii_digits(raw_val)
            try:
                if fmt == "grouped":
                    res = format_lakh_crore(val_ascii)
                    return {"result": res}
                elif fmt == "currency":
                    res = format_currency_words(float(val_ascii))
                    return {"result": res}
                elif fmt == "fraction":
                    from ..numbers import fraction_to_bangla_words
                    res = fraction_to_bangla_words(float(val_ascii))
                    return {"result": res}
                elif fmt == "ordinal":
                    from ..numbers import to_classical_ordinal
                    res = to_classical_ordinal(int(val_ascii))
                    return {"result": res}
                elif fmt == "date_ordinal":
                    from ..numbers import to_date_ordinal
                    res = to_date_ordinal(int(val_ascii))
                    return {"result": res}
                else:
                    if "." in val_ascii:
                        res = decimal_to_bangla_words(val_ascii)
                    else:
                        res = number_to_bangla_words(int(val_ascii))
                    return {"result": res}
            except (ValueError, TypeError) as ve:
                return {"result": "", "error": f"Invalid numeric input '{raw_val}': {str(ve)}"}

        elif name == "normalize_text":
            raw_text = arguments.get("text") or ""
            profile = arguments.get("profile", "bd_standard")
            res = normalize(raw_text, profile=profile)
            return {"result": res}

        elif name == "lint_text":
            raw_text = arguments.get("text") or ""
            check_spelling = arguments.get("check_spelling", False)
            issues = lint_text(raw_text, include_spelling=check_spelling)
            diagnostics = [
                {
                    "rule_id": issue.rule_id,
                    "message": issue.message,
                    "line": issue.line,
                    "col": issue.col,
                    "severity": issue.severity.value,
                    "matched": issue.matched_text,
                    "suggestion": issue.suggestion
                }
                for issue in issues
            ]
            return {"issues": diagnostics, "issue_count": len(diagnostics)}

        elif name == "repair_text":
            from ..normalize.repair import repair_text
            raw_text = arguments.get("text") or ""
            profile = arguments.get("profile", "bd_standard")
            repaired, fixes = repair_text(raw_text, profile=profile)
            return {
                "original": raw_text,
                "repaired": repaired,
                "fixes_count": len(fixes),
                "fixes": fixes
            }

        elif name == "prosody_scan":
            from ..prosody import scan_line, verify_payar
            raw_text = arguments.get("text") or ""
            metre = arguments.get("metre", "aksharbritta")
            if arguments.get("verify_payar", False):
                res = verify_payar(raw_text)
                return {
                    "is_valid_payar": res.is_valid_payar,
                    "part1_morae": res.part1_morae,
                    "part2_morae": res.part2_morae,
                    "total_morae": res.total_morae,
                    "explanation": res.explanation
                }
            else:
                res = scan_line(raw_text, metre_system=metre)
                return {
                    "metre_system": res.metre_system,
                    "total_morae": res.total_morae,
                    "total_syllables": res.total_syllables,
                    "open_syllables": res.open_syllables,
                    "closed_syllables": res.closed_syllables,
                    "word_mora_breakdown": res.word_mora_breakdown,
                    "scansion_notation": res.scansion_notation
                }

        elif name == "generate_writ_prayer":
            from ..legal import determine_writ_type, generate_writ_prayer, CONSTITUTIONAL_PROVISIONS
            rem = arguments.get("remedy") or ""
            subj = arguments.get("subject") or ""
            auth = arguments.get("authority") or ""
            wtype = determine_writ_type(rem)
            prayers = generate_writ_prayer(wtype, subj, auth)
            return {
                "writ_type": wtype.value,
                "constitutional_article": CONSTITUTIONAL_PROVISIONS.get(wtype, ""),
                "prayers": prayers
            }

        elif name == "spellcheck_text":
            from ..normalize.lexicon import get_default_lexicon
            raw_text = arguments.get("text") or ""
            lex = get_default_lexicon()
            issues = lex.audit_text(raw_text)
            return {
                "issues_count": len(issues),
                "issues": issues
            }

        elif name == "generate_deed_clause":
            from ..legal import (
                generate_saf_kabala_clause,
                generate_encumbrance_free_clause,
                format_deed_schedule,
                DeedSchedule
            )
            dtype = arguments.get("deed_type", "saf_kabala")
            if dtype == "saf_kabala":
                vname = arguments.get("vendor_name", "বিক্রেতা")
                pname = arguments.get("purchaser_name", "ক্রেতা")
                taka = float(arguments.get("consideration_taka", 0))
                clause = generate_saf_kabala_clause(vname, pname, taka)
                return {"deed_type": "saf_kabala", "clause": clause}
            elif dtype == "encumbrance_free":
                clause = generate_encumbrance_free_clause()
                return {"deed_type": "encumbrance_free", "clause": clause}
            elif dtype == "schedule":
                sch = DeedSchedule(
                    district=arguments.get("district", ""),
                    thana=arguments.get("thana", ""),
                    mouza=arguments.get("mouza", ""),
                    jl_no=arguments.get("jl_no", ""),
                    khatian_no=arguments.get("khatian_no", ""),
                    dag_no=arguments.get("dag_no", ""),
                    land_area=arguments.get("land_area", ""),
                    boundaries=arguments.get("boundaries")
                )
                text = format_deed_schedule(sch)
                return {"deed_type": "schedule", "schedule_text": text}
            else:
                return {
                    "deed_type": dtype,
                    "error": f"Unknown deed_type '{dtype}'. Allowed: 'saf_kabala', 'encumbrance_free', 'schedule'."
                }

        elif name == "format_date":
            raw_date = str(arguments.get("date", "")).strip()
            calendar_type = arguments.get("calendar", "gregorian")
            try:
                from ..numbers.dates import format_date_bangla, format_date_bongabdo, gregorian_to_bongabdo
                if calendar_type in ("bongabdo", "bangabda"):
                    formatted = format_date_bongabdo(raw_date, from_gregorian=True)
                    y, m, d = gregorian_to_bongabdo(raw_date)
                    return {
                        "input": raw_date,
                        "calendar": "bongabdo",
                        "formatted": formatted,
                        "bongabdo_year": y,
                        "bongabdo_components": {"year": y, "month": m, "day": d}
                    }
                else:
                    formatted = format_date_bangla(raw_date, ordinal_suffix=bool(arguments.get("ordinal_suffix", True)))
                    return {
                        "input": raw_date,
                        "calendar": "gregorian",
                        "formatted": formatted
                    }
            except Exception as e:
                return {"error": f"Failed to format date: {e}"}

        elif name == "audit_literary_text":
            from ..creative import audit_literary_text
            txt = str(arguments.get("text", ""))
            arch = str(arguments.get("archetype", "general"))
            return {"result": audit_literary_text(txt, archetype=arch)}

        elif name == "lookup_lapidary":
            from ..creative import lookup_lapidary
            term = str(arguments.get("term", ""))
            res = lookup_lapidary(term)
            return {"term": term, "equivalents": list(res) if res else []}

        elif name == "generate_literary_prompt":
            from ..creative import generate_literary_prompt
            src = str(arguments.get("source_text", ""))
            author = arguments.get("author")
            arch = str(arguments.get("archetype", "auto"))
            rhymed = bool(arguments.get("rhymed", False))
            prompt = generate_literary_prompt(src, author=author, genre_or_archetype=arch, rhymed=rhymed)
            return {"result": prompt}

        else:
            raise ValueError(f"Unknown tool: {name}")

    def run_stdio(self, max_frame_bytes: int = 10 * 1024 * 1024):
        """
        Runs standard JSON-RPC 2.0 stdio server loop for Model Context Protocol (MCP) clients
        (Claude Desktop, Cursor, Antigravity, Windsurf).
        Guards against unbounded line allocations by enforcing max_frame_bytes (default: 10MB).
        Guarantees UTF-8 serialization across all operating systems (including Windows charmap).
        """
        import sys
        if hasattr(sys.stdout, "reconfigure"):
            try:
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
                sys.stdin.reconfigure(encoding="utf-8", errors="replace")
                sys.stderr.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

        def _write_resp(resp_obj):
            payload_str = json.dumps(resp_obj, ensure_ascii=False) + "\n"
            try:
                sys.stdout.write(payload_str)
                sys.stdout.flush()
            except (UnicodeEncodeError, LookupError):
                if hasattr(sys.stdout, "buffer"):
                    sys.stdout.buffer.write(payload_str.encode("utf-8", errors="replace"))
                    sys.stdout.buffer.flush()
                else:
                    sys.stdout.write(json.dumps(resp_obj, ensure_ascii=True) + "\n")
                    sys.stdout.flush()

        while True:
            raw_line = sys.stdin.readline(max_frame_bytes)
            if not raw_line:
                break
            if len(raw_line) >= max_frame_bytes and not raw_line.endswith("\n"):
                # Consume until next newline to realign stream
                sys.stdin.readline()
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32600, "message": "Payload Too Large: JSON-RPC frame exceeds maximum size limit (10MB)"}
                }
                _write_resp(err_resp)
                continue

            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                msg = json.loads(raw_line)
                msg_id = msg.get("id")
                method = msg.get("method")
                params = msg.get("params", {})

                if method == "initialize":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {
                                "tools": {}
                            },
                            "serverInfo": {
                                "name": "bhashabid-mcp",
                                "version": "1.1.1"
                            }
                        }
                    }
                elif method in ("notifications/initialized", "initialized"):
                    continue
                elif method == "tools/list":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "tools": [
                                {
                                    "name": t["name"],
                                    "description": t["description"],
                                    "inputSchema": t["parameters"]
                                }
                                for t in self.list_tools()
                            ]
                        }
                    }
                elif method == "tools/call":
                    tool_name = params.get("name")
                    args = params.get("arguments", {})
                    out = self.call_tool(tool_name, args)
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps(out, ensure_ascii=False, indent=2)
                                }
                            ]
                        }
                    }
                elif method == "ping":
                    resp = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
                else:
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "error": {"code": -32601, "message": f"Method {method} not found"}
                    }
                _write_resp(resp)
            except Exception as ex:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": msg.get("id") if "msg" in locals() else None,
                    "error": {"code": -32603, "message": str(ex)}
                }
                _write_resp(err_resp)

def main():
    srv = BhashabidMCPServer()
    srv.run_stdio()

if __name__ == "__main__":
    main()
