# Bhashabid System Status

- **Current Release**: v1.2.0
- **Gate Status**: Released by maintainer decision (2026-11-20)
- **Kill Switch**: INACTIVE (`state/STOP` not present)
- **Last Updated**: 2026-11-20

## Verified State
- Unit & regression suite: 185/185 passing on Windows and Linux (`python -m unittest discover -s eval/unit`).
- Engine gold set (`eval/gold/engine_gold.jsonl`, llm-hypothesis, pending native review): 0/52 false positives on clean text; Guru-chandali 10/10, honorific 14/14, calque 8/8 detected (`python eval/benchmarks/engine_accuracy.py`).
- Single code tree: `tools/bn_*`, `tools/mcp_server`, `tools/cli.py` are aliases of the `bhashabid` package.
- Knowledge base: 50 cards marked `reviewed`, all by one reviewer (project author); 6 carry a generic reviewer name.
- MCP: 12 tools; CLI: 24 subcommands.
- LLM pilot (`eval/llm_ab/2026-11-20`): Haiku 12/11/11 and Sonnet 10/10/12 of 12 tasks for base / skill / skill+tools.
- Scraper gated to approved sources + robots.txt; news feeds (BBC, Prothom Alo, Daily Star, DW, TBS) are not registered and therefore not fetched.

## Known Gaps (not yet done)
- Only a 12-task single-vendor LLM pilot exists (REQ-039 / P7); a large multi-vendor benchmark with blind native rating is pending (needs paid API approval).
- Learning loop does not learn: practice/harvest re-run existing rules on edited news text; mistake ledger unchanged since 2026-11-11; `distill` only validates and syncs files.
- `SKILL.md` is ~890 `cl100k_base` tokens, above the 600-token REQ-036 target; the unit test uses a words×1.3 estimate.
- REQ-014, REQ-031, REQ-033, REQ-034, REQ-035 not implemented in code (skill guidance only); REQ-015, REQ-027, REQ-036 partial. See `specs/traceability.csv`.
- Independent second native-speaker review of cards and of the gold set.
- Writ/deed templates not reviewed by a legal professional.
