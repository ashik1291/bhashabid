# tools/learning_loop.py
# Semi-autonomous learning loop: ingest real text -> detect what the engine cannot decide ->
# draft evidence cards -> human approval (P2) -> distill approved knowledge into engine + skill.
import glob
import hashlib
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from bhashabid.lint import lint_text
from bhashabid.lint.guru_chandali import convert_to_cholito, is_cholito_token
from bhashabid.lint.sadhu_paradigm import SADHU_FORMS
from bhashabid.normalize.lexicon import get_default_lexicon
from bhashabid.normalize.repair import repair_text
from bhashabid.normalize.unicode import canonicalize_unicode

BN_WORD = re.compile(r"[ঀ-৥ৰ-৿]{2,}")  # Bengali letters/signs, not digits ০-৯
LATIN_WORD = re.compile(r"(?<![\w./@#-])[A-Za-z][A-Za-z-]{2,}(?![\w./@-])")
SENTENCE_SPLIT = re.compile(r"(?<=[।?!])\s+|\n+")
CODE_SPAN = re.compile(r"```[\s\S]*?```|`[^`\n]+`|https?://\S+|\S+@\S+")
# Latin tokens that are normal inside Bengali text (acronyms, units, ids) are not term candidates.
LATIN_ALLOW = re.compile(r"^(?:[A-Z]{2,}[\dA-Z-]*|[A-Za-z]{1,3}\d+|\w+-\d+)$")
SADHU_SUFFIXES = sorted([
    "িয়াছিলেন", "িয়াছিলাম", "িয়াছিল", "িয়াছেন", "িয়াছে", "িয়াছি", "িয়াছ",
    "িতেছিলেন", "িতেছিল", "িতেছেন", "িতেছে", "িতেছি", "িলেন", "িলাম", "িল",
    "িবেন", "িবে", "িব", "িতেন", "িতে", "িত", "িয়া",
], key=len, reverse=True)
SADHU_SUFFIXES = [canonicalize_unicode(s) for s in SADHU_SUFFIXES]

ACTION_FIELDS = {
    "add_lexicon": ["word"],
    "add_term": ["english", "bengali"],
    "add_idiom": ["english", "flawed_calque", "natural_bengali"],
    "add_sadhu_root": ["root"],
    "manual": [],
}


STOP_FILE = os.path.join(REPO_ROOT, "state", "STOP")


def _check_stop(stop_file: str = None):
    """Constitution kill switch: refuse to run while state/STOP exists."""
    if os.path.exists(stop_file or STOP_FILE):
        raise RuntimeError("state/STOP exists: learning loop halted (kill switch).")


@dataclass
class LoopPaths:
    drafts_dir: str = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts")
    learned_dir: str = os.path.join(REPO_ROOT, "knowledge", "cards", "learned")
    rejected_dir: str = os.path.join(REPO_ROOT, "knowledge", "cards", "rejected")
    lexicon_additions: str = os.path.join(REPO_ROOT, "bhashabid", "assets", "learned", "lexicon_additions.txt")
    sadhu_roots: str = os.path.join(REPO_ROOT, "bhashabid", "assets", "learned", "sadhu_roots.json")
    idioms_json: List[str] = field(default_factory=lambda: [
        os.path.join(REPO_ROOT, "bhashabid", "assets", "idioms", "bilingual_idioms.json"),
        os.path.join(REPO_ROOT, "tools", "assets", "idioms", "bilingual_idioms.json"),
    ])
    terms_md: str = os.path.join(REPO_ROOT, "skills", "bangla-expert", "references", "technical_terms.md")
    cases_jsonl: str = os.path.join(REPO_ROOT, "eval", "gold", "learned_cases.jsonl")
    rebuild_bundle: bool = True
    stop_file: str = STOP_FILE


# ---------------------------------------------------------------- ingest
def ingest(paths: List[str]) -> List[Dict]:
    """Reads .txt (one document per file), .jsonl ({text, source?, sector?}) and .json ({id: text} or [text])
    files or directories."""
    files = []
    for p in paths:
        if os.path.isdir(p):
            files += sorted(glob.glob(os.path.join(p, "**", "*.txt"), recursive=True))
            files += sorted(glob.glob(os.path.join(p, "**", "*.jsonl"), recursive=True))
            files += sorted(glob.glob(os.path.join(p, "**", "*.json"), recursive=True))
        elif os.path.isfile(p):
            files.append(p)
    docs = []
    for f in files:
        name = os.path.basename(f)
        with open(f, encoding="utf-8") as fh:
            if f.endswith(".json"):
                data = json.load(fh)
                items = data.items() if isinstance(data, dict) else enumerate(data)
                for key, val in items:
                    text = val.get("text") if isinstance(val, dict) else val
                    if isinstance(text, str):
                        docs.append({"text": text, "source": f"{name}:{key}", "sector": ""})
            elif f.endswith(".jsonl"):
                for line in fh:
                    if line.strip():
                        rec = json.loads(line)
                        docs.append({"text": rec["text"], "source": rec.get("source", name), "sector": rec.get("sector", "")})
            else:
                docs.append({"text": fh.read(), "source": name, "sector": ""})
    return docs


