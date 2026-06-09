from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
ARXIV_ID_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
MOCK_IDS_RE = re.compile(r"\b2606\.000(?:0[1-9]|1[0-8])\b")
MOCK_STRONG_TEXT = [r"Self Evolving Agents for Tool Use Skills"]
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
MOCK_AUTHOR_CLUSTER_THRESHOLD = 3


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate that a generated issue is tied to its real candidate pool."
    )
    parser.add_argument("--report", default="data/reports/runs/last-run.json")
    parser.add_argument("--mode", choices=["daily", "manual"], default="daily")
    parser.add_argument("--max-fallback-days", type=int, default=2)
    parser.add_argument("--allow-reuse-existing-source", action="store_true")
    args = parser.parse_args(argv)

    errors: list[str] = []
    report_path = REPO_ROOT / args.report
    report = _load_json(report_path, errors)
    if not isinstance(report, dict):
        errors.append(f"Run report must be a JSON object: {_rel(report_path)}")
        return _finish(errors)

    publish_date = _parse_date(report.get("publish_date") or report.get("date"), "publish_date", errors)
    target_date = _parse_date(report.get("target_date"), "target_date", errors)
    actual_date = _parse_date(report.get("actual_date"), "actual_date", errors)
    if not publish_date or not target_date or not actual_date:
        return _finish(errors)

    one_off_manual_reuse = (
        args.mode == "manual"
        and args.allow_reuse_existing_source
        and str(publish_date) == "2026-06-09"
        and str(target_date) == "2026-06-05"
        and str(actual_date) == "2026-06-05"
        and bool(report.get("reuse_existing_source"))
    )

    expected_target = publish_date - timedelta(days=2)
    if not one_off_manual_reuse and target_date != expected_target:
        errors.append(
            "target_date must equal publish_date - 2 days: "
            f"publish_date={publish_date} target_date={target_date} expected={expected_target}"
        )

    fallback_days = int(report.get("fallback_days") or 0)
    if fallback_days < 0 or fallback_days > args.max_fallback_days:
        errors.append(f"fallback_days must be between 0 and {args.max_fallback_days}: {fallback_days}")

    delta = (target_date - actual_date).days
    fallback_used = bool(report.get("fallback_used"))
    fallback_from = str(report.get("fallback_from") or "")
    if delta < 0:
        errors.append(f"actual_date cannot be after target_date: target_date={target_date} actual_date={actual_date}")
    if delta > args.max_fallback_days:
        errors.append(
            f"actual_date is outside fallback window: target_date={target_date} actual_date={actual_date} max={args.max_fallback_days}"
        )
    if delta > fallback_days:
        errors.append(f"actual_date fallback delta exceeds run fallback_days: delta={delta} fallback_days={fallback_days}")
    if delta == 0 and fallback_used:
        errors.append("fallback_used must be false when actual_date equals target_date")
    if delta > 0:
        if not fallback_used:
            errors.append("fallback_used must be true when actual_date is older than target_date")
        if fallback_from != str(target_date):
            errors.append(f"fallback_from must equal target_date: fallback_from={fallback_from} target_date={target_date}")

    if report.get("mock"):
        errors.append("production issue must not be generated from mock data")
    if not args.allow_reuse_existing_source and report.get("reuse_existing_source"):
        errors.append("daily production issue must not reuse committed source candidates")
    if not args.allow_reuse_existing_source and report.get("fetch_mode") == "existing_processed":
        errors.append("daily production fetch_mode cannot be existing_processed")
    if not args.allow_reuse_existing_source and int(report.get("request_count") or 0) <= 0:
        errors.append("daily production run must perform at least one arXiv request")

    paths = _expected_paths(actual_date)
    for key, expected in paths.items():
        report_key = "candidate_manifest" if key == "manifest_file" else key
        if report.get(report_key) and str(report.get(report_key)) != expected:
            errors.append(f"run report {report_key} must point to actual_date artifact: {report.get(report_key)} != {expected}")

    raw = _load_json(REPO_ROOT / paths["raw_candidate_file"], errors)
    papers = _load_json(REPO_ROOT / paths["processed_papers_file"], errors)
    scored = _load_json(REPO_ROOT / paths["candidate_file"], errors)
    selected = _load_json(REPO_ROOT / paths["selected_file"], errors)
    manifest = _load_json(REPO_ROOT / paths["manifest_file"], errors)

    if not isinstance(papers, list) or not isinstance(scored, list) or not isinstance(selected, dict) or not isinstance(manifest, dict):
        errors.append("candidate lineage requires papers.json, scored_papers.json, selected_papers.json, and candidate_manifest.json")
        return _finish(errors)

    paper_ids = _paper_ids(papers)
    raw_ids = _paper_ids(raw) if isinstance(raw, list) else []
    candidate_ids = _scored_ids(scored)
    featured_ids = _scored_ids(selected.get("featured", []))
    mention_ids = _scored_ids(selected.get("mentions", []))
    selected_ids = featured_ids + mention_ids

    if not paper_ids:
        errors.append("processed papers.json is empty")
    if not candidate_ids:
        errors.append("scored_papers.json is empty")
    if len(candidate_ids) != len(set(candidate_ids)):
        errors.append("scored_papers.json contains duplicate arXiv IDs")
    if [paper_id for paper_id in candidate_ids if paper_id not in set(paper_ids)]:
        errors.append("scored_papers.json contains IDs not present in processed papers.json")
    if raw_ids and set(paper_ids) - set(raw_ids):
        errors.append("processed papers.json contains IDs not present in raw actual_date papers.json")
    if [paper_id for paper_id in selected_ids if paper_id not in set(candidate_ids)]:
        errors.append("selected_papers.json contains IDs outside scored_papers.json")

    _check_published_dates(actual_date, papers, errors)
    _check_report_count(report, ["deduped_papers"], len(paper_ids), errors)
    _check_report_count(report, ["candidate_count", "total_candidates"], len(candidate_ids), errors)
    _check_report_count(report, ["featured_count", "featured"], len(featured_ids), errors)
    _check_report_count(report, ["mentions_count", "mentions"], len(mention_ids), errors)
    _check_ids(report, "candidate_ids", candidate_ids, errors)
    _check_ids(report, "featured_ids", featured_ids, errors)
    _check_ids(report, "mention_ids", mention_ids, errors)
    _check_ids(report, "selected_ids", selected_ids, errors)

    if one_off_manual_reuse:
        if len(candidate_ids) != 344:
            errors.append(f"one-off 2026-06-09 source reuse must have 344 candidates, found {len(candidate_ids)}")
        if len(featured_ids) != 6:
            errors.append(f"one-off 2026-06-09 source reuse must have 6 featured papers, found {len(featured_ids)}")
        if len(mention_ids) != 20:
            errors.append(f"one-off 2026-06-09 source reuse must have 20 mention papers, found {len(mention_ids)}")

    for key, expected in {
        "publish_date": str(publish_date),
        "target_date": str(target_date),
        "actual_date": str(actual_date),
        "fallback_used": actual_date != target_date,
        "candidate_count": len(candidate_ids),
        "raw_candidate_count": len(paper_ids),
        "featured_count": len(featured_ids),
        "mentions_count": len(mention_ids),
        "candidate_file": paths["candidate_file"],
        "raw_candidate_file": paths["raw_candidate_file"],
        "processed_papers_file": paths["processed_papers_file"],
        "selected_file": paths["selected_file"],
    }.items():
        if str(manifest.get(key)) != str(expected):
            errors.append(f"candidate_manifest {key} mismatch: {manifest.get(key)} != {expected}")
    for key, expected in {
        "paper_ids": paper_ids,
        "candidate_ids": candidate_ids,
        "featured_ids": featured_ids,
        "mention_ids": mention_ids,
        "selected_ids": selected_ids,
    }.items():
        if list(manifest.get(key) or []) != expected:
            errors.append(f"candidate_manifest {key} does not match actual source files")

    docs = _load_docs(publish_date, target_date, actual_date, len(candidate_ids), len(featured_ids), len(mention_ids), selected_ids, errors)
    _check_static(publish_date, docs, errors)
    _check_mock_text(json.dumps({"papers": papers, "scored": scored, "selected": selected, "manifest": manifest}, ensure_ascii=False), REPO_ROOT / paths["candidate_file"], errors)

    if errors:
        return _finish(errors)
    print(
        "candidate_lineage_guard=passed "
        f"mode={args.mode} publish_date={publish_date} target_date={target_date} actual_date={actual_date} "
        f"fallback_days={fallback_days} candidate_count={len(candidate_ids)} featured={len(featured_ids)} mentions={len(mention_ids)} "
        f"one_off_manual_reuse={one_off_manual_reuse}"
    )
    return 0


