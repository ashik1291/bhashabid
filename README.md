# Bhashabid (ভাষাবিদ) — The Deterministic Bengali Language Coprocessor Engine

### *Deterministic Bengali linguistic coprocessor engine & progressive skill layer for LLMs, with human-reviewed knowledge cards.*

[![Security CI](https://github.com/ashik1291/bhashabid/actions/workflows/security_audit.yml/badge.svg)](https://github.com/ashik1291/bhashabid/actions/workflows/security_audit.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: >=3.10](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/bhashabid.svg)](https://pypi.org/project/bhashabid/)
[![Tests: 185 Passing](https://img.shields.io/badge/Tests-185%20Passing-brightgreen.svg)](eval/unit)
[![Security: Self-Assessed](https://img.shields.io/badge/Security-Self--Assessed-informational.svg)](SECURITY.md)
[![Security: Bandit 0-Vuln](https://img.shields.io/badge/Security-Bandit%200--Vuln-brightgreen.svg)](SECURITY.md)
[![Dependencies: 0 CVEs](https://img.shields.io/badge/Dependencies-0%20CVEs%20(OSV)-brightgreen.svg)](SECURITY.md)
[![Secrets: 0 Leaks](https://img.shields.io/badge/Secrets-0%20Leaks-brightgreen.svg)](SECURITY.md)
[![Supply Chain: Sigstore Attested](https://img.shields.io/badge/Supply%20Chain-Sigstore%20Attested-blue.svg)](SECURITY.md)
[![P2 Provenance: 50 Author-Reviewed Cards](https://img.shields.io/badge/P2%20Provenance-50%20Author--Reviewed%20Cards-blueviolet.svg)](knowledge/cards)
[![Core Skill: ~890 cl100k tokens](https://img.shields.io/badge/Core%20Skill-~890%20cl100k%20tokens-yellow.svg)](skills/bangla-expert/SKILL.md)

> **Bhashabid** (ভাষাবিদ) is, to our knowledge, the first open-source **MCP server + Agent Skill** that bundles offline Bengali normalization, register/honorific linting, statutory numerals and dates, and Payar prosody for LLMs. It works alongside a model without retraining it: the skill gives compact style guidance across **17 professional sectors**, and the deterministic tools handle what models get wrong from memory. It builds on earlier Bengali NLP work such as [BNLP](https://github.com/sagorbrur/bnlp), [csebuetnlp/normalizer](https://github.com/csebuetnlp/normalizer) and [bnunicodenormalizer](https://pypi.org/project/bnunicodenormalizer/).

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

```python
import bhashabid
# 10-Second Test: Automatic Unicode & spelling repair (<2ms, Zero-LLM)
repaired, _ = bhashabid.repair("ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন.")
print(repaired)  # "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।"
```
*(See [Deep-Dive Usage & Integrations](#-deep-dive-usage--integrations) below for full Python SDK, CLI tools, and MCP documentation).*

---

### Option C: Web & Mobile AI Chat (Claude Web, Gemini Web, ChatGPT)
If you don't use an AI code editor or CLI, you can use Bhashabid directly in web browsers:
- 📦 **Claude Web Skill**: Upload [`bhashabid-skill.zip`](bhashabid-skill.zip) via **Upload a skill** with code execution enabled; the bundle includes the offline engine (`scripts/bn.py`), so no MCP server is needed. Rebuild with `python scripts/build_skill_bundle.py`.
- 💎 **Gemini Web**: Create a **Bhashabid Gem** or attach instructions directly.
- 🤖 **ChatGPT Web**: Create a **Custom GPT** with `bhashabid-skill.zip` or use **Custom Instructions** (<1,500 chars).

👉 **[Complete Step-by-Step Web Guide (docs/WEB_CHAT_USER_GUIDE.md)](docs/WEB_CHAT_USER_GUIDE.md)**
👉 **[View Three-Tier Standalone Prompts (STANDALONE_ALL_IN_ONE.md)](skills/bangla-expert/STANDALONE_ALL_IN_ONE.md)**

---

## 🎯 What Bhashabid Does & What Problem It Solves Uniquely

### The Production Reality: Frontier LLMs (~80–85% Fluent) & The Deterministic "Last-Mile"
Frontier large language models (such as GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro) are remarkably competent. Across standard Bengali conversation, translation, and open-ended generation, frontier models are broadly fluent. They are not illiterate or broken. *(The often-quoted "~80–85% fluency / 15–20% gap" framing in this README is the author's working estimate; it has not been measured by this project — see [Measured Accuracy](#-measured-accuracy--what-is-and-isnt-verified).)*

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
- **Bhashabid Coprocessor (Deterministic Guardrail)**: Handles the 15% deterministic last mile—zero-latency Unicode canonicalization, Bangla Academy orthography repair, statutory banking numbers/words, honorific concordance checking, and compact, on-demand context guidance via MCP & pure local Python.

---

## 📊 Side-by-Side Comparison: Frontier LLMs vs. Bhashabid Coprocessor

| Linguistic & Production Dimension | Frontier LLM Baseline (Probabilistic Generation) | Bhashabid Neurosymbolic Coprocessor (Deterministic Guard) | Empirical Production Example |
| :--- | :--- | :--- | :--- |
| **1. South Asian Currency & Numbers** | High fluency, but frequently defaults to Western 3-digit comma grouping (`1,234,567.50`). | Mathematically guarantees South Asian Lakh/Crore grouping and official check words in Bengali. | Input: `1234567.50`<br>Raw LLM: `1,234,567.50` ⚠️<br>Bhashabid: **"১২,৩৪,৫৬৭.৫০ (বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা মাত্র)"** ✔️ |
| **2. Unicode NFC & Punctuation** | Emits mixed Unicode codepoints (NFD/broken Hasanta) and ASCII periods (`.`) instead of Dari (`।`). | Deterministically canonicalizes Unicode (NFC with precomposed য়/ড়/ঢ়) and converts terminal periods to Dari while preserving decimals (`৩.১৪`). | Raw LLM: `"তিনি বাড়ি গেলেন."` ⚠️<br>Bhashabid: **"তিনি বাড়ি গেলেন।"** ✔️ |
| **3. Bangla Academy Orthography** | Frequently blends archaic, dialectal, and modern spellings based on historical internet training data (*ষ্টেশন, পাখী, পোষ্ট*). | Deterministically normalizes loanwords and native vocabulary to official Bangla Academy standards (*স্টেশন, পাখি, পোস্ট*). | Raw LLM: `"রেল ষ্টেশনে পাখী ডাকছে"` ⚠️<br>Bhashabid: **"রেল স্টেশনে পাখি ডাকছে"** ✔️ |
| **4. Pronominal & Verbal Honorifics** | Prone to register drift across multi-clause sentences (mixing informal *তারা* with honorific *দিয়েছিলেন*). | Enforces strict grammatical concordance (*তারা ... দিয়েছিল* vs *তাঁরা ... দিয়েছিলেন*) across clause boundaries. | Raw LLM: `"তারা অর্থ ফেরত দিয়েছিলেন"` ⚠️<br>Bhashabid: **"তাঁরা সেই অর্থ ফেরত দিয়েছিলেন"** ✔️ |
| **5. Passive Voice English Calques** | Translates technical passives with literal *"দ্বারা"* (*"মুদ্রাস্ফীতির দ্বারা চালিত"*). | Converts passive calques into natural, active causal Bengali syntax. | Raw LLM: `"মুদ্রাস্ফীতির দ্বারা চালিত রাজস্ব ঘাটতি"` ⚠️<br>Bhashabid: **"মুদ্রাস্ফীতিজনিত কারণে রাজস্ব ঘাটতি বৃদ্ধি পেয়েছে"** ✔️ |
| **6. Judicial Writ Formulas (Article 102)** | Approximates legal phrasing colloquially (*"জিজ্ঞেস করে রুল জারি করেছে"*). | Enforces Supreme Court of Bangladesh statutory Rule Nisi show-cause and prayer formulas. | Raw LLM: `"কেন বেআইনি হবে না জিজ্ঞেস করে রুল দিয়েছে"` ⚠️<br>Bhashabid: **"কেন বেআইনি ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন"** ✔️ |
| **7. Secretariat Administrative Memos** | Calques English salutations (*"Dear Sir"* ➔ *"প্রিয় মহাশয়"*). | Enforces official *Bangladesh Secretariat Instructions* (*সচিবালয় নির্দেশমালা*) opening and closing protocols. | Raw LLM: `"প্রিয় মহাশয়, আশা করি ভালো আছেন"` ⚠️<br>Bhashabid: **"বরাবর... বিষয়:... জনাব, বিনীত নিবেদন এই যে..."** ✔️ |
| **8. Classical 14-Akshar Payar Scansion** | Cannot reliably count poetic morae due to subword BPE tokenization abstraction. | Deterministic phonological syllabifier (*মুক্তদল* vs *রুদ্ধদল*) verifies exact 8+6=14 akshar Payar cadence. | Raw LLM: Pseudo-verse with broken 16/17 syllable rhythm ⚠️<br>Bhashabid: **Validates exact 8+6=14 akshar Payar couplets** ✔️ |
| **9. Context Window & Token Efficiency** | Dumping massive style guides (5,000–10,000 tokens) exhausts context, increases latency, and costs money. | Compact root skill kernel (**~890 tokens** on `cl100k_base`, ~700 on `o200k_base`; Bengali script tokenizes densely), loading domain guides on-demand. | Raw LLM: 10,000+ token monolithic prompt injection ⚠️<br>Bhashabid: **~890-token kernel + 0-token Python offloading** ✔️ |
| **10. Local Offline Edge Execution** | Requires active internet, cloud API keys, and 500ms–2000ms latency per request. | 100% offline, local execution with 78,000+ word lexicon; measured ~110,000–175,000 words/s (normalize) and ~11,000–13,000 words/s (lint / repair) on a laptop CPU. | Raw LLM: Cloud dependent, network latency, API costs ⚠️<br>Bhashabid: **Pure local Python, 0 network calls, $0.00 marginal cost** ✔️ |

---

## 🏛️ The 4 Pioneering Architectural Pillars

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   USER PROMPT / AI AGENT TASK                                     │
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  │
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│              CORE SKILL KERNEL (Compact, ~890 cl100k Tokens, Domains Loaded On-Demand)            │
└───────────────────────┬─────────────────────────┬─────────────────────────┬───────────────────────┘
                        │                         │                         │
                        ▼ [Pillar 1]              ▼ [Pillar 3]              ▼ [Pillar 4]
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│  PROGRAMMATIC TOKEN CEILING   │ │   MODULAR DOMAIN ISOLATION    │ │ DETERMINISTIC COPROCESSOR     │
│ • ~890 cl100k Tokens          │ │ • 9 Progressive Domain Guides │ │ • Pure Python / MCP Server    │
│ • Universal Grammar Invariant │ │ • 17 Specialized Sectors      │ │ • ~11k–175k words/second      │
│ • Zero Context Bloat          │ │ • 0.0 Unrelated Prompt Tokens │ │ • Exact Math, Unicode & Dari  │
└───────────────────────────────┘ └───────────────────────────────┘ └───────────────▲───────────────┘
                                                  ▲                                 │
                                                  │                                 │
                                                  │ [Pillar 2: Supervised Loop]     │
                        ┌─────────────────────────┴─────────────────────────┐       │
                        │ HARVESTER ➔ DRAFT CARDS ➔ HUMAN REVIEW GATE (P2)  ├───────┘
                        │ Real-World Anomalies ➔ Verified Invariants Distill│
                        └───────────────────────────────────────────────────┘
```

### 1. Compact Skill Kernel with Progressive Disclosure
- **Problem**: Monolithic linguistic system prompts (5,000–20,000 tokens) cause severe context dilution, high latency, and high API expenses.
- **Solution**: The root skill kernel (`skills/bangla-expert/SKILL.md` and `.cursor/rules/bangla-expert.mdc`) is kept compact (**~890 tokens** on `cl100k_base`). It contains only universal structural invariants; domain reference files are retrieved via progressive disclosure. Note: this exceeds the 600-token target in REQ-036 — the unit test uses a word-count estimate that undercounts Bengali; see [Measured Accuracy](#-measured-accuracy--what-is-and-isnt-verified).

### 2. Human-Reviewed Knowledge Cards & Regression Harness
- **Problem**: Manually appending example sentences to prompts causes prompt bloat, and un-reviewed machine-generated rules drift into hallucinated grammar.
- **Solution**: Rules live as knowledge cards and engine rules that a human edits and reviews. The `harvest` / `practice` / `synthesize-cards` commands are a **regression harness**: they run the linter over corpora and draft candidate cards from its findings, but they can only surface patterns the engine already knows, and `distill` validates and syncs files rather than writing rules. New rules come from reviewed errors in real LLM outputs (see `eval/llm_ab/`, `eval/gold/`). Knowledge cards cannot enter production without a **recorded human sign-off** (reviewer name, date, and a SHA-256 content fingerprint that detects later edits; it is not a cryptographic signature).

### 3. Modular Domain Isolation (9 Progressive Guides)
- **Problem**: Exposing all specialized vocabularies simultaneously confuses model style and wastes tokens.
- **Solution**: 17 sectors are organized into **9 isolated reference guides**. An agent writing poetry burns **0.0 prompt tokens** on Supreme Court writ rules or central bank banking regulations.

### 4. Deterministic Python Offloading via MCP (Zero Token Cost)
- **Problem**: LLMs struggle with mathematical lookups, comma spacing, and phonological syllable counting.
- **Solution**: Bhashabid offloads deterministic operations to local Python algorithms via the **Model Context Protocol (MCP)** and CLI, with exact, unit-tested results for numbers, dates and Unicode, and **0 prompt tokens burned**.

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
| **10** | **ICT & Software Engineering** | Bangladesh Computer Council (BCC) computing standards, Unicode canonical normalization, open-source localization. | [`technical_terms.md`](skills/bangla-expert/references/technical_terms.md) |
| **11** | **Education & NCTB Pedagogy** | National Curriculum and Textbook Board (NCTB) 4-tier Creative Questioning taxonomy (উদ্দীপক, জ্ঞান, অনুধাবন, প্রয়োগ, উচ্চতর দক্ষতা). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **12** | **Translation & Calque Naturalization** | De-calquing passive voice (*দ্বারা*), naturalizing English idioms (*বাগধারা ও প্রবচন*), semantic tri-layer model (*অভিধা, লক্ষণা, ব্যঞ্জনা*). | [`grammar_registers.md`](skills/bangla-expert/references/grammar_registers.md) |
| **13** | **Consumer E-Commerce & Retail Logistics** *(NEW)* | Consumers' Rights Protection Act 2009, e-CAB guidelines, escrow settlement, refund honorific concordance (*তারা বনাম তাঁরা*), courier tracking. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **14** | **Customer Support & Omnichannel Messaging** *(NEW)* | Telecom & omnichannel standards, administrative ticketing resolution nomenclature, preserving alphanumeric tracking IDs (`TCK-942`). | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **15** | **MFS, Microfinance & Grassroots FinTech** *(NEW)* | Bangladesh Bank Payment Systems Dept (PSD) MFS guidelines, Microcredit Regulatory Authority (MRA) rules, fraud prevention warnings. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **16** | **Citizen Digital Services & Smart Governance** *(NEW)* | Aspire to Innovate (a2i) Citizen Service Standards, Bangladesh National Portal style, National ID (NID) registration rules, Citizen Charters. | [`ecommerce_fintech_civic.md`](skills/bangla-expert/references/ecommerce_fintech_civic.md) |
| **17** | **Mass Media & Digital Journalism** *(NEW)* | Bangladesh Press Council Code of Ethics & Stylebook, Press Institute of Bangladesh (PIB) standards, neutral reporting attribution. | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) |

---

## 🧪 Measured Accuracy — What Is and Isn't Verified

Bhashabid follows an anti-self-deception policy (Principle P8). This section separates what has been **measured** from what is **not yet measured**.

### Measured (deterministic engine, no LLM in the loop)

| Check | Result | How to reproduce |
| :--- | :--- | :--- |
| Unit & regression suite | **185 / 185 passing** (Windows & Linux) | `python -m unittest discover -s eval/unit` |
| Numbers 0–99, lakh/crore grouping, currency, fractions, Bongabdo dates | Exact, unit-tested | `eval/unit/test_bn_numbers.py` |
| Gold set — Guru-chandali detection | 10 / 10 detected, 10 / 10 auto-repaired | `python eval/benchmarks/engine_accuracy.py` |
| Gold set — pronoun/verb honorific & person clashes | 14 / 14 detected, 14 / 14 auto-repaired | 〃 |
| Gold set — calques & mechanical passives | 8 / 8 detected, 4 / 8 auto-repaired (others flagged for rewrite) | 〃 |
| Gold set — clean sentences (news, legal, dialogue, consistent Sadhu) | **0 / 52 false positives**; `repair` leaves all 52 unchanged | 〃 |
| Throughput (laptop CPU, single thread) | normalize ~110k–175k words/s · repair ~11k–13k words/s · lint ~11k words/s (varies by run) | — |

**Limits of these numbers:** the gold set (`eval/gold/engine_gold.jsonl`, ~90 sentences) was drafted by an LLM assistant together with the rule changes, and is still awaiting native-speaker review. Treat it as an optimistic upper bound and a regression guard, not as real-world accuracy. The engine is rule-based: it only catches patterns it has rules for.

### LLM pilot (with vs. without skill and tools)

[`eval/llm_ab/2026-11-20`](eval/llm_ab/2026-11-20/README.md): 12 tasks, Claude Haiku and Sonnet, deterministic scoring.

| model | no skill | old skill | old skill + MCP | new skill, text only | new skill + bundled engine |
|---|---|---|---|---|---|
| Haiku | 12/12 | 11/12 | 11/12 | 12/12 | 12/12 |
| Sonnet | 10/12 | 10/12 | 12/12 | 12/12 | 12/12 |

The old skill text gave no consistent gain; tools fixed the two tasks models get wrong from memory (Bangabda date conversion, Payar metre). The rewritten skill routes those facts to the MCP tools, the bundled engine, or reference tables, and passed all 12 in both modes. Caveat: those fixes were written after seeing failures on this same task set, so a held-out set is needed. n = 12, one vendor: a pilot, not proof.

### Not yet measured

- **LLM uplift at scale.** No large, multi-vendor (GPT, Gemini), multi-sample benchmark with blind native-speaker rating yet (REQ-039 / P7). `eval/benchmarks/benchmark_matrix.py` and `benchmark_evaluator.py` use hand-written example outputs and are illustrative only.
- **Per-sector quality.** The 17 sector guides are reference guidance for the LLM; apart from the deterministic tools (numbers, dates, writ/deed templates, prosody), sector-level output quality has not been benchmarked.
- **Skill token budget.** `SKILL.md` is ~890 tokens on `cl100k_base` (~700 on `o200k_base`), above the 600-token REQ-036 target.
- **Unicode form.** Output uses precomposed য়/ড়/ঢ় (U+09DF/09DC/09DD), matching common keyboards; strict Unicode NFC decomposes these three. If a system requires strict NFC, apply `unicodedata.normalize('NFC', text)` after Bhashabid.
- **Knowledge cards.** All 50 cards were reviewed by one native speaker (the project author); 6 carry a generic reviewer name. Independent second review is pending.

### Engine coverage by sector

| Sector(s) | Deterministic support | Status |
| :--- | :--- | :--- |
| All sectors | Unicode canonical form, Dari, numbers, dates, orthography, Guru-chandali, honorific concordance | ✅ Tested |
| Classical Poetry & Prosody | 14-akshar Payar / Aksharbritta scansion | ✅ Tested on canonical lines |
| Constitutional Writs, Land Deeds | Template generators (prayers, schedules, clauses) | 🟡 Templates not yet reviewed by a lawyer |
| Banking, MFS, E-Commerce | Lakh/crore, currency words, ID preservation | 🟡 Numbers tested; prose guidance only |
| Translation & Calque | Calque/idiom detection (~110 phrases + generic passive rule) | 🟡 Pattern-based |
| Healthcare, Agronomy, Admin, Education, Academic, ICT, Journalism, Civic, Support, Creative | Reference guides for the LLM | ⚪ Guidance only, unmeasured |


---

## 🚀 Deep-Dive Usage & Integrations

### 1. Python SDK Reference (`import bhashabid`)
```python
import bhashabid

# 1. Automated Unicode canonicalization, spelling & Dari punctuation (<2ms, Zero-LLM)
repaired, diffs = bhashabid.repair("ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন.")
print(repaired)  # "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।"

# 2. 78,000+ Word Offline Phonetic Spellchecker (sub-10ms)
suggestions = bhashabid.spellcheck("আবিস্কার")
print(suggestions)  # ['আবিষ্কার']

# 3. Statutory South Asian Lakh/Crore Currency & Number Formatting
print(bhashabid.format_number("1234567.50"))        # "১২,৩৪,৫৬৭.৫০"
print(bhashabid.format_currency_words(1234567.50))  # "বারো লাখ চৌত্রিশ হাজার পাঁচ শত সাতষট্টি টাকা পঞ্চাশ পয়সা"
print(bhashabid.format_date_bongabdo(1433, 1, 1))   # "১লা বৈশাখ, ১৪৩৩ বঙ্গাব্দ"

# 4. Static Grammar, Honorific & Calque Linter
issues = bhashabid.lint("তুমি সিদ্ধান্ত নেন")
for issue in issues:
    print(issue.suggestion)  # "তুমি সিদ্ধান্ত নাও" / "আপনি সিদ্ধান্ত নেন"

# 5. Classical 14-Akshar Payar Scansion (8+6)
result = bhashabid.verify_payar("কাশীদাস কহে সাধু শুনে পুণ্যবান")
print(result.is_valid_payar)  # True
print(result.total_morae)     # 14 (8+6)
print(result.explanation)     # "শুদ্ধ পয়ার ছন্দ: ৮+৬=১৪ মাত্রার পর্ব ও মধ্যযতি যথাযথভাবে বিন্যস্ত।"
```

### 2. Developer CLI Reference
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
# Output: বারো লাখ চৌত্রিশ হাজার পাঁচ শত সাতষট্টি টাকা পঞ্চাশ পয়সা

# Lint text for grammatical, honorific, and calque errors
bhashabid lint "তারা সেই অর্থ ফেরত দিয়েছিলেন এবং বিষয়টি বিদ্যুৎ দ্বারা চালিত."

# Verify 14-akshar Payar poetic metre (8+6)
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar

# Draft High Court constitutional writ prayers (Article 102)
bhashabid writ --remedy "detention" --subject "জনাব করিম" --authority "স্বরাষ্ট্র সচিব"

# Check global IDE integration health
bhashabid status
```

### 3. Model Context Protocol (MCP) Server
Expose Bhashabid's deterministic tools via stdio MCP for Claude Desktop, Claude Code, Cursor, Windsurf, or Zed:
```bash
bhashabid-mcp
# or: bhashabid mcp
```
**Exposed Deterministic Tools** (12):
- `repair_text`, `normalize_text`: Unicode canonicalization, Bangla Academy orthography, Dari punctuation, register/calque repair.
- `lint_text`, `spellcheck_text`: Guru-chandali, honorific concordance, calques; 78k-word offline spellcheck.
- `convert_number`, `format_date`: Cardinal/ordinal words, currency, lakh/crore grouping; Gregorian and Bongabdo dates (`ordinal_suffix: false` for "১৫ নভেম্বর" style).
- `prosody_scan`: Aksharbritta scansion and 14-akshar Payar validation.
- `generate_writ_prayer`, `generate_deed_clause`: Article 102 writ prayers and land-deed clauses.
- `audit_literary_text`, `generate_literary_prompt`, `lookup_lapidary`: literary audit and lexicon helpers.

---

## 🛡️ Constitutional Governance (Principle P2 & P8)

1. **Principle P2 (Human Provenance Gate)**: No knowledge card enters production without a recorded native-speaker review, non-empty verified exemplars, and a SHA-256 content fingerprint (tamper-evidence, not a cryptographic signature). **50 / 50 cards** were reviewed by the project author `Ashikur Rahman Bhuiyan` (independent second review pending) (with 19 candidate cards in `knowledge/cards/drafts/` queued for review).
2. **Principle P4 (Deterministic Tools for Rules)**: Rules that can be computed with discrete mathematics or grammars are implemented in code, not left to probabilistic prompt guesses.
3. **Principle P8 (Anti-Self-Deception & Memory)**: Flaws detected across real-world corpora are permanently logged in [`memory/mistakes/ledger.jsonl`](memory/mistakes/ledger.jsonl) and sealed as automated unit tests in [`eval/unit/`](eval/unit/).

---

## 🔒 Security & Defensive Self-Assessment

Bhashabid was self-assessed with an AI-assisted review following the **[Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill)** checklist (not an independent third-party audit). CI runs Bandit, an OSV dependency audit and a secret scanner on every push:
- **Zero Dynamic Execution**: 100% pure Python AST with zero calls to `eval()`, `exec()`, or dynamic code execution.
- **Offline Purity**: Operates in-memory without network telemetry or external APIs; the only declared runtime dependency is `pyyaml`.
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
