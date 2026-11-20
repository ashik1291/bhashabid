# tools/sector_sources.py
# Sector-wise Bengali text from licence-approved open sources (P3) for the learning loop.
# Fetches only hosts registered in memory/sources/registry.yaml and only paths robots.txt allows,
# via AutonomousScraper.is_fetch_permitted. Excerpts are stored locally (gitignored) with their URL.
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Dict, List, Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.autonomous_scraper import AutonomousScraper, USER_AGENT

INBOX_DIR = os.path.join(REPO_ROOT, "eval", "corpora", "inbox")
SEEN_PATH = os.path.join(REPO_ROOT, "state", "learning_sources_seen.json")
LICENSES = {
    "wikipedia": "CC BY-SA 4.0 (bn.wikipedia.org)",
    "wikisource": "Public domain texts / CC BY-SA 4.0 (bn.wikisource.org)",
}

# Verified index pages (category or author pages that list articles), per sector.
SECTOR_SOURCES: Dict[str, List[tuple]] = {
    "Macroeconomics & Banking": [("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের অর্থনীতি"), ("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের ব্যাংক"), ("wikipedia", "বিষয়শ্রেণী:ব্যাংকিং")],
    "Healthcare & Epidemiology": [("wikipedia", "বিষয়শ্রেণী:স্বাস্থ্য"), ("wikipedia", "বিষয়শ্রেণী:সংক্রামক রোগ"), ("wikipedia", "বিষয়শ্রেণী:চিকিৎসাবিজ্ঞান")],
    "Agronomy & Disaster Management": [("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের কৃষি"), ("wikipedia", "বিষয়শ্রেণী:কৃষি"),
                                       ("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের প্রাকৃতিক দুর্যোগ"), ("wikipedia", "বিষয়শ্রেণী:ঘূর্ণিঝড়")],
    "Constitutional Law & Writs": [("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের আইন"), ("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের সংবিধান")],
    "Administrative Governance & Memos": [("wikipedia", "বিষয়শ্রেণী:বাংলাদেশ সরকার")],
    "Education & NCTB Pedagogy": [("wikipedia", "বিষয়শ্রেণী:শিক্ষা"), ("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের বিশ্ববিদ্যালয়")],
    "ICT & Software Engineering": [("wikipedia", "বিষয়শ্রেণী:কম্পিউটার বিজ্ঞান"), ("wikipedia", "বিষয়শ্রেণী:প্রোগ্রামিং ভাষা"), ("wikipedia", "বিষয়শ্রেণী:ইন্টারনেট")],
    "Mass Media & Digital Journalism": [("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের গণমাধ্যম"), ("wikipedia", "বিষয়শ্রেণী:বাংলাদেশের সংবাদপত্র")],
    "Creative Fiction & Dialogue": [("wikipedia", "বিষয়শ্রেণী:বাংলা সাহিত্য")],
    "Classical Poetry & Prosody": [("wikipedia", "বিষয়শ্রেণী:বাংলা কবিতা")],
    "Classical Literature (Sadhu)": [("wikisource", "লেখক:বঙ্কিমচন্দ্র চট্টোপাধ্যায়"), ("wikisource", "লেখক:ঈশ্বরচন্দ্র বিদ্যাসাগর"),
                                     ("wikisource", "লেখক:রবীন্দ্রনাথ ঠাকুর")],
}

_LINK = re.compile(r'href="/wiki/([^"#?]+)"')
_PARA = re.compile(r"<p[^>]*>(.*?)</p>", re.S)
_TAG = re.compile(r"<[^>]+>")
_REF = re.compile(r"\[\s*[০-৯0-9a-zA-Z ]{1,6}\s*\]")
_SENT = re.compile(r"(?<=[।?!])\s+")
_SKIP_NS = ("বিষয়শ্রেণী:", "চিত্র:", "ফাইল:", "উইকিপিডিয়া:", "সাহায্য:", "বিশেষ:", "আলোচনা:", "টেমপ্লেট:", "লেখক:",
            "Special:", "File:", "Category:", "Help:", "Template:", "Portal:", "প্রবেশদ্বার:")


def _url(site: str, title: str) -> str:
    return f"https://bn.{site}.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))


