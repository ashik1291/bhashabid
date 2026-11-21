# Bhashabid Corpus Coverage Audit (engine agreement rate)

- **Execution Timestamp**: `2026-11-21 18:47:29`
- **Approved Knowledge Invariants**: `50` production cards
- **Quarantined Candidate Drafts**: `21` (Principle P2 review queue)
- **External Corpora Ingested**: `20` source files (`176` total sentences)
- **Clean Native Benchmarks**: `166`
- **Canary Flaws Trapped**: `10`
- **Active Anomaly Candidates**: `0`

> **Read carefully:** *Engine agreement* = share of sentences the current rules already classify as clean or as a known flaw. It is circular (the rules were tuned on this data), is not accuracy, and is not evidence of learning or coverage. Sectors with fewer than 30 sentences are marked INSUFFICIENT DATA.

## 1. Domain & Sector Engine Agreement

| Domain / Sector | Sentences | Clean Benchmark | Trapped Canaries | Engine Agreement | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Academic Research & Methodology | 11 | 90.9% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Administrative Governance & Memos | 11 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Agronomy & Disaster Management | 13 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Banking & Macroeconomics | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Administrative Governance | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Tax & Customs | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Official Administrative | 1 | 0.0% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Land Conveyancing & Deeds | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Macroeconomic & Finance | 2 | 50.0% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Judicial & High Court | 2 | 50.0% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Sports Vernacular | 2 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Corporate & Tech | 2 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Disaster Early Warning | 2 | 50.0% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Citizen Digital Services & Smart Governance | 4 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Classical Poetry & Prosody | 5 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Consumer E-Commerce & Retail Logistics | 8 | 87.5% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Creative Fiction & Dialogue | 7 | 71.4% | 2 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Customer Support & Conversational Chat | 8 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Education & NCTB Pedagogy | 12 | 91.7% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Healthcare & Epidemiology | 12 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| ICT & Software Engineering | 7 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Land Registry & Deeds | 14 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Constitutional Law & Writs | 18 | 94.4% | 1 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Macroeconomics & Banking | 12 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Mass Media & Digital Journalism | 4 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| MFS, Microfinance & Grassroots FinTech | 4 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Education & Pedagogy | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Science & Encyclopedic | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Poetic Prosody | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Agronomy & Crop Protection | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Healthcare & Medicine | 1 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |
| Translation & Calque Naturalization | 6 | 100.0% | 0 | `100%` | INSUFFICIENT DATA (n<30; rate not meaningful) |

**Average Engine Agreement on Current Batch (circular; not accuracy)**: `100.0%`

## 2. Autonomous Ingestion & Convergence Criteria

1. **When does practice on the same batch stop?**
   - **Threshold**: When a domain reaches $\ge 95\%$ saturation and $\le 0$ novel anomalies discovered over 3 consecutive rounds.
   - **Result**: Practicing beyond 3-5 rounds on a static batch yields diminishing returns. Compute must shift to new data ingestion.

2. **When is new data ingested?**
   - **Immediate Ingestion Trigger**: As soon as saturation index exceeds `0.90` or when new anomalies $\Delta A = 0$.
   - **Ingestion Channels**:
     - Unharvested files in `eval/corpora/sources/` or `eval/corpora/inbox/`.
     - Dynamic Adversarial Perturbation with elevated entropy.
     - Live RSS feeds / open government circulars.

3. **Autonomous Learning Pipeline Role Separation**:
   - **Autonomous (Machine)**: Data fetching, tokenization, multi-domain linting, canary trapping, duplicate guarding, draft card synthesis, and post-approval distillation.
   - **Human Gate (Principle P2)**: Reviewing and approving candidate cards in `knowledge/cards/drafts/` via GitHub PR.
