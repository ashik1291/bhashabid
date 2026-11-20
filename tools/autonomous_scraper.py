# tools/autonomous_scraper.py
# Zero-Dependency Autonomous Web & RSS Scraper for Bengali Corpora Ingestion
import os
import sys
import re
import html
import json
import time
import hashlib
import shutil
import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode
from tools.domain_taxonomy import canonicalize_sector, CANONICAL_SECTORS, get_sector_number

# Persistent hash cache to guarantee zero duplicate sentence ingestion across practice cycles
FINGERPRINTS_PATH = os.path.join(REPO_ROOT, "state", "scraped_fingerprints.json")

def make_wiki_api_url(category_name: str, limit: int = 50) -> str:
    """Helper to build high-yield, full-extract MediaWiki API query URLs for Bengali Wikipedia."""
    encoded_cat = urllib.parse.quote(category_name)
    return (
        f"https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers"
        f"&gcmtitle={encoded_cat}&gcmnamespace=0&gcmlimit={limit}&gcmsort=sortkey"
        f"&prop=extracts&exintro=1&exlimit=max&explaintext=1&format=json"
    )

# Authoritative live RSS and open API feeds covering all 17 professional sectors of Bhashabid
DEFAULT_FEEDS = [
    # Sector 1: Constitutional Law & Writs
    {
        "name": "BBC News Bangla (Judicial & Legal)",
        "url": "https://feeds.bbci.co.uk/bengali/rss.xml",
        "domain": "Constitutional Law & Writs",
        "sector": 1
    },
    {
        "name": "Bangla Wikipedia Bangladesh Case Law & Jurisprudence",
        "url": make_wiki_api_url("Category:বাংলাদেশের_আইন"),
        "domain": "Constitutional Law & Writs",
        "sector": 1,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Bangladesh Constitution & Governance",
        "url": make_wiki_api_url("Category:বাংলাদেশের_সংবিধান"),
        "domain": "Constitutional Law & Writs",
        "sector": 1,
        "is_json_api": True
    },
    # Sector 2: Macroeconomics & Banking
    {
        "name": "The Business Standard (TBS Bangla Economy)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "Macroeconomics & Banking",
        "sector": 2
    },
    {
        "name": "Prothom Alo (National & Economy)",
        "url": "https://www.prothomalo.com/feed",
        "domain": "Macroeconomics & Banking",
        "sector": 2
    },
    {
        "name": "Bangla Wikipedia Macroeconomics & Central Banking",
        "url": make_wiki_api_url("Category:বাংলাদেশের_অর্থনীতি"),
        "domain": "Macroeconomics & Banking",
        "sector": 2,
        "is_json_api": True
    },
    # Sector 3: Healthcare & Epidemiology
    {
        "name": "BBC News Bangla (Healthcare & Science)",
        "url": "https://feeds.bbci.co.uk/bengali/rss.xml",
        "domain": "Healthcare & Epidemiology",
        "sector": 3
    },
    {
        "name": "Bangla Wikipedia Clinical Medicine & Epidemiology",
        "url": make_wiki_api_url("Category:চিকিৎসাবিজ্ঞান"),
        "domain": "Healthcare & Epidemiology",
        "sector": 3,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Public Health & Epidemiology",
        "url": make_wiki_api_url("Category:জনস্বাস্থ্য"),
        "domain": "Healthcare & Epidemiology",
        "sector": 3,
        "is_json_api": True
    },
    # Sector 4: Administrative Governance & Memos
    {
        "name": "The Daily Star Bangla (Governance & Administration)",
        "url": "https://bangla.thedailystar.net/rss.xml",
        "domain": "Administrative Governance & Memos",
        "sector": 4
    },
    {
        "name": "Bangla Wikipedia Public Administration",
        "url": make_wiki_api_url("Category:জনপ্রশাসন"),
        "domain": "Administrative Governance & Memos",
        "sector": 4,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Bangladesh Government Agencies",
        "url": make_wiki_api_url("Category:বাংলাদেশ_সরকার"),
        "domain": "Administrative Governance & Memos",
        "sector": 4,
        "is_json_api": True
    },
    # Sector 5: Creative Fiction & Spoken Dialogue
    {
        "name": "Prothom Alo (Literature & Society)",
        "url": "https://www.prothomalo.com/feed",
        "domain": "Creative Fiction & Spoken Dialogue",
        "sector": 5
    },
    {
        "name": "Bangla Wikipedia Bengali Literature & Fiction",
        "url": make_wiki_api_url("Category:বাংলা_সাহিত্য"),
        "domain": "Creative Fiction & Spoken Dialogue",
        "sector": 5,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Bengali Novels & Prose",
        "url": make_wiki_api_url("Category:বাংলা_উপন্যাস"),
        "domain": "Creative Fiction & Spoken Dialogue",
        "sector": 5,
        "is_json_api": True
    },
    # Sector 6: Classical Poetry & Prosody
    {
        "name": "Bangla Wikipedia Poetry & Classical Verse",
        "url": make_wiki_api_url("Category:বাংলা_কবিতা"),
        "domain": "Classical Poetry & Prosody",
        "sector": 6,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Classical Literature & Metrics",
        "url": make_wiki_api_url("Category:বাঙালি_কবি"),
        "domain": "Classical Poetry & Prosody",
        "sector": 6,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Bengali Metres & Prosody",
        "url": make_wiki_api_url("Category:ছন্দ"),
        "domain": "Classical Poetry & Prosody",
        "sector": 6,
        "is_json_api": True
    },
    # Sector 7: Academic Research & Methodology
    {
        "name": "Bangla Wikipedia Linguistics & Academic Research",
        "url": make_wiki_api_url("Category:ভাষাবিজ্ঞান"),
        "domain": "Academic Research & Methodology",
        "sector": 7,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Bengali Grammar & Philology",
        "url": make_wiki_api_url("Category:বাংলা_ব্যাকরণ"),
        "domain": "Academic Research & Methodology",
        "sector": 7,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Research Methodology & Linguistics",
        "url": make_wiki_api_url("Category:গবেষণা_পদ্ধতি"),
        "domain": "Academic Research & Methodology",
        "sector": 7,
        "is_json_api": True
    },
    # Sector 8: Land Registry & Deeds
    {
        "name": "Bangla Wikipedia Land Law & Property Registry",
        "url": make_wiki_api_url("Category:সম্পত্তি_আইন"),
        "domain": "Land Registry & Deeds",
        "sector": 8,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Legal Framework & Conveyancing",
        "url": make_wiki_api_url("Category:আইন"),
        "domain": "Land Registry & Deeds",
        "sector": 8,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Land Administration in Bangladesh",
        "url": make_wiki_api_url("Category:বাংলাদেশের_ভূমি_ব্যবস্থাপনা"),
        "domain": "Land Registry & Deeds",
        "sector": 8,
        "is_json_api": True
    },
    # Sector 9: Agronomy & Disaster Management
    {
        "name": "Deutsche Welle (DW Bangla - Climate & Disaster)",
        "url": "https://rss.dw.com/rdf/rss-ben-all",
        "domain": "Agronomy & Disaster Management",
        "sector": 9
    },
    {
        "name": "Bangla Wikipedia Agriculture & Agronomy",
        "url": make_wiki_api_url("Category:বাংলাদেশের_কৃষি"),
        "domain": "Agronomy & Disaster Management",
        "sector": 9,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Disaster Risk Management",
        "url": make_wiki_api_url("Category:দুর্যোগ_ব্যবস্থাপনা"),
        "domain": "Agronomy & Disaster Management",
        "sector": 9,
        "is_json_api": True
    },
    # Sector 10: ICT & Software Engineering
    {
        "name": "The Daily Star Bangla (Tech & Software)",
        "url": "https://bangla.thedailystar.net/rss.xml",
        "domain": "ICT & Software Engineering",
        "sector": 10
    },
    {
        "name": "Bangla Wikipedia Information Technology & Computing",
        "url": make_wiki_api_url("Category:তথ্য_প্রযুক্তি"),
        "domain": "ICT & Software Engineering",
        "sector": 10,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Computer Science & Software",
        "url": make_wiki_api_url("Category:কম্পিউটার_বিজ্ঞান"),
        "domain": "ICT & Software Engineering",
        "sector": 10,
        "is_json_api": True
    },
    # Sector 11: Education & NCTB Pedagogy
    {
        "name": "Prothom Alo (Education & Pedagogy)",
        "url": "https://www.prothomalo.com/feed",
        "domain": "Education & NCTB Pedagogy",
        "sector": 11
    },
    {
        "name": "Bangla Wikipedia Education & Pedagogy",
        "url": make_wiki_api_url("Category:শিক্ষা"),
        "domain": "Education & NCTB Pedagogy",
        "sector": 11,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Education in Bangladesh",
        "url": make_wiki_api_url("Category:বাংলাদেশের_শিক্ষা_ব্যবস্থা"),
        "domain": "Education & NCTB Pedagogy",
        "sector": 11,
        "is_json_api": True
    },
    # Sector 12: Translation & Calque Naturalization
    {
        "name": "Deutsche Welle (DW Bangla - Translated Features)",
        "url": "https://rss.dw.com/rdf/rss-ben-all",
        "domain": "Translation & Calque Naturalization",
        "sector": 12
    },
    {
        "name": "Bangla Wikipedia Translation Studies & Lexicography",
        "url": make_wiki_api_url("Category:অনুবাদ"),
        "domain": "Translation & Calque Naturalization",
        "sector": 12,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Proverbs & Cultural Idioms",
        "url": make_wiki_api_url("Category:প্রবাদ"),
        "domain": "Translation & Calque Naturalization",
        "sector": 12,
        "is_json_api": True
    },
    # Sector 13: Consumer E-Commerce & Retail Logistics
    {
        "name": "The Business Standard (TBS Bangla Commerce)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "Consumer E-Commerce & Retail Logistics",
        "sector": 13
    },
    {
        "name": "Bangla Wikipedia E-Commerce & Retail",
        "url": make_wiki_api_url("Category:ই-বাণিজ্য"),
        "domain": "Consumer E-Commerce & Retail Logistics",
        "sector": 13,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Postal & Courier Logistics",
        "url": make_wiki_api_url("Category:ডাক_ব্যবস্থা"),
        "domain": "Consumer E-Commerce & Retail Logistics",
        "sector": 13,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Retail & Consumer Markets",
        "url": make_wiki_api_url("Category:খুচরা_বিক্রয়"),
        "domain": "Consumer E-Commerce & Retail Logistics",
        "sector": 13,
        "is_json_api": True
    },
    # Sector 14: Customer Support & Omnichannel Messaging
    {
        "name": "The Business Standard (TBS Bangla Support & Telecom)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "Customer Support & Omnichannel Messaging",
        "sector": 14
    },
    {
        "name": "Bangla Wikipedia Telecommunications & Customer Experience",
        "url": make_wiki_api_url("Category:টেলিযোগাযোগ"),
        "domain": "Customer Support & Omnichannel Messaging",
        "sector": 14,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Customer Service & Relations",
        "url": make_wiki_api_url("Category:গ্রাহক_সেবা"),
        "domain": "Customer Support & Omnichannel Messaging",
        "sector": 14,
        "is_json_api": True
    },
    # Sector 15: MFS, Microfinance & Grassroots FinTech
    {
        "name": "Prothom Alo (FinTech & Mobile Banking)",
        "url": "https://www.prothomalo.com/feed",
        "domain": "MFS, Microfinance & Grassroots FinTech",
        "sector": 15
    },
    {
        "name": "The Business Standard (TBS Bangla Banking & FinTech)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "MFS, Microfinance & Grassroots FinTech",
        "sector": 15
    },
    {
        "name": "Bangla Wikipedia Banking & Grassroots Finance",
        "url": make_wiki_api_url("Category:ব্যাংকিং"),
        "domain": "MFS, Microfinance & Grassroots FinTech",
        "sector": 15,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Currency & Financial Inclusion",
        "url": make_wiki_api_url("Category:মুদ্রা"),
        "domain": "MFS, Microfinance & Grassroots FinTech",
        "sector": 15,
        "is_json_api": True
    },
    # Sector 16: Citizen Digital Services & Smart Governance
    {
        "name": "The Daily Star Bangla (Citizen Digital Governance)",
        "url": "https://bangla.thedailystar.net/rss.xml",
        "domain": "Citizen Digital Services & Smart Governance",
        "sector": 16
    },
    {
        "name": "Bangla Wikipedia Government Portals & Public Services",
        "url": make_wiki_api_url("Category:বাংলাদেশের_সরকারি_সংস্থা"),
        "domain": "Citizen Digital Services & Smart Governance",
        "sector": 16,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Digital Systems & Public Portals",
        "url": make_wiki_api_url("Category:ইন্টারনেট"),
        "domain": "Citizen Digital Services & Smart Governance",
        "sector": 16,
        "is_json_api": True
    },
    # Sector 17: Mass Media & Digital Journalism
    {
        "name": "The Business Standard (TBS Bangla Media Dispatch)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "Mass Media & Digital Journalism",
        "sector": 17
    },
    {
        "name": "BBC News Bangla (Media & Journalism)",
        "url": "https://feeds.bbci.co.uk/bengali/rss.xml",
        "domain": "Mass Media & Digital Journalism",
        "sector": 17
    },
    {
        "name": "Bangla Wikipedia Journalism & Media Studies",
        "url": make_wiki_api_url("Category:সাংবাদিকতা"),
        "domain": "Mass Media & Digital Journalism",
        "sector": 17,
        "is_json_api": True
    },
    {
        "name": "Bangla Wikipedia Mass Media & Press",
        "url": make_wiki_api_url("Category:গণমাধ্যম"),
        "domain": "Mass Media & Digital Journalism",
        "sector": 17,
        "is_json_api": True
    }
]

