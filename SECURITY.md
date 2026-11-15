# Security Policy & Vulnerability Disclosure

## 🛡️ Security Overview & Architecture

Bhashabid (ভাষাবিদ) is engineered as a deterministic, offline-first linguistic coprocessor engine. It is designed from the ground up with a strict security boundary:

1. **Zero-LLM Purity & Zero Phone-Home**:
   - The core runtime engine (`bhashabid`) contains **zero external network calls**, zero telemetry, and zero third-party model dependencies.
   - Text processed through Bhashabid is evaluated entirely in-memory and never leaves the host machine.
2. **Pure Python AST Invariance**:
   - The engine strictly prohibits dynamic evaluation (`eval()`, `exec()`, `compile()`).
   - All normalization, spellchecking, prosody scansion, and linting rules are deterministic state machines and pre-compiled regex automata.
3. **Model Context Protocol (MCP) Boundary Protection**:
   - The bundled MCP server (`bhashabid-mcp`) implements strict input validation and type sanitization, isolating the host environment against command injection, format string exploits, and buffer overflows.
4. **Supply Chain Integrity & Provenance (Principle P2)**:
   - All production knowledge cards undergo cryptographically signed human review (`sha256` signatures).
   - PyPI release builds utilize GitHub Actions OpenID Connect (OIDC) with Sigstore cryptographic provenance attestations (PEP 740).

---

## 📋 Supported Versions

We provide active security patches and vulnerability audits for the following versions:

| Version | Supported          | Security Scan Status |
| :------ | :----------------- | :------------------- |
| `1.0.x` | :white_check_mark: | Active (Bandit 0-vuln, pip-audit clean) |
| `< 1.0` | :x:                | Deprecated           |

---

## 🔍 Continuous Security Scans

The repository maintains an automated multi-layer security audit suite:

1. **Static Application Security Testing (SAST)**:
   - Automated `bandit` AST analysis across all library and tooling files.
   - Configured to reject any `Medium` or `High` severity findings.
2. **Software Composition Analysis (SCA)**:
   - `pip-audit` checks against the PyPA Advisory Database and Google OSV.dev.
   - Core runtime dependencies are strictly minimal (`pyyaml >= 6.0`).
3. **Automated Regression Suite**:
   - `eval/unit/test_security_posture.py` enforces AST purity, MCP input injection resistance, and offline execution invariants.

---

## 🚨 Reporting a Vulnerability

We deeply appreciate the efforts of security researchers in keeping open-source linguistic infrastructure safe.

If you identify a security vulnerability, please report it responsibly:

1. **GitHub Private Security Advisory (Preferred)**:
   - Navigate to the [Security Advisories](https://github.com/ashik1291/bhashabid/security/advisories) tab of the repository and click **"New draft advisory"**.
2. **Direct Contact**:
   - Maintainer: **Ashikur Rahman Bhuiyan** ([@ashik1291](https://github.com/ashik1291))
   - Subject: `[SECURITY] Bhashabid Vulnerability Report: <Brief Description>`

### Disclosure Guidelines
- Please provide detailed reproduction steps or a minimal proof-of-concept (PoC).
- Do not disclose security vulnerabilities publicly on GitHub issues or social media until a coordinated fix and CVE have been issued.
- We aim to acknowledge receipt of vulnerability reports within 48 hours and release patches within 7 business days for verified critical vulnerabilities.
