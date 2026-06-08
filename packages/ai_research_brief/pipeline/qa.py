from __future__ import annotations

from datetime import date
import json
import re
from pathlib import Path

from ..models import QAReport
from .select import build_repeat_history

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
BAD_VISIBLE = [
    r"每日\s*07:12\s*更新",
    r"Daily\s+07:12",
    r"T\+2\s+ARXIV",
    r"T\+2\s+arXiv",
    r"完整候选池与评分",
    r"full candidate pool and scoring",
    r"今日重点[:：]",
    r"Today's focus:",
    r"摘要" + r"显示",
    r"建议" + r"先看每篇",
    r"重点" + r"核验",
    r"The abstract" + r" points to",
]


def run_qa(day: date, content_dir: Path, reports_dir: Path, target_date: date | None = None, publish_date: date | None = None) -> QAReport:
    target_date = target_date or day
    publish_date = publish_date or day
    warnings: list[str] = []
    errors: list[str] = []
    checked: list[str] = []
    docs: dict[str, list[tuple[Path, dict, str]]] = {"zh": [], "en": []}

    for lang in ("zh", "en"):
        pages = sorted((content_dir / lang / "daily").glob(f"{publish_date}-*.md"))
        briefs = []
        sources = []
        for path in pages:
            checked.append(str(path))
            parsed = _parse_markdown(path, errors)
            if not parsed:
                continue
            meta, body = parsed
            docs[lang].append((path, meta, body))
            if meta.get("page_type") == "brief" and not path.stem.endswith("-sources"):
                briefs.append(path)
            if meta.get("page_type") == "sources" or path.stem.endswith("-sources"):
                sources.append(path)
            _check_doc(path, meta, body, day, target_date, publish_date, errors, warnings)
        if len(briefs) != 1:
            errors.append(f"Expected exactly one {lang} brief for {publish_date}, found {len(briefs)}")
        if len(sources) != 1:
            errors.append(f"Expected exactly one {lang} source page for {publish_date}, found {len(sources)}")

    repo_root = content_dir.parents[1]
    _check_processed(day, repo_root, checked, errors)
    _check_pairs(docs, errors)
    _check_static(publish_date, repo_root, checked, errors, docs)
    _check_repeat(day, publish_date, repo_root, docs, errors, warnings)

    report = QAReport(
        date=publish_date,
        target_date=target_date,
        actual_date=day,
        fallback_from=target_date if target_date != day else None,
        passed=not errors,
        warnings=warnings,
        errors=errors,
        checked_files=checked,
    )
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / (str(publish_date) + ".json")).write_text(report.model_dump_json(indent=2), encoding="utf-8")
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
            meta[key.strip()] = int(value) if value.isdigit() else value.strip('"')
    return meta, match.group(2)


def _check_doc(path: Path, meta: dict, body: str, day: date, target_date: date, publish_date: date, errors: list[str], warnings: list[str]) -> None:
    required = ["title", "date", "target_date", "actual_date", "lang", "slug", "summary", "tags", "generated_at", "page_type", "candidate_count", "featured_count", "mentions_count"]
    for key in required:
        if meta.get(key) in (None, "", []):
            errors.append(f"Missing frontmatter field {key}: {path}")
    if str(meta.get("date")) != str(publish_date):
        errors.append(f"Frontmatter publication date mismatch: {path}")
    if str(meta.get("actual_date")) != str(day):
        errors.append(f"Frontmatter actual_date mismatch: {path}")
    if str(meta.get("target_date")) != str(target_date):
        errors.append(f"Frontmatter target_date mismatch: {path}")
    if str(meta.get("slug")) != path.stem:
        errors.append(f"Slug/path mismatch: {path}")
    if meta.get("page_type") == "brief" and not meta.get("sources_page"):
        errors.append(f"Brief is missing sources_page: {path}")
    if meta.get("page_type") == "sources" and not meta.get("brief_page"):
        errors.append(f"Sources page is missing brief_page: {path}")
    visible = "\n".join([str(meta.get("title", "")), str(meta.get("summary", "")), body])
    for pattern in BAD_VISIBLE:
        if re.search(pattern, visible, re.I):
            errors.append(f"Deprecated visible wording matched {pattern}: {path}")
    featured_count = int(meta.get("featured_count") or 0)
    if meta.get("page_type") == "brief" and featured_count > 0:
        _check_featured_explanations(path, meta, body, errors)
    if not re.search(r"https://arxiv\.org/abs/\d{4}\.\d{4,5}", body):
        warnings.append(f"No arXiv URL found: {path}")


def _check_featured_explanations(path: Path, meta: dict, body: str, errors: list[str]) -> None:
    chunks = re.split(r"\n###\s+\d+\.\s+", body)[1:]
    featured_count = int(meta.get("featured_count") or 0)
    for index, chunk in enumerate(chunks[:featured_count], start=1):
        text = _strip(chunk)
        if meta.get("lang") == "zh":
            if "核心：" not in text or len(re.sub(r"\s+", "", text)) < 80:
                errors.append(f"Featured paper {index} lacks a full structured Chinese explanation: {path}")
        elif "Core idea:" not in text or len(re.findall(r"\b\w+\b", text)) < 45:
            errors.append(f"Featured paper {index} lacks a full structured English explanation: {path}")


def _check_processed(day: date, repo_root: Path, checked: list[str], errors: list[str]) -> None:
    processed = repo_root / "data" / "processed" / str(day)
    for name in ["papers.json", "scored_papers.json", "selected_papers.json"]:
        path = processed / name
        checked.append(str(path))
        if not path.exists():
            errors.append(f"Missing processed artifact: {path}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON: {path}")


