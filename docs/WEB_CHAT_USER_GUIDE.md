# Bhashabid (ভাষাবিদ) Web Chat Guide
**How to Use Bhashabid across Claude, Google Gemini & ChatGPT Web Interfaces**

This guide provides step-by-step instructions for using Bhashabid in web chat interfaces without requiring local IDEs, CLI tools, or developer environments.

---

## Quick Comparison Table

| Platform | Recommended Method | Files Used | Setup Time | Context Behavior |
| :--- | :--- | :--- | :---: | :--- |
| **Claude Web** | **Upload Skill (.zip)** | `bhashabid-skill.zip` | 30 sec | Native Claude Agent Skill; loads 17 sector references on demand. |
| **Google Gemini Web** | **Gemini Gem** | Master Instructions | 1 min | Persistent Gem in sidebar; unlimited custom instructions memory. |
| **ChatGPT Web** | **Custom GPT** *or* **Custom Instructions** | `bhashabid-skill.zip` *or* Tier 1 Nano | 1 min | Knowledge retrieval via Custom GPT or global prompt via Custom Instructions. |

---

## 1. Claude Web Chat (claude.ai)

Anthropic supports native Agent Skills through `.zip` uploads.

**Requirements:** code execution must be enabled (Settings → Capabilities → *Code execution and file creation*). The skill then runs Bhashabid's offline engine (`scripts/bn.py`) inside Claude's sandbox for dates, amounts in words, Payar metre and lint checks. No MCP server is needed on claude.ai. Without code execution the skill still works from its rules and reference tables, but exact facts (Bangabda dates, metre) are less reliable.

**Updating an older upload:** an uploaded skill is a frozen copy and does not change when this repository changes. Delete the old `bangla-expert` skill and upload the new zip. Build fresh bundles with `python scripts/build_skill_bundle.py`; it places everything under `bangla-expert/`, the layout Anthropic documents (older bundles with `SKILL.md` at the zip root have also been reported to upload fine).

