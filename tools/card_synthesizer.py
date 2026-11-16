# tools/card_synthesizer.py
# Automated Knowledge Card Synthesizer & Error Clustering Engine
import os
import sys
import yaml
import glob
import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode

DRAFTS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts")
CARDS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards")
REJECTED_DIR = os.path.join(REPO_ROOT, "knowledge", "cards", "rejected")

AUTHORITATIVE_DOMAIN_STANDARDS = {
    "Constitutional Law & Writs": [
        "Constitution of the People's Republic of Bangladesh (Article 102)",
        "Supreme Court of Bangladesh Judicial Precedents",
        "Bangla Academy Law Dictionary"
    ],
    "Macroeconomics & Banking": [
        "Bangladesh Bank Prudential Regulations & Monetary Policy",
        "Bangla Academy Financial & Economic Terminology",
        "The Business Standard Verified Macroeconomic Feed"
    ],
    "Healthcare & Epidemiology": [
        "Bangla Academy Medical Science Dictionary (চিকিৎসাবিজ্ঞান পরিভাষা)",
        "Directorate General of Health Services (DGHS) Bangladesh"
    ],
    "Administrative Governance & Memos": [
        "Secretariat Instructions (সচিবালয় নির্দেশমালা, জনপ্রশাসন মন্ত্রণালয়)",
        "Bangladesh Government Official Memo Standards"
    ],
    "Creative Fiction & Dialogue": [
        "Bangla Academy Standard Bengali Grammar (প্রমিত বাংলা ভাষার ব্যাকরণ)",
        "Bangla Academy Modern Bengali Dictionary (আধুনিক বাংলা অভিধান)"
    ],
    "Classical Poetry & Prosody": [
        "Rabindranath Tagore & Probodh Chandra Sen Bengali Prosody (ছন্দতত্ত্ব)",
        "Classical 14-Akshar Payar Metric Canon"
    ],
    "Academic Research & Methodology": [
        "Bangla Academy Linguistic Research Methodology Guidelines",
        "Linguistic Society of Bangladesh Peer-Reviewed Standards"
    ],
    "Land Registry & Deeds": [
        "Transfer of Property Act 1882 & Registration Act 1908",
        "Ministry of Land Official Saf-Kabala Deed Conveyancing Protocol"
    ],
    "Agronomy & Disaster Management": [
        "Ministry of Agriculture & Department of Agricultural Extension (DAE)",
        "Disaster Management Bureau Standing Orders on Disaster (SOD)"
    ],
    "ICT & Software Engineering": [
        "Bangladesh Computer Council (BCC) Bengali Computing & Unicode Standards",
        "Open-Source Bengali Localization Best Practices"
    ],
    "Education & NCTB Pedagogy": [
        "National Curriculum and Textbook Board (NCTB) Standard Bengali",
        "Ministry of Education Pedagogical Guidelines"
    ],
    "Translation & Calque Naturalization": [
        "Bangla Academy Standard Bengali Grammar (প্রমিত বাংলা ভাষার ব্যাকরণ)",
        "Bangla Academy Promito Byaboharik Bangla Obhidhan",
        "Bengali Syntax Naturalization Guidelines"
    ],
    "Consumer E-Commerce & Retail Logistics": [
        "Consumers' Rights Protection Act 2009 (ভোক্তা অধিকার সংরক্ষণ আইন ২০০৯)",
        "e-Commerce Association of Bangladesh (e-CAB) Operational Guidelines",
        "Universal Postal Union & Domestic Courier Conveyancing Standards"
    ],
    "Citizen Digital Services & Smart Governance": [
        "Aspire to Innovate (a2i) Citizen Service Standards (স্মার্ট নাগরিক সেবা রূপরেখা)",
        "Bangladesh National Portal (bangladesh.gov.bd) Terminology Guide",
        "Election Commission Bangladesh National ID Registration Rules"
    ],
    "Customer Support & Conversational Chat": [
        "Bangla Academy Conversational Polite Register Standards",
        "Telecom & Omnichannel Customer Experience Quality Benchmarks"
    ],
    "MFS, Microfinance & Grassroots FinTech": [
        "Bangladesh Bank Payment Systems Department (PSD) MFS Guidelines",
        "Microcredit Regulatory Authority (MRA) Rules & Standards",
        "Anti-Money Laundering & Financial Fraud Prevention Protocols"
    ],
    "Mass Media & Digital Journalism": [
        "Bangladesh Press Council Code of Ethics & Stylebook",
        "Press Institute of Bangladesh (PIB) Media Reporting Standards"
    ]
}

