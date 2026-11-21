# Check change log (checks are otherwise frozen)

| date | task | change | why | seen outputs first? |
|---|---|---|---|---|
| 2026-11-21 | V01, V24 | `লাখ` -> `(লাখ\|লক্ষ)` | `লক্ষ` is a valid standard form of the same number word; the strict check wrongly failed correct answers. Applies equally to every condition. | yes (V01 base from ChatGPT and Gemini) |

Rule: a check may be widened to accept a valid variant, never narrowed, and every change is logged here. Report the original-strict and widened pass counts if they differ.
| 2026-11-21 | V04 | added `lacks(সাড়ে তিন দশমিক)` | Bug fix: the substring match passed ChatGPT-skill's wrong answer `সাড়ে তিন দশমিক সাত পাঁচ` (= 3.5.75). Narrowing, but corrects a false pass; applies to all conditions. | yes (V04 outputs) |
| 2026-11-21 | V17 | verbs `গিয়া`/`খাইল` widened to also accept `গমন করিয়া` and `ভোজন/আহার করিল` | Check was over-specific: consistent Sadhu with literary synonyms (as in the source sentence) is correct but failed. Applies to all conditions. | yes (V17 outputs) |
| 2026-11-21 | scorer | engine-defect metrics computed only on Bengali-dominant lines | English explanation lines produced false `ascii_period` hits (Gemini V08/V11). Metric only; task checks unchanged. | yes |
