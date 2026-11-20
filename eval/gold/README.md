# Engine Gold Set (`engine_gold.jsonl`)

Labelled Bengali sentences used to measure the deterministic linter and repair engine
(`bhashabid.lint`, `bhashabid.repair`) without any LLM in the loop.

| Label | Meaning | Expected engine behaviour |
|---|---|---|
| `clean` | Correct standard Bengali (Cholito or consistent Sadhu), incl. dialogue | No lint issue; `repair` leaves text unchanged |
| `guru_chandali` | Sadhu and Cholito forms mixed in one sentence | `RULE-LINT-GURU-CHANDALI` |
| `honorific` | Pronoun–verb register/person mismatch | `RULE-LINT-HONORIFIC-*` or `RULE-LINT-PERSON-*` |
| `calque` | Literal English calque / mechanical passive | `RULE-LINT-CALQUE` |

Run: `python eval/benchmarks/engine_accuracy.py` (add `--json` for machine output).

## Provenance & limits (P2, P8)

- Status: **llm-hypothesis**. Sentences were drafted by an LLM assistant and have **not yet been
  confirmed by a native-speaker reviewer**. Treat labels as provisional until reviewed.
- The set is small (~90 sentences) and was written by the same party that tuned the rules, so the
  scores are an optimistic upper bound for these rule families, not a measure of real-world accuracy.
  A held-out set written by someone else is needed for an unbiased number.
- It measures only the deterministic engine. It says nothing about how much the skill improves an LLM.
