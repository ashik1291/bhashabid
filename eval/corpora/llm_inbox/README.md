# LLM Output Inbox (learning-loop input)

Put real Bengali text you want the system to learn from here, ideally LLM outputs you have read
(ChatGPT, Gemini, Claude) or approved-source text. Accepted formats:

- `*.txt` — one document per file
- `*.jsonl` — one `{"text": "...", "source": "gemini", "sector": "..."}` per line
- `*.json` — `{"id": "text", ...}` or `["text", ...]` (e.g. `eval/llm_ab/*/out_*.json`)

## Teaching corrections (most valuable input)
When you read an LLM answer and fix it, save the pair. The system diffs them word by word and drafts the
right card: English → Bengali term, Sadhu → Cholito root, phrase → idiom/calque, single word → replacement
(spelling or word choice), verb-ending change → rule for review. Corrections the engine already makes are skipped.

```jsonl
{"llm": "প্রধান উপদেষ্টার দ্বারা সভাপতিত্ব করা বৈঠক", "fixed": "প্রধান উপদেষ্টার সভাপতিত্বে অনুষ্ঠিত বৈঠক", "sector": "Mass Media & Digital Journalism"}
```
In an answers file from `learn prompts`, use `{"LP03": {"llm": "...", "fixed": "..."}}`.

## Practice prompts
`bhashabid learn prompts --count 10 [--sectors ...]` prints unused prompts (spread over sectors) and creates an
answer file here. Paste each model answer (or a correction pair), then run `bhashabid learn cycle`.

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