CANONICAL_DOMAIN_MAP = {
    "Judicial & High Court": "Constitutional Law & Writs",
    "Banking & Macroeconomics": "Macroeconomics & Banking",
    "Macroeconomic & Finance": "Macroeconomics & Banking",
    "Healthcare & Medicine": "Healthcare & Epidemiology",
    "Administrative Governance": "Administrative Governance & Memos",
    "Official Administrative": "Administrative Governance & Memos",
    "Poetic Prosody": "Classical Poetry & Prosody",
    "Land Conveyancing & Deeds": "Land Registry & Deeds",
    "Agronomy & Crop Protection": "Agronomy & Disaster Management",
    "Disaster Early Warning": "Agronomy & Disaster Management",
    "Education & Pedagogy": "Education & NCTB Pedagogy",
    "Science & Encyclopedic": "ICT & Software Engineering",
    "Corporate & Tech": "ICT & Software Engineering",
    "E-Commerce & Retail": "Consumer E-Commerce & Retail Logistics",
    "E-Commerce": "Consumer E-Commerce & Retail Logistics",
    "Logistics & Delivery": "Consumer E-Commerce & Retail Logistics",
    "Public Services": "Citizen Digital Services & Smart Governance",
    "Smart Governance": "Citizen Digital Services & Smart Governance",
    "Customer Care": "Customer Support & Conversational Chat",
    "Conversational": "Customer Support & Conversational Chat",
    "MFS & FinTech": "MFS, Microfinance & Grassroots FinTech",
    "FinTech": "MFS, Microfinance & Grassroots FinTech",
    "Media & Journalism": "Mass Media & Digital Journalism",
    "Journalism": "Mass Media & Digital Journalism",
    "translation": "Translation & Calque Naturalization",
    "general": "Translation & Calque Naturalization",
}

HTML_NOISE_TOKENS = {
    "nbsp", "amp", "quot", "apos", "lt", "gt", "copy", "reg", "trade",
    "ndash", "mdash", "hellip", "para", "laquo", "raquo", "bull"
}

def is_meta_instruction(text: str) -> bool:
    """Checks if a string is an imperative meta-instruction rather than an authentic Bengali exemplar sentence."""
    if not text or not isinstance(text, str):
        return True
    instruction_patterns = [
        r"ব্যবহার করুন",
        r"পুনর্লিখন করুন",
        r"অনুবাদ করুন",
        r"পরিহার করুন",
        r"প্রমিত বাংলা অনুবাদ",
        r"বন্ধনীসহ ব্যবহার",
        r"চলিত রীতিতে",
        r"স্বাভাবিকভাবে পুনর্লিখন",
        r"সংশোধন করুন",
        r"(?:ব্যবহার|অনুবাদ|পুনর্লিখন|সংশোধন)\s+করা\s+(?:প্রয়োজন|উচিত|হবে)",
        r"বিকল্প \d+",
    ]
    for pat in instruction_patterns:
        if re.search(pat, text):
            return True
    return False

def extract_exemplars_from_suggestion(suggestion: str) -> List[str]:
    """
    Extracts concrete Bengali exemplar sentences from a suggestion.
    If the suggestion embeds alternatives in quotes, extracts pure sentences.
    If the suggestion is a pure meta-instruction, returns an empty list.
    """
    if not suggestion:
        return []
    quoted = re.findall(r"'([^']+)'", suggestion)
    valid_quoted = [q.strip() for q in quoted if q.strip() and not is_meta_instruction(q)]
    if valid_quoted:
        return valid_quoted
    if is_meta_instruction(suggestion):
        return []
    return [suggestion.strip()]