def _expected_paths(actual_date: date) -> dict[str, str]:
    prefix = f"data/processed/{actual_date}"
    return {
        "raw_candidate_file": f"data/raw/{actual_date}/papers.json",
        "processed_papers_file": f"{prefix}/papers.json",
        "candidate_file": f"{prefix}/scored_papers.json",
        "selected_file": f"{prefix}/selected_papers.json",
        "manifest_file": f"{prefix}/candidate_manifest.json",
    }


def _load_docs(
    publish_date: date,
    target_date: date,
    actual_date: date,
    candidate_count: int,
    featured_count: int,
    mentions_count: int,
    selected_ids: list[str],
    errors: list[str],
) -> dict[str, dict[str, tuple[Path, dict, str]]]:
    docs: dict[str, dict[str, tuple[Path, dict, str]]] = {"zh": {}, "en": {}}
    for lang in ("zh", "en"):
        pages = sorted((REPO_ROOT / "data" / "content" / lang / "daily").glob(f"{publish_date}-*.md"))
        briefs: list[tuple[Path, dict, str]] = []
        sources: list[tuple[Path, dict, str]] = []
        for path in pages:
            parsed = _parse_markdown(path, errors)
            if not parsed:
                continue
            meta, body = parsed
            _check_doc(path, meta, body, lang, publish_date, target_date, actual_date, candidate_count, featured_count, mentions_count, selected_ids, errors)
            if meta.get("page_type") == "brief" and not path.stem.endswith("-sources"):
                briefs.append((path, meta, body))
            elif meta.get("page_type") == "sources" or path.stem.endswith("-sources"):
                sources.append((path, meta, body))
        if len(briefs) != 1:
            errors.append(f"Expected exactly one {lang} brief for {publish_date}, found {len(briefs)}")
        else:
            docs[lang]["brief"] = briefs[0]
        if len(sources) != 1:
            errors.append(f"Expected exactly one {lang} source page for {publish_date}, found {len(sources)}")
        else:
            docs[lang]["sources"] = sources[0]
    _check_pairs(docs, errors)
    return docs


