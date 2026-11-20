# LLM A/B Pilot — 2026-11-20 (with skill vs. without skill)

First live comparison of real model outputs (REQ-039 / P7 pilot). Small and single-vendor; read the limits below.

## Setup
- 12 tasks across 11 sectors (`tasks.json`).
- Models: Claude Haiku and Claude Sonnet, run as isolated sub-agents.
  - **base**: own knowledge only; no files, skills, MCP or code.
  - **skill**: read `skills/bangla-expert/SKILL.md` + the references it points to; no MCP or code.
- `+repair`: the same output passed through `bhashabid.repair` (the offline engine, no LLM).
- Raw outputs: `out_<model>_<condition>.json`. Scoring: `python eval/llm_ab/2026-11-20/score.py` (deterministic checks only).

## Results

| model | condition | task checks passed | engine-flagged defects |
|---|---|---|---|
| haiku | base | 12/12 | 3 (one real Sadhu/Cholito mix in T09) |
| haiku | base+repair | 12/12 | 3 (repair declines: Sadhu-dominant text) |
| haiku | skill | 11/12 | 0 |
| sonnet | base | 10/12 | 0 |
| sonnet | skill | 10/12 | 0 |

Per-task differences:
- **T09 (writ prayer)**: Haiku without the skill mixed Sadhu (`দর্শাইতে`, `হইবে`, `করিবেন`) with Cholito (`জারি করে`, `বলে`); with the skill it did not. The only defect the skill removed.
- **T10 (Payar)**: Haiku without the skill wrote two valid 8+6 lines; with the skill one line was 9+6. Sonnet failed in both conditions. The skill text does not help metre; the `prosody_scan` tool would.
- **T07 (Bangabda)**: Sonnet gave 16 Dec 2025 = ২ পৌষ in both conditions (correct: ১ পৌষ ১৪৩২ under the revised calendar). The skill did not fix it; the `format_date` tool would.
- All other tasks (lakh/crore grouping, cheque words, Dari, calque-free translation, official letter format, honorifics, fractions, Cholito rewrite) were correct **without** the skill for both models.

## Engine bug found by this run (fixed)
`তুমি যা বলবে তাই করব` (correct: implied subject আমি) was flagged as a person clash, and `repair` changed `করব` → `করবে`, altering meaning. Relative markers (`যা`, `তাই`, `যত`, `যেমন`, `যেখানে`) now count as clause boundaries; the sentence is in the gold set as `CLN-053`.

## Limits
- n = 12 tasks, one sample per condition, one vendor (two model sizes). Differences of 1 task are within noise.
- Checks are deterministic and cover only measurable features; fluency, naturalness and factual quality were not judged.
- The task set and scorer were written by the same assistant that edited the engine. Two scorer bugs (nukta form; T06/T07 patterns too strict) were found by reading outputs and fixed before these numbers; they are disclosed here.
- Needs: more tasks, multiple samples, other vendors (GPT, Gemini), and blind native-speaker rating.