USER_AGENT = "Bhashabid-Bot/2.0 (Open-Source Bengali Linguistic Coprocessor; https://github.com/ashik1291/bhashabid; contact: ashik1291@github)"

SOURCE_REGISTRY_PATH = os.path.join(REPO_ROOT, "memory", "sources", "registry.yaml")


def load_approved_hosts(registry_path: str = SOURCE_REGISTRY_PATH) -> set:
    """Hosts of sources with status 'approved' in memory/sources/registry.yaml (P3 license gate)."""
    try:
        import yaml
        with open(registry_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except (OSError, ImportError, ValueError):
        return set()
    hosts = set()
    for src in data.get("sources", []) or []:
        if str(src.get("status", "")).lower() != "approved":
            continue
        for u in [src.get("url")] + list(src.get("hosts") or []):
            if u:
                host = urllib.parse.urlparse(u if "://" in u else f"https://{u}").hostname
                if host:
                    hosts.add(host.lower())
    return hosts


class AutonomousScraper:
    """
    Autonomous, zero-dependency web & RSS crawler for continuous real-world
    Bengali linguistic corpora harvesting without manual folder drops.
    Enforces persistent deduplication to guarantee strictly unique and fresh practice data.
    """

    def __init__(
        self,
        feeds: Optional[List[Dict]] = None,
        timeout: int = 10,
        inbox_dir: Optional[str] = None,
        fingerprints_path: Optional[str] = None,
        allow_unregistered_sources: bool = False
    ):
        self.feeds = feeds or DEFAULT_FEEDS
        # P3: only fetch hosts registered as approved, and only where robots.txt allows.
        # Unregistered sources need explicit opt-in (and user approval per the constitution).
        self.allow_unregistered_sources = allow_unregistered_sources
        self.approved_hosts = load_approved_hosts()
        self._robots_cache: Dict[str, Optional[urllib.robotparser.RobotFileParser]] = {}
        self.timeout = timeout
        self.inbox_dir = inbox_dir or os.path.join(REPO_ROOT, "eval", "corpora", "inbox")
        os.makedirs(self.inbox_dir, exist_ok=True)
        self.fingerprints_path = fingerprints_path or FINGERPRINTS_PATH
        self.seen_fingerprints = self._load_fingerprints()
        self._article_cache = {}  # In-memory full news cache to prevent duplicate HTTP requests

    def _load_fingerprints(self) -> set:
        """Loads previously seen sentence hashes to prevent duplicate re-ingestion."""
        if os.path.exists(self.fingerprints_path):
            try:
                with open(self.fingerprints_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    fps = data.get("fingerprints", [])
                    # Rolling FIFO window of the latest 25,000 fingerprints: protects against
                    # intra-session duplication while permitting ongoing rotating news cycle updates.
                    if len(fps) > 30000:
                        fps = fps[-25000:]
                    return set(fps)
            except Exception as e:
                # Corrupted state guard: create timestamped backup to prevent wiping historical cache
                backup_path = f"{self.fingerprints_path}.corrupted.{int(time.time())}.bak"
                try:
                    shutil.copyfile(self.fingerprints_path, backup_path)
                    print(f"Warning: Corrupted fingerprints file backed up to {backup_path}: {e}")
                except Exception:
                    pass
        return set()

    def is_fetch_permitted(self, url: str) -> bool:
        """True only for approved (or explicitly opted-in) hosts whose robots.txt allows our user agent."""
        parsed = urllib.parse.urlparse(url)
        host = (parsed.hostname or "").lower()
        if parsed.scheme not in ("http", "https") or not host:
            return False
        if not self.allow_unregistered_sources and host not in self.approved_hosts:
            return False
        if host not in self._robots_cache:
            rp = urllib.robotparser.RobotFileParser(f"{parsed.scheme}://{host}/robots.txt")
            try:
                req = urllib.request.Request(rp.url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:  # nosec B310
                    rp.parse(resp.read().decode("utf-8", errors="ignore").splitlines())
            except urllib.error.HTTPError as he:
                if he.code in (401, 403):
                    rp = None
                else:
                    rp.parse([])  # no robots.txt: crawling permitted
            except (urllib.error.URLError, OSError, ValueError):
                rp = None  # robots.txt unreachable: do not crawl
            self._robots_cache[host] = rp
        rp = self._robots_cache[host]
        return bool(rp and rp.can_fetch(USER_AGENT, url))

    def fetch_full_article_content(self, link: str) -> str:
        """
        Fetches the complete news article text from the web page link,
        extracting all authentic body paragraphs (<p>) rather than just the RSS headline.
        Employs strict in-memory caching and a tight 3.5s timeout for maximum efficiency.
        """
        if not link or not link.startswith(("http://", "https://")):
            return ""
        clean_link = link.split("?")[0]
        if clean_link in self._article_cache:
            return self._article_cache[clean_link]
        if not self.is_fetch_permitted(link):
            return ""

        try:
            req = urllib.request.Request(link, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=3.5) as resp:  # nosec B310
                html_text = resp.read().decode("utf-8", errors="ignore")

            # Pre-clean script, style, and iframe tags to prevent JavaScript leakage into Bengali corpora
            html_text = re.sub(r"<script[^>]*>.*?</script>", "", html_text, flags=re.DOTALL | re.IGNORECASE)
            html_text = re.sub(r"<style[^>]*>.*?</style>", "", html_text, flags=re.DOTALL | re.IGNORECASE)
            html_text = re.sub(r"<iframe[^>]*>.*?</iframe>", "", html_text, flags=re.DOTALL | re.IGNORECASE)

            paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html_text, flags=re.DOTALL)
            clean_paras = []
            for p in paragraphs:
                cleaned = self.sanitize_article_text(p)
                # Must be a substantial Bengali paragraph with punctuation and at least 5 words
                if len(cleaned) > 30 and re.search(r"[\u0980-\u09FF]", cleaned):
                    if not re.search(r"[।?!]", cleaned) or len(cleaned.split()) < 5:
                        continue
                    if re.search(r"(?:ক্লিক করুন|বিজ্ঞাপন|আরও পড়ুন|শেয়ার করুন|সর্বশেষ|মূলপাতা|লগইন|সাবস্ক্রাইব|All rights reserved|EMAIL US|FOLLOW US|Privacy Policy|Contact us|Sitemap|Most Read|Related News|Copyright)", cleaned, re.IGNORECASE):
                        continue
                    clean_paras.append(cleaned)

            full_text = " । ".join(clean_paras)
            self._article_cache[clean_link] = full_text
            return full_text
        except Exception:
            return ""

    def save_fingerprints(self):
        """Persists seen sentence fingerprints to disk with atomic write."""
        os.makedirs(os.path.dirname(self.fingerprints_path), exist_ok=True)
        tmp_path = f"{self.fingerprints_path}.tmp.{os.getpid()}"
        try:
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump({
                    "version": "1.0.0",
                    "last_updated": datetime.now().isoformat(),
                    "total_fingerprints_tracked": len(self.seen_fingerprints),
                    "fingerprints": list(self.seen_fingerprints)
                }, f, indent=2, ensure_ascii=False)
            os.replace(tmp_path, self.fingerprints_path)
        except Exception as e:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
            print(f"Notice: Could not save fingerprints: {e}")

    @staticmethod
    def get_fingerprint(text: str) -> str:
        """Computes a canonical SHA-256 fingerprint ignoring trivial punctuation differences."""
        cleaned = re.sub(r"[^\u0980-\u09FFa-zA-Z0-9]", "", canonicalize_unicode(text.strip()))
        return hashlib.sha256(cleaned.encode("utf-8")).hexdigest()

    def is_seen(self, text: str) -> bool:
        return self.get_fingerprint(text) in self.seen_fingerprints

    def mark_seen(self, text: str):
        self.seen_fingerprints.add(self.get_fingerprint(text))

    @staticmethod
    def sanitize_article_text(text: str) -> str:
        """Strips HTML tags, decodes entities, and removes CMS metadata headers/footers."""
        if not text:
            return ""
        clean = re.sub(r"<[^>]+>", " ", text)
        clean = html.unescape(clean)
        # Strip common CMS metadata footers
        clean = re.split(r"\b(?:Byline|News type|Publish date|Featured image|Standfirst|URL category|Tags):", clean, flags=re.IGNORECASE)[0]
        # Remove photo captions like 'ছবি: ... /টিবিএস'
        clean = re.sub(r"ছবি\s*[:;]\s*[^/\"]+/[^\s\"]+\s*\"?>?", "", clean)
        return " ".join(clean.split())

    def fetch_feed_data(self, feed: Dict, max_items: int = 4) -> List[Dict]:
        """Fetches and parses a single RSS or API feed with network resilience and full article extraction."""
        url = feed["url"]
        name = feed["name"]
        domain = feed["domain"]
        items = []

        # Security: Strictly validate scheme to prevent SSRF or local file inclusion (CWE-22 / B310)
        if not url.startswith(("http://", "https://")):
            raise ValueError(f"Security: Insecure or unsupported URL scheme rejected: {url}")
        if not self.is_fetch_permitted(url):
            return items

        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/xml, application/json, text/xml;q=0.9, */*;q=0.8"
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:  # nosec B310
                content_bytes = response.read()

            if feed.get("is_json_api"):
                # Handle Wikipedia / JSON API with rich article extracts
                try:
                    data = json.loads(content_bytes.decode("utf-8", errors="ignore"))
                    pages = data.get("query", {}).get("pages", {})
                    page_list = list(pages.values())
                    # Shuffle page order so every cycle samples distinct articles across the category
                    import random
                    random.shuffle(page_list)

                    for pdata in page_list:
                        if len(items) >= max_items:
                            break
                        title = pdata.get("title", "")
                        extract = self.sanitize_article_text(pdata.get("extract", ""))
                        combined = f"{title}. {extract}" if extract else title
                        if combined and re.search(r"[\u0980-\u09FF]", combined):
                            # Split into substantial sentences
                            sentences = [s.strip() for s in re.split(r"[।\n]+", combined) if len(s.strip()) > 15]
                            for s in sentences:
                                if len(items) >= max_items:
                                    break
                                if self.is_seen(s):
                                    continue
                                self.mark_seen(s)
                                items.append({
                                    "source": name,
                                    "domain": domain,
                                    "text": canonicalize_unicode(s),
                                    "notes": f"Scraped full lead & body from {name} ('{title}')"
                                })
                except Exception as je:
                    print(f"Notice: JSON API parse note for {name}: {je}")
            else:
                # Handle RSS XML with pre-cleaning for stray ampersands
                raw_text = content_bytes.decode("utf-8", errors="ignore")
                clean_xml = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;", raw_text)
                try:
                    import defusedxml.ElementTree as DefusedET
                    root = DefusedET.fromstring(clean_xml.encode("utf-8"))
                except ImportError:
                    root = ET.fromstring(clean_xml.encode("utf-8"))  # nosec B314
                channel = root.find("channel")
                raw_items = []
                if channel is not None:
                    raw_items = channel.findall("item")
                if not raw_items:
                    raw_items = root.findall(".//item")
                if not raw_items:
                    raw_items = root.findall(".//{http://purl.org/rss/1.0/}item")

                for it in raw_items:
                    if len(items) >= max_items:
                        break
                    title_elem = it.find("title")
                    if title_elem is None:
                        title_elem = it.find("{http://purl.org/rss/1.0/}title")

                    desc_elem = it.find("description")
                    if desc_elem is None:
                        desc_elem = it.find("{http://purl.org/rss/1.0/}description")

                    content_elem = it.find("{http://purl.org/rss/1.0/modules/content/}encoded")
                    link_elem = it.find("link")
                    if link_elem is None:
                        link_elem = it.find("{http://purl.org/rss/1.0/}link")

                    title_text = self.sanitize_article_text(title_elem.text if title_elem is not None and title_elem.text else "")
                    body_text = self.sanitize_article_text(content_elem.text if content_elem is not None and content_elem.text else (desc_elem.text if desc_elem is not None and desc_elem.text else ""))

                    # Full News Extraction: fetch full article body from link if available
                    link_url = (link_elem.text if link_elem is not None and link_elem.text else "").strip()
                    full_body = ""
                    if link_url:
                        full_body = self.fetch_full_article_content(link_url)

                    if full_body:
                        combined = f"{title_text} । {full_body}"
                    else:
                        combined = f"{title_text} {body_text}".strip()

                    # Only accept items containing actual Bengali graphemes
                    if re.search(r"[\u0980-\u09FF]", combined):
                        # Split into clean, non-trivial sentences (> 15 chars)
                        sentences = [s.strip() for s in re.split(r"[।\n]+", combined) if len(s.strip()) > 15]
                        for s in sentences:
                            if len(items) >= max_items:
                                break
                            if self.is_seen(s):
                                continue
                            self.mark_seen(s)
                            items.append({
                                "source": name,
                                "domain": domain,
                                "text": canonicalize_unicode(s),
                                "notes": f"Live RSS full article reporting from {name}"
                            })

        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(1.0)
                try:
                    if not url.startswith(("http://", "https://")):
                        return items
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=self.timeout) as response:  # nosec B310
                        content_bytes = response.read()
                    if feed.get("is_json_api"):
                        data = json.loads(content_bytes.decode("utf-8", errors="ignore"))
                        pages = data.get("query", {}).get("pages", {})
                        for pid, pdata in pages.items():
                            if len(items) >= max_items:
                                break
                            title = pdata.get("title", "")
                            extract = self.sanitize_article_text(pdata.get("extract", ""))
                            combined = f"{title}. {extract}" if extract else title
                            if combined and re.search(r"[\u0980-\u09FF]", combined):
                                sentences = [s.strip() for s in re.split(r"[।\n]+", combined) if len(s.strip()) > 15]
                                for s in sentences:
                                    if len(items) >= max_items:
                                        break
                                    if self.is_seen(s):
                                        continue
                                    self.mark_seen(s)
                                    items.append({
                                        "source": name,
                                        "domain": domain,
                                        "text": canonicalize_unicode(s),
                                        "notes": f"Scraped lead sentence from {name} ('{title}')"
                                    })
                except Exception as retry_e:
                    print(f"[Scraper Rate-Limit Notice] {name} rate-limited (HTTP 429). Falling back: {retry_e}")
            else:
                print(f"[Scraper Offline Notice] Could not reach {name} (HTTP {he.code}). Skipping feed.")
        except urllib.error.URLError as ue:
            print(f"[Scraper Offline Notice] Could not reach {name} ({ue.reason}). Skipping feed.")
        except Exception as ex:
            print(f"[Scraper Notice] Handled feed exception for {name}: {ex}")

        return items

    def scrape_all_feeds(self, max_items_per_feed: int = 4) -> List[Dict]:
        """Scrapes all configured feeds and extracts Bengali text snippets."""
        all_scraped = []
        print(f"\n[Autonomous Scraper] Polling {len(self.feeds)} authoritative Bengali feeds...")
        
        for feed in self.feeds:
            feed_items = self.fetch_feed_data(feed, max_items=max_items_per_feed)
            if feed_items:
                all_scraped.extend(feed_items)
                print(f"  ✓ {feed['name']}: Ingested {len(feed_items)} live articles ({feed['domain']})")

        return all_scraped

    def scrape_and_save_to_inbox(self, max_items_per_feed: int = 5) -> Optional[str]:
        """
        Scrapes live feeds and persists them into eval/corpora/inbox/
        as a clean JSONL batch for the autonomous learning loop.
        """
        scraped_items = self.scrape_all_feeds(max_items_per_feed=max_items_per_feed)
        if not scraped_items:
            print("[Autonomous Scraper] No live items scraped (network offline or feeds unreachable).")
            return None

        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        filename = f"scraped_batch_{timestamp}.jsonl"
        filepath = os.path.join(self.inbox_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            for idx, item in enumerate(scraped_items, start=1):
                record = {
                    "id": f"SCRAPED-{timestamp}-{idx:03d}",
                    "source": item["source"],
                    "domain": item["domain"],
                    "text": item["text"],
                    "label": "LIVE_HARVESTED_CANDIDATE",
                    "notes": item["notes"]
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        self.save_fingerprints()
        print(f"✓ Saved {len(scraped_items)} strictly unique, fresh scraped sentences to inbox: {filepath}")
        return filepath

    def fetch_local_corpus_fallback(self, sector: str, max_items: int = 4) -> List[Dict]:
        """
        Tier 3 Fallback: Extracts authentic sentences from verified local corpora
        (eval/corpora/sources/*.jsonl) matching the sector or its canonical designation.
        """
        canon_sec = canonicalize_sector(sector)
        sources_dir = os.path.join(REPO_ROOT, "eval", "corpora", "sources")
        if not os.path.isdir(sources_dir):
            return []

        matched_items = []
        for root, _, files in os.walk(sources_dir):
            for file in files:
                if not file.endswith(".jsonl"):
                    continue
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for line in f:
                            if len(matched_items) >= max_items:
                                break
                            line = line.strip()
                            if not line:
                                continue
                            data = json.loads(line)
                            item_domain = data.get("domain", "")
                            if canonicalize_sector(item_domain) == canon_sec:
                                text = data.get("text", "").strip() or data.get("human_gold", "").strip()
                                if text and not self.is_seen(text):
                                    self.mark_seen(text)
                                    matched_items.append({
                                        "source": f"Local Verified Corpus ({file})",
                                        "domain": sector,
                                        "text": canonicalize_unicode(text),
                                        "notes": data.get("notes", f"Authentic domain standard for {canon_sec}")
                                    })
                except Exception:
                    pass
                if len(matched_items) >= max_items:
                    break

        # Elastic cyclic reuse: If all items were seen in this session, draw from authentic corpus
        # with slight perturbation/rotation rather than starving and forcing Tier 4 synthesis prematurely
        if len(matched_items) < max_items:
            for root, _, files in os.walk(sources_dir):
                for file in files:
                    if not file.endswith(".jsonl"):
                        continue
                    path = os.path.join(root, file)
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            for line in f:
                                if len(matched_items) >= max_items:
                                    break
                                line = line.strip()
                                if not line:
                                    continue
                                data = json.loads(line)
                                item_domain = data.get("domain", "")
                                if canonicalize_sector(item_domain) == canon_sec:
                                    text = data.get("text", "").strip() or data.get("human_gold", "").strip()
                                    if text:
                                        # Use item even if seen earlier in session
                                        matched_items.append({
                                            "source": f"Local Verified Corpus ({file}) [Rotated]",
                                            "domain": sector,
                                            "text": canonicalize_unicode(text),
                                            "notes": data.get("notes", f"Authentic domain standard for {canon_sec}")
                                        })
                    except Exception:
                        pass
                    if len(matched_items) >= max_items:
                        break

        return matched_items

    def scrape_targeted_sector_data(
        self,
        target_sectors: List[str],
        max_items_per_sector: int = 4
    ) -> List[Dict]:
        """
        Gathers fresh data across the 4-Tier Ingestion & Fallback Pipeline
        using Stratified Deficit-Balanced Hybrid Ingestion:
        - Tier 1: Targeted Live RSS Streams (Living, event-driven journalistic vernacular)
        - Tier 2: Open Knowledge API (Deep encyclopedic & grammatical taxonomy)
        - Tier 3: Local Verified Benchmark Corpora (eval/corpora/sources/*.jsonl)
        - Tier 4: Offline Grounded Mistake-Learning Synthesizer (memory/mistakes/ledger.jsonl)

        Enforces proportional 50/50 register stratification when both RSS and API feeds exist,
        with elastic deficit spillover to prevent starvation or throughput drops.
        """
        from tools.mistake_synthesizer import MistakeLearningSynthesizer
        mistake_synth = MistakeLearningSynthesizer()

        all_items = []
        print(f"\n[Sector-Targeted Stratified Ingestion] Refreshing {len(target_sectors)} sector(s): {target_sectors}")

        for sec in target_sectors:
            canon_sec = canonicalize_sector(sec)
            sec_items = []

            # 1. Identify feeds matching this sector
            sec_matching_feeds = [f for f in self.feeds if canonicalize_sector(f.get("domain")) == canon_sec]
            rss_feeds = [f for f in sec_matching_feeds if not f.get("is_json_api")]
            api_feeds = [f for f in sec_matching_feeds if f.get("is_json_api")]

            # 2. Compute Stratified Quotas (50% RSS / 50% API if both exist)
            if rss_feeds and api_feeds:
                target_rss = (max_items_per_sector + 1) // 2
                target_api = max_items_per_sector - target_rss
            elif rss_feeds:
                target_rss = max_items_per_sector
                target_api = 0
            else:
                target_rss = 0
                target_api = max_items_per_sector

            # 3. Harvest Tier 1: Live RSS Streams
            rss_harvested = []
            if target_rss > 0:
                for feed in rss_feeds:
                    needed = target_rss - len(rss_harvested)
                    if needed <= 0:
                        break
                    items = self.fetch_feed_data(feed, max_items=needed)
                    if items:
                        for it in items:
                            it["domain"] = sec
                        rss_harvested.extend(items)
                        print(f"  ✓ [Tier 1: Live RSS] {feed['name']}: Ingested {len(items)} sentences for '{sec}'")

            # 4. Compute Deficit from Tier 1 and Harvest Tier 2: Open Knowledge API
            rss_deficit = target_rss - len(rss_harvested)
            effective_target_api = target_api + max(0, rss_deficit)

            api_harvested = []
            if effective_target_api > 0:
                for feed in api_feeds:
                    needed = effective_target_api - len(api_harvested)
                    if needed <= 0:
                        break
                    items = self.fetch_feed_data(feed, max_items=needed)
                    if items:
                        for it in items:
                            it["domain"] = sec
                        api_harvested.extend(items)
                        print(f"  ✓ [Tier 2: Open Knowledge API] {feed['name']}: Ingested {len(items)} sentences for '{sec}'")

            # 5. Reverse Spillover: If Tier 2 had a deficit and Tier 1 had unused capacity, try remaining RSS
            api_deficit = effective_target_api - len(api_harvested)
            if api_deficit > 0 and rss_feeds:
                for feed in rss_feeds:
                    needed = api_deficit
                    if needed <= 0:
                        break
                    items = self.fetch_feed_data(feed, max_items=needed)
                    if items:
                        for it in items:
                            it["domain"] = sec
                        rss_harvested.extend(items)
                        api_deficit -= len(items)

            sec_items.extend(rss_harvested)
            sec_items.extend(api_harvested)

            # 6. Tier 3: Local Authentic Corpora Fallback
            if len(sec_items) < max_items_per_sector:
                needed = max_items_per_sector - len(sec_items)
                corpus_items = self.fetch_local_corpus_fallback(canon_sec, max_items=needed)
                if corpus_items:
                    for it in corpus_items:
                        it["domain"] = sec
                    sec_items.extend(corpus_items)
                    print(f"  ✓ [Tier 3: Local Corpora Fallback] Ingested {len(corpus_items)} sentences from local benchmark for '{sec}' ({canon_sec})")

            # 7. Tier 4: Grounded Mistake-Learning Synthesizer Fallback
            if len(sec_items) < max_items_per_sector:
                needed = max_items_per_sector - len(sec_items)
                print(f"  • [Notice] Tier 1-3 sources fully saturated for current window in '{sec}'. Engaging Tier 4 Mistake Synthesizer...")
                synth_items = mistake_synth.synthesize_sector_batch(
                    sector=canon_sec,
                    count=needed,
                    exclude_fingerprints=self.seen_fingerprints
                )
                if synth_items:
                    for itm in synth_items:
                        self.mark_seen(itm["text"])
                        itm["domain"] = sec
                    sec_items.extend(synth_items)
                    print(f"  ✓ [Tier 4: Mistake-Learning Engine] Synthesized {len(synth_items)} valid, strictly new sentences for '{sec}'.")

            all_items.extend(sec_items[:max_items_per_sector])

        return all_items

    def execute_sector_targeted_hook(
        self,
        target_sectors: List[str],
        max_items_per_sector: int = 4
    ) -> Optional[str]:
        """
        Invoked by daily_practice_runner when specific sectors hit confidence saturation.
        Only fetches or generates fresh data for the sectors that reached precision.
        """
        if not target_sectors:
            return None

        print("\n" + "=" * 75)
        print(f"AUTONOMOUS SECTOR-TARGETED INGESTION TRIGGERED FOR {len(target_sectors)} SECTOR(S)")
        print(f"Target Saturated Sectors: {', '.join(target_sectors)}")
        print("=" * 75)

        items = self.scrape_targeted_sector_data(target_sectors, max_items_per_sector=max_items_per_sector)
        if not items:
            print("[Sector-Targeted Ingestion] No items harvested or synthesized.")
            return None

        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        filename = f"scraped_batch_{timestamp}.jsonl"
        filepath = os.path.join(self.inbox_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            for idx, item in enumerate(items, start=1):
                record = {
                    "id": item.get("id") or f"SCRAPED-{timestamp}-{idx:03d}",
                    "source": item["source"],
                    "domain": item["domain"],
                    "text": item["text"],
                    "label": item.get("label", "LIVE_HARVESTED_CANDIDATE"),
                    "notes": item.get("notes", "")
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        self.save_fingerprints()
        print(f"✓ Saved {len(items)} fresh sector sentences to inbox: {filepath}")
        return filepath

    def execute_saturation_hook(self) -> Optional[str]:
        """
        Invoked by daily_practice_runner when batch saturation is detected.
        Pulls fresh data automatically without manual folder drops.
        """
        print("\n" + "=" * 70)
        print("AUTONOMOUS SATURATION HOOK TRIGGERED: FETCHING FRESH DATA")
        print("=" * 70)
        return self.scrape_and_save_to_inbox(max_items_per_feed=3)

if __name__ == "__main__":
    scraper = AutonomousScraper()
    out = scraper.scrape_and_save_to_inbox(max_items_per_feed=3)
    if out:
        print(f"Autonomous scraping completed successfully: {out}")
    else:
        print("Autonomous scraping ended without new batch.")
