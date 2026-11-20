---
name: bangla-expert
description: Standard Bangladeshi Bengali (Bangla Academy) writing, translation and checking. Orthography, Sadhu/Cholito register, honorific agreement, lakh/crore numbers and taka in words, Bangabda dates, Payar metre, official letters and legal formats across 17 sectors. Use for any Bengali output.
---

# Bengali Writing (Bhashabid)

## 1. Exact facts come from tools, not memory
Use the first option available:
- **MCP tools** (`bhashabid` server): `convert_number`, `format_date`, `prosody_scan`, `lint_text`, `repair_text`, `generate_writ_prayer`, `generate_deed_clause`.
- **Code execution**: run this skill's engine, e.g. `python scripts/bn.py number 1234567.50 --currency`, `date 2025-12-16 --bongabdo`, `date 2026-11-15 --no-suffix`, `prosody "<line>" --verify-payar`, `lint "<text>"`, `repair "<text>"` (add `--to-cholito` to convert Sadhu text).
- **Neither**: use the rules below and the tables in `references/numerals.md`.

Always use a tool (or the tables) for Bangabda dates, amounts in words and Payar line counts. For long or formal text, run `lint` on the draft and fix every issue it reports.

## 2. Rules models commonly break
- One register per text: Cholito (করেছে, তার) or Sadhu (করিয়াছে, তাহার), never mixed. Agreement: আপনি করেন, তুমি করো, তুই করিস; তিনি গেলেন, সে গেল.
- No English-passive calques: not "X দ্বারা পরিচালিত/প্রভাবিত" but "X-এর নেতৃত্বে / X-এর কারণে". Translate idioms by meaning.
- Spelling: loanwords use স, not ষ (স্টেশন, পোস্ট); non-Sanskrit words take short ি (সরকারি, পাখি).
- Numbers: lakh/crore grouping ১২,৩৪,৫৬৭; prose percent "শতাংশ"; 1.5 দেড়, 2.5 আড়াই, 3.5 and up সাড়ে; keep IDs such as TCK-942 unchanged.
- End sentences with ।, but keep the dot in decimals, URLs and abbreviations (ড., মো.).
- Dates in news or official prose: ১৫ নভেম্বর (no ই/শে); Bengali-calendar dates keep ১লা বৈশাখ.
- Keep code, JSON keys and identifiers in English. Output only the requested text.

## 3. References (read only the one the task needs)
`official_letters.md` applications, memos · `constitutional_writs.md` Article 102 writs · `academic_legal_medical.md` deeds, health, agriculture, NCTB · `ecommerce_fintech_civic.md` MFS, e-commerce, civic services · `journalism_domains.md` news, banking · `creative_writing.md` fiction, poetry · `numerals.md` numbers, Bangabda dates, Payar counting · `orthography.md` spelling · `grammar_registers.md` register tables · `idioms.md` English idioms → natural Bengali.
