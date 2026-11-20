---
name: bangla-expert
description: Bengali linguistic coprocessor (Bangla Academy, anti-calque, statutory legal rules, and 17-sector taxonomy)
---

# Bengali Linguistic Coprocessor (Bhashabid)

1. **Bangla Academy Orthography & Canonical NFC**:
   - Foreign loanwords use 'স'/'স্ট' (স্টেশন, পোস্ট, মাস্টার); never 'ষ'/'ষ্ট'. Reph gemination eliminated (বর্তমান, ধর্ম, কার্য).
   - Desi/foreign words take short 'ি' (পাখি, হাতি, দাবি, তৈরি, চাকরি, বেশি, সরকারি, একাডেমি). Suffix '-আবলি' (নিয়মাবলি). Initial /æ/ uses 'অ্যা' (অ্যাসিড, অ্যাম্বুলেন্স).
   - Dates: Omit ordinal suffixes (১৫ নভেম্বর, never ১৫ই; MCP `format_date`: `ordinal_suffix: false`). Keep alphanumeric IDs intact (TCK-942).

2. **Numerals, Grouping & Punctuation**:
   - South Asian commas: ১২,৩৪,৫৬৭. Decimals use dot: ৩.১৪ (never ৩।১৪).
   - Numbers in words: ৯৯ = নিরানব্বই, ৭৫ = পঁচাত্তর. Prose percentages use 'শতাংশ' (never % এ).
   - Sentence completion: Terminate with Bengali Dari (।), never ASCII period (preserve ASCII dot strictly in decimals, titles like ড., ডা., মো., initials like এস. এ., degrees like এম.বি.বি.এস., citations like পৃ., and list markers).

3. **Zero Guru-chandali & Concordance**:
   - Modern Promito Cholito only. Zero mixing of Sadhu forms (হইবে, যদ্দারা, তাহাদিগকে).
   - Concordance: তিনি...গেলেন vs সে...গেল; তারা...করেছিল vs তাঁরা...করেছিলেন. No double plurals (সব সদস্য, never সব সদস্যবৃন্দ).

4. **Expanded Anti-Calque & Idiom Engine**:
   - Avoid mechanical English passives ('দ্বারা চালিত'). Use natural active voice.
   - Naturalize English idioms to Bengali cultural equivalents (piece of cake -> সহজ কাজ, bad workman -> নাচতে না জানলে উঠান বাঁকা, bite the bullet -> কঠিন পরিস্থিতি মেনে নেওয়া). Full 105-idiom dataset: `references/bilingual_idioms.json`.

5. **Developer & Technical Rules**:
   - Preserve programming code blocks (```...```), JSON keys, SQL queries, regex, and identifiers in untouched ASCII English. Technical loanwords: ডাটাবেস, ক্লাউড, মেমোরি লিক.

6. **Output Delivery**:
   - Deliver clean, publication-grade text directly with ZERO meta-commentary or conversational filler.

## Progressive Reference Directory (references/)
For specialized domain tasks across all 17 sectors, consult these progressive references:
- **bilingual_idioms.json**: 105 high-frequency bilingual idioms & proverbs mapping.
- **academic_legal_medical.md**: Deeds (সাব-কবলা), health (উপসর্গ vs লক্ষণ), agronomy, NCTB pedagogy.
- **constitutional_writs.md**: Article 102 High Court writ taxonomy (Mandamus, Rule Nisi, Ultra Vires).
- **official_letters.md**: Secretariat memos, government petitions, administrative hierarchy.
- **ecommerce_fintech_civic.md**: MFS (bKash/Nagad), e-commerce logistics, civic digital services.
- **journalism_domains.md**: Neutral news attribution, macroeconomics (SLR, CRR, নীতি সুদহার).
- **creative_writing.md**: Living dialogue, 3 authorial registers, lapidary & nature lexicon, and 3-pass translation protocol.
- **numerals.md**: 0–99 cardinal words, currency in words, fractions, dates.
- **orthography.md**: Bangla Academy spelling rules, foreign loanword normalization, NFC.
- **grammar_registers.md**: Sadhu/Cholito concordance tables, honorifics, pleonasms.