def _check_pairs(docs: dict[str, list[tuple[Path, dict, str]]], errors: list[str]) -> None:
    for lang in ("zh", "en"):
        brief = _first(docs, lang, "brief")
        source = _first(docs, lang, "sources")
        if not brief or not source:
            continue
        brief_path, brief_meta, brief_body = brief
        source_path, source_meta, source_body = source
        for key in ["date", "target_date", "actual_date", "fallback_from", "candidate_count", "featured_count", "mentions_count", "lang"]:
            if str(brief_meta.get(key, "")) != str(source_meta.get(key, "")):
                errors.append(f"Brief/source metadata mismatch for {key}: {brief_path} vs {source_path}")
        if brief_meta.get("sources_page") != f"/{lang}/daily/{source_meta.get('slug')}/":
            errors.append(f"Brief sources_page does not match source slug: {brief_path}")
        if source_meta.get("brief_page") != f"/{lang}/daily/{brief_meta.get('slug')}/":
            errors.append(f"Source brief_page does not match brief slug: {source_path}")
        if _ids(brief_body) != _source_selected_ids(source_body):
            errors.append(f"Brief/source selected arXiv IDs differ for {lang}")
    zh = _first(docs, "zh", "brief")
    en = _first(docs, "en", "brief")
    if not zh or not en:
        errors.append("Missing bilingual brief pair")
        return
    for key in ["date", "actual_date", "candidate_count", "featured_count", "mentions_count"]:
        if str(zh[1].get(key, "")) != str(en[1].get(key, "")):
            errors.append(f"zh/en metadata mismatch for {key}")
    if _ids(zh[2]) != _ids(en[2]):
        errors.append("zh/en selected arXiv IDs differ")


def _check_static(day: date, repo_root: Path, checked: list[str], errors: list[str], docs: dict[str, list[tuple[Path, dict, str]]]) -> None:
    public = repo_root / "apps" / "web" / "public"
    for path in [public / "zh" / "feed.xml", public / "en" / "feed.xml", public / "sitemap.xml", public / "search-index.json"]:
        checked.append(str(path))
        if not path.exists():
            errors.append(f"Missing static artifact: {path}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in BAD_VISIBLE:
            if re.search(pattern, text, re.I):
                errors.append(f"Static artifact contains deprecated wording matched {pattern}: {path}")
    search_index = public / "search-index.json"
    if search_index.exists():
        try:
            rows = json.loads(search_index.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("search-index.json is not valid JSON")
        else:
            seen = set()
            for row in rows:
                for field in ["title", "date", "lang", "url", "source_url", "summary", "tags", "topics", "authors", "content_excerpt", "type", "text"]:
                    if field not in row:
                        errors.append(f"Search index missing field: {field}")
                key = (row.get("lang"), row.get("date"))
                if key in seen:
                    errors.append(f"Search index contains duplicate public issue for {key}")
                seen.add(key)
            if not any(str(row.get("date")) == str(day) for row in rows):
                errors.append(f"Search index does not include publication date {day}")
    sitemap_text = (public / "sitemap.xml").read_text(encoding="utf-8") if (public / "sitemap.xml").exists() else ""
    for lang in ("zh", "en"):
        for doc in (_first(docs, lang, "brief"), _first(docs, lang, "sources")):
            if doc and f"/{lang}/daily/{doc[1].get('slug')}/" not in sitemap_text:
                errors.append(f"Sitemap missing {lang} page slug {doc[1].get('slug')}")


def _check_repeat(day: date, publish_date: date, repo_root: Path, docs: dict[str, list[tuple[Path, dict, str]]], errors: list[str], warnings: list[str]) -> None:
    history = build_repeat_history(day, days=30, repo_root=repo_root)
    history = {key: value for key, value in history.items() if str(value.get("date")) != str(publish_date)}
    if not history:
        return
    for lang in ("zh", "en"):
        brief = _first(docs, lang, "brief")
        if not brief:
            continue
        featured_ids, mention_ids = _section_ids(brief[2])
        if set(featured_ids) & set(mention_ids):
            errors.append(f"{lang} featured and mentions overlap in the same issue")
        for arxiv_id in featured_ids:
            previous = history.get(f"arxiv:{arxiv_id.lower()}")
            if previous:
                errors.append(f"{lang} featured paper {arxiv_id} repeats recent {previous.get('section')} from {previous.get('date')}")
        if len(featured_ids) != int(brief[1].get("featured_count") or 0):
            warnings.append(f"{lang} featured_count differs from parsed featured ids")


def _first(docs: dict[str, list[tuple[Path, dict, str]]], lang: str, page_type: str):
    for row in docs[lang]:
        if row[1].get("page_type") == page_type:
            return row
    return None


def _section_ids(body: str) -> tuple[list[str], list[str]]:
    match = re.search(r"\n##\s+(其他值得关注|Other papers worth tracking)\b", body)
    if match:
        return _ids(body[: match.start()]), _ids(body[match.start():])
    return _ids(body), []


def _source_selected_ids(body: str) -> list[str]:
    start = re.search(r"\n##\s+(入选论文|Selected papers)\b", body)
    if start:
        body = body[start.start():]
    end = re.search(r"\n##\s+(候选池样例|Candidate pool sample)\b", body)
    if end:
        body = body[: end.start()]
    return _ids(body)


def _ids(text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text)))


def _strip(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[#*_`>-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()