def _check_doc(path: Path, meta: dict, body: str, lang: str, publish_date: date, target_date: date, actual_date: date, candidate_count: int, featured_count: int, mentions_count: int, selected_ids: list[str], errors: list[str]) -> None:
    for key in ["title", "date", "target_date", "actual_date", "lang", "slug", "page_type", "candidate_count", "featured_count", "mentions_count"]:
        if meta.get(key) in (None, "", []):
            errors.append(f"Missing {key} in {_rel(path)}")
    for key, expected in {
        "date": str(publish_date),
        "target_date": str(target_date),
        "actual_date": str(actual_date),
        "lang": lang,
        "candidate_count": candidate_count,
        "featured_count": featured_count,
        "mentions_count": mentions_count,
    }.items():
        if str(meta.get(key)) != str(expected):
            errors.append(f"{_rel(path)} frontmatter {key} mismatch: {meta.get(key)} != {expected}")
    if str(meta.get("slug")) != path.stem:
        errors.append(f"{_rel(path)} slug/path mismatch")
    parsed_ids = _source_selected_ids(body) if meta.get("page_type") == "sources" else _ids(body)
    if parsed_ids != selected_ids:
        errors.append(f"{_rel(path)} selected arXiv IDs do not match selected_papers.json")
    _check_mock_text("\n".join([str(meta.get("title", "")), str(meta.get("summary", "")), body]), path, errors)


def _check_pairs(docs: dict[str, dict[str, tuple[Path, dict, str]]], errors: list[str]) -> None:
    for lang in ("zh", "en"):
        brief = docs.get(lang, {}).get("brief")
        source = docs.get(lang, {}).get("sources")
        if not brief or not source:
            continue
        if brief[1].get("sources_page") != f"/{lang}/daily/{source[1].get('slug')}/":
            errors.append(f"{_rel(brief[0])} sources_page does not point to paired source page")
        if source[1].get("brief_page") != f"/{lang}/daily/{brief[1].get('slug')}/":
            errors.append(f"{_rel(source[0])} brief_page does not point to paired brief")
    zh = docs.get("zh", {}).get("brief")
    en = docs.get("en", {}).get("brief")
    if zh and en and _ids(zh[2]) != _ids(en[2]):
        errors.append("zh/en selected arXiv IDs differ")


