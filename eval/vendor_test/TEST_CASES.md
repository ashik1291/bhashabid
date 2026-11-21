# Bhashabid manual multi-vendor test pack

37 frozen tasks. Checks are fixed in `tasks.py` before any result exists.

## How to run

1. Pick vendors (e.g. ChatGPT, Gemini). Same model tier for every condition of a vendor; write the exact model name down.
2. Each task in a **fresh chat**, two conditions:
   - `base`: paste `ready/Vxx__base.txt`.
   - `skill`: paste `ready/Vxx__skill.txt` (skill + the reference the routing table selects + the task).
   - `skillcore` (only if `skill` is too long to paste): `ready/Vxx__skillcore.txt` = SKILL.md + task, no reference. Record it as `<vendor>__skillcore.md`; never mix it with `skill` runs.
3. Copy only the model's final Bengali answer. Do not edit it.
4. Send the answer back in chat (or save `results/<vendor>__<condition>.md`, one `## Vxx` heading per task).
5. Do not tune the skill or rules while testing.

Tasks marked *(human only)* have no automatic check; they are for the native-speaker blind rating.

## Tasks

### V01 · numerals · Macroeconomics & Banking

```text
Write the amount 2500000 taka in Bengali digits using South Asian lakh/crore comma grouping, then in Bengali words.
```

### V02 · numerals · Macroeconomics & Banking

```text
Write the number 123456789 in Bengali digits using South Asian lakh/crore comma grouping, then in Bengali words.
```

### V03 · numerals · Education & NCTB Pedagogy

```text
Give the Bengali ordinal words (as full words, not digits) for 1st, 2nd, 3rd, 4th, 5th and 10th.
```

### V04 · numerals · Education & NCTB Pedagogy

```text
Write the decimal 3.75 in Bengali words, as it would be read aloud.
```

### V05 · numerals · Culinary & Daily Life

```text
Write in Bengali: "Add 3.5 cups of rice and cook for 4.5 hours." Use natural Bengali words for the fractional amounts.
```

### V06 · dates · Mass Media & Digital Journalism

```text
In Bengali, write the date 21 February 2026 (Gregorian; Bengali digits, Bengali month name) and say it is International Mother Language Day.
```

### V07 · dates · Citizen Digital Services & Smart Governance

```text
Pohela Boishakh 1433 falls on 14 April 2026. In Bengali, state the Bengali-calendar date of 15 April 2026, using Bengali digits.
```

### V08 · dates · Customer Support & Conversational Chat

```text
Write the times 3:45 PM and 2:30 PM the way they are spoken in natural Bengali.
```

### V09 · dates · Mass Media & Digital Journalism

```text
Write the date 16 December 2026 in Bengali (Bengali digits, Bengali month name) and say it is Victory Day (Bijoy Dibosh).
```

### V10 · calque · Translation & Calque Naturalization

```text
Translate into natural Bengali newspaper prose: "The report was prepared by the committee and is characterised by delays."
```

### V11 · calque · Translation & Calque Naturalization

```text
Translate into natural Bengali: "It was raining cats and dogs, so the match was called off."
```

### V12 · calque · Translation & Calque Naturalization

```text
Translate into natural Bengali: "He kicked the bucket last year."
```

### V13 · calque · Sports Journalism

```text
Write a 2-sentence Bengali cricket report: Bangladesh lost to India by 5 wickets. Use Bengali digits.
```

### V14 · calque · Macroeconomics & Banking

```text
Write a 2-sentence Bengali news line: inflation rose to 9.5 percent in October, mainly driven by food prices. Use Bengali digits.
```

### V15 · sadhu_cholito · Literary & Language

```text
Rewrite in standard modern Cholito Bengali: "সে গৃহে গমন করিয়া ভোজন করিল এবং নিদ্রা গেল।"
```

### V16 · sadhu_cholito · Literary & Language

```text
Rewrite in standard modern Cholito Bengali: "তিনি বলিলেন যে আমি আসিব না।"
```

### V17 · sadhu_cholito · Literary & Language

```text
Rewrite in consistent Sadhu bhasha (no Cholito forms): "সে বাড়ি গিয়ে ভাত খেল এবং ঘুমাল।"
```

### V18 · register · Customer Support & Conversational Chat

```text
Write 2 Bengali sentences to a customer (address them as আপনি) saying refund REF-7781 will arrive within 3 working days. Use Bengali digits for the number of days.
```

### V19 · register · Creative Fiction & Dialogue

```text
Write a 4-line Bengali dialogue: a 14-year-old boy first talks to his best friend using তুই, then to his headmaster using আপনি.
```

### V20 · register · Education & NCTB Pedagogy

```text
Write 4 Bengali sentences about a respected teacher who retired after 30 years, referring to the teacher with the honorific তিনি throughout (never সে).
```

### V21 · official · Administrative Governance & Memos

