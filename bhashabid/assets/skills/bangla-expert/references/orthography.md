# Bangla Academy Orthography & Technical Language Standards

## 1. Foreign Loanwords Rule (বিদেশি শব্দে 'ষ' বর্জন)
- Foreign words (English, Persian, Arabic, Portuguese) never use `ষ`. Use `স` or `শ`:
  - Correct: স্টেশন, পোস্ট, মাস্টার, আগস্ট, বাস, ক্লাস, পাসপোর্ট, ফটোস্ট্যাট
  - Incorrect: ষ্টেশন, পোষ্ট, মাষ্টার, আগষ্ট, বাষ, ক্লাষ, পাষপোর্ট, ফটোষ্ট্যাট
- Sanskrit / Tatsama words preserve retroflex `ষ` according to Natwa-Bidhan:
  - Correct: কষ্ট, সৃষ্টি, বৃষ্টি, নষ্ট, অনুষ্ঠান

## 2. Vowel Harmonization (হ্রস্ব-ইকার ও হ্রস্ব-উকার)
- Non-Sanskrit (tatbhava, desi, foreign loanwords) words always take short `ি` (হ্রস্ব-ইকার):
  - Correct: পাখি, হাতি, দাদি, নানি, শাড়ি, বাড়ি, গাড়ি, সরকারি, ইংরেজি, জাপানি, একাডেমি
  - Incorrect: পাখী, হাতী, দাদী, শাড়ী, সরকারী, ইংরেজী, একাডেমী
- Adjectives ending in `ঈ` take `ি` when nominalized with `-তা` or `-ত্ব`:
  - Correct: প্রতিদ্বন্দ্বী -> প্রতিদ্বন্দ্বিতা; স্থায়ী -> স্থায়িত্ব; সহযোগী -> সহযোগিতা

## 3. Unicode Canonicalization & Punctuation
- Ensure precomposed single characters for য় (U+09DF), ড় (U+09DC), and ঢ় (U+09DD) instead of base letter + nukta.
- Terminate Bengali declarative and imperative sentences with Dari (`।` U+0964), not English period (`.`).
- Preserve English periods inside web URLs (`bangladesh.gov.bd`), email addresses, and decimal numbers (`৩.১৪`).

## 4. Software Engineering & Technical Language Protocol
- **Strict Code Block & Identifier Preservation**:
  - Keep all fenced code blocks (` ```python `, ` ```javascript `, ` ```sql `, ` ```bash `) and inline backticks (`` `variable` ``) strictly in original ASCII English.
  - Never translate programming keywords (`def`, `class`, `import`, `return`, `SELECT`, `WHERE`), JSON schema keys, REST endpoints (`/api/v1/auth`), regex patterns, or Git commands.
- **Technical vocabulary** (Bengali vs. loanword, spelling, glossary): see `technical_terms.md`.

## 5. Alphanumeric IDs, Security CVEs & Number Grouping
- Preserve support ticket numbers, transactional hashes, Git commit SHAs, and security vulnerabilities untranslated:
  - Examples: `TCK-942`, `TRX-98214`, `CVE-2024-1234`, `commit 6eb943b`
- Format currency amounts and standalone large quantities using standard South Asian comma grouping:
  - Correct: ১২,৩৪,৫৬৭ টাকা (or 12,34,567 taka)
  - Decimals use dot: ৩.১৪ শতাংশ (never ৩।১৪)

## 6. Homophone & Chandrabindu Disambiguation (সমোচ্চারিত শব্দ ও চন্দ্রবিন্দু)
- **কাচ বনাম কাঁচা**:
  - `কাচ` (Glass, কাচের টুকরো, কাচপাত্র, আতশ কাচ — বাংলা একাডেমি নিয়মে চন্দ্রবিন্দু সম্পূর্ণ বর্জনীয়)।
  - `কাঁচা` (Unripe/Raw, কাঁচা আম, কাঁচকলা, কাঁচা রাস্তা — চন্দ্রবিন্দুযুক্ত)।
