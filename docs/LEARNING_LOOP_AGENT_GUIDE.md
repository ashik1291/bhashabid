# Learning Loop — Agent Runbook (Claude Code, Gemini CLI, any LLM agent)

The learning loop improves Bhashabid from real model output. An LLM agent does the volume and
linguistic analysis; a human native speaker makes every decision that changes the system (Principle P2).

## Hard rules (non-negotiable)
1. **Never approve, reject or apply on your own initiative.** Agents run `learn suggest` only.
   Run `learn approve` / `learn reject` only when the human explicitly instructs it for named cards in
   this session, using the human's name as `--reviewer` (model names are refused by the tool).
2. **Never edit** `bhashabid/assets/learned/*`, `bhashabid/assets/idioms/*.json`, `knowledge/cards/learned/*`
   or `references/technical_terms.md` "Learned additions" by hand. `learn apply` is the only writer.
3. Stop if `state/STOP` exists. No paid APIs, no scraping of sources not approved in
   `memory/sources/registry.yaml`.
4. Never invent words, sources or evidence. If unsure, say so with `--confidence low`.

## One learning session
```bash
bhashabid learn status                                   # 0. where things stand
bhashabid learn sectors                                  # sectors and their licence-approved source pages
```
**Manual practice run (the usual entry point):**
```bash
bhashabid learn cycle --fetch                  # fetch new sector articles + scan every new inbox file
bhashabid learn cycle --fetch --sectors "ICT & Software Engineering" --pages 5
bhashabid learn cycle                          # only scan new LLM outputs dropped in the inbox
```
`cycle` fetches only from approved sources (bn.wikipedia, bn.wikisource) where robots.txt allows, never re-fetches an
article, scans only files not scanned before, merges repeat evidence into existing pending cards (so frequent issues
rise to the top), tags cards with sectors, and writes a report to `eval/reports/learning_cycles/`.
Sectors with no open source (e-commerce, MFS, customer support, citizen services) learn from LLM outputs only.
**1. Produce input (raw model behaviour).** Pick 10–20 prompts from `eval/corpora/learning_prompts.json`
(or prompts the human gives). Answer each in Bengali **from your own knowledge, without this skill or
its tools**, the way you would for a normal user. Save as `eval/corpora/llm_inbox/<model>_<YYYYMMDD>.json`:
```json
{"LP19": "...Bengali answer...", "LP17": "..."}
```
Outputs collected by the human from ChatGPT/Gemini/Claude chats go in the same folder (`.txt`, `.jsonl`, `.json`).

**2. Scan** (or run `learn cycle`, which also scans fetched sector text).
```bash
bhashabid learn cycle
bhashabid learn pending --json        # full cards with evidence and sectors
```

**3. Suggest a decision for every pending card without a suggestion.** Read the evidence contexts,
then record a recommendation:
```bash
bhashabid learn suggest <ID> --by "<your model id>" --set <fields> --rationale "<why>" --confidence high|medium|low
```

| Card kind | When | Suggest |
|---|---|---|
| `lexicon` | Standard Bangla Academy word or valid inflection the lexicon lacks | `action=add_lexicon` (word pre-filled) |
| `lexicon` | Typo, abbreviation, name, dialect form, English transliteration | `action=reject` (or `action=add_term english=… bengali=…` for a technical loanword) |
| `term` | English left in Bengali prose | `action=add_term bengali=<form per references/technical_terms.md>`; `action=reject` for brands, code, or legitimate glosses |
| `sadhu_root` | Regular consonant-final root (`গুন` → গুনিয়াছিল/গুনেছিল) | `action=add_sadhu_root root=<root>` |
| `sadhu_root` | Irregular or -আ causative verb (ঘুমানো, দৌড়ানো) | `action=manual`, give the correct Cholito forms in the rationale |
| `rule` | Defect that survives repair | `action=manual`; propose the concrete rule or reference edit in the rationale |

Any card can instead propose an idiom:
`--set action=add_idiom english="…" flawed_calque="<literal calque seen>" natural_bengali="…"`.

**4. Report to the human.** List each card: candidate, evidence count, your suggestion, confidence,
one-line rationale. Give the commands to accept:
```bash
bhashabid learn approve <ID> --reviewer "<Human Name>" --accept-suggestion
bhashabid learn reject  <ID> --reviewer "<Human Name>" --reason "<why>"
```
Stop and wait for the human.

**5. After the human approves**, apply and verify:
```bash
bhashabid learn apply                         # distills, logs regression cases, rebuilds skill bundles
python -m unittest discover -s eval/unit      # must stay green
python eval/benchmarks/engine_accuracy.py     # false positives on clean text must stay 0
```
Commit with the applied card IDs in the message. Do not push or tag unless asked.

## What gets learned where
| Approved action | Destination | Effect |
|---|---|---|
| `add_lexicon` | `bhashabid/assets/learned/lexicon_additions.txt` | Spellcheck/unknown-word detection accept the word |
| `add_sadhu_root` | `bhashabid/assets/learned/sadhu_roots.json` | Sadhu→Cholito converts every tense/person of the root |
| `add_idiom` | `bhashabid/assets/idioms/bilingual_idioms.json` (+ generated `references/idioms.md`) | Lint flags and repair fixes the calque; the skill shows the idiom |
| `add_term` | `references/technical_terms.md` → "Learned additions" | The skill guides models to the approved Bengali term |
| every action | `eval/gold/learned_cases.jsonl`, `knowledge/cards/learned/` | Audit trail and regression cases |