```text
Write a short formal Bengali leave application to a school headmaster for 3 days of sick leave, in standard Bangladeshi application format.
```

### V22 · official · Administrative Governance & Memos *(human only)*

```text
Write the opening two lines of an official Bangladesh government memo conveying approval of a development project. Use standard Bangladeshi secretariat wording.
```

### V23 · official · Constitutional Law & Writs

```text
In Bengali, write how a High Court Division bench issues a Rule Nisi asking why a government order should not be declared illegal.
```

### V24 · official · Land Conveyancing & Deeds

```text
Write in Bengali the standard operative clause of a sale deed stating that the seller transfers a plot of land to the buyer for 500000 taka. Use Bengali digits with lakh grouping.
```

### V25 · official · Healthcare & Epidemiology

```text
Write Bengali patient instructions: take 1 tablet of 250 mg three times a day after meals for 5 days. Use Bengali digits.
```

### V26 · orthography · Education & NCTB Pedagogy

```text
Write one natural Bengali sentence that contains the words: station, post office and bird.
```

### V27 · orthography · Mass Media & Digital Journalism

```text
Write 3 Bengali sentences about the monsoon in Bangladesh.
```

### V28 · convention · Technology & Corporate *(project convention)*

```text
Explain in 3 Bengali sentences what a database and machine learning are.
```

### V29 · convention · Citizen Digital Services & Smart Governance *(project convention)*

```text
In Bangladeshi standard Bengali, politely ask a stranger for a glass of water.
```

### V30 · poetry · Classical Poetry & Prosody

```text
Write 2 Bengali lines about the Meghna river in Payar metre: exactly 14 akshar (syllables) per line, split 8+6. Output only the two lines.
```

### V31 · long_news · Macroeconomics & Banking

```text
Write a Bengali news report of 200-250 words for a Bangladeshi daily using these facts: (1) Bangladesh Bank raised the policy rate by 50 basis points to 10 percent. (2) Inflation was 10.87 percent in October, up from 9.92 percent in September. (3) Total loan disbursement this quarter was 1234567890 taka. (4) On Tuesday 17 November 2026 the Executive Committee of the National Economic Council (ECNEC), chaired by the Chief Adviser, approved 10 projects costing 8425.51 crore taka. Use Bengali digits, lakh/crore comma grouping for full amounts, the word শতাংশ instead of the % sign, and standard newspaper Cholito. Output only the report.
```

### V32 · bangabda · Citizen Digital Services & Smart Governance

```text
Convert each Gregorian date to the Bangladesh Bengali-calendar (Bangabda) date, written with Bengali digits and the Bengali month name, one per line: 14 April 2026; 21 February 2026; 15 November 2026; 17 November 2026; 16 December 2026.
```

### V33 · amounts · Macroeconomics & Banking

```text
For each amount, write it in Bengali digits with lakh/crore grouping, then in Bengali words followed by টাকা, one per line: 1050; 100000; 2500000; 10000000; 123456789.50; 7005003.
```

### V34 · sadhu_long · Literary & Language

```text
Write a Bengali short story of at least 150 words about an old ferryman on the river Padma, entirely in consistent Sadhu bhasha (সাধু ভাষা). Use no Cholito verb or pronoun forms anywhere. Output only the story.
```

### V35 · payar4 · Classical Poetry & Prosody

```text
Write exactly 4 lines of Bengali verse about the monsoon in Payar metre: every line has 14 akshar split 8+6, rhyming in couplets (AABB). Output only the four lines.
```

### V36 · legal_long · Constitutional Law & Writs

```text
Draft in Bengali the operative prayer of an Article 102 writ petition asking the High Court Division to declare a municipal demolition order illegal, with separate prayer clauses (ক), (খ), (গ) and (ঘ), following Bangladesh writ practice.
```

### V37 · sadhu2cholito_long · Literary & Language

```text
Rewrite the following passage entirely in standard modern Cholito Bengali, keeping the meaning and the quoted dialogue. Output only the rewritten passage.

একদা এক গ্রামে এক বৃদ্ধ কৃষক বাস করিত। প্রত্যহ প্রভাতে সে ক্ষেত্রে গমন করিয়া হলকর্ষণ করিত এবং সন্ধ্যায় গৃহে ফিরিয়া আসিত। তাহার পুত্র নগরে বিদ্যাশিক্ষা করিতেছিল। একদিন বৃদ্ধ শুনিল যে তাহার পুত্র পরীক্ষায় উত্তীর্ণ হইয়াছে। আনন্দে সে মিষ্টান্ন ক্রয় করিয়া প্রতিবেশীদিগকে বিতরণ করিল। প্রতিবেশীগণ বলিল, "তোমার পুত্র একদিন বড় মানুষ হইবে।" বৃদ্ধ হাসিয়া কহিল, "আমি কেবল চাহি, সে যেন সৎ থাকে।"
```
