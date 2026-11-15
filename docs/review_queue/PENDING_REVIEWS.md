# Expert Linguistic Review Packet (PENDING_REVIEWS.md)

Standard: **Bangla Academy (Dhaka) & Paschimbanga Bangla Akademi (Kolkata)**  
Constitutional Rule: **Principle P2 (Human Native Provenance Required)**

> [!IMPORTANT]
> The only cards awaiting human review are candidate drafts located in `knowledge/cards/drafts/`.
> Production cards in `knowledge/cards/` are already reviewed, tested, and active.

---

## Instructions for Human Reviewers via GitHub PR
1. Inspect the pending draft cards below or directly in `knowledge/cards/drafts/`.
2. Open a Pull Request on GitHub with your review decision, reviewer name, and affiliation.
3. Once approved and merged, draft cards remain preserved in `knowledge/cards/drafts/` as a permanent public record of your contribution!

---

## 📥 Pending Candidate Queue (3 Cards Awaiting Human Review)

### Draft 1: [CRD-DFT-009] Candidate Rule for Technical Acronym: OAuth
- **File**: `knowledge\cards\drafts\CRD-DFT-009.yaml`
- **Domain**: `ICT & Software Engineering` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: When referencing the authentication framework 'OAuth', use the standard Bengali phonetic transliteration 'ওঅথ' along with 'OAuth' in parentheses on first mention, preserving technical clarity without leaving raw English tokens or unresolved documentation paths.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ ওঅথ (OAuth) হলো ইন্টারনেট ব্যবহারকারীদের নিরাপদ প্রমাণীকরণের একটি উন্মুক্ত প্রমিত প্রটোকল।
  - ✓ অ্যাপ্লিকেশনটিতে নিরাপদ প্রবেশাধিকার নিশ্চিত করতে ওঅথ ২.০ (OAuth 2.0) ফ্রেমওয়ার্ক ব্যবহার করা হয়েছে।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ মিডিয়াউইকির ওঅথ সমর্থনের জন্য দেখুন mw:Help:OAuth ওঅথ হল প্রবেশ প্রতিনিধিদের জন্য...
  - ✗ OAuth ব্যবহার করে ইউজারের ডাটা ফেচ করা হচ্ছে।

**Common LLM Error**: LLMs emit raw unadapted English technical tokens or unformatted documentation paths instead of standard Bengali technical transliteration with parenthetical English.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Computer Science & Software, Principle P2 Human Provenance Audit Gate, Bangladesh Computer Council (BCC) Bengali Computing & Unicode Standards, Open-Source Bengali Localization Best Practices

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-009 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 2: [CRD-DFT-014] Candidate Rule for Administrative Term: Continuation Form
- **File**: `knowledge\cards\drafts\CRD-DFT-014.yaml`
- **Domain**: `Education & NCTB Pedagogy` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: When referring to administrative verification forms such as 'continuation form' in academic contexts, use standard Bengali terminology such as 'অধ্যয়ন ধারাবাহিকতা ফরম' or 'ধারাবাহিকতা প্রত্যয়ন ফরম', optionally retaining the English term in parentheses.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ শিক্ষার্থী থাকার প্রমাণ হিসেবে প্রতি তিন মাস অন্তর প্রতিষ্ঠানপ্রধানের প্রত্যয়নসহ 'অধ্যয়ন ধারাবাহিকতা ফরম' (continuation form) জমা দিতে হবে।
  - ✓ বৃত্তিপ্রাপ্ত শিক্ষার্থীদের নিয়মিত উপস্থিতির প্রমাণ হিসেবে প্রতি ত্রৈমাসিকে ধারাবাহিকতা প্রত্যয়ন ফরম দাখিল করা বাধ্যতামূলক।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ শিক্ষার্থী থাকার প্রমাণ হিসেবে ৩ মাস পর পর বিভাগীয় এবং শিক্ষানুস্থানের প্রধানের স্বাক্ষর থাকা 'continution form' জমা দিতে হয়
  - ✗ স্টুডেন্ট কন্টিনিউয়েশন ফর্ম ফিলাপ করে অফিসে সাবমিট করতে হবে।

**Common LLM Error**: LLMs emit raw English jargon or unstandardized transliterations instead of formal administrative Bengali terms.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Education & Pedagogy, Principle P2 Human Provenance Audit Gate, National Curriculum and Textbook Board (NCTB) Standard Bengali, Ministry of Education Pedagogical Guidelines

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-014 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 3: [CRD-DFT-016] Candidate Rule for Syntactic Typology Acronym: SVO / SOV
- **File**: `knowledge\cards\drafts\CRD-DFT-016.yaml`
- **Domain**: `Academic Research & Methodology` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: In linguistic and academic syntactic analysis, translate sentence-order typology acronyms such as SVO and SOV using standard Bengali grammatical categories ('কর্তা-ক্রিয়া-কর্ম' for SVO and 'কর্তা-কর্ম-ক্রিয়া' for SOV), retaining the Latin acronym in parentheses for scholarly reference.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বাংলা ভাষার স্বাভাবিক পদক্রম হলো কর্তা-কর্ম-ক্রিয়া (SOV), পক্ষান্তরে ইংরেজি প্রধানত কর্তা-ক্রিয়া-কর্ম (SVO) পদক্রমের ভাষা।
  - ✓ বাক্যতাত্ত্বিক তুলনামূলক গবেষণায় প্রমিত বাংলা পদক্রমের স্বাতন্ত্র্য বিশ্লেষণ করা হয়েছে।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ ইংরেজি একটি উল্লেখযোগ্য SVO ভাষা
  - ✗ যেমন- "অহন(কর্তা) ভালোবাসে(ক্রিয়া) তাকে(কর্ম)" হলো একটি SVO পদক্রম

