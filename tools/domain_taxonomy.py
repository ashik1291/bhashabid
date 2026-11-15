# tools/domain_taxonomy.py
# Authoritative 17-Sector Domain Taxonomy & Canonical Normalizer
from typing import Dict, List, Optional

# Canonical 17 Professional Sectors in Bhashabid
CANONICAL_SECTORS: List[str] = [
    "Constitutional Law & Writs",                  # Sector 1
    "Macroeconomics & Banking",                    # Sector 2
    "Healthcare & Epidemiology",                    # Sector 3
    "Administrative Governance & Memos",           # Sector 4
    "Creative Fiction & Spoken Dialogue",          # Sector 5
    "Classical Poetry & Prosody",                  # Sector 6
    "Academic Research & Methodology",             # Sector 7
    "Land Registry & Deeds",                       # Sector 8
    "Agronomy & Disaster Management",              # Sector 9
    "ICT & Software Engineering",                  # Sector 10
    "Education & NCTB Pedagogy",                   # Sector 11
    "Translation & Calque Naturalization",         # Sector 12
    "Consumer E-Commerce & Retail Logistics",      # Sector 13
    "Customer Support & Omnichannel Messaging",    # Sector 14
    "MFS, Microfinance & Grassroots FinTech",      # Sector 15
    "Citizen Digital Services & Smart Governance", # Sector 16
    "Mass Media & Digital Journalism"              # Sector 17
]

