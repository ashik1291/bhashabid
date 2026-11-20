---
name: bhashabid-learning
description: Run a Bhashabid learning session - generate or collect Bengali LLM output, scan it for cases the engine cannot decide, record suggestions on candidate cards, and (only after human approval) apply them. Use when asked to run, continue or report on the learning loop.
---

# Bhashabid Learning Session

Follow `docs/LEARNING_LOOP_AGENT_GUIDE.md` exactly. Summary:

1. `bhashabid learn status`; stop if `state/STOP` exists.
2. Answer 10–20 prompts from `eval/corpora/learning_prompts.json` in Bengali **without** the bangla-expert skill or MCP tools; save to `eval/corpora/llm_inbox/<model>_<YYYYMMDD>.json` as `{"LPxx": "answer"}`.
3. `bhashabid learn scan eval/corpora/llm_inbox`, then `bhashabid learn pending --json`.
4. For each card without a suggestion: `bhashabid learn suggest <ID> --by "<model id>" --set ... --rationale "..." --confidence ...` (decision table in the guide).
5. Report a table of suggestions to the human and give the approve/reject commands. **Do not approve, reject or apply yourself** unless the human explicitly instructs it for named cards with their name as reviewer.
6. After approval: `bhashabid learn apply`, run the unit tests and `python eval/benchmarks/engine_accuracy.py`, then commit (no push or tag unless asked).
