# LLM Output Inbox (learning-loop input)

Put real Bengali text you want the system to learn from here, ideally LLM outputs you have read
(ChatGPT, Gemini, Claude) or approved-source text. Accepted formats:

- `*.txt` — one document per file
- `*.jsonl` — one `{"text": "...", "source": "gemini", "sector": "..."}` per line
- `*.json` — `{"id": "text", ...}` or `["text", ...]` (e.g. `eval/llm_ab/*/out_*.json`)

Answers keyed by prompt IDs from `eval/corpora/learning_prompts.json` (e.g. `{"LP19": "..."}`) are tagged with
that prompt's sector automatically. Files here are gitignored (local input only).

Then run the loop:

```bash
bhashabid learn cycle --fetch                      # manual practice run: sector sources + new inbox files, report
bhashabid learn scan eval/corpora/llm_inbox        # or scan a folder directly
bhashabid learn pending                            # review candidates with their evidence
bhashabid learn approve CAND-LEXICON-xxxx --reviewer "Your Name"
bhashabid learn approve CAND-TERM-xxxx --reviewer "Your Name" --set bengali=ডিপ্লয়মেন্ট
bhashabid learn approve CAND-SADHU-ROOT-xxxx --reviewer "Your Name" --set root=গুন
bhashabid learn reject CAND-xxxx --reviewer "Your Name" --reason "abbreviation"
bhashabid learn apply                              # distill approved cards, add regression cases, rebuild bundles
```

Any card can be turned into an idiom on approval:
`--set action=add_idiom english="..." flawed_calque="..." natural_bengali="..."`.