def _get(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec B310 - gated by is_fetch_permitted
        return resp.read().decode("utf-8", errors="ignore")


def _article_links(page_html: str, is_category: bool) -> List[str]:
    if is_category:
        m = re.search(r'id="mw-pages"(.*?)</div>\s*</div>', page_html, re.S)
        body = m.group(1) if m else ""
    else:
        body = page_html.split('id="mw-content-text"', 1)[-1]
    out = []
    for raw in _LINK.findall(body):
        title = urllib.parse.unquote(raw).replace("_", " ")
        # Any namespaced page (বিষয়শ্রেণী:, রচনা:, লেখক:, ...) is navigation, not article text.
        if ":" not in title and not title.startswith(_SKIP_NS) and title not in out:
            out.append(title)
    return out


def _sentences(page_html: str, limit: int) -> List[str]:
    body = page_html.split('id="mw-content-text"', 1)[-1]
    out = []
    for p in _PARA.findall(body):
        text = _REF.sub("", html.unescape(_TAG.sub("", p))).strip()
        for s in _SENT.split(text):
            s = s.strip()
            if 20 <= len(s) <= 300 and re.search(r"[ঀ-৿]{3}", s):
                out.append(s)
                if len(out) >= limit:
                    return out
    return out


def _load_seen(path: str) -> set:
    try:
        with open(path, encoding="utf-8") as f:
            return set(json.load(f))
    except (OSError, ValueError):
        return set()


def _save_seen(seen: set, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted(seen), f, ensure_ascii=False)


def fetch_sector_texts(sectors: Optional[List[str]] = None, pages_per_sector: int = 3, sentences_per_page: int = 30,
                       inbox_dir: str = INBOX_DIR, seen_path: str = SEEN_PATH, delay: float = 1.0) -> Dict:
    """Fetches new (not yet seen) articles per sector and writes one JSONL file to the inbox.
    Returns {"file": path or None, "per_sector": {sector: sentences}, "skipped": [reasons]}."""
    gate = AutonomousScraper()
    seen = _load_seen(seen_path)
    records, per_sector, skipped = [], {}, []
    for sector in sectors or list(SECTOR_SOURCES):
        if sector not in SECTOR_SOURCES:
            skipped.append(f"unknown sector: {sector}")
            continue
        taken = 0
        for site, index_title in SECTOR_SOURCES[sector]:
            if taken >= pages_per_sector:
                break
            index_url = _url(site, index_title)
            if not gate.is_fetch_permitted(index_url):
                skipped.append(f"not permitted (registry/robots): {index_url}")
                continue
            try:
                links = _article_links(_get(index_url), index_title.startswith("বিষয়শ্রেণী:"))
            except Exception as e:  # network or HTML problems should not stop the cycle
                skipped.append(f"{index_title}: {type(e).__name__}")
                continue
            for title in links:
                if taken >= pages_per_sector:
                    break
                url = _url(site, title)
                if url in seen or not gate.is_fetch_permitted(url):
                    continue
                time.sleep(delay)
                try:
                    page = _get(url)
                    sents = _sentences(page, sentences_per_page)
                    if len(sents) < 5:
                        # Index of chapters/editions (common on Wikisource): read the first chapter instead.
                        for sub in _article_links(page, is_category=False)[:3]:
                            sub_url = _url(site, sub)
                            if sub_url in seen or not gate.is_fetch_permitted(sub_url):
                                continue
                            time.sleep(delay)
                            sub_sents = _sentences(_get(sub_url), sentences_per_page)
                            if len(sub_sents) >= 5:
                                seen.add(sub_url)
                                url, sents = sub_url, sub_sents
                                break
                except Exception as e:
                    skipped.append(f"{title}: {type(e).__name__}")
                    continue
                seen.add(url)
                if not sents:
                    continue
                taken += 1
                records += [{"text": s, "source": url, "sector": sector, "license": LICENSES[site]} for s in sents]
                per_sector[sector] = per_sector.get(sector, 0) + len(sents)
            time.sleep(delay)
    _save_seen(seen, seen_path)
    path = None
    if records:
        os.makedirs(inbox_dir, exist_ok=True)
        path = os.path.join(inbox_dir, f"sector_sources_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return {"file": path, "per_sector": per_sector, "skipped": skipped}