# ---------------------------------------------------------------- detect
# Inflectional and clitic endings: a token whose stem (or verbal noun) is known is not a lexicon gap.
_INFLECTIONS = sorted({canonicalize_unicode(e) for e in [
    "েছিলেন", "েছিলাম", "েছিল", "চ্ছিলেন", "চ্ছিল", "ছিলেন", "ছিলাম", "ছিল", "েছেন", "েছে", "েছি", "েছো",
    "চ্ছেন", "চ্ছে", "চ্ছি", "চ্ছো", "য়েছেন", "য়েছে", "য়েছি", "য়ে", "লেন", "লাম", "বেন", "বে", "বি",
    "তেন", "তাম", "তে", "েন", "লি", "লো", "ে", "ি", "ো", "ল", "ব", "ত", "য়",
    "গুলোও", "গুলোর", "গুলো", "টাও", "টিও", "টাই", "টিই", "রাও", "দেরও", "দের", "রা", "কে", "ের", "র", "ও", "ই",
]}, key=len, reverse=True)
_CHOLITO_FORMS = set(SADHU_FORMS.values())


def is_known_inflection(tok: str, lex) -> bool:
    if tok in _CHOLITO_FORMS or is_cholito_token(tok):
        return True
    for e in _INFLECTIONS:
        if tok.endswith(e) and len(tok) > len(e) + 1:
            stem = tok[: -len(e)]
            if any(lex.is_known(x) for x in (stem, stem + "া", stem + "ো", stem + "ানো", stem + "ি")):
                return True
    return False


def guess_sadhu_root(token: str) -> str:
    for sfx in SADHU_SUFFIXES:
        if token.endswith(sfx) and len(token) > len(sfx) + 1:
            return token[: -len(sfx)]
    return ""


def detect_candidates(docs: List[Dict], min_count: int = 2) -> List[Dict]:
    """Finds what the engine cannot decide on. Returns aggregated candidates with evidence."""
    lex = get_default_lexicon()
    agg: Dict[tuple, Dict] = {}

    def add(kind, detected_by, key, sentence, source, **extra):
        c = agg.setdefault((kind, key), {"kind": kind, "detected_by": detected_by, "candidate": key,
                                         "count": 0, "contexts": [], "sources": set(), **extra})
        c["count"] += 1
        if len(c["contexts"]) < 3 and sentence not in c["contexts"]:
            c["contexts"].append(sentence)
        c["sources"].add(source)

    for doc in docs:
        text = canonicalize_unicode(CODE_SPAN.sub(" ", doc["text"]))
        for sent in (s.strip() for s in SENTENCE_SPLIT.split(text)):
            if not re.search(r"[ঀ-৿]", sent):
                continue
            src = doc["source"]
            # 1. Words the lexicon does not know and cannot correct with confidence: new words or terms.
            for m in BN_WORD.finditer(sent):
                tok = m.group(0)
                if sent[m.end():m.end() + 1] == ".":  # abbreviation (মো., ড.), not a word
                    continue
                if (not lex.is_known(tok) and not is_known_inflection(tok, lex)
                        and not lex.suggest_corrections(tok, max_suggestions=1, max_distance=1.0)):
                    add("lexicon", "UNKNOWN_WORD", tok, sent, src)
            # 2. English words left untranslated inside Bengali prose: technical-term candidates.
            # (English in parentheses is a deliberate first-use gloss: রুল নিশি (Rule Nisi).)
            for w in LATIN_WORD.findall(re.sub(r"\([^)]*\)", " ", sent)):
                if not LATIN_ALLOW.match(w):
                    add("term", "UNTRANSLATED_ENGLISH", w.lower(), sent, src)
            # 3. Sadhu forms the paradigm cannot convert.
            for tok in convert_to_cholito(sent)[2]:
                add("sadhu_root", "SADHU_UNRESOLVED", tok, sent, src, root_guess=guess_sadhu_root(tok))
            # 4. Defects that remain after automatic repair: need a human-written rule.
            repaired, _ = repair_text(sent)
            for issue in lint_text(repaired):
                add("rule", "LINT_UNRESOLVED", f"{issue.rule_id}: {issue.matched_text}", sent, src)

    out = []
    for c in agg.values():
        # Lexicon candidates need repeated evidence; the rest are rarer and worth a look at count 1.
        if c["kind"] == "lexicon" and c["count"] < min_count:
            continue
        c["sources"] = sorted(c["sources"])
        out.append(c)
    return sorted(out, key=lambda c: (-c["count"], c["kind"], c["candidate"]))


