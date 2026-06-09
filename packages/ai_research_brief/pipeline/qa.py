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
MOCK_VISIBLE = [
    r"Self Evolving Agents for Tool Use Skills",
]
MOCK_FIXTURE_AUTHOR_NAMES = [
    r"Alice Chen",
    r"Bob Smith",
    r"Carol Li",
    r"Dan Wang",
    r"Eva Green",
    r"Frank Moore",
    r"Grace Kim",
    r"Henry Liu",
    r"Ivy Park",
    r"Jack Sun",
    r"Kai Zhao",
    r"Lina Ortiz",
    r"Mona Singh",
    r"Nate Brown",
    r"Olivia Martin",
    r"Paul Davis",
    r"Qian Wu",
    r"Rita Gomez",
    r"Sam Taylor",
]
MOCK_AUTHOR_CO_OCCURRENCE_THRESHOLD = 3
MOCK_IDS_RE = re.compile(r"\b2606\.000(?:0[1-9]|1[0-8])\b")


def run_qa(day: date, content_dir: Path, reports_dir: Path, target_date: date | None = None, publish_date: date | None = None) -> QAReport:
    target_date = target_date or day
    publish_date = publish_date or day
    warnings: list[str] = []
    errors: list[str] = []
    checked: list[str] = []
    docs: dict[str, list[tuple[Path, dict, str]]] = {"zh": [], "en": []}
    repo_root = content_dir.parents[1]
    allow_mock_fixture = _is_mock_fixture_run(day, repo_root)

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
            _check_doc(path, meta, body, day, target_date, publish_date, errors, warnings, allow_mock_fixture)
        if len(briefs) != 1:
            errors.append(f"Expected exactly one {lang} brief for {publish_date}, found {len(briefs)}")
        if len(sources) != 1:
            errors.append(f"Expected exactly one {lang} source page for {publish_date}, found {len(sources)}")

    _check_processed(day, repo_root, checked, errors)
    _check_candidate_source(day, publish_date, target_date, repo_root, docs, checked, errors, allow_mock_fixture)
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


def _check_doc(path: Path, meta: dict, body: str, day: date, target_date: date, publish_date: date, errors: list[str], warnings: list[str], allow_mock_fixture: bool = False) -> None:
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
    _check_no_mock_text(visible, path, publish_date, errors, allow_mock_fixture=allow_mock_fixture)
    featured_count = int(meta.get("featured_count") or 0)
    if meta.get("page_type") == "brief" and featured_count > 0 and not allow_mock_fixture:
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
    papers_payload = None
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
        if name == "papers.json":
            papers_payload = payload
    _check_paper_publication_dates(day, processed / "papers.json", papers_payload, errors)


def _check_paper_publication_dates(day: date, path: Path, payload, errors: list[str]) -> None:
    if not isinstance(payload, list):
        errors.append(f"Processed papers artifact is not a list: {path}")
        return
    if not payload:
        errors.append(f"Processed papers artifact is empty: {path}")
        return
    wrong_dates: list[str] = []
    for row in payload:
        if not isinstance(row, dict):
            wrong_dates.append("<non-object>")
            continue
        arxiv_id = str(row.get("arxiv_id") or row.get("id") or "<missing-id>")
        published_at = str(row.get("published_at") or "")
        if not published_at.startswith(str(day)):
            wrong_dates.append(f"{arxiv_id}:{published_at or '<missing-published_at>'}")
        if len(wrong_dates) >= 5:
            break
    if wrong_dates:
        errors.append(
            f"Processed papers in {path} must be newly fetched for actual_date {day}; "
            f"found mismatched published_at values: {', '.join(wrong_dates)}"
        )


