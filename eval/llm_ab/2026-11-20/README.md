# LLM A/B Pilot — 2026-11-20 (base vs. skill vs. skill + MCP tools)

First live comparison of real model outputs (REQ-039 / P7 pilot). Small and single-vendor; read the limits below.

## Setup
- 12 tasks across 11 sectors (`tasks.json`).
- Models: Claude Haiku and Claude Sonnet, run as isolated sub-agents.
  - **base**: own knowledge only; no files, skills, MCP or code.
  - **skill**: read `skills/bangla-expert/SKILL.md` + the references it points to; no MCP or code.
  - **tools**: old skill + the `bhashabid` MCP tools (the installed server, i.e. the released package, not this branch).
  - **v2text**: rewritten tool-routing skill (built bundle), no code and no MCP; simulates Gemini or claude.ai without code execution.
  - **v2code**: rewritten skill + its bundled engine via code execution (`scripts/bn.py`), no MCP; simulates claude.ai with code execution.
- `+repair`: the same output passed through `bhashabid.repair` (the offline engine, no LLM).
- Raw outputs: `out_<model>_<condition>.json`. Scoring: `python eval/llm_ab/2026-11-20/score.py` (deterministic checks only).

## Results

| model | base | old skill | old skill + MCP | new skill, text only | new skill + bundled engine |
|---|---|---|---|---|---|
| haiku | 12/12 | 11/12 | 11/12 | 12/12 | 12/12 |
| sonnet | 10/12 | 10/12 | 12/12 | **12/12** | **12/12** |

Engine-flagged defects: Haiku base 3 (Sadhu/Cholito mix), all other runs 0.

**Caveat on the new-skill columns:** the rewritten skill's calendar table and Payar rule were added after seeing the T07/T10 failures on these same 12 tasks. These columns show that the fix works on the failures it targets; they are not an unbiased estimate. A held-out task set is needed.

`+repair` changed no task result in any condition.

Per-task differences:
- **T07 (Bangabda date)**: Sonnet gave 16 Dec 2025 = ২ পৌষ in base and skill (correct: ১ পৌষ ১৪৩২, revised calendar). With the `format_date` tool it was correct.
- **T10 (Payar metre)**: Sonnet failed in base and skill; with `prosody_scan` it produced two valid 8+6 lines. Haiku: valid in base, one 9+6 line with skill, valid with tools.
- **T09 (writ prayer)**: Haiku base mixed Sadhu (`দর্শাইতে`, `হইবে`, `করিবেন`) with Cholito (`জারি করে`, `বলে`); not in skill or tools runs. Both tool-using agents found `generate_writ_prayer` classified a detention petition as Habeas Corpus and added an interim-bail prayer, and wrote the Rule Nisi prayer themselves.
- **T08 (fractions)**: Haiku with tools wrote `সাড়ে দুই সপ্তাহ` (wrong; 2.5 = আড়াই). Correct in base and skill. Tools did not prevent it.
- All other tasks (lakh/crore grouping, cheque words, Dari, calque-free translation, official letter, honorifics, Cholito rewrite) were correct in every condition.

Reading: on this small set the skill text alone gave no consistent gain; the deterministic MCP tools fixed the two tasks models get wrong from memory (calendar conversion, metre counting) for Sonnet.

## Engine bug found by this run (fixed)
`তুমি যা বলবে তাই করব` (correct: implied subject আমি) was flagged as a person clash, and `repair` changed `করব` → `করবে`, altering meaning. Relative markers (`যা`, `তাই`, `যত`, `যেমন`, `যেখানে`) now count as clause boundaries; the sentence is in the gold set as `CLN-053`.

## Limits
- n = 12 tasks, one sample per condition, one vendor (two model sizes). Differences of 1 task are within noise.
- Checks are deterministic and cover only measurable features; fluency, naturalness and factual quality were not judged.
- The task set and scorer were written by the same assistant that edited the engine. Two scorer bugs (nukta form; T06/T07 patterns too strict) were found by reading outputs and fixed before these numbers; they are disclosed here.
- Needs: more tasks, multiple samples, other vendors (GPT, Gemini), and blind native-speaker rating.
