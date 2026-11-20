# Changelog

All notable changes to Bhashabid are documented here following Semantic Versioning.

## [1.1.1] - 2026-11-20
### Fixed
- **Abbreviation & Initials Protection**: Resolved period-to-Dari over-conversion. Protected titles (`ড.`, `ডা.`, `মো.`), name initials (`এস. এ.`, `টি. এস.`), academic degrees (`এম.বি.বি.এস.`, `পিএইচ.ডি.`), citations (`পৃ.`, `নং.`, `খ্রি.`), list markers (`১.`, `ক.`), and multi-dot IP addresses (`১৯২.১৬৮.১.১`) from Dari mutation.
- **Universal Reph Gemination (Rule 1.02)**: Generalized elimination of doubled consonants after Reph (`বর্ত্তমান` -> `বর্তমান`, `কর্ত্তব্য` -> `কর্তব্য`, `কীর্ত্তি` -> `কীর্তি`, `সর্ব্ব` -> `সর্ব`, `চর্চ্চা` -> `চর্চা`, `অর্দ্ধেক` -> `অর্ধেক`, `মূর্চ্ছা` -> `মূর্ছা`).
- **Initial Loanword /æ/ Standardization (Rule 2.01)**: Normalized obsolete initial `এ্যা` to standard `অ্যা` (`এ্যাসিড` -> `অ্যাসিড`, `এ্যাম্বুলেন্স` -> `অ্যাম্বুলেন্স`).
- **Sanskrit Suffix Shortening (Rule 1.01)**: Standardized `-আবলী` to `-াবলি` (`নিয়মাবলি`, `শর্তাবলি`, `রচনাবলি`, `তথ্যাবলি`).
- **Pleonasm & Concordance Expansion**: Unified double plural elimination across all combinations of `সব`/`সকল` + `গণ`/`বৃন্দ`/`সমূহ` and added `কেবলমাত্র` -> `কেবল` repair.
- **Unit & Regression Suite**: Expanded automated unit tests to 181 passing tests (100% green).

## [1.1.0] - 2026-11-19
### Added
- **First-Class Claude Code CLI MCP Support**: Automatic stdio tool registration and health checking in `~/.claude.json`.
- **Packaged Pure Agent Skill**: Built lean `bhashabid-skill.zip` and `bhashabid.skill` for direct upload to Claude Web and ChatGPT Custom GPTs.
- **Web Chat User Guide (`docs/WEB_CHAT_USER_GUIDE.md`)**: Full visual walkthrough for Claude Web, Google Gemini Web (Gems), and ChatGPT Web.
- **3 Production Creative Writing Meta-Invariants**: Codified Semantic Conservation & Scale Integrity, Modern Pop-Culture Entity Exemption, and Dignified Cognitive Metaphor Mapping into Sector 5 & 12.
- **Automated Tag-Based PyPI Deployment**: Added `push: tags: ['v*']` trigger to GitHub Actions PyPI Trusted Publishing workflow.
- **Test Suite Expansion**: 178 automated unit tests passing 100% green.

## [1.0.1] - 2026-11-15
### Added
- **Literary & Creative Mastery Framework**: Expanded 17-sector taxonomy and lapidary database.
- **Cross-Platform Visual Architecture Documentation**.

## [0.4.0] - 2026-11-11 - Cycle 4 Release
### Added
- Regional Dialect Profiles in `tools/bn_normalize/profiles.py` (`bd_standard` vs `wb_standard`).
- High-throughput streaming batch normalizer in `pipeline/03_process/batch_normalizer.py` (> 290,000 words/sec).
- Human Review Liaison packet generator (`tools/review_packet_generator.py`) and review queue packet (`docs/review_queue/packet_001_initial_cards.md`).
- Knowledge card `CRD-ORT-003` (Regional Orthographic Variations).
- Comprehensive test suite expansion (46 automated tests passing in 3.6s).

## [0.3.0] - 2026-11-11 - Cycle 3 Release
### Added
- Developer CLI `bhashabid` (`tools/cli.py`) with `number`, `normalize`, and `lint` subcommands.
- Standard distribution packaging via `pyproject.toml` (v0.3.0).
- IDE & Runtime Adapters: Cursor rules (`adapters/cursor/.cursorrules`) and Claude prompt (`adapters/claude/claude_system_prompt.txt`).
- Architecture Decision Records: ADR-001 (Progressive Skill Disclosure) and ADR-002 (Deterministic Bengali Token Boundaries).
- Cross-Model Benchmark Matrix (`eval/benchmarks/benchmark_matrix.py`) showing +90.0% net lift over raw baseline LLMs.
- Full traceability: All 40 initial requirements (REQ-001 through REQ-040) marked `IMPLEMENTED` with 41 passing automated tests.

## [0.2.0] - 2026-11-11 - Cycle 2 Release
### Added
- Static Linguistic Linter `tools/bn_lint` detecting Sadhu-Cholito mixing (Guru-chandali), honorific clashes, and English calques.
- Bidirectional honorific suggestion engine (`তুমি সিদ্ধান্ত নাও` vs `আপনি সিদ্ধান্ত নেন`).
- Model Context Protocol (MCP) server `tools/mcp_server/`.
- Knowledge cards for Case Markers (`CRD-GRM-003`), Sandhi (`CRD-GRM-004`), Samas (`CRD-GRM-005`), and Anti-Calques (`CRD-TRN-001`).
- Source verification and cleaning pipeline skeleton in `pipeline/`.

## [0.1.0] - 2026-11-11 - Cycle 1 Release
### Added
- Deterministic normalizer `tools/bn_normalize` (Unicode NFC, composite nukta precomposition, Dari punctuation, loanword orthography).
- Progressive skill architecture `skills/bangla-expert/SKILL.md` (< 600 tokens) with modular reference guides.
- Knowledge cards: `CRD-NUM-001`, `CRD-ORT-001`, `CRD-ORT-002`, `CRD-GRM-001`, `CRD-GRM-002`.
- Initial benchmark suite in `eval/benchmarks/run_cycle1_evals.py`.

## [0.0.1] - 2026-11-11 - Bootstrap
### Added
- Repository foundation, constitution, EARS requirements (REQ-001..040), 15 BMAD agent personas.
- Deterministic numeral engine `tools/bn_numbers` with 0-99 irregular lookup, lakh/crore formatting, ordinals, currency, and fractions.
- Mistake ledger `memory/mistakes/ledger.jsonl` and automated regression test runner.
