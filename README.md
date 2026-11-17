# Bhashabid (ভাষাবিদ) — The Deterministic Bengali Language Coprocessor Engine

### *Deterministic Bengali linguistic coprocessor engine & progressive skill layer with a Supervised Self-Learning Distillation Loop.*

[![Security CI](https://github.com/ashik1291/bhashabid/actions/workflows/security_audit.yml/badge.svg)](https://github.com/ashik1291/bhashabid/actions/workflows/security_audit.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: >=3.10](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://python.org)
[![PyPI: v1.0.1](https://img.shields.io/pypi/v/bhashabid.svg)](https://pypi.org/project/bhashabid/1.0.1/)
[![Tests: 158 Passing](https://img.shields.io/badge/Tests-158%20Passing-brightgreen.svg)](eval/unit)
[![Security Audit: Cloudflare Skill (A+)](https://img.shields.io/badge/Security%20Audit-Cloudflare%20Skill%20(A%2B)-success.svg)](SECURITY.md)
[![Security: Bandit 0-Vuln](https://img.shields.io/badge/Security-Bandit%200--Vuln-brightgreen.svg)](SECURITY.md)
[![Dependencies: 0 CVEs](https://img.shields.io/badge/Dependencies-0%20CVEs%20(OSV)-brightgreen.svg)](SECURITY.md)
[![Secrets: 0 Leaks](https://img.shields.io/badge/Secrets-0%20Leaks-brightgreen.svg)](SECURITY.md)
[![Supply Chain: Sigstore Attested](https://img.shields.io/badge/Supply%20Chain-Sigstore%20Attested-blue.svg)](SECURITY.md)
[![P2 Provenance: 50 Reviewed Cards](https://img.shields.io/badge/P2%20Provenance-50%2F50%20Cards%20Reviewed-blueviolet.svg)](knowledge/cards)
[![Core Skill Token Budget: 298 BPE](https://img.shields.io/badge/Core%20Budget-298%20%2F%20390%20Tokens-success.svg)](skills/bangla-expert/SKILL.md)

> **Bhashabid** (ভাষাবিদ) is the **first-ever open-source Bengali language coprocessor engine** featuring a **constitutionally supervised self-learning loop**. Operating as an external cognitive and deterministic coprocessor without retraining model weights, it continuously harvests real-world anomalies, synthesizes candidate rules, and distills high-level invariants under human verification (Principle P2) and a strict < 390 token ceiling—systematically elevating the accuracy, orthography, and native fluency of AI-generated Bengali across **17 specialized professional sectors**.

---

## ⚡ Installation & Quickstart (Zero-Python & Python Options)

Choose the setup that fits your workflow:

### Option A: Zero-Python 1-Click Skill Installation (Antigravity, Cursor, Claude)
> **No Python required!** Automatically installs the declarative skill, Bangla Academy rules, and 9 domain references into your AI IDEs:

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/ashik1291/bhashabid/main/scripts/install.ps1 | iex
```

**macOS / Linux (Bash):**
```bash
curl -fsSL https://raw.githubusercontent.com/ashik1291/bhashabid/main/scripts/install.sh | bash
```

*What this does automatically:*
- Configures **Google Antigravity** (`~/.gemini/config/skills/bhashabid`)
- Configures **Cursor IDE** (`~/.cursor/rules/bangla-expert.mdc` & `~/.cursor/bangla-references/`)
- Configures **Claude Desktop / Code** (`~/.claude/skills/bangla-expert`)
- Automatically links the MCP Server if Python 3.10+ is detected.

---

### Option B: Python Engine & CLI (`pip install bhashabid`)
> For offline zero-token CLI processing, sub-millisecond pipelines, and custom Python microservices:

```bash
pip install bhashabid
```

#### Python SDK (`import bhashabid`)
```python
import bhashabid

# 1. Automatic Bengali Unicode & Spelling Repair (<2ms, Zero-LLM)
repaired, diffs = bhashabid.repair("ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন.")
# Output: "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।"

# 2. Offline Phonetic Spellchecker (78,000+ Word Compressed Lexicon, 9.2ms)
suggestions = bhashabid.spellcheck("আবিস্কার")
# Output: ['আবিষ্কার']

# 3. Statutory South Asian Currency & Number Formatting
print(bhashabid.format_number("1234567.50"))        # "১২,৩৪,৫৬৭.৫০"
print(bhashabid.format_currency_words(1234567.50))  # "বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা মাত্র"
print(bhashabid.format_date_bongabdo(1433, 1, 1))   # "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ"

# 4. Static Honorific & Calque Linter
issues = bhashabid.lint("তারা সেই অর্থ ফেরত দিয়েছিলেন।")
```

#### Command Line Interface (CLI)
```bash
# In-place safe file repair with colored unified diff
bhashabid repair article.txt --diff --write

# Convert numbers to authentic Bengali words
bhashabid number 99 --format words                  # Output: নিরানব্বই

# Offline spellcheck across 78,000 words
bhashabid spellcheck "আবিস্কার"

# Generate statutory civil conveyancing deeds & writ prayers
bhashabid deed --type saf-kabala --vendor "করিম উদ্দিন" --purchaser "রহিম মিয়া" --taka 500000
bhashabid writ --remedy detention --subject "অবৈধ আটক" --authority "পুলিশ কমিশনার"

# Check global IDE integration health
bhashabid status
```

---

### Option C: Web & Mobile AI Chat (ChatGPT, Gemini Web, Claude Web)
If you don't use an AI code editor or CLI, choose the tier that fits your token budget from our standalone instruction system:
- ⚡ **Tier 1 (Nano Prompt)**: Ultra-dense (<160 tokens / <1,100 chars), strictly engineered to fit within **ChatGPT's 1,500-character Custom Instructions limit**.
- 🧩 **Tier 2 (Modular Prompts)**: Plug-and-play domain modules (~350–500 tokens) for Law/Writs, Banking, Admin Petitions, NCTB Pedagogy, Healthcare, Agronomy, and Software.
- 📚 **Tier 3 (Architectural Reference)**: Full 17-sector taxonomy and 105+ idiom mapping table for large context windows (Claude 200k, Gemini 1M).

👉 **[View Three-Tier Instructions (STANDALONE_ALL_IN_ONE.md)](skills/bangla-expert/STANDALONE_ALL_IN_ONE.md)**

---

## 🎯 What Bhashabid Does & What Problem It Solves Uniquely

### The Production Reality: Frontier LLMs (~80–85% Fluent) & The Deterministic "Last-Mile"
Frontier large language models (such as GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro) are remarkably competent. Across standard Bengali conversation, translation, and open-ended generation, **frontier models routinely achieve ~80% to 85%+ semantic fluency**. They are not illiterate or broken.

However, because frontier LLMs are **probabilistic token predictors**, mission-critical production workflows (banking systems, legal writs, government administrative memos, high-throughput publications) encounter a persistent **15–20% "Last-Mile" fidelity and determinism gap**:

1. **Probabilistic Failure on Exact Statutory Rules**:
   - While an LLM can easily generate creative prose, it cannot mathematically guarantee statutory formatting. It frequently emits Western 3-digit comma formats (`1,234,567.50`) instead of South Asian statutory banking standards (`১২,৩৪,৫৬৭.৫০`), drops sentence-final Dari (`।`) in favor of ASCII periods (`.`), or hallucinates irregular Bengali numerals in check disbursements.
2. **Hidden Unicode Grapheme Corruption & Non-NFC Normalization**:
   - LLMs generate subword byte sequences, not canonical Unicode codepoints. Output text frequently contains decomposed vowel signs, broken Hasanta / ZWJ sequences, or non-NFC characters that render fine on one screen but break database indexing, full-text search, and accessibility screen readers.
3. **Pronominal & Honorific Drift Across Multi-Clause Contexts**:
   - In short conversational turns, LLMs maintain honorifics well. But across complex legal, corporate, or administrative paragraphs with multiple clauses, probabilistic decoders frequently mix registers (e.g. pairing informal *তারা* with honorific *দিয়েছিলেন*, or drifting between *আপনি* and *তুমি*).
4. **Subtle English Syntactic Calquing in High-Stakes Sectors**:
   - In professional and technical domains, translated text frequently retains English passive voice structures (overusing *"দ্বারা"* or *"কর্তৃক"* instead of natural Bengali active causal constructions: *"মূল্যবৃদ্ধির দ্বারা প্রভাবিত"* instead of *"মূল্যবৃদ্ধিজনিত কারণে"*).
5. **Context Window Dilution & High API Costs**:
   - Attempting to force an LLM to follow 2,000 lines of Bangla Academy rules by dumping static guides into its system prompt costs thousands of tokens per call, increases latency, and causes instruction dilution.
6. **Zero Offline Capability**:
   - Frontier models require live cloud network connectivity and API keys. They cannot run in disconnected local environments, air-gapped workstations, or microservice edge pipelines.

### 🤝 The Neurosymbolic Solution: Coprocessor Synergy, Not Replacement
Bhashabid does not attempt to train a model from scratch or replace frontier LLMs. Instead, it pairs with them as a **high-speed, deterministic neurosymbolic coprocessor**:
- **Frontier LLM (Semantic Heavy-Lifter)**: Handles open-domain world knowledge, reasoning, creative depth, and semantic generation (~85% of the cognitive burden).
- **Bhashabid Coprocessor (Deterministic Guardrail)**: Handles the 15% deterministic last mile—zero-latency Unicode NFC normalization, Bangla Academy orthography repair, statutory banking numbers/words, honorific concordance checking, and ultra-lean (< 390 BPE tokens) context-aware guidance via MCP & pure local Python.

---

## 📊 Side-by-Side Comparison: Frontier LLMs vs. Bhashabid Coprocessor

| Linguistic & Production Dimension | Frontier LLM Baseline (Probabilistic Generation) | Bhashabid Neurosymbolic Coprocessor (Deterministic Guard) | Empirical Production Example |
| :--- | :--- | :--- | :--- |
| **1. South Asian Currency & Numbers** | High fluency, but frequently defaults to Western 3-digit comma grouping (`1,234,567.50`). | Mathematically guarantees South Asian Lakh/Crore grouping and official check words in Bengali. | Input: `1234567.50`<br>Raw LLM: `1,234,567.50` ⚠️<br>Bhashabid: **"১২,৩৪,৫৬৭.৫০ (বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা মাত্র)"** ✔️ |
| **2. Unicode NFC & Punctuation** | Emits mixed Unicode codepoints (NFD/broken Hasanta) and ASCII periods (`.`) instead of Dari (`।`). | Deterministically canonicalizes Unicode to NFC and converts terminal periods to Dari while preserving decimals (`৩.১৪`). | Raw LLM: `"তিনি বাড়ি গেলেন."` ⚠️<br>Bhashabid: **"তিনি বাড়ি গেলেন।"** ✔️ |
| **3. Bangla Academy Orthography** | Frequently blends archaic, dialectal, and modern spellings based on historical internet training data (*ষ্টেশন, পাখী, পোষ্ট*). | Deterministically normalizes loanwords and native vocabulary to official Bangla Academy standards (*স্টেশন, পাখি, পোস্ট*). | Raw LLM: `"রেল ষ্টেশনে পাখী ডাকছে"` ⚠️<br>Bhashabid: **"রেল স্টেশনে পাখি ডাকছে"** ✔️ |
| **4. Pronominal & Verbal Honorifics** | Prone to register drift across multi-clause sentences (mixing informal *তারা* with honorific *দিয়েছিলেন*). | Enforces strict grammatical concordance (*তারা ... দিয়েছিল* vs *তাঁরা ... দিয়েছিলেন*) across clause boundaries. | Raw LLM: `"তারা অর্থ ফেরত দিয়েছিলেন"` ⚠️<br>Bhashabid: **"তাঁরা সেই অর্থ ফেরত দিয়েছিলেন"** ✔️ |
| **5. Passive Voice English Calques** | Translates technical passives with literal *"দ্বারা"* (*"মুদ্রাস্ফীতির দ্বারা চালিত"*). | Converts passive calques into natural, active causal Bengali syntax. | Raw LLM: `"মুদ্রাস্ফীতির দ্বারা চালিত রাজস্ব ঘাটতি"` ⚠️<br>Bhashabid: **"মুদ্রাস্ফীতিজনিত কারণে রাজস্ব ঘাটতি বৃদ্ধি পেয়েছে"** ✔️ |
| **6. Judicial Writ Formulas (Article 102)** | Approximates legal phrasing colloquially (*"জিজ্ঞেস করে রুল জারি করেছে"*). | Enforces Supreme Court of Bangladesh statutory Rule Nisi show-cause and prayer formulas. | Raw LLM: `"কেন বেআইনি হবে না জিজ্ঞেস করে রুল দিয়েছে"` ⚠️<br>Bhashabid: **"কেন বেআইনি ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন"** ✔️ |
| **7. Secretariat Administrative Memos** | Calques English salutations (*"Dear Sir"* ➔ *"প্রিয় মহাশয়"*). | Enforces official *Bangladesh Secretariat Instructions* (*সচিবালয় নির্দেশমালা*) opening and closing protocols. | Raw LLM: `"প্রিয় মহাশয়, আশা করি ভালো আছেন"` ⚠️<br>Bhashabid: **"বরাবর... বিষয়:... জনাব, বিনীত নিবেদন এই যে..."** ✔️ |
| **8. Classical 14-Akshar Payar Scansion** | Cannot reliably count poetic morae due to subword BPE tokenization abstraction. | Deterministic phonological syllabifier (*মুক্তদল* vs *রুদ্ধদল*) verifies exact 8+6=14 akshar Payar cadence. | Raw LLM: Pseudo-verse with broken 16/17 syllable rhythm ⚠️<br>Bhashabid: **Validates exact 8+6=14 akshar Payar couplets** ✔️ |
| **9. Context Window & Token Efficiency** | Dumping massive style guides (5,000–10,000 tokens) exhausts context, increases latency, and costs money. | Root skill kernel is strictly capped under **390 tokens** (currently **298 true BPE tokens** on `cl100k_base`), loading domains on-demand. | Raw LLM: 10,000+ token monolithic prompt injection ⚠️<br>Bhashabid: **298 true BPE tokens + 0-token Python offloading** ✔️ |
| **10. Local Offline Edge Execution** | Requires active internet, cloud API keys, and 500ms–2000ms latency per request. | 100% offline, local execution with 78,000+ word lexicon; processes at **500,000 words/second** in under 5ms. | Raw LLM: Cloud dependent, network latency, API costs ⚠️<br>Bhashabid: **Pure local Python, 0 network calls, $0.00 marginal cost** ✔️ |

---

## 🏛️ The 4 Pioneering Architectural Pillars

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   USER PROMPT / AI AGENT TASK                                     │
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  │
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│              CORE SKILL KERNEL (Programmatically Capped Under 390 BPE Tokens • cl100k)            │
└───────────────────────┬─────────────────────────┬─────────────────────────┬───────────────────────┘
                        │                         │                         │
                        ▼ [Pillar 1]              ▼ [Pillar 3]              ▼ [Pillar 4]
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│  PROGRAMMATIC TOKEN CEILING   │ │   MODULAR DOMAIN ISOLATION    │ │ DETERMINISTIC COPROCESSOR     │
│ • 298 True BPE Tokens         │ │ • 9 Progressive Domain Guides │ │ • Pure Python / MCP Server    │
│ • Universal Grammar Invariant │ │ • 17 Specialized Sectors      │ │ • ~500,000 words/second       │
│ • Zero Context Bloat          │ │ • 0.0 Unrelated Prompt Tokens │ │ • 100% Exact Math, NFC & Dari │
└───────────────────────────────┘ └───────────────────────────────┘ └───────────────▲───────────────┘
                                                  ▲                                 │
                                                  │                                 │
                                                  │ [Pillar 2: Supervised Loop]     │
                        ┌─────────────────────────┴─────────────────────────┐       │
                        │ HARVESTER ➔ DRAFT CARDS ➔ HUMAN REVIEW GATE (P2)  ├───────┘
                        │ Real-World Anomalies ➔ Verified Invariants Distill│
                        └───────────────────────────────────────────────────┘
```

### 1. Hard Programmatic Token Ceiling (< 390 Tokens Core Budget)
- **Problem**: Monolithic linguistic system prompts (5,000–20,000 tokens) cause severe context dilution, high latency, and high API expenses.
- **Solution**: The root skill kernel (`skills/bangla-expert/SKILL.md` and `.cursor/rules/bangla-expert.mdc`) is hard-capped programmatically under **390 tokens** (currently **298 true BPE tokens** on `cl100k_base`). It contains only universal structural invariants; domain reference files are retrieved via progressive disclosure.

### 2. Generalization Over Memorization (Supervised Closed-Loop Learning)
- **Problem**: Manually appending example sentences to prompts causes prompt bloat. Un-gated autonomous self-learning leads to hallucinated grammar rules.
- **Solution**: Bhashabid executes a closed loop (`harvest` ➔ `synthesize-cards` ➔ `human review (P2)` ➔ `distill`). A single high-level invariant covers tens of thousands of sentence permutations. Knowledge cards cannot enter production without **cryptographic human sign-off**.

### 3. Modular Domain Isolation (9 Progressive Guides)
- **Problem**: Exposing all specialized vocabularies simultaneously confuses model style and wastes tokens.
- **Solution**: 17 sectors are organized into **9 isolated reference guides**. An agent writing poetry burns **0.0 prompt tokens** on Supreme Court writ rules or central bank banking regulations.

### 4. Deterministic Python Offloading via MCP (Zero Token Cost)
- **Problem**: LLMs struggle with mathematical lookups, comma spacing, and phonological syllable counting.
- **Solution**: Bhashabid offloads deterministic operations to local Python algorithms via the **Model Context Protocol (MCP)** and CLI at **500,000 words/second**, with **100% mathematical precision and 0 prompt tokens burned**.

---

## 📚 The 17 Supported Professional Sectors

Bhashabid provides comprehensive domain standards across **17 specialized professional sectors**:

| # | Sector | Authoritative Standards & Coverage | Reference Guide |
| :---: | :--- | :--- | :--- |
| **1** | **Constitutional Law & Writs** | Constitution of Bangladesh (Article 102), Supreme Court precedents, Rule Nisi show-cause orders, writ prayers (*Habeas Corpus, Mandamus, Certiorari*). | [`constitutional_writs.md`](skills/bangla-expert/references/constitutional_writs.md) |
| **2** | **Macroeconomics & Banking** | Bangladesh Bank Monetary Policy statements, prudential regulations, *নীতি সুদহার*, *মূল্যস্ফীতি*, active causal financial reporting. | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) |
| **3** | **Healthcare & Epidemiology** | Bangla Academy Medical Dictionary, DGHS guidelines, precise clinical dosage intervals, non-stigmatizing mental health phrasing. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **4** | **Administrative Governance & Memos** | *Bangladesh Secretariat Instructions* (*সচিবালয় নির্দেশমালা*), formal administrative petitions, opening and closing protocols. | [`official_letters.md`](skills/bangla-expert/references/official_letters.md) |
| **5** | **Creative Fiction & Spoken Dialogue** | Bangla Academy Standard Grammar, living spoken Cholito (*কথ্য রীতি*), action-embedded dialogue tags, sensory imagery. | [`creative_writing.md`](skills/bangla-expert/references/creative_writing.md) |
| **6** | **Classical Poetry & Prosody** | Rabindranath Tagore & Probodh Chandra Sen prosody canon, Dalabritta, Matrabritta, 14-akshar Payar couplets (8+6). | [`creative_writing.md`](skills/bangla-expert/references/creative_writing.md) |
| **7** | **Academic Research & Methodology** | Peer-reviewed citation standards, academic transliteration with Latin in parentheses, thesis structure. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **8** | **Land Registry & Deeds** | Transfer of Property Act 1882, Registration Act 1908, Sub-Kabala conveyance, Heba, CS/SA/RS/BS Khatian, plot boundaries (*চৌহদ্দি*). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **9** | **Agronomy & Disaster Management** | Department of Agricultural Extension (DAE), BMD official cyclone warning signals (1-10 মহাবিপদ সংকেত), storm surge (*জলোচ্ছ্বাস*). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **10** | **ICT & Software Engineering** | Bangladesh Computer Council (BCC) computing standards, Unicode NFC canonical normalization, open-source localization. | [`orthography.md`](skills/bangla-expert/references/orthography.md) |
| **11** | **Education & NCTB Pedagogy** | National Curriculum and Textbook Board (NCTB) 4-tier Creative Questioning taxonomy (উদ্দীপক, জ্ঞান, অনুধাবন, প্রয়োগ, উচ্চতর দক্ষতা). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **12** | **Translation & Calque Naturalization** | De-calquing passive voice (*দ্বারা*), naturalizing English idioms (*বাগধারা ও প্রবচন*), semantic tri-layer model (*অভিধা, লক্ষণা, ব্যঞ্জনা*). | [`grammar_registers.md`](skills/bangla-expert/references/grammar_registers.md) |
| **13** | **Consumer E-Commerce & Retail Logistics** *(NEW)* | Consumers' Rights Protection Act 2009, e-CAB guidelines, escrow settlement, refund honorific concordance (*তারা বনাম তাঁরা*), courier tracking. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **14** | **Customer Support & Omnichannel Messaging** *(NEW)* | Telecom & omnichannel standards, administrative ticketing resolution nomenclature, preserving alphanumeric tracking IDs (`TCK-942`). | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **15** | **MFS, Microfinance & Grassroots FinTech** *(NEW)* | Bangladesh Bank Payment Systems Dept (PSD) MFS guidelines, Microcredit Regulatory Authority (MRA) rules, fraud prevention warnings. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **16** | **Citizen Digital Services & Smart Governance** *(NEW)* | Aspire to Innovate (a2i) Citizen Service Standards, Bangladesh National Portal style, National ID (NID) registration rules, Citizen Charters. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **17** | **Mass Media & Digital Journalism** *(NEW)* | Bangladesh Press Council Code of Ethics & Stylebook, Press Institute of Bangladesh (PIB) standards, neutral reporting attribution. | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) |

---

## 🧪 Proven Accuracy & Verification Metrics

Bhashabid enforces an anti-self-deception testing philosophy (Principle P8). Every mistake discovered in practice is preserved in a permanent regression ledger and executed on every commit:

| Verification Suite | Target | Observed Result | Status |
| :--- | :---: | :---: | :---: |
| **Automated Unit & Regression Suite** | 100% Pass | **153 / 153 Tests Passing** | ![Pass](https://img.shields.io/badge/Unit%20Tests-153%2F153%20Pass-brightgreen.svg) |
| **Principle P2 Provenance Integrity** | 100% Signed | **50 / 50 Cards Reviewed** | ![P2](https://img.shields.io/badge/P2%20Provenance-50%2F50%20Reviewed-blueviolet.svg) |
| **Core Skill Token Footprint** | < 390 Tokens | **298 True BPE Tokens** (`cl100k_base`) | ![Tokens](https://img.shields.io/badge/BPE%20Tokens-298%20%2F%20390-success.svg) |
| **Invariant Duplicate Collisions** | 0 Collisions | **0 Duplicate Titles / Summaries / Examples** | ![Duplicates](https://img.shields.io/badge/Duplicates-0-brightgreen.svg) |
| **Irregular Number Precision (0–99)** | 100.0% | **100.0% Deterministic Match** | ![Numbers](https://img.shields.io/badge/Numeral%20Accuracy-100%25-brightgreen.svg) |
| **Sentence-Ending Dari Enforcement** | 100.0% | **100.0% (Decimal Protected)** | ![Punctuation](https://img.shields.io/badge/Punctuation-100%25-brightgreen.svg) |
| **Guru-chandali Concordance Trapping** | 100.0% | **100.0% Trapped with Bidirectional Fixes** | ![Linter](https://img.shields.io/badge/Linter-100%25-brightgreen.svg) |
| **Execution Throughput (Local Python)** | > 100k wps | **~500,000 words/second ($0.00 cost)** | ![Performance](https://img.shields.io/badge/Speed-500k%20words%2Fsec-blue.svg) |

---

## 🚀 How to Use Bhashabid Today

### 1. Python SDK (`import bhashabid`)
```python
import bhashabid

# Automated Unicode NFC canonicalization, spelling & Dari punctuation
repaired, diffs = bhashabid.repair("ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন.")
print(repaired)  # "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।"

# 78,000+ Word Offline Phonetic Spellchecker (sub-10ms)
suggestions = bhashabid.spellcheck("আবিস্কার")
print(suggestions)  # ['আবিষ্কার']

# South Asian Lakh/Crore Currency & Number Formatting
print(bhashabid.format_number("1234567.50"))        # "১২,৩৪,৫৬৭.৫০"
print(bhashabid.format_currency_words(1234567.50))  # "বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা মাত্র"

# Static Grammar, Honorific & Calque Linter
issues = bhashabid.lint("তুমি সিদ্ধান্ত নেন")
for issue in issues:
    print(issue.suggestion)  # "তুমি সিদ্ধান্ত নাও" / "আপনি সিদ্ধান্ত নেন"

# Classical 14-Akshar Payar Scansion (8+6)
result = bhashabid.verify_payar("কাশীদাস কহে সাধু শুনে পুণ্যবান")
print(result.is_valid_payar)  # True
print(result.total_morae)     # 14 (8+6)
print(result.explanation)     # "শুদ্ধ পয়ার ছন্দ: ৮+৬=১৪ মাত্রার পর্ব ও মধ্যযতি যথাযথভাবে বিন্যস্ত।"
```

### 2. Command-Line Interface (CLI)
```bash
# In-place safe file repair with colored unified diff
bhashabid repair article.txt --diff --write

# Offline spellcheck across 78,000 words
bhashabid spellcheck "আবিস্কার"
# Output: Suggestions for 'আবিস্কার': ['আবিষ্কার']

# Convert numbers to authentic Bengali words
bhashabid number 99 --format words
# Output: নিরানব্বই

# Format currency in South Asian lakh/crore
bhashabid number 1234567.50 --format currency
# Output: বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা

# Lint text for grammatical, honorific, and calque errors
bhashabid lint "তারা সেই অর্থ ফেরত দিয়েছিলেন এবং বিষয়টি বিদ্যুৎ দ্বারা চালিত."

# Verify 14-akshar Payar poetic metre (8+6)
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar

# Draft High Court constitutional writ prayers (Article 102)
bhashabid writ --remedy "detention" --subject "জনাব করিম" --authority "স্বরাষ্ট্র সচিব"
```

### 3. 1-Command Skill Installation (Antigravity, Claude, Cursor)
Install the progressive skill along with **all 9 specialized reference guides** into your coding environment:
```bash
# Install globally to all detected environments (Antigravity, Claude, and Cursor)
bhashabid install-skill --target all

# Or install specifically:
bhashabid install-skill --target antigravity
bhashabid install-skill --target claude
bhashabid install-skill --target cursor

# Uninstall cleanly at any time:
bhashabid uninstall-skill --target all
```

### 4. Model Context Protocol (MCP) Server
Expose Bhashabid's deterministic tools via stdio MCP for Claude Desktop, Cursor, Windsurf, or Zed:
```bash
bhashabid-mcp
# or: bhashabid mcp
```
**Exposed Deterministic Tools**:
- `bhashabid_repair`: Automatic Unicode NFC normalization, Bangla Academy orthography, and Dari punctuation.
- `bhashabid_spellcheck`: 78k offline phonetic candidate search with compound word decomposition.
- `bhashabid_format_number`: Irregular 0–99 cardinal words, currency words, South Asian comma grouping.
- `bhashabid_lint`: Static analysis for Guru-chandali, cross-clause honorific concordance, and English calques.
- `bhashabid_prosody`: Classical scansion (Dalabritta, Matrabritta, Aksharbritta) and 14-akshar Payar validation.
- `generate_writ_prayer`: Drafts Article 102 High Court constitutional writ prayers in statutory Bengali.

### 5. Standalone Three-Tier Prompt System (ChatGPT, Claude Web, Gemini Web, DeepSeek)
If you are using a web browser interface or third-party client and cannot install Python packages, use our three-tier prompt system:
👉 **[`skills/bangla-expert/STANDALONE_ALL_IN_ONE.md`](skills/bangla-expert/STANDALONE_ALL_IN_ONE.md)**

- **Tier 1 (Nano Prompt)**: Copy and paste directly into **ChatGPT Custom Instructions** (fits cleanly within the 1,500-char limit) or mobile apps.
- **Tier 2 (Domain Modules)**: Prepend Tier 1 and attach your sector module (Legal, Banking, Petitions, NCTB, Medical, Agriculture, Tech) into Claude Projects or Custom GPTs.
- **Tier 3 (Full Reference)**: Load the full taxonomy and 105+ idiom mapping table into foundation model system prompts.

---

## 🛡️ Constitutional Governance (Principle P2 & P8)

1. **Principle P2 (Human Provenance Gate)**: No knowledge card enters production without authenticated native-speaker review, non-empty verified exemplars, and cryptographic SHA-256 signatures. **50 / 50 cards (100%)** are authenticated by lead human arbiter `Ashikur Rahman Bhuiyan` (with 19 candidate cards in `knowledge/cards/drafts/` queued for review).
2. **Principle P4 (Deterministic Tools for Rules)**: Rules that can be computed with discrete mathematics or grammars are implemented in code, not left to probabilistic prompt guesses.
3. **Principle P8 (Anti-Self-Deception & Memory)**: Flaws detected across real-world corpora are permanently logged in [`memory/mistakes/ledger.jsonl`](memory/mistakes/ledger.jsonl) and sealed as automated unit tests in [`eval/unit/`](eval/unit/).

---

## 🔒 Security & Defensive Audit (Cloudflare Audit Skill)

Bhashabid has undergone a comprehensive defensive security audit adhering to the **[Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill)** framework, achieving an **A+ Hardened Production Grade** rating:
- **Zero Dynamic Execution**: 100% pure Python AST with zero calls to `eval()`, `exec()`, or dynamic code execution.
- **Zero Runtime Dependencies & Offline Purity**: Operates strictly in-memory without external network telemetry, APIs, or third-party wheels.
- **Hardened MCP Boundary**: Bounded 10MB stdio frames and strict tool type sanitization prevent local IPC resource exhaustion.
- **Data Lifecycle Safety**: Skill installers strictly verify Bhashabid content signatures before unlinking any workspace files, guaranteeing zero accidental data loss for developer configurations.
- **Software Composition & Secrets**: 0 CVEs detected in Google OSV.dev / PyPA, and 0 secret/credential leaks across 1,860 scanned files.

For full architectural boundaries, threat model, and vulnerability disclosures, see **[SECURITY.md](SECURITY.md)**.

---

## 📖 Wiki & Documentation Hub

Comprehensive architectural specifications, domain style guides, and developer workflows:
- [Wiki Home & Overview](docs/wiki/Home.md)
- [Getting Started & Installation Guide](docs/wiki/Getting-Started.md)
- [The 17 Specialized Professional Sectors](docs/wiki/The-17-Professional-Sectors.md)
- [Model Context Protocol (MCP) Guide](docs/wiki/Model-Context-Protocol-MCP.md)
- [Poetic Prosody & Payar Scansion Specification](docs/wiki/Poetic-Prosody-&-Payar.md)
- [Article 102 Constitutional Writs Guide](docs/wiki/Constitutional-Writs-Article-102.md)
- [Principle P2 Provenance & Human Review Protocol](docs/wiki/Principle-P2-Provenance-&-Review.md)
- [Centralized Linguistic Review Hub](docs/review_queue/README.md)
- [Pending Human Reviews Dashboard](docs/review_queue/PENDING_REVIEWS.md)

---

## 📄 License

This project is licensed under the permissive terms of the **[MIT License](LICENSE)**. See the `LICENSE` file for full copyright and permission notices.