# Alias and granular sub-domain map to canonical sectors
SECTOR_ALIAS_MAP: Dict[str, str] = {
    # Sector 1: Constitutional Law & Writs
    "Constitutional Law & Writs": "Constitutional Law & Writs",
    "Judicial & High Court": "Constitutional Law & Writs",
    "Legal & Constitutional Writs": "Constitutional Law & Writs",
    "Constitutional Law & High Court Writs": "Constitutional Law & Writs",
    "Judicial & Legal": "Constitutional Law & Writs",

    # Sector 2: Macroeconomics & Banking
    "Macroeconomics & Banking": "Macroeconomics & Banking",
    "Banking & Macroeconomics": "Macroeconomics & Banking",
    "Macroeconomic & Finance": "Macroeconomics & Banking",
    "Macroeconomic & Business Reporting": "Macroeconomics & Banking",
    "Tax & Customs": "Macroeconomics & Banking",
    "Macroeconomics & Banking Journalism": "Macroeconomics & Banking",
    "Economy & Finance": "Macroeconomics & Banking",

    # Sector 3: Healthcare & Epidemiology
    "Healthcare & Epidemiology": "Healthcare & Epidemiology",
    "Healthcare & Medicine": "Healthcare & Epidemiology",
    "Healthcare, Clinical Advisories & Epidemiology": "Healthcare & Epidemiology",
    "Clinical Medicine & Epidemiology": "Healthcare & Epidemiology",
    "Public Health & Epidemiology": "Healthcare & Epidemiology",

    # Sector 4: Administrative Governance & Memos
    "Administrative Governance & Memos": "Administrative Governance & Memos",
    "Administrative Governance": "Administrative Governance & Memos",
    "Official Administrative": "Administrative Governance & Memos",
    "Administrative Applications & Petitions": "Administrative Governance & Memos",
    "Epistolary Hierarchy & Formal Letter Writing": "Administrative Governance & Memos",
    "Administrative Governance & Secretariat Petitions": "Administrative Governance & Memos",
    "Official Letters": "Administrative Governance & Memos",

    # Sector 5: Creative Fiction & Spoken Dialogue
    "Creative Fiction & Spoken Dialogue": "Creative Fiction & Spoken Dialogue",
    "Creative Fiction & Dialogue": "Creative Fiction & Spoken Dialogue",
    "Literary Fiction & Story Writing": "Creative Fiction & Spoken Dialogue",
    "Creative Fiction & Living Spoken Dialogue": "Creative Fiction & Spoken Dialogue",
    "Bengali Literature & Fiction": "Creative Fiction & Spoken Dialogue",

    # Sector 6: Classical Poetry & Prosody
    "Classical Poetry & Prosody": "Classical Poetry & Prosody",
    "Poetic Prosody": "Classical Poetry & Prosody",
    "Classical Poetic Prosody & Metaphoric Diction": "Classical Poetry & Prosody",
    "Classical Poetry & Prosodic Scansion": "Classical Poetry & Prosody",
    "Poetry & Classical Verse": "Classical Poetry & Prosody",

    # Sector 7: Academic Research & Methodology
    "Academic Research & Methodology": "Academic Research & Methodology",
    "Science & Encyclopedic": "Academic Research & Methodology",
    "Academic Research & Public Healthcare": "Academic Research & Methodology",
    "Linguistics & Academic Research": "Academic Research & Methodology",
    "Bengali Grammar & Philology": "Academic Research & Methodology",

    # Sector 8: Land Registry & Deeds
    "Land Registry & Deeds": "Land Registry & Deeds",
    "Land Conveyancing & Deeds": "Land Registry & Deeds",
    "Land Registry & Deeds Conveyancing": "Land Registry & Deeds",
    "Land Registry, Agronomy & NCTB Pedagogy": "Land Registry & Deeds",
    "Land Law & Property Registry": "Land Registry & Deeds",

    # Sector 9: Agronomy & Disaster Management
    "Agronomy & Disaster Management": "Agronomy & Disaster Management",
    "Agronomy & Crop Protection": "Agronomy & Disaster Management",
    "Disaster Early Warning": "Agronomy & Disaster Management",
    "Agronomy & Disaster Early Warning": "Agronomy & Disaster Management",
    "Climate & Disaster": "Agronomy & Disaster Management",
    "Agriculture & Agronomy": "Agronomy & Disaster Management",

    # Sector 10: ICT & Software Engineering
    "ICT & Software Engineering": "ICT & Software Engineering",
    "Corporate & Tech": "ICT & Software Engineering",
    "ICT, Unicode Standards & Software Engineering": "ICT & Software Engineering",
    "Information Technology & Computing": "ICT & Software Engineering",
    "Computer Science & Software": "ICT & Software Engineering",

    # Sector 11: Education & NCTB Pedagogy
    "Education & NCTB Pedagogy": "Education & NCTB Pedagogy",
    "Education & Pedagogy": "Education & NCTB Pedagogy",
    "Education & NCTB Creative Pedagogy": "Education & NCTB Pedagogy",
    "Education in Bangladesh & Curriculum": "Education & NCTB Pedagogy",

    # Sector 12: Translation & Calque Naturalization
    "Translation & Calque Naturalization": "Translation & Calque Naturalization",
    "Translation, Calque De-Naturalization & Idioms": "Translation & Calque Naturalization",
    "Calque De-Naturalization": "Translation & Calque Naturalization",
    "Translation Studies": "Translation & Calque Naturalization",
    "Proverbs & Idioms": "Translation & Calque Naturalization",

    # Sector 13: Consumer E-Commerce & Retail Logistics
    "Consumer E-Commerce & Retail Logistics": "Consumer E-Commerce & Retail Logistics",
    "Consumer E-Commerce": "Consumer E-Commerce & Retail Logistics",
    "E-Commerce & Retail": "Consumer E-Commerce & Retail Logistics",
    "Postal & Courier Logistics": "Consumer E-Commerce & Retail Logistics",

    # Sector 14: Customer Support & Omnichannel Messaging
    "Customer Support & Omnichannel Messaging": "Customer Support & Omnichannel Messaging",
    "Customer Support & Conversational Chat": "Customer Support & Omnichannel Messaging",
    "Customer Support": "Customer Support & Omnichannel Messaging",
    "Telecommunications & Customer Experience": "Customer Support & Omnichannel Messaging",

    # Sector 15: MFS, Microfinance & Grassroots FinTech
    "MFS, Microfinance & Grassroots FinTech": "MFS, Microfinance & Grassroots FinTech",
    "Microfinance & FinTech": "MFS, Microfinance & Grassroots FinTech",
    "Mobile Banking & FinTech": "MFS, Microfinance & Grassroots FinTech",
    "Microcredit & Financial Inclusion": "MFS, Microfinance & Grassroots FinTech",

    # Sector 16: Citizen Digital Services & Smart Governance
    "Citizen Digital Services & Smart Governance": "Citizen Digital Services & Smart Governance",
    "Smart Governance": "Citizen Digital Services & Smart Governance",
    "Digital Bangladesh & Citizen Services": "Citizen Digital Services & Smart Governance",
    "Government Portals & Public Services": "Citizen Digital Services & Smart Governance",

    # Sector 17: Mass Media & Digital Journalism
    "Mass Media & Digital Journalism": "Mass Media & Digital Journalism",
    "Sports Vernacular": "Mass Media & Digital Journalism",
    "Journalism & Media Studies": "Mass Media & Digital Journalism",
    "Mass Media": "Mass Media & Digital Journalism"
}


