# bhashabid/creative/lapidary.py
# Pre-compiled Lapidary, Flora, Fauna & Classical Nature Lexicon
from typing import Dict, Tuple, Optional, List

LAPIDARY_MAP: Dict[str, Tuple[str, ...]] = {
    # Precious minerals & gemstones
    "amethyst": ("রক্তনীলমণি", "নীলমণি"),
    "amber": ("পিঙ্গল-আভ", "মধুরঙা", "তৃণমণি"),
    "lapis lazuli": ("বৈদূর্যমণি", "নীলা"),
    "lapis": ("বৈদূর্যমণি", "নীলা"),
    "turquoise": ("ফিরোজা", "পেরোজ"),
    "jade": ("সূর্যকান্ত", "মার্জান"),
    "emerald": ("মরকত", "পান্না"),
    "ruby": ("চুনি", "পদ্মরাগ"),
    "sapphire": ("ইন্দ্রনীল", "নীলকান্তমণি"),
    "diamond": ("হীরক", "হীরা"),
    "opal": ("দুধিয়া পাথর", "চন্দ্রকান্তমণি"),
    "garnet": ("তামড়ামণি", "গোমেদ"),
    "mother-of-pearl": ("শুক্তিমুক্তা", "ঝিনুকের দীপ্তি"),
    "coral": ("প্রবাল", "বিদ্রুম"),
    "pearl": ("মুক্তা", "মোতি"),
    
    # Marine & Zoological Anatomy
    "jellyfish bell": ("ছত্র", "ঘণ্টাকার দেহ"),
    "tentacles": ("কর্ষিকা",),
    "slough": ("নির্মোক", "পরিত্যক্ত খোলস"),
    "ecdysis": ("নির্মোক মোচন", "ত্বক পরিবর্তন"),
    "larva": ("কীট", "শূককীট"),
    "pollen": ("পরাগ", "পুষ্পরেণু"),
    "nectar": ("মকরন্দ", "পুষ্পরস"),
    
    # Atmospheric & Poetic Imagery
    "azure": ("নীলিমা", "সুনীল"),
    "mendicants": ("ভিক্ষুদল", "পরিব্রাজক", "তপস্বী"),
    "hunter-pierced": ("ব্যাধবিদ্ধ",),
    "blood-script": ("রুধিরলিপিকা", "রক্তলিপি"),
    "city of sorcery": ("জাদুপুর", "মায়াপুরী"),
    "conch-white": ("শঙ্খশুভ্র",),
    "twilight": ("গোধূলি", "সাঁঝের মায়া"),
    "dawn": ("ঊষা", "অরুণোদয়"),
    "abyss": ("অততল", "গহন অতল"),
}

# Reverse lookup from flawed transliterations to standard literary Bengali
TRANSLITERATION_SURRENDERS: Dict[str, Tuple[str, str]] = {
    "অ্যামেথিস্ট": ("রক্তনীলমণি / নীলমণি", "খনিজ রত্নের অপ্রয়োজনীয় ইংরেজি লিপ্যন্তর"),
    "অ্যাম্বার": ("পিঙ্গল-আভ / মধুরঙা", "গাঢ় সোনালি-বাদামি বর্ণে প্রমিত সাহিত্যিক প্রতিশব্দ বাঞ্ছনীয়"),
    "অ্যাম্বার-রঙা": ("পিঙ্গল-আভ / মধুরঙা", "প্রমিত সাহিত্যিক প্রতিশব্দ 'পিঙ্গল-আভ' বা 'মধুরঙা'"),
    "টারকোয়েজ": ("ফিরোজা / পেরোজ", "ঐতিহ্যবাহী বাংলা রত্ননাম 'ফিরোজা'"),
    "লাপিস লাজুলি": ("বৈদূর্যমণি", "ধ্রুপদী বাংলা সাহিত্যিক রূপ 'বৈদূর্যমণি'"),
    "জেড": ("সূর্যকান্ত / মার্জান", "প্রমিত রত্ননাম 'সূর্যকান্ত'"),
    "মাদার অব পার্ল": ("শুক্তিমুক্তা / ঝিনুকের দীপ্তি", "প্রমিত সাহিত্যিক রূপ 'শুক্তিমুক্তা'"),
}

def lookup_lapidary(term: str) -> Optional[Tuple[str, ...]]:
    """
    Returns authentic Bengali literary equivalents for mineral, gem, or anatomical terms.
    """
    cleaned = term.strip().lower()
    return LAPIDARY_MAP.get(cleaned)

def check_transliteration_surrenders(text: str) -> List[Dict[str, str]]:
    """
    Scans text for transliterated foreign minerals and returns naturalization suggestions.
    """
    issues = []
    for flawed, (sugg, reason) in TRANSLITERATION_SURRENDERS.items():
        if flawed in text:
            issues.append({
                "term": flawed,
                "suggestion": sugg,
                "reason": reason
            })
    return issues