SCRAPING_NOISE_TOKENS = HTML_NOISE_TOKENS | {
    "ctrl", "alt", "shift", "tab", "esc", "enter", "delete", "insert", "caps", "space", "home", "pgup", "pgdn", "key",
    "pdf", "sms", "otp", "nid", "tin", "bin", "url", "api", "app", "web", "sim", "bdt", "usd", "eur",
    "atm", "pos", "ram", "rom", "cpu", "gpu", "wifi", "qr", "pin", "jpg", "jpeg", "png", "zip", "mp3", "mp4",
    "mbps", "kbps", "gb", "mb", "tb", "ghz", "khz", "mhz", "fps", "dpi", "px", "rem", "em", "doc", "docx", "xls", "xlsx",
    "tck", "inv", "ref", "id", "seq",
    # Hardware wallets, brand names, and peripheral models
    "ledger", "trezor", "nano", "bitbox", "keepkey", "yubikey", "safepal", "ellipal", "coolwallet", "metamask", "phantom"
}

def is_scraping_noise(matched: str, raw_context: str = "") -> bool:
    """
    Detects if a matched anomaly string is web scraping noise, HTML entities,
    Roman numerals, hardware/brand names, proper acronyms, or already explained in Bengali parentheses.
    """
    m = (matched or "").strip()
    if not m:
        return True

    # Token-set deduplication (e.g. 'BMCS, BMCS' -> 'BMCS')
    sub_tokens = [t.strip().lower() for t in re.split(r"[,;]+", m) if t.strip()]
    if not sub_tokens:
        return True

    # HTML entity check (e.g. '&nbsp;', '&#39;', '&quot;')
    clean_html = re.sub(r"[&;#]+", "", m).lower()
    if clean_html in HTML_NOISE_TOKENS or re.match(r"^&[a-zA-Z0-9#]+;$", m):
        return True

    # Check against known noise and brand tokens
    if m.lower() in SCRAPING_NOISE_TOKENS:
        return True
    if all(t in SCRAPING_NOISE_TOKENS for t in sub_tokens):
        return True

    # Serial tracking code or model code (e.g. TCK-942, INV-104, CRD-001, Nano S, Model T)
    if re.match(r"^[A-Za-z]{2,6}[-_]?\d+$", m):
        return True
    if re.search(r"\b(model\s+[a-z0-9]+|nano\s+[a-z0-9]+)\b", m, re.I):
        return True

    # Roman numeral check (e.g. XXIII, VIII)
    clean_num = re.sub(r"[\s,]+", "", m)
    if clean_num and re.match(r"^[IVXLCDMivxlcdm]+$", clean_num):
        return True

    # Parenthetical transliteration check:
    # If the text already has parenthetical Bengali (e.g. 'Pence (পেন্স)' or 'পেন্স (Pence)')
    if raw_context:
        for tok in sub_tokens:
            if len(tok) >= 2:
                # English followed by Bengali in parentheses: Word (বাংলা)
                if re.search(rf"{re.escape(tok)}\s*\([^\)]*[\u0980-\u09FF]+", raw_context, re.IGNORECASE):
                    return True
                # Bengali followed by English in parentheses: বাংলা (Word)
                if re.search(rf"[\u0980-\u09FF]+\s*\([^\)]*{re.escape(tok)}", raw_context, re.IGNORECASE):
                    return True

        # Proper uppercase acronyms with Bengali enclitic inflections (e.g. BMCS-এর, UNESCO-র, WHO-এর)
        for raw_tok in re.split(r"[,;\s]+", m):
            raw_tok = raw_tok.strip()
            if re.fullmatch(r"[A-Z]{2,6}", raw_tok):
                if re.search(rf"\b{re.escape(raw_tok)}-(?:এর|র|কে|তে|য়|এ)\b", raw_context):
                    return True

    return False