def _check_static(publish_date: date, docs: dict[str, dict[str, tuple[Path, dict, str]]], errors: list[str]) -> None:
    search_path = REPO_ROOT / "apps" / "web" / "public" / "search-index.json"
    rows = _load_json(search_path, errors)
    if isinstance(rows, list):
        keys: set[tuple[str, str]] = set()
        for row in rows:
            if not isinstance(row, dict):
                errors.append("search-index.json contains a non-object row")
                continue
            key = (str(row.get("lang", "")), str(row.get("date", "")))
            if key in keys:
                errors.append(f"search-index.json contains duplicate public issue for {key}")
            keys.add(key)
        for lang in ("zh", "en"):
            if (lang, str(publish_date)) not in keys:
                errors.append(f"search-index.json missing {lang} issue for {publish_date}")
    sitemap = REPO_ROOT / "apps" / "web" / "public" / "sitemap.xml"
    sitemap_text = sitemap.read_text(encoding="utf-8", errors="ignore") if sitemap.exists() else ""
    if not sitemap_text:
        errors.append("Missing sitemap.xml")
    for lang in ("zh", "en"):
        for page_type in ("brief", "sources"):
            doc = docs.get(lang, {}).get(page_type)
            if doc and f"/{lang}/daily/{doc[1].get('slug')}/" not in sitemap_text:
                errors.append(f"sitemap.xml missing {lang}/{page_type} slug {doc[1].get('slug')}")


def _check_published_dates(actual_date: date, papers: list[dict], errors: list[str]) -> None:
    wrong: list[str] = []
    for row in papers:
        if not isinstance(row, dict):
            wrong.append("<non-object>")
            continue
        arxiv_id = str(row.get("arxiv_id") or row.get("id") or "<missing-id>")
        published_at = str(row.get("published_at") or "")
        if not published_at.startswith(str(actual_date)):
            wrong.append(f"{arxiv_id}:{published_at or '<missing-published_at>'}")
        if len(wrong) >= 5:
            break
    if wrong:
        errors.append(f"processed papers must be from actual_date {actual_date}; mismatches: {', '.join(wrong)}")


def _paper_ids(rows) -> list[str]:
    if not isinstance(rows, list):
        return []
    return [str(row.get("arxiv_id") or row.get("id") or "") for row in rows if isinstance(row, dict) and (row.get("arxiv_id") or row.get("id"))]


def _scored_ids(rows) -> list[str]:
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


def _ids(text: str) -> list[str]:
    return list(dict.fromkeys(ARXIV_ID_RE.findall(text)))


def _source_selected_ids(body: str) -> list[str]:
    start = re.search(r"\n##\s+(入选论文|Selected papers)\b", body)
    if start:
        body = body[start.start():]
    end = re.search(r"\n##\s+(候选池样例|Candidate pool sample)\b", body)
    if end:
        body = body[: end.start()]
    return _ids(body)


def _check_report_count(report: dict, keys: list[str], expected: int, errors: list[str]) -> None:
    for key in keys:
        if report.get(key) is not None:
            if int(report.get(key) or -1) != expected:
                errors.append(f"run report {key} mismatch: {report.get(key)} != {expected}")
            return
    errors.append(f"run report missing count field; expected one of {keys}")


def _check_ids(report: dict, key: str, expected: list[str], errors: list[str]) -> None:
    if report.get(key) is not None and list(report.get(key) or []) != expected:
        errors.append(f"run report {key} does not match actual source files")


def _parse_markdown(path: Path, errors: list[str]) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"Missing frontmatter: {_rel(path)}")
        return None
    meta: dict = {}
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


def _check_mock_text(text: str, path: Path, errors: list[str]) -> None:
    if MOCK_IDS_RE.search(text):
        errors.append(f"Mock arXiv ID 2606.000xx found in production content/source: {_rel(path)}")
    for pattern in MOCK_STRONG_TEXT:
        if re.search(pattern, text, re.I):
            errors.append(f"Mock fixture text matched {pattern}: {_rel(path)}")
    matched_authors = [pattern for pattern in MOCK_FIXTURE_AUTHOR_NAMES if re.search(pattern, text, re.I)]
    if len(matched_authors) >= MOCK_AUTHOR_CLUSTER_THRESHOLD:
        errors.append(f"Mock fixture author cluster matched {len(matched_authors)} names in {_rel(path)}: {', '.join(matched_authors[:6])}")


def _parse_date(value, name: str, errors: list[str]) -> date | None:
    try:
        return date.fromisoformat(str(value))
    except Exception:
        errors.append(f"Invalid {name}: {value!r}")
        return None


def _load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Missing JSON: {_rel(path)}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON {_rel(path)}: {exc}")
    return None


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _finish(errors: list[str]) -> int:
    if errors:
        print("candidate_lineage_guard=failed")
        for item in errors:
            print(f"::error::{item}")
        return 1
    print("candidate_lineage_guard=passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