def canonicalize_sector(name: Optional[str]) -> str:
    """
    Normalizes any domain, alias, historical label, or sector name
    into its canonical 17-sector designation.
    """
    if not name:
        return "General"
    cleaned = name.strip()
    if cleaned in SECTOR_ALIAS_MAP:
        return SECTOR_ALIAS_MAP[cleaned]

    # Substring / case-insensitive fuzzy fallback
    lowered = cleaned.lower()
    for alias, canonical in SECTOR_ALIAS_MAP.items():
        if alias.lower() == lowered:
            return canonical

    for canonical in CANONICAL_SECTORS:
        if canonical.lower() in lowered or lowered in canonical.lower():
            return canonical

    # Keyword heuristics
    if any(k in lowered for k in ["writ", "court", "law", "legal", "বিচার", "আইন"]):
        return "Constitutional Law & Writs"
    if any(k in lowered for k in ["bank", "macro", "tax", "finance", "অর্থনীতি", "মুদ্রা"]):
        return "Macroeconomics & Banking"
    if any(k in lowered for k in ["health", "medicin", "epidemiol", "চিকিৎসা", "রোগ"]):
        return "Healthcare & Epidemiology"
    if any(k in lowered for k in ["gov", "admin", "memo", "petition", "প্রশাসন", "সচিব"]):
        return "Administrative Governance & Memos"
    if any(k in lowered for k in ["fiction", "story", "novel", "dialogue", "কথ্য", "সাহিত্য"]):
        return "Creative Fiction & Spoken Dialogue"
    if any(k in lowered for k in ["poem", "poet", "prosod", "payar", "ছন্দ", "কবিতা"]):
        return "Classical Poetry & Prosody"
    if any(k in lowered for k in ["research", "academic", "linguistic", "thesis", "বিজ্ঞান"]):
        return "Academic Research & Methodology"
    if any(k in lowered for k in ["land", "deed", "khatian", "দলিল", "খতিয়ান"]):
        return "Land Registry & Deeds"
    if any(k in lowered for k in ["agronomy", "disaster", "cyclone", "crop", "কৃষি", "দুর্যোগ"]):
        return "Agronomy & Disaster Management"
    if any(k in lowered for k in ["tech", "software", "ict", "cloud", "কম্পিউটার"]):
        return "ICT & Software Engineering"
    if any(k in lowered for k in ["edu", "nctb", "pedagogy", "শিক্ষা", "পাঠ্য"]):
        return "Education & NCTB Pedagogy"
    if any(k in lowered for k in ["translat", "calque", "idiom", "প্রবাদ", "অনুবাদ"]):
        return "Translation & Calque Naturalization"
    if any(k in lowered for k in ["ecom", "e-com", "retail", "courier", "ডেলিভারি", "বাণিজ্য"]):
        return "Consumer E-Commerce & Retail Logistics"
    if any(k in lowered for k in ["support", "chat", "ticket", "গ্রাহক", "সেবা"]):
        return "Customer Support & Omnichannel Messaging"
    if any(k in lowered for k in ["mfs", "fintech", "microfinance", "বিকাশ", "নগদ"]):
        return "MFS, Microfinance & Grassroots FinTech"
    if any(k in lowered for k in ["citizen", "smart", "portal", "nid", "নাগরিক"]):
        return "Citizen Digital Services & Smart Governance"
    if any(k in lowered for k in ["media", "journal", "press", "sport", "সংবাদ", "সাংবাদিক"]):
        return "Mass Media & Digital Journalism"

    return cleaned


def get_sector_number(name: str) -> Optional[int]:
    """Returns 1-based sector number (1..17) for a given sector name or alias."""
    c = canonicalize_sector(name)
    try:
        return CANONICAL_SECTORS.index(c) + 1
    except ValueError:
        return None