**Common LLM Error**: LLMs leave linguistic typology abbreviations untranslated without standard Bengali grammatical equivalents.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Bengali Grammar & Philology, Principle P2 Human Provenance Audit Gate, Bangla Academy Linguistic Research Methodology Guidelines, Linguistic Society of Bangladesh Peer-Reviewed Standards

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-016 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

## 🛡️ Active Production Cards (35 Approved in `knowledge/cards/`)

### Card 1: [CRD-DFT-001] Candidate Rule for Pattern: দ্বারা চালিত
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 2: [CRD-DFT-002] Candidate Rule for Pattern: পড়িয়া
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 3: [CRD-DFT-004] Candidate Rule for Pattern: জিজ্ঞেস করে একটি রুল
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 4: [CRD-DFT-005] Candidate Rule for Pattern: বড় বিপদের সংকেত
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 5: [CRD-DFT-006] Candidate Rule for Pattern: ঝোপের চারপাশে পেটাচ্ছেন
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 6: [CRD-DFT-007] Candidate Rule for Pattern: অনুপস্থিতিতে দায়িত্বভার পালন
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 7: [CRD-DFT-008] Candidate Rule for Pattern: alphabet
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Bengali Native Speaker)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 8: [CRD-DOM-001] Official Administrative Applications & Petitions (দাপ্তরিক আবেদন ও দরখাস্তের প্রমিত কাঠামো)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 9: [CRD-DOM-002] Letter Writing & Correspondence Registers (চিঠিপত্র ও সামাজিক যোগাযোগের অনুশাসন)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 10: [CRD-DOM-003] Literary Fiction & Story Writing (কথাসাহিত্য, গল্প ও সংলাপ লিখন শৈলী)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 11: [CRD-DOM-004] Academic & Scholarly Research Prose (শিক্ষায়তনিক ও গবেষণা প্রবন্ধ শৈলী)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 12: [CRD-DOM-005] Book Authoring & Non-Fiction Essays (মননশীল প্রবন্ধ ও গ্রন্থ প্রণয়ন রীতি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 13: [CRD-DOM-006] Corporate & Marketing Copywriting (কর্পোরেট যোগাযোগ ও বাণিজ্যিক কপিরাইটিং)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 14: [CRD-DOM-007] Legal Drafting & Contracts (আইনি দলিল, চুক্তিপত্র ও নোটিশ লিখন)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 15: [CRD-DOM-008] Healthcare & Medical Public Advisories (চিকিৎসাসেবা ও জনস্বাস্থ্য যোগাযোগ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 16: [CRD-DOM-009] Classical Bengali Prosody & Poetic Scansion (বাংলা ছন্দবিজ্ঞান ও পয়ার প্রকরণ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 17: [CRD-DOM-010] Land Records & Property Deeds (ভূমি রেজিস্ট্রি, খতিয়ান ও সাফ-কবলা দলিল)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 18: [CRD-DOM-011] Agronomy, Meteorology & Disaster Bulletins (কৃষি সম্প্রসারণ, আবহাওয়া ও দুর্যোগ পূর্বাভাস)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 19: [CRD-DOM-012] NCTB Creative Pedagogy & Exam Questioning (জাতীয় শিক্ষাক্রম ও সৃজনশীল প্রশ্নপদ্ধতি কাঠামো)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 20: [CRD-DOM-013] Poetic Metaphors, Imagery & Figurative Diction (কাব্যিক রূপক, চিত্রকল্প ও ভাবার্থ প্রকাশ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 21: [CRD-GRM-001] Sadhu-Cholito Verb Consistency (গুরুচণ্ডালী দোষ পরিহার)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 22: [CRD-GRM-002] Honorific Concordance Across Pronouns and Verbs (আপনি / তুমি / তুই)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 23: [CRD-GRM-003] Bengali Case Markers and Postposition Agreement (কারক ও বিভক্তি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 24: [CRD-GRM-004] Bengali Euphonic Junctions (সন্ধি: স্বরসন্ধি ও ব্যঞ্জনসন্ধি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 25: [CRD-GRM-005] Bengali Compound Formation (সমাস: দ্বন্দ্ব, দ্বিগু, তৎপুরুষ ও কর্মধারয়)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 26: [CRD-NUM-001] Irregular Bengali Cardinal Numbers 0-99 (০-৯৯ অনিয়মিত সংখ্যা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 27: [CRD-ORT-001] Unicode NFC Canonicalization and Composite Graphemes (য়, ড়, ঢ়)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 28: [CRD-ORT-002] Bangla Academy Loanword S-Rule (বিদেশি শব্দে 'স' বনাম 'ষ')
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 29: [CRD-ORT-003] Regional Orthographic Variations (বাংলাদেশ প্রমিত বনাম পশ্চিমবঙ্গ বানানরীতি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 30: [CRD-TRN-001] Translation Idioms vs Literal English Calques (ভাবানুবাদ বনাম আক্ষরিক অনুবাদ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 31: [CRD-TRN-002] High Court & Judicial Reporting Formulas (হাইকোর্টের রুল ও রিট মামলার প্রমিত পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 32: [CRD-TRN-003] Macroeconomic & Financial News Syntax (অর্থনৈতিক সংবাদ ও বাংলাদেশ ব্যাংক পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 33: [CRD-TRN-004] Sports Vernacular & Cricket Reporting (ক্রিকেট ও ক্রীড়া সংবাদ পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 34: [CRD-TRN-005] Article 102 Constitutional Writs Taxonomy & Drafting (সংবিধানের ১০২ অনুচ্ছেদের রিট মামলার প্রমিত পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 35: [CRD-TRN-006] Proverbs, Idioms & Metaphoric Equivalence (প্রবাদ-প্রবচন, বাগধারা ও রূপকার্থ সমীকরণ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)