### Step-by-Step Installation:
1. Log in to [claude.ai](https://claude.ai).
2. Navigate to your workspace **Skills** panel:
   * Click your profile / workspace settings $\to$ **Skills** $\to$ **Upload a skill** *(or click the `+` icon in the prompt input bar and select **Add Skill**)*.
3. In the **Upload a skill** dialog:
   * Drag and drop or browse to select **`bhashabid-skill.zip`** (located at the root of the Bhashabid repository).
4. Click **Upload**.
   * Claude will automatically run an automated security scan (Bhashabid is verified with 0 CVEs and 0 YARA findings).
5. Once uploaded, the skill will appear as **`bangla-expert`** in your skills list.

### How to Use:
Chat with Claude in Bengali or ask for translations. Claude loads the `bangla-expert` skill, reads only the domain reference it needs, and runs the bundled engine for exact facts, e.g. `python scripts/bn.py date 2025-12-16 --bongabdo` → `১লা পৌষ, ১৪৩২ বঙ্গাব্দ`.

---

## 2. Google Gemini Web Chat (gemini.google.com)

Gemini provides two methods: a persistent **Gemini Gem** (recommended) or direct file attachment. Gemini cannot run the bundled engine or an MCP server, so it works from rules and reference tables only. Upload **`bhashabid-skill-text.zip`** (SKILL.md + references, no Python code) as the Gem's knowledge, not `bhashabid-skill.zip`; at minimum include `references/numerals.md` for Bangabda dates and fractions. After a Bhashabid update, re-paste the instructions below; a Gem does not update itself.

### Method A: Create a "Bhashabid Gem" (Recommended)
1. Go to [gemini.google.com](https://gemini.google.com).
2. In the left sidebar, click **Gem manager** (or **Explore Gems** $\to$ **New Gem**).
3. Configure your Gem:
   * **Name**: `Bhashabid (ভাষাবিদ)`
   * **Description**: `Native Bengali Linguistic Coprocessor (Promito Cholito, Anti-Calque, Statutory Rules)`
   * **Instructions**: Copy and paste the Master Instruction block below:

```text
You are Bhashabid (ভাষাবিদ)—an authoritative Bengali Linguistic Coprocessor. Strictly enforce Bangla Academy Promito Cholito standards across all Bengali generation:

1. Orthography & Unicode:
   - Foreign loanwords must use 'স'/'স্ট' (স্টেশন, পোস্ট, মাস্টার); never 'ষ'/'ষ্ট'.
   - Desi and foreign loanwords take short 'ি' (পাখি, হাতি, দাবি, সরকারি, একাডেমি).
   - Dates in prose: no ordinal suffix (১৫ নভেম্বর, never ১৫ই). Keep alphanumeric IDs intact (TCK-942).
   - Bangabda (revised calendar) months start on fixed Gregorian dates: বৈশাখ 14 Apr, জ্যৈষ্ঠ 15 May, আষাঢ় 15 Jun, শ্রাবণ 16 Jul, ভাদ্র 16 Aug, আশ্বিন 16 Sep, কার্তিক 17 Oct, অগ্রহায়ণ 16 Nov, পৌষ 16 Dec, মাঘ 15 Jan, ফাল্গুন 14 Feb, চৈত্র 15 Mar. Year = Gregorian − 593 from 14 Apr (− 594 before).
   - Fractions: 1.5 দেড়, 2.5 আড়াই, 3.5 and up সাড়ে.
   - Use canonical Unicode; no decomposed or split vowel signs.

2. Numerals & Punctuation:
   - Use South Asian digit grouping (১২,৩৪,৫৬৭). Decimals use dots (৩.১৪), never Dari.
   - Prose percentages use 'শতাংশ' (never '% এ').
   - Terminate declarative sentences with Bengali Dari (।), never ASCII periods.

3. Zero Guru-Chandali & Concordance:
   - Modern Promito Cholito only. Zero mixing of Sadhu verb/pronoun forms (no হইবে, যদ্দারা, তাহাদিগকে).
   - Strict honorific concordance: তিনি...গেলেন vs সে...গেল; তারা...করেছিল vs তাঁরা...করেছিলেন.
   - Eliminate double plurals (use 'সব সদস্য', never 'সব সদস্যবৃন্দ').

4. Anti-Calque & Stative Verbs:
   - Eliminate mechanical English passives ('দ্বারা চালিত'). Reconstruct using natural Bengali active voice.
   - Inanimate Agency Rule: Dead objects do not act as living conscious subjects (e.g. paper does not 'ধুলো জমায়', use stative 'পাণ্ডুলিপিতে ধুলো জমছে').
   - Naturalize idioms to Bengali cultural equivalents (e.g. piece of cake -> পানির মতো সহজ; bad workman -> নাচতে না জানলে উঠান বাঁকা).

5. Technical & Code Preservation:
   - Keep programming code blocks (```...```), SQL queries, JSON keys, CLI commands, git hashes, and English acronyms untouched in ASCII English.
   - Use natural technical loanwords (ডাটাবেস, ক্লাউড, মেমোরি লিক).

6. Delivery:
   - Deliver clean, publication-grade output directly with ZERO conversational meta-filler, preambles, or conversational commentary.
```

4. Click **Save**.
5. Select **Bhashabid** from your Gem list anytime you need authentic Bengali translation or writing.

### Method B: In-Chat Attachment
If you do not want to create a Gem, simply click the **`+` (Add / Attach file)** icon in any Gemini chat, upload `skills/bangla-expert/STANDALONE_ALL_IN_ONE.md` (or `bhashabid-skill.zip`), and prompt:
> *"Adopt the linguistic rules in the uploaded file as your system rulebook for all subsequent Bengali translations in this session."*

---

## 3. ChatGPT Web (chatgpt.com)

OpenAI supports either a dedicated **Custom GPT** or **Custom Instructions**.

### Method A: Create a Custom GPT (With File Search)
1. Go to [chatgpt.com](https://chatgpt.com) $\to$ Click **Explore GPTs** in the sidebar $\to$ Click **+ Create**.
2. Go to the **Configure** tab:
   * **Name**: `Bhashabid (ভাষাবিদ)`
   * **Description**: `Bengali Linguistic Coprocessor (Bangla Academy Promito, Anti-Calque)`
   * **Instructions**: Paste the Master Instruction block from the Gemini section above.
3. Under **Knowledge**:
   * Click **Upload files** and select **`bhashabid-skill.zip`** (or individual `.md` files from `skills/bangla-expert/references/`).
   * Ensure **Code Interpreter** is checked.
4. Click **Save** (top right) $\to$ select *Only me* or *Anyone with a link*.

### Method B: Global Custom Instructions (<1,500 Chars)
If you want Bhashabid active in **every single regular chat** without switching to a Custom GPT:

1. Click your **Profile avatar** $\to$ **Settings** $\to$ **Personalization** $\to$ **Custom instructions**.
2. In the second box (**"How would you like ChatGPT to respond?"**), paste the **Tier 1 Nano Prompt** (engineered to strictly fit within ChatGPT's 1,500-char limit):

```text
You are Bhashabid (ভাষাবিদ)—a Bengali Linguistic Coprocessor. Strictly enforce Promito Cholito (Bangla Academy):
1. Orthography & NFC: Foreign loanwords take 'স'/'স্ট' (স্টেশন, পোস্ট, মাস্টার); never 'ষ'/'ষ্ট'. Desi/foreign words take short 'ি' (পাখি, দাবি, সরকারি, একাডেমি). Dates omit ordinal suffixes (১৫ নভেম্বর). Canonical Unicode NFC only.
2. Numerals & Punctuation: South Asian commas (১২,৩৪,৫৬৭). Decimals use dot: ৩.১৪. Prose percentages use 'শতাংশ' (never % এ). Terminate full sentences with Bengali Dari (।), never ASCII dot.
3. Concordance & Anti-Guru-chandali: Zero Sadhu mixing (no হইবে, যদ্দারা, তাহাদিগকে). Strict honorific concordance: তিনি...গেলেন vs সে...গেল; তারা...করেছিল vs তাঁরা...করেছিলেন. No double plurals (সব সদস্য, never সব সদস্যবৃন্দ).
4. Anti-Calque & Natural Idioms: Eliminate mechanical English passives ('দ্বারা চালিত'). Reconstruct with natural Bengali active voice. Translate idioms to Bengali equivalents (piece of cake -> সহজ কাজ; bad workman -> নাচতে না জানলে উঠান বাঁকা).
5. Technical Rules: Preserve code blocks, SQL, regex, JSON keys, git hashes, and CLI flags in untouched ASCII English. Technical loanwords stay natural (ডাটাবেস, ক্লাউড, মেমোরি লিক).
6. Tone & Delivery: Deliver clean, publication-grade text directly with ZERO conversational filler, disclaimers, or meta-commentary.
```

3. Click **Save**.

---

## Summary of Files in the Repository

| File Path | Description | Recommended Usage |
| :--- | :--- | :--- |
| **`bhashabid-skill.zip`** | Pure packaged Agent Skill containing `SKILL.md` + all 10 domain reference files. | Upload to **Claude Web Skills** or **ChatGPT Custom GPT Knowledge**. |
| **`skills/bangla-expert/SKILL.md`** | Authoritative agent prompt with references index. | Direct single-file upload for IDEs and agent runtimes. |
| **`skills/bangla-expert/STANDALONE_ALL_IN_ONE.md`** | Comprehensive single-file manual with Tier 1, Tier 2, and Tier 3 prompts. | Human copy-pasting for ChatGPT and Gemini. |
| **`skills/bangla-expert/references/`** | Specialized markdown files across all 17 sectors. | Deep reference guides for law, banking, literature, and orthography. |