# ---------------------------------------------------------------- draft cards
def card_id(kind: str, candidate: str) -> str:
    return f"CAND-{kind.upper().replace('_', '-')}-{hashlib.sha1(candidate.encode('utf-8')).hexdigest()[:8]}"


def _known_ids(paths: LoopPaths) -> set:
    ids = set()
    for d in (paths.drafts_dir, paths.learned_dir, paths.rejected_dir):
        for f in glob.glob(os.path.join(d, "CAND-*.yaml")):
            ids.add(os.path.basename(f)[:-5])
    return ids


def _proposed_decision(c: Dict) -> Dict:
    if c["kind"] == "lexicon":
        return {"action": "add_lexicon", "word": c["candidate"]}
    if c["kind"] == "term":
        return {"action": "add_term", "english": c["candidate"], "bengali": None}
    if c["kind"] == "sadhu_root":
        return {"action": "add_sadhu_root", "root": c.get("root_guess") or None}
    return {"action": "manual", "note": "Write or extend a rule/reference; not applied automatically."}


def draft_cards(candidates: List[Dict], paths: LoopPaths = None) -> List[str]:
    """Writes one pending card per new candidate. Never approves anything (P2)."""
    paths = paths or LoopPaths()
    os.makedirs(paths.drafts_dir, exist_ok=True)
    known = _known_ids(paths)
    written = []
    for c in candidates:
        cid = card_id(c["kind"], c["candidate"])
        if cid in known:
            continue
        card = {
            "id": cid,
            "title": f"Learning candidate ({c['kind']}): {c['candidate']}",
            "kind": c["kind"],
            "candidate": c["candidate"],
            "detected_by": c["detected_by"],
            "evidence": {"count": c["count"], "sources": c["sources"], "contexts": c["contexts"]},
            "decision": _proposed_decision(c),
            "confidence": "llm-hypothesis",
            "review": {"status": "PENDING_HUMAN_REVIEW", "reviewer_name": None, "reviewed_date": None, "applied_date": None},
        }
        path = os.path.join(paths.drafts_dir, f"{cid}.yaml")
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(card, f, allow_unicode=True, sort_keys=False)
        written.append(path)
    return written