def _check_candidate_source(
    day: date,
    publish_date: date,
    target_date: date,
    repo_root: Path,
    docs: dict[str, list[tuple[Path, dict, str]]],
    checked: list[str],
    errors: list[str],
    allow_mock_fixture: bool = False,
) -> None:
    processed = repo_root / "data" / "processed" / str(day)
    paths = {
        "papers": processed / "papers.json",
        "scored": processed / "scored_papers.json",
        "selected": processed / "selected_papers.json",
        "manifest": processed / "candidate_manifest.json",
    }
    payloads: dict[str, object] = {}
    for key, path in paths.items():
        checked.append(str(path))
        if not path.exists():
            if key == "manifest":
                errors.append(f"Missing candidate manifest: {path}")
            continue
        try:
            payloads[key] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON: {path}")
    papers = payloads.get("papers")
    scored = payloads.get("scored")
    selected = payloads.get("selected")
    manifest = payloads.get("manifest")
    if not isinstance(papers, list) or not isinstance(scored, list) or not isinstance(selected, dict):
        return
    candidate_ids = _scored_json_ids(scored)
    paper_ids = _paper_json_ids(papers)
    featured_ids = _scored_json_ids(selected.get("featured", []))
    mention_ids = _scored_json_ids(selected.get("mentions", []))
    selected_ids = featured_ids + mention_ids
    if not candidate_ids:
        errors.append(f"No candidate IDs found in {paths['scored']}")
    if [paper_id for paper_id in selected_ids if paper_id not in set(candidate_ids)]:
        errors.append("selected_papers.json contains IDs not present in scored_papers.json")
    if [paper_id for paper_id in candidate_ids if paper_id not in set(paper_ids)]:
        errors.append("scored_papers.json contains IDs not present in papers.json")
    if isinstance(manifest, dict):
        expected = {
            "publish_date": str(publish_date),
            "target_date": str(target_date),
            "actual_date": str(day),
            "candidate_count": len(candidate_ids),
            "featured_count": len(featured_ids),
            "mentions_count": len(mention_ids),
        }
        for key, value in expected.items():
            if str(manifest.get(key)) != str(value):
                errors.append(f"candidate_manifest {key} mismatch: {manifest.get(key)} != {value}")
        if list(manifest.get("candidate_ids") or []) != candidate_ids:
            errors.append("candidate_manifest candidate_ids do not match scored_papers.json")
        if list(manifest.get("selected_ids") or []) != selected_ids:
            errors.append("candidate_manifest selected_ids do not match selected_papers.json")
    for lang in ("zh", "en"):
        brief = _first(docs, lang, "brief")
        source = _first(docs, lang, "sources")
        for doc in (brief, source):
            if not doc:
                continue
            path, meta, body = doc
            if int(meta.get("candidate_count") or -1) != len(candidate_ids):
                errors.append(f"{path} candidate_count does not match scored_papers.json")
            if int(meta.get("featured_count") or -1) != len(featured_ids):
                errors.append(f"{path} featured_count does not match selected_papers.json")
            if int(meta.get("mentions_count") or -1) != len(mention_ids):
                errors.append(f"{path} mentions_count does not match selected_papers.json")
            parsed_ids = _source_selected_ids(body) if meta.get("page_type") == "sources" else _ids(body)
            if parsed_ids != selected_ids:
                errors.append(f"{path} selected IDs differ from selected_papers.json")
    _check_no_mock_text(json.dumps(payloads, ensure_ascii=False), paths["scored"], publish_date, errors, allow_mock_fixture=allow_mock_fixture)


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
    for key in ["date", "target_date", "actual_date", "candidate_count", "featured_count", "mentions_count"]:
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


def _paper_json_ids(rows) -> list[str]:
    if not isinstance(rows, list):
        return []
    return [str(row.get("arxiv_id") or row.get("id") or "") for row in rows if isinstance(row, dict) and (row.get("arxiv_id") or row.get("id"))]


def _scored_json_ids(rows) -> list[str]:
    if not isinstance(rows, list):
        return []
    ids: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        paper = row.get("paper") if isinstance(row.get("paper"), dict) else {}
        arxiv_id = paper.get("arxiv_id") or paper.get("id") or row.get("arxiv_id") or row.get("id")
        if arxiv_id:
            ids.append(str(arxiv_id))
    return ids


def _is_mock_fixture_run(day: date, repo_root: Path) -> bool:
    manifest_path = repo_root / "data" / "processed" / str(day) / "candidate_manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    return manifest.get("mock") is True


def _check_no_mock_text(text: str, path: Path, publish_date: date, errors: list[str], allow_mock_fixture: bool = False) -> None:
    if allow_mock_fixture:
        return
    if MOCK_IDS_RE.search(text):
        errors.append(f"Mock arXiv ID 2606.000xx found in non-mock content/source: {path}")
    for pattern in MOCK_VISIBLE:
        if re.search(pattern, text, re.I):
            errors.append(f"Mock fixture text matched {pattern}: {path}")
    matched_authors = [pattern for pattern in MOCK_FIXTURE_AUTHOR_NAMES if re.search(pattern, text, re.I)]
    if len(matched_authors) >= MOCK_AUTHOR_CO_OCCURRENCE_THRESHOLD:
        authors = ", ".join(matched_authors[:6])
        errors.append(f"Mock fixture author cluster matched {len(matched_authors)} names ({authors}): {path}")


def _strip(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[#*_`>-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()
