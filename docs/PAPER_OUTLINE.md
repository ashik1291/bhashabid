# Paper outline (draft; no result numbers until real data exists)

Status: skeleton only. Every `TBD` below needs data from `eval/vendor_test/`, `eval/heldout/` and `eval/reports/fp_audit_*`.

## Working title
Bhashabid: A Deterministic Rule-Based Coprocessor and Human-Approved Rule-Growth Loop for Bengali LLM Output

## Claim (deliberately narrow)
A small offline rule engine plus a compact skill/MCP interface reduces specific, checkable defect classes (numeral/date formatting, Guru-Chandali mixing, honorific clashes, English calques, Unicode/orthography) in Bengali LLM output, at low token cost, and a human-approved loop can extend the rules. We do **not** claim general Bengali quality gains, autonomous learning, or neuro-symbolic training.

## Venue fit
Resource / tool / demo track (BLP workshop, LREC-COLING, EMNLP/ACL demo), or a software journal. Not a main-track modelling paper.

## Sections
1. Introduction: LLM Bengali failure modes (cite own measured baseline rates: TBD).
2. Related work: Bengali spell/grammar tools, BanglaBERT-style models, tool-augmented LLMs, linguistic linters. Baselines to run: TBD.
3. System: engine (normalize, lint, repair, numbers, dates, prosody), skill bundle, MCP server, offline/pip/web-skill delivery.
4. Rule-growth loop: collect -> detect -> draft card -> native-speaker approval -> apply. State plainly that it is human curation with tooling.
5. Evaluation
   - 5.1 Held-out set: annotators, agreement (kappa), frozen hash. TBD
   - 5.2 Multi-vendor study: vendors x {base, skill, tools, +repair}; core pass rate with Wilson CI; McNemar paired tests; blind native-speaker ratings. TBD
   - 5.3 False-positive audit on native text (`eval/benchmarks/fp_audit.py`; triaged sample). TBD
   - 5.4 Learning curve on held-out set (`heldout_curve.py`), before/after N approved corrections. TBD
   - 5.5 Ablation: skill text vs tools vs repair.
6. Error analysis and bugs found by the audit (e.g. auto-repair rewriting proper nouns, fixed in v1.2.1): report honestly.
7. Threats to validity
   - Rules and gold set authored by the same party; mitigated only by the independent held-out set.
   - Task checks written by an LLM that knew the engine.
   - Manual vendor runs: model-version drift, prompt sensitivity, small n (30 tasks).
   - Some checks encode Bangladesh-standard/project conventions (reported separately).
   - Wikipedia text presumed clean may contain real errors.
8. Limitations and ethics: not a replacement for native review; dialect and West-Bengal usage; licences of sources.
9. Release: code, held-out set (if annotators agree), vendor prompts and raw outputs.

## Do not write until
- Held-out set frozen and annotated by 2+ native speakers.
- Vendor results collected and scored.
- FP audit triaged by a native speaker.

## Engine gaps found during vendor testing (log)
- Misspelling `মুসলধারে` (correct `মুষলধারে`, produced by Gemini base on V11) is not flagged by lint or the lexicon audit.
- Skill-condition regression on V04: ChatGPT read 3.75 as `সাড়ে তিন দশমিক সাত পাঁচ` (over-applied the `সাড়ে` rule). Candidate fix after the runs: clarify in SKILL.md that `সাড়ে` is only for .5.
- Engine false positive: consistent Sadhu sentence `সে গৃহে গমন করিয়া অন্ন ভোজন করিল এবং নিদ্রা গেল` is flagged RULE-LINT-GURU-CHANDALI (`গেল`/`সে` treated as Cholito markers). Fix after the vendor runs; until then engine-defect counts on Sadhu answers (V17) are inflated.
- Repair rewrote the correct numeral `ঊননব্বই` to `উননব্বই` (found when scoring V02; pre-existing at HEAD). Fixed: initial ঈ/ঊ removed from auto-repair swaps.
