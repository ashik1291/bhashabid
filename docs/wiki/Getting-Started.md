# Getting Started with Bhashabid (ভাষাবিদ)

Bhashabid can be installed and used in multiple workflows depending on your environment.

---

## 1. Quick Installation (Python >= 3.10)

### Official Release via PyPI (Recommended)
```bash
pip install bhashabid
```

### Developer Mode (From Source)
```bash
# Clone the repository
git clone https://github.com/ashik1291/bhashabid.git
cd bhashabid

# Install locally in editable mode
pip install -e .
```

---

## 2. Command Line Interface (CLI)

The `bhashabid` executable provides instant terminal access to all linguistic engines:

### Install Skill with all References in 1 Command
```bash
# Automatically install SKILL.md and all 8 reference guides to Antigravity, Claude, or Cursor
bhashabid install-skill --target all
```

### In-Place File Repair & Diff
```bash
# Preview changes with unified color diff
bhashabid repair article.txt --diff

# Safe in-place file repair
bhashabid repair article.txt --write
```

### 78,000+ Word Offline Phonetic Spellchecker
```bash
bhashabid spellcheck "আবিস্কার"
# Output: Suggestions for 'আবিস্কার': ['আবিষ্কার']
```

### Numeral & Currency Conversion
```bash
bhashabid number 99
# Output: নিরানব্বই

bhashabid number 1234567 --format grouped
# Output: ১২,৩৪,৫৬৭

bhashabid number 55000.75 --format currency
# Output: পঞ্চান্ন হাজার টাকা পঁচাত্তর পয়সা
```

### Orthography Normalization
```bash
bhashabid normalize "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন."
# Output: ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।
```

### Real-Time Grammar & Calque Linting
```bash
bhashabid lint "তুমি সিদ্ধান্ত নেন এবং এটি বিদ্যুৎ দ্বারা চালিত."
```

### Poetic Prosody & Payar Verification
```bash
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar
# Output:
# পয়ার ছন্দ যাচাই: শুদ্ধ (VALID)
# পর্ব ১ (৮ মাত্রা): 8 | পর্ব ২ (৬ মাত্রা): 6 | মোট: 14
```

### High Court Writ Guidance
```bash
bhashabid writ --remedy "detention" --subject "জনাব করিম" --authority "স্বরাষ্ট্র সচিব"
```

### System Health & Installation Audit
```bash
# Check integration status across Cursor, Antigravity, and Claude
bhashabid status
```

### Knowledge Distillation & Skill Synchronization
```bash
# Re-compile approved cards, verify < 390 token budget, and sync globally
bhashabid distill
```

### Human Linguistic Review (Principle P2 Sign-Off)
```bash
# Approve a pending draft card from knowledge/cards/drafts/
bhashabid review --card CRD-DFT-001 --reviewer "Your Name" --affiliation "Native Speaker" --action approve
```

---

## 3. Python SDK Usage

```python
import bhashabid

# 1. 1-Liner Automatic Repair (Unicode NFC, Bangla Academy spelling & Dari)
repaired, diffs = bhashabid.repair("তিনি স্টেশন থেকে বাড়ি ফিরলেন.")
print(repaired)  # "তিনি স্টেশন থেকে বাড়ি ফিরলেন।"

# 2. 78,000+ Word Offline Phonetic Spellchecker (sub-10ms)
suggestions = bhashabid.spellcheck("আবিস্কার")
print(suggestions)  # ['আবিষ্কার']

# 3. Statutory South Asian Currency & Number Formatting
print(bhashabid.format_number("1234567.50"))        # "১২,৩৪,৫৬৭.৫০"
print(bhashabid.format_currency_words(1234567.50))  # "বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা মাত্র"

# 4. Static Grammar, Honorific & Calque Linter
issues = bhashabid.lint("তুমি সিদ্ধান্ত নেন")
for issue in issues:
    print(issue.message, "->", issue.suggestion)

# 5. Classical 14-Akshar Payar Verification (8+6)
is_valid, report = bhashabid.verify_payar("কাশীদাস কহে সাধু শুনে পুণ্যবান")
print(is_valid)  # True
```
