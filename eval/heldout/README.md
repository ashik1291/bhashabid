# Held-out set (to be written by native speakers)

Put the frozen set in `heldout.jsonl`, same schema as `eval/gold/engine_gold.jsonl`:
`{"id","label","sector","text"}` with label in `clean | guru_chandali | honorific | calque`.

Rules (these make the learning-curve and accuracy numbers valid):
1. Written by 2+ native speakers who have **not** seen the lint rules or the engine output. Record annotators and their agreement (Cohen's kappa) in `ANNOTATORS.md`.
2. Frozen before the first measurement. `heldout_curve.py` stores the file's SHA-256; a changed hash means a new, non-comparable curve.
3. Never use these items to write or approve rules, lexicon additions or replacements. Failures go to a *separate* dev set.
4. Aim for 300-500 items, balanced over the 17 sectors, including many clean sentences (for false-positive rate).
5. Run `python eval/benchmarks/heldout_curve.py --label "baseline"` first, then after every batch of `learn apply`.
