from __future__ import annotations

from datetime import date
import json
import re
from pathlib import Path

from ..models import QAReport


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
FORBIDDEN_PATTERNS = [
    r"\bguaranteed breakthrough\b",
    r"\bproduction ready\b",
    r"已被证实",
    r"必然",
    r"颠覆",
    r"革命性突破",
]
PEER_REVIEW_PATTERNS = [
    r"accepted by\s+(NeurIPS|ICML|ICLR|ACL|CVPR|EMNLP)",
    r"被\s*(NeurIPS|ICML|ICLR|ACL|CVPR|EMNLP)\s*接收",
]


def run_qa(day: date, content_dir: Path, reports_dir: Path) -> QAReport:
    warnings: list[str] = []
    errors: list[str] = []
    checked: list[str] = []
    docs: dict[str, list[tuple[Path, dict, str]]] = {"zh": [], "en": []}

    for lang in ("zh", "en"):
        pages = sorted((content_dir / lang / "daily").glob(f"{day}-*.md"))
        brief_pages: list[Path] = []
        source_pages: list[Path] = []
        for path in pages:
            checked.append(str(path))
            parsed = _parse_markdown(path, errors)
            if not parsed:
                continue
            meta, body = parsed
            docs[lang].append((path, meta, body))
            if str(meta.get("page_type")) == "brief" and not path.stem.endswith("-sources"):
                brief_pages.append(path)
            if str(meta.get("page_type")) == "sources" or path.stem.endswith("-sources"):
                source_pages.append(path)
            _check_markdown_doc(path, meta, body, day, errors, warnings)

        if not brief_pages:
            errors.append(f"Missing {lang} daily brief for {day}")
        if not source_pages:
            errors.append(f"Missing {lang} sources page for {day}")

    _check_processed(day, content_dir.parents[1], checked, errors)
    _check_static_artifacts(day, content_dir.parents[1], checked, errors)
    _check_bilingual_quality(docs, warnings, errors)

    report = QAReport(date=day, passed=not errors, warnings=warnings, errors=errors, checked_files=checked)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / (str(day) + ".json")).write_text(report.model_dump_json(indent=2), encoding="utf-8")
    return report


def _parse_markdown(path: Path, errors: list[str]) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"Missing or invalid frontmatter: {path}")
        return None
    meta = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            meta[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            meta[key.strip()] = value.strip('"')
    return meta, match.group(2)


def _check_markdown_doc(path: Path, meta: dict, body: str, day: date, errors: list[str], warnings: list[str]) -> None:
    required = ["title", "date", "lang", "slug", "summary", "tags", "generated_at"]
    for key in required:
        if meta.get(key) in (None, "", []):
            errors.append(f"Missing frontmatter field {key}: {path}")
    if str(meta.get("date")) != str(day):
        errors.append(f"Frontmatter date mismatch: {path}")
    if str(meta.get("slug")) != path.stem:
        errors.append(f"Slug/path mismatch: {path}")
    if not re.search(r"https://arxiv\.org/abs/\d{4}\.\d{4,5}", body):
        warnings.append(f"No arXiv URL found: {path}")
    if str(meta.get("page_type")) == "sources" and "Score breakdown:" not in body:
        errors.append(f"Sources page lacks score breakdown: {path}")
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, body, re.I):
            errors.append(f"Forbidden wording matched {pattern}: {path}")
    for pattern in PEER_REVIEW_PATTERNS:
        if re.search(pattern, body, re.I):
            errors.append(f"Possible fabricated peer-review acceptance wording: {path}")
    for code_url in re.findall(r"Code URL:\s*([^\n]+)", body):
        clean = code_url.strip()
        if clean != "none verified" and not clean.startswith("https://github.com/"):
            errors.append(f"Unverified or unsupported code URL: {path}: {clean}")
    if meta.get("lang") == "zh":
        english_terms = re.findall(r"\b[A-Za-z][A-Za-z0-9+\-]{3,}\b", body)
        if len(english_terms) > 180:
            warnings.append(f"Chinese page has many English terms; review terminology: {path}")
    if meta.get("lang") == "en" and len(body.strip()) < 200:
        errors.append(f"English page is too short: {path}")


def _check_processed(day: date, repo_root: Path, checked: list[str], errors: list[str]) -> None:
    processed = repo_root / "data" / "processed" / str(day)
    for name in ["papers.json", "scored_papers.json", "selected_papers.json"]:
        path = processed / name
        checked.append(str(path))
        if not path.exists():
            errors.append(f"Missing processed artifact: {path}")
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON: {path}")
            continue
        rows = payload if isinstance(payload, list) else payload.get("featured", []) + payload.get("mentions", []) if isinstance(payload, dict) else []
        if name == "papers.json":
            for index, row in enumerate(rows):
                for field in ["title", "abstract", "authors", "abs_url"]:
                    if not row.get(field):
                        errors.append(f"Paper {index} missing {field}: {path}")


def _check_static_artifacts(day: date, repo_root: Path, checked: list[str], errors: list[str]) -> None:
    public = repo_root / "apps" / "web" / "public"
    for path in [public / "zh" / "feed.xml", public / "en" / "feed.xml", public / "sitemap.xml", public / "search-index.json"]:
        checked.append(str(path))
        if not path.exists():
            errors.append(f"Missing static artifact: {path}")
    search_index = public / "search-index.json"
    if search_index.exists():
        try:
            rows = json.loads(search_index.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("search-index.json is not valid JSON")
        else:
            if not any(str(row.get("date")) == str(day) for row in rows):
                errors.append(f"Search index does not include {day}")
            for field in ["title", "date", "lang", "url", "summary", "tags", "topics", "authors", "content_excerpt"]:
                if rows and field not in rows[0]:
                    errors.append(f"Search index missing field: {field}")


def _check_bilingual_quality(docs: dict[str, list[tuple[Path, dict, str]]], warnings: list[str], errors: list[str]) -> None:
    zh_briefs = [body for _, meta, body in docs["zh"] if meta.get("page_type") == "brief"]
    en_briefs = [body for _, meta, body in docs["en"] if meta.get("page_type") == "brief"]
    if zh_briefs and en_briefs and zh_briefs[0][:500] == en_briefs[0][:500]:
        errors.append("English brief appears to duplicate Chinese content")
    if not en_briefs:
        errors.append("Missing English brief content")
    if not zh_briefs:
        errors.append("Missing Chinese brief content")
