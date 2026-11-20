# Welcome to the Bhashabid (ভাষাবিদ) Wiki

**Bhashabid** (ভাষাবিদ) is the first-ever open-source Bengali language coprocessor engine featuring a **constitutionally supervised self-learning loop**. Operating as an external cognitive and deterministic coprocessor without retraining model weights, it continuously harvests real-world anomalies, synthesizes candidate rules, and distills high-level invariants under human verification (Principle P2) and a strict < 390 token ceiling—systematically elevating the accuracy, orthography, and native fluency of AI-generated Bengali across **17 specialized professional sectors**.

---

## 🧭 Wiki Contents

1. [Getting Started & Installation](Getting-Started.md)
   - CLI usage, Python SDK, MCP setup, and agent skill installation for Cursor, Antigravity, and Claude.
2. [The 17 Specialized Professional Sectors](The-17-Professional-Sectors.md)
   - Comprehensive domain standards across Law, Banking, FinTech, E-Commerce, Medicine, Administration, Fiction, Prosody, Agriculture, and more.
3. [Model Context Protocol (MCP) Integration](Model-Context-Protocol-MCP.md)
   - Connecting Bhashabid's deterministic Python tools to Cursor, Claude Desktop, Windsurf, and Zed.
4. [Poetic Prosody & Payar Verification](Poetic-Prosody-&-Payar.md)
   - Phonological syllabification, mora counting, Aksharbritta, Matrabritta, and Payar (8+6=14) scansion.
5. [Article 102 Constitutional Writs](Constitutional-Writs-Article-102.md)
   - High Court writ petitions (Habeas Corpus, Mandamus, Certiorari, Prohibition, Quo Warranto) and statutory prayers.
6. [Principle P2 Provenance & Human Review](Principle-P2-Provenance-&-Review.md)
   - The human review protocol (reviewer, date, SHA-256 content fingerprint) for knowledge cards.
7. [Centralized Linguistic Review Hub](../review_queue/README.md)
   - Community guidelines for reviewing and submitting candidate cards via GitHub Pull Requests.

---

## 🏛️ The 4 Pioneering Architectural Pillars

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   USER PROMPT / AI AGENT TASK                                     │
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  │
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│              CORE SKILL KERNEL (Compact, ~1.26k cl100k Tokens, Domains Loaded On-Demand)          │
└───────────────────────┬─────────────────────────┬─────────────────────────┬───────────────────────┘
                        │                         │                         │
                        ▼ [Pillar 1]              ▼ [Pillar 3]              ▼ [Pillar 4]
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│  PROGRAMMATIC TOKEN CEILING   │ │   MODULAR DOMAIN ISOLATION    │ │ DETERMINISTIC COPROCESSOR     │
│ • ~1.26k cl100k Tokens        │ │ • 9 Progressive Domain Guides │ │ • Pure Python / MCP Server    │
│ • Universal Grammar Invariant │ │ • 17 Specialized Sectors      │ │ • ~11k–175k words/second      │
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

- **Pillar 1: Compact Skill Kernel**: Progressive disclosure keeps the always-loaded kernel compact (~1,260 tokens on `cl100k_base`; Bengali script tokenizes densely) and loads domain guides only on demand.
- **Pillar 2: Supervised Self-Learning Distillation Loop**: Unlike unconstrained autonomous agents that hallucinate grammar rules, Bhashabid pairs an anomaly harvester with a human-in-the-loop (Principle P2) cryptographic sign-off gate before distilling high-level invariants.
- **Pillar 3: Modular Domain Isolation**: 17 professional sectors are organized into **9 isolated reference guides** loaded strictly on demand; unrelated domain knowledge burns 0.0 prompt tokens.
- **Pillar 4: Deterministic MCP Offloading (Zero Token Cost)**: Irregular 0–99 numerals, South Asian currency commas, Unicode NFC canonical normalization, and 14-akshar Payar scansion run as local Python (measured ~110k–175k words/s for normalization, ~11–13k words/s for lint/repair).

---

## 🧪 System Health & Proven Accuracy Metrics

| Metric | Target | Current Production Status |
| :--- | :---: | :---: |
| **Unit & Regression Tests** | 100% Pass | **112 / 112 Tests Passing (100% Green)** |
| **Principle P2 Provenance Cards** | 100% Reviewed | **50 / 50 cards reviewed by the project author (content-fingerprinted)** |
| **Core Skill Token Footprint** | REQ-036: < 600 | **~1,260 `cl100k_base` tokens (over target)** |
| **Domain Sectors Supported** | 17 Sectors | **17 Sectors across 9 Reference Guides** |
| **Duplicate Collisions** | 0 Collisions | **0 Duplicate Titles, Summaries, or Exemplars** |