def get_domain_standards(domain: str) -> List[str]:
    canonical = CANONICAL_DOMAIN_MAP.get(domain, domain)
    return AUTHORITATIVE_DOMAIN_STANDARDS.get(
        canonical,
        ["Bangla Academy Standard Bengali Grammar", "Corpus Harvester Anomaly Detector"]
    )

class CardSynthesizer:
    """
    Automated Knowledge Card Synthesizer.
    Takes anomalies, unhandled translation calques, or domain traps harvested from real text,
    clusters recurring failure patterns, and drafts structured candidate knowledge cards for human review.
    """

    def __init__(self, drafts_dir: Optional[str] = None):
        self.drafts_dir = drafts_dir or DRAFTS_DIR
        os.makedirs(self.drafts_dir, exist_ok=True)
        os.makedirs(REJECTED_DIR, exist_ok=True)

    @staticmethod
    def get_existing_card_ids() -> set:
        existing = set()
        for f in glob.glob(os.path.join(CARDS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        for f in glob.glob(os.path.join(DRAFTS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        for f in glob.glob(os.path.join(REJECTED_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        return existing

    @staticmethod
    def get_next_draft_id() -> str:
        existing = CardSynthesizer.get_existing_card_ids()
        num = 1
        while f"CRD-DFT-{num:03d}" in existing:
            num += 1
        return f"CRD-DFT-{num:03d}"

    @staticmethod
    def find_existing_card_by_pattern(pattern: str, title: str) -> Optional[Tuple[str, Dict, str]]:
        """
        Duplicate Guard: Checks if a linguistic pattern or title is already covered
        in production cards (knowledge/cards/*.yaml), rejected cards (knowledge/cards/rejected/*.yaml),
        or existing drafts (knowledge/cards/drafts/*.yaml).
        Returns (filepath, card_dict, category) where category is 'production', 'rejected', or 'draft'.
        """
        norm_pattern = pattern.strip().lower()
        norm_title = title.strip().lower()

        # Token set for the incoming pattern (e.g. 'bmcs, bmcs' -> {'bmcs'})
        p_tokens = set(re.findall(r"[a-z0-9\u0980-\u09ff]+", norm_pattern))

        def card_matches(c: Dict) -> bool:
            c_title = (c.get("title") or "").strip().lower()
            c_summary = (c.get("rule_summary") or "").strip().lower()

            # Exact or substring match
            if norm_pattern in c_title or norm_pattern in c_summary or norm_title == c_title:
                return True

            # Pattern substring of card title or card pattern extracted from title
            # e.g. title: "Candidate Rule for Pattern: BMCS" -> pat: "bmcs"
            pat_match = re.search(r"pattern:\s*([^'\"]+)", c_title)
            if pat_match:
                extracted_pat = pat_match.group(1).strip().lower()
                if extracted_pat and (extracted_pat in norm_pattern or extracted_pat in p_tokens):
                    return True

            # Token overlap check (if all significant tokens in pattern exist in title/summary)
            sig_tokens = [tok for tok in p_tokens if len(tok) > 1]
            if sig_tokens and all(tok in c_title or tok in c_summary for tok in sig_tokens):
                return True

            # Also check bad_examples in card for identical anomaly string
            bads = [str(b).lower() for b in c.get("bad_examples", []) or []]
            if any(norm_pattern in b for b in bads):
                return True

            return False

        # 1. Check production cards
        for f in glob.glob(os.path.join(CARDS_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                if card_matches(c):
                    return (f, c, "production")
            except Exception:
                continue

        # 2. Check rejected cards (prevent re-synthesizing noise rejected by human reviewers)
        for f in glob.glob(os.path.join(REJECTED_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                if card_matches(c):
                    return (f, c, "rejected")
            except Exception:
                continue

        # 3. Check existing draft cards
        for f in glob.glob(os.path.join(DRAFTS_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                if card_matches(c):
                    return (f, c, "draft")
            except Exception:
                continue

        return None

    def synthesize_draft_from_anomaly(
        self,
        title: str,
        domain: str,
        register: str,
        rule_summary: str,
        bad_examples: List[str],
        good_examples: List[str],
        common_llm_error: str,
        sources: List[str],
        draft_id: Optional[str] = None
    ) -> str:
        # Internal deduplication of examples
        bads = list(dict.fromkeys([b.strip() for b in bad_examples if b and b.strip()]))
        goods = list(dict.fromkeys([g.strip() for g in good_examples if g and g.strip()]))

        cid = draft_id or self.get_next_draft_id()
        review_notes = (
            "Candidate card synthesized by Bhashabid Autonomous Learning Loop. Requires human linguistic review and authentic positive Bengali exemplars (good_examples)."
            if not goods else
            "Candidate card synthesized by Bhashabid Autonomous Learning Loop. Pending human native-speaker sign-off."
        )
        card_data = {
            "id": cid,
            "title": title,
            "domain": domain,
            "profile": "bd_standard",
            "register": register,
            "rule_summary": rule_summary,
            "good_examples": goods,
            "bad_examples": bads,
            "common_llm_error": common_llm_error,
            "sources": sources,
            "confidence": "candidate",
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "last_modified": datetime.now().strftime("%Y-%m-%d"),
            "review": {
                "reviewer_name": None,
                "reviewer_affiliation": None,
                "reviewed_date": None,
                "status": "PENDING_HUMAN_REVIEW",
                "notes": review_notes,
                "signature_hash": None
            }
        }

        out_path = os.path.join(self.drafts_dir, f"{cid}.yaml")
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.dump(card_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

        return out_path

    def cluster_and_synthesize_anomalies(self, anomalies: List[Dict]) -> List[str]:
        """
        Clusters a list of harvested anomalies and generates draft cards.
        Applies strict Duplicate Guard to prevent redundant card creation.
        """
        created = []
        clusters: Dict[str, List[Dict]] = {}
        for a in anomalies:
            rule_id = a.get("rule_id", "ANOMALY-GENERAL")
            matched = (a.get("matched") or a.get("raw_text") or "general").strip()
            # Group by rule_id and leading lexical token signature so distinct calques stay separated
            tokens = matched.split()
            lex_sig = " ".join(tokens[:3]) if tokens else matched
            sig = f"{rule_id}::{lex_sig}"
            if sig not in clusters:
                clusters[sig] = []
            clusters[sig].append(a)

        for sig, items in clusters.items():
            if len(items) >= 1:
                first = items[0]
                rule_id = first.get("rule_id", "ANOMALY-GENERAL")
                raw_text = first.get("raw_text", "")
                matched = first.get("matched", raw_text or "Unknown")
                # Deduplicate repeated comma-separated tokens (e.g. "BMCS, BMCS" -> "BMCS")
                if matched:
                    deduped_tokens = list(dict.fromkeys([t.strip() for t in re.split(r"[,;]+", matched) if t.strip()]))
                    if deduped_tokens:
                        matched = ", ".join(deduped_tokens)
                domain = first.get("domain", "translation")
                
                # Filter out HTML entity remnants, Roman numerals, hardware brands, parenthetical terms, and empty noise
                if is_scraping_noise(matched, raw_context=raw_text):
                    continue

                title = f"Candidate Rule for Pattern: {matched[:40]}"
                
                # DUPLICATE GUARD CHECK
                existing = self.find_existing_card_by_pattern(matched, title)
                if existing:
                    filepath, card_data, category = existing
                    if category in ["production", "rejected"]:
                        # Already covered by production or rejected by human review; skip completely
                        continue
                    else:
                        # Merge new unique examples into existing draft card
                        updated = False
                        cur_bads = card_data.get("bad_examples", []) or []
                        cur_goods = card_data.get("good_examples", []) or []
                        cur_sources = card_data.get("sources", []) or []

                        # If card was generic translation and a specific domain is detected, upgrade domain
                        if card_data.get("domain") in ["translation", "general"] and domain not in ["translation", "general"]:
                            card_data["domain"] = domain
                            updated = True

                        for it in items:
                            raw = (it.get("raw_text") or "").strip()
                            sug = (it.get("suggestion") or "").strip()
                            if raw and raw not in cur_bads and len(cur_bads) < 5:
                                cur_bads.append(raw)
                                updated = True
                            exemplars = extract_exemplars_from_suggestion(sug)
                            for ex in exemplars:
                                if ex and ex not in cur_goods and len(cur_goods) < 5:
                                    cur_goods.append(ex)
                                    updated = True

                        # Enrich with authoritative domain standards if missing
                        domain_standards = get_domain_standards(card_data.get("domain", domain))
                        for std in domain_standards:
                            if std not in cur_sources:
                                cur_sources.append(std)
                                updated = True

                        if updated:
                            card_data["bad_examples"] = cur_bads
                            card_data["good_examples"] = cur_goods
                            card_data["sources"] = cur_sources
                            card_data["last_modified"] = datetime.now().strftime("%Y-%m-%d")
                            with open(filepath, "w", encoding="utf-8") as yf:
                                yaml.dump(card_data, yf, allow_unicode=True, sort_keys=False)
                        created.append(filepath)
                        continue

                cid = self.get_next_draft_id()
                reg = "formal"
                
                # Synthesize appropriate, domain-aware linguistic summary & error type
                if "CALQUE" in rule_id:
                    rule_sum = f"English calque or passive construction '{matched}' requires naturalization into standard Bengali phrasing."
                    llm_err = f"LLMs emit literal English passive calques or unidiomatic syntax for '{matched}'."
                elif "RAW-ENGLISH" in rule_id:
                    rule_sum = f"Foreign terminology or unquoted Latin-script word '{matched}' requires standard Bengali terminology or phonetic transliteration with English in parentheses."
                    llm_err = f"LLMs emit unadapted English terminology '{matched}' in Bengali contexts."
                elif "GURU-CHANDALI" in rule_id:
                    rule_sum = f"Sadhu-Cholito discordance in '{matched}' must be harmonized to standard modern Cholito."
                    llm_err = f"LLMs mix Sadhu and Cholito registers in '{matched}'."
                elif "HONORIFIC" in rule_id:
                    rule_sum = f"Pronominal and verbal honorific concordance mismatch for '{matched}' requires harmonization."
                    llm_err = f"LLMs produce honorific discordance between subject pronoun and verb for '{matched}'."
                else:
                    rule_sum = f"Linguistic pattern '{matched}' requires evaluation against standard Bengali register."
                    llm_err = f"LLMs emit non-standard usage for '{matched}'."

                bads = [it.get("raw_text", matched) for it in items[:3]]
                
                # Extract genuine Bengali exemplars, strictly filtering out imperative meta-instructions
                goods = []
                for it in items:
                    sug = (it.get("suggestion") or "").strip()
                    exemplars = extract_exemplars_from_suggestion(sug)
                    for ex in exemplars:
                        if ex not in goods and len(goods) < 5:
                            goods.append(ex)

                domain_standards = get_domain_standards(domain)
                verified_sources = [
                    f"Corpus Harvest Provenance: {first.get('source', 'Authoritative Bengali Corpus')}",
                    "Principle P2 Human Provenance Audit Gate"
                ] + domain_standards

                p = self.synthesize_draft_from_anomaly(
                    title=title,
                    domain=domain,
                    register=reg,
                    rule_summary=rule_sum,
                    bad_examples=bads,
                    good_examples=goods,
                    common_llm_error=llm_err,
                    sources=verified_sources,
                    draft_id=cid
                )
                created.append(p)

        return created