# ---------------------------------------------------------------- human review
def _load(path: str) -> Dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _save(card: Dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(card, f, allow_unicode=True, sort_keys=False)


def list_pending(paths: LoopPaths = None) -> List[Dict]:
    paths = paths or LoopPaths()
    return [_load(f) for f in sorted(glob.glob(os.path.join(paths.drafts_dir, "CAND-*.yaml")))]


# Model or tool names are not human reviewers (P2: agents never self-approve).
_NON_HUMAN_REVIEWER = re.compile(r"(?i)\b(claude|gemini|gpt|chatgpt|openai|anthropic|llm|ai|bot|agent|assistant|model|copilot|llama|mistral)\b")
CONFIDENCE_LEVELS = ("high", "medium", "low")


def _check_human_reviewer(reviewer: str) -> str:
    name = (reviewer or "").strip()
    if not name:
        raise ValueError("A human reviewer name is required (Principle P2).")
    if _NON_HUMAN_REVIEWER.search(name):
        raise ValueError(f"'{name}' looks like a model or tool. Only a human native speaker may approve (Principle P2); "
                         "agents record recommendations with `learn suggest`.")
    return name


def suggest(cid: str, by: str, updates: Optional[Dict] = None, rationale: str = "",
            confidence: str = "medium", paths: LoopPaths = None) -> Dict:
    """Records an agent/LLM recommendation on a pending card. Never changes the review status."""
    paths = paths or LoopPaths()
    if not by or not by.strip():
        raise ValueError("`by` must name the suggesting model or person.")
    if confidence not in CONFIDENCE_LEVELS:
        raise ValueError(f"confidence must be one of {CONFIDENCE_LEVELS}")
    path = os.path.join(paths.drafts_dir, f"{cid}.yaml")
    card = _load(path)
    decision = dict(card.get("decision") or {})
    decision.update({k: v for k, v in (updates or {}).items() if v not in (None, "")})
    action = decision.get("action")
    if action not in ACTION_FIELDS and action != "reject":
        raise ValueError(f"Unknown action '{action}'. Use one of: {', '.join(ACTION_FIELDS)}, reject")
    missing = [k for k in ACTION_FIELDS.get(action, []) if not decision.get(k)]
    if missing:
        raise ValueError(f"{cid}: suggested action '{action}' needs: {', '.join(missing)}")
    card["llm_suggestion"] = {"by": by.strip(), "date": date.today().isoformat(), "decision": decision,
                              "rationale": rationale.strip(), "confidence": confidence}
    _save(card, path)
    return card


def approve(cid: str, reviewer: str, updates: Optional[Dict] = None, paths: LoopPaths = None,
            accept_suggestion: bool = False) -> Dict:
    """Records a human approval. Requires a human reviewer name and every field the chosen action needs.
    With accept_suggestion, the recorded LLM suggestion is used as the starting decision."""
    paths = paths or LoopPaths()
    reviewer = _check_human_reviewer(reviewer)
    path = os.path.join(paths.drafts_dir, f"{cid}.yaml")
    card = _load(path)
    decision = dict(card.get("decision") or {})
    if accept_suggestion:
        sug = card.get("llm_suggestion")
        if not sug:
            raise ValueError(f"{cid}: no LLM suggestion recorded to accept.")
        if sug["decision"].get("action") == "reject":
            raise ValueError(f"{cid}: the suggestion is to reject; use `learn reject`.")
        decision = dict(sug["decision"])
    decision.update({k: v for k, v in (updates or {}).items() if v not in (None, "")})
    action = decision.get("action")
    if action not in ACTION_FIELDS:
        raise ValueError(f"Unknown action '{action}'. Use one of: {', '.join(ACTION_FIELDS)}")
    missing = [k for k in ACTION_FIELDS[action] if not decision.get(k)]
    if missing:
        raise ValueError(f"{cid}: action '{action}' needs: {', '.join(missing)}")
    card["decision"] = decision
    card["confidence"] = "reviewed"
    card["review"].update({"status": "APPROVED", "reviewer_name": reviewer, "reviewed_date": date.today().isoformat(),
                           "accepted_llm_suggestion": bool(accept_suggestion)})
    _save(card, path)
    return card


def reject(cid: str, reviewer: str, reason: str = "", paths: LoopPaths = None) -> str:
    paths = paths or LoopPaths()
    reviewer = _check_human_reviewer(reviewer)
    src = os.path.join(paths.drafts_dir, f"{cid}.yaml")
    card = _load(src)
    card["review"].update({"status": "REJECTED", "reviewer_name": reviewer, "reviewed_date": date.today().isoformat(), "notes": reason})
    os.makedirs(paths.rejected_dir, exist_ok=True)
    dst = os.path.join(paths.rejected_dir, f"{cid}.yaml")
    _save(card, dst)
    os.remove(src)
    return dst


def _read_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def _read_json(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- distill
def _append_unique_line(path: str, line: str) -> bool:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    existing = _read_text(path).splitlines() if os.path.exists(path) else []
    if line in existing:
        return False
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return True


def _apply_lexicon(d: Dict, paths: LoopPaths) -> str:
    word = canonicalize_unicode(d["word"].strip())
    _append_unique_line(paths.lexicon_additions, word)
    return f"lexicon += {word}"


def _apply_sadhu_root(d: Dict, paths: LoopPaths) -> str:
    root = canonicalize_unicode(d["root"].strip())
    roots = _read_json(paths.sadhu_roots) if os.path.exists(paths.sadhu_roots) else []
    if root not in roots:
        roots.append(root)
        os.makedirs(os.path.dirname(paths.sadhu_roots), exist_ok=True)
        with open(paths.sadhu_roots, "w", encoding="utf-8", newline="\n") as f:
            json.dump(roots, f, ensure_ascii=False, indent=2)
            f.write("\n")
    return f"sadhu roots += {root}"


def _apply_idiom(d: Dict, paths: LoopPaths) -> str:
    entry_base = {
        "english": d["english"].strip(),
        "flawed_calque": d["flawed_calque"].strip(),
        "calque_pattern": r"\s+".join(re.escape(w) for w in d["flawed_calque"].split()),
        "natural_bengali": d["natural_bengali"].strip(),
        "category": (d.get("category") or "COLLOQUIAL").upper(),
    }
    for p in paths.idioms_json:
        if not os.path.exists(p):
            continue
        items = _read_json(p)
        if any(i["flawed_calque"] == entry_base["flawed_calque"] for i in items):
            continue
        n = 1 + max([int(i["id"].split("-")[-1]) for i in items if i["id"].startswith("IDM-")] or [0])
        items.append({"id": f"IDM-{n:03d}", **entry_base})
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(items, ensure_ascii=False, indent=2) + "\n")
    return f"idiom += {entry_base['english']} → {entry_base['natural_bengali']}"


LEARNED_TERMS_HEADER = "## Learned additions (human-approved)"


def _apply_term(d: Dict, paths: LoopPaths) -> str:
    line = f"- {d['english'].strip()} → {d['bengali'].strip()}"
    text = _read_text(paths.terms_md) if os.path.exists(paths.terms_md) else ""
    if line not in text:
        if LEARNED_TERMS_HEADER not in text:
            text = text.rstrip("\n") + f"\n\n{LEARNED_TERMS_HEADER}\n"
        text = text.rstrip("\n") + "\n" + line + "\n"
        with open(paths.terms_md, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    return f"term += {line[2:]}"


APPLIERS = {"add_lexicon": _apply_lexicon, "add_sadhu_root": _apply_sadhu_root,
            "add_idiom": _apply_idiom, "add_term": _apply_term}


def apply_approved(paths: LoopPaths = None) -> Dict[str, List[str]]:
    """Distills APPROVED cards into engine assets / skill references, records regression cases,
    moves the cards to knowledge/cards/learned/ and rebuilds the skill bundles."""
    paths = paths or LoopPaths()
    _check_stop(paths.stop_file)
    report = {"applied": [], "manual": [], "pending": []}
    for path in sorted(glob.glob(os.path.join(paths.drafts_dir, "CAND-*.yaml"))):
        card = _load(path)
        if card["review"].get("status") != "APPROVED" or not card["review"].get("reviewer_name"):
            report["pending"].append(card["id"])
            continue
        d = card["decision"]
        if d["action"] == "manual":
            report["manual"].append(f"{card['id']}: {card['candidate']}")
            continue
        report["applied"].append(f"{card['id']}: {APPLIERS[d['action']](d, paths)}")
        os.makedirs(os.path.dirname(paths.cases_jsonl), exist_ok=True)
        with open(paths.cases_jsonl, "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps({"id": card["id"], "action": d["action"], "decision": d,
                                "contexts": card["evidence"]["contexts"]}, ensure_ascii=False) + "\n")
        card["review"]["applied_date"] = date.today().isoformat()
        os.makedirs(paths.learned_dir, exist_ok=True)
        _save(card, os.path.join(paths.learned_dir, os.path.basename(path)))
        os.remove(path)
    if report["applied"] and paths.rebuild_bundle:
        import importlib.util
        spec = importlib.util.spec_from_file_location("build_skill_bundle", os.path.join(REPO_ROOT, "scripts", "build_skill_bundle.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.build()
    return report


def status(paths: LoopPaths = None) -> Dict:
    """Counts cards per stage, for humans and agents."""
    paths = paths or LoopPaths()
    pending = list_pending(paths)
    out = {
        "pending_total": len(pending),
        "pending_without_suggestion": sum(1 for c in pending if not c.get("llm_suggestion")),
        "pending_with_suggestion": sum(1 for c in pending if c.get("llm_suggestion")),
        "approved_not_applied": sum(1 for c in pending if c["review"].get("status") == "APPROVED"),
        "learned": len(glob.glob(os.path.join(paths.learned_dir, "CAND-*.yaml"))),
        "rejected": len(glob.glob(os.path.join(paths.rejected_dir, "CAND-*.yaml"))),
        "by_kind": {},
    }
    for c in pending:
        out["by_kind"][c["kind"]] = out["by_kind"].get(c["kind"], 0) + 1
    return out


def scan(paths_in: List[str], min_count: int = 2, paths: LoopPaths = None) -> Dict:
    _check_stop((paths or LoopPaths()).stop_file)
    docs = ingest(paths_in)
    cands = detect_candidates(docs, min_count=min_count)
    written = draft_cards(cands, paths)
    by_kind = defaultdict(int)
    for c in cands:
        by_kind[c["kind"]] += 1
    return {"documents": len(docs), "candidates": len(cands), "new_cards": len(written), "by_kind": dict(by_kind)}
