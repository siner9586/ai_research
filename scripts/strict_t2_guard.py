from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
BAD_VISIBLE = [
    r"每日\s*07:12\s*更新",
    r"Daily\s+07:12",
    r"T\+2\s+ARXIV",
    r"T\+2\s+arXiv",
    r"今日重点[:：]",
    r"Today's focus:",
    r"完整候选池与评分",
    r"full candidate pool and scoring",
    r"摘要" + r"显示",
    r"建议" + r"先看每篇",
    r"重点" + r"核验",
    r"The abstract" + r" points to",
]
MOCK_VISIBLE = [
    r"Self Evolving Agents for Tool Use Skills",
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
MOCK_IDS_RE = re.compile(r"\b2606\.000(?:0[1-9]|1[0-8])\b")
MAX_EMPTY_DAY_LOOKBACK = 7


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate publication/data-date invariants for generated briefs.")
    parser.add_argument("--report", default="data/reports/runs/last-run.json")
    parser.add_argument("--skip-diff-scope", action="store_true")
    args = parser.parse_args(argv)

    errors: list[str] = []
    report_path = REPO_ROOT / args.report
    if not report_path.exists():
        errors.append(f"Missing run report: {report_path.relative_to(REPO_ROOT)}")
        return _finish(errors)

    report = _load_json(report_path, errors)
    if not isinstance(report, dict):
        errors.append(f"Run report is not an object: {report_path.relative_to(REPO_ROOT)}")
        return _finish(errors)

    publish_date = _parse_date(report.get("publish_date") or report.get("date"), "publish_date", errors)
    target_date = _parse_date(report.get("target_date"), "target_date", errors)
    actual_date = _parse_date(report.get("actual_date"), "actual_date", errors)
    if not publish_date or not target_date or not actual_date:
        return _finish(errors)

    expected_target = publish_date - timedelta(days=2)
    fallback_days = int(report.get("fallback_days") or 0)
    fallback_used = bool(report.get("fallback_used"))
    fallback_from = str(report.get("fallback_from") or "")

    if target_date != expected_target:
        errors.append(f"target_date must equal publish_date - 2 days: publish_date={publish_date} target_date={target_date} expected={expected_target}")
    if fallback_days < 0 or fallback_days > MAX_EMPTY_DAY_LOOKBACK:
        errors.append(f"fallback_days must be between 0 and {MAX_EMPTY_DAY_LOOKBACK}: {fallback_days}")
    if actual_date > target_date:
        errors.append(f"actual_date cannot be after target_date: target_date={target_date} actual_date={actual_date}")
    if actual_date < target_date:
        if not fallback_used:
            errors.append(f"fallback_used must be true when actual_date is before target_date: target_date={target_date} actual_date={actual_date}")
        if fallback_days <= 0:
            errors.append("fallback_days must be positive when using an older non-empty source date")
        if fallback_from != str(target_date):
            errors.append(f"fallback_from must equal target_date when using an older source date: fallback_from={fallback_from} target_date={target_date}")
    if actual_date == target_date and fallback_used:
        errors.append(f"fallback_used must be false when actual_date equals target_date: {actual_date}")
    if report.get("mock"):
        errors.append("production guard cannot validate a mock run")
    if int(report.get("total_candidates") or 0) <= 0:
        errors.append("run report must contain a positive total_candidates count")
    if int(report.get("deduped_papers") or 0) <= 0:
        errors.append("run report must contain a positive deduped_papers count")
    if int(report.get("candidate_count") or 0) <= 0:
        errors.append("run report must contain a positive candidate_count count")

    docs = _check_content(publish_date, target_date, actual_date, errors)
    _check_candidate_source(report, publish_date, target_date, actual_date, docs, errors)
    _check_processed(actual_date, errors)
    _check_static(publish_date, docs, errors)
    _check_no_future_public_issue(publish_date, errors)
    if not args.skip_diff_scope:
        _check_git_diff_scope(publish_date, actual_date, errors)
    return _finish(errors)


def _check_content(publish_date: date, target_date: date, actual_date: date, errors: list[str]) -> dict[str, dict[str, tuple[Path, dict, str]]]:
    docs: dict[str, dict[str, tuple[Path, dict, str]]] = {"zh": {}, "en": {}}
    for lang in ("zh", "en"):
        daily_dir = REPO_ROOT / "data" / "content" / lang / "daily"
        pages = sorted(daily_dir.glob(f"{publish_date}-*.md"))
        briefs: list[tuple[Path, dict, str]] = []
        sources: list[tuple[Path, dict, str]] = []
        for path in pages:
            parsed = _parse_markdown(path, errors)
            if not parsed:
                continue
            meta, body = parsed
            _check_doc(path, meta, body, lang, publish_date, target_date, actual_date, errors)
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


def _check_doc(path: Path, meta: dict, body: str, lang: str, publish_date: date, target_date: date, actual_date: date, errors: list[str]) -> None:
    required = ["title", "date", "target_date", "actual_date", "lang", "slug", "summary", "page_type", "candidate_count", "featured_count", "mentions_count"]
    for key in required:
        if meta.get(key) in (None, "", []):
            errors.append(f"Missing frontmatter field {key}: {path.relative_to(REPO_ROOT)}")
    if str(meta.get("date")) != str(publish_date):
        errors.append(f"date mismatch in {path.relative_to(REPO_ROOT)}: {meta.get('date')} != {publish_date}")
    if str(meta.get("target_date")) != str(target_date):
        errors.append(f"target_date mismatch in {path.relative_to(REPO_ROOT)}: {meta.get('target_date')} != {target_date}")
    if str(meta.get("actual_date")) != str(actual_date):
        errors.append(f"actual_date mismatch in {path.relative_to(REPO_ROOT)}: {meta.get('actual_date')} != {actual_date}")
    if str(meta.get("lang")) != lang:
        errors.append(f"lang mismatch in {path.relative_to(REPO_ROOT)}")
    if str(meta.get("slug")) != path.stem:
        errors.append(f"slug/path mismatch in {path.relative_to(REPO_ROOT)}")
    if int(meta.get("candidate_count") or 0) <= 0:
        errors.append(f"candidate_count must be positive in {path.relative_to(REPO_ROOT)}")
    if int(meta.get("featured_count") or 0) <= 0 and meta.get("page_type") == "brief":
        errors.append(f"featured_count must be positive in production brief: {path.relative_to(REPO_ROOT)}")
    visible = "\n".join([str(meta.get("title", "")), str(meta.get("summary", "")), body])
    for pattern in BAD_VISIBLE:
        if re.search(pattern, visible, re.I):
            errors.append(f"Deprecated visible wording matched {pattern}: {path.relative_to(REPO_ROOT)}")
    _check_no_mock_text(visible, path, publish_date, errors)


def _check_pairs(docs: dict[str, dict[str, tuple[Path, dict, str]]], errors: list[str]) -> None:
    for lang in ("zh", "en"):
        brief = docs.get(lang, {}).get("brief")
        source = docs.get(lang, {}).get("sources")
        if not brief or not source:
            continue
        brief_path, brief_meta, brief_body = brief
        source_path, source_meta, source_body = source
        for key in ["date", "target_date", "actual_date", "fallback_from", "candidate_count", "featured_count", "mentions_count"]:
            if str(brief_meta.get(key, "")) != str(source_meta.get(key, "")):
                errors.append(f"Brief/source metadata mismatch for {key}: {brief_path.relative_to(REPO_ROOT)} vs {source_path.relative_to(REPO_ROOT)}")
        if brief_meta.get("sources_page") != f"/{lang}/daily/{source_meta.get('slug')}/":
            errors.append(f"Brief sources_page does not match source slug: {brief_path.relative_to(REPO_ROOT)}")
        if source_meta.get("brief_page") != f"/{lang}/daily/{brief_meta.get('slug')}/":
            errors.append(f"Source brief_page does not match brief slug: {source_path.relative_to(REPO_ROOT)}")
        if _brief_ids(brief_body) != _source_selected_ids(source_body):
            errors.append(f"Brief/source selected arXiv IDs differ for {lang}")
    zh = docs.get("zh", {}).get("brief")
    en = docs.get("en", {}).get("brief")
    if zh and en:
        for key in ["date", "target_date", "actual_date", "candidate_count", "featured_count", "mentions_count"]:
            if str(zh[1].get(key, "")) != str(en[1].get(key, "")):
                errors.append(f"zh/en metadata mismatch for {key}")
        if _brief_ids(zh[2]) != _brief_ids(en[2]):
            errors.append("zh/en selected arXiv IDs differ")


def _check_candidate_source(
    report: dict,
    publish_date: date,
    target_date: date,
    actual_date: date,
    docs: dict[str, dict[str, tuple[Path, dict, str]]],
    errors: list[str],
) -> None:
    paths = _source_paths(report, actual_date)
    papers = _load_json(REPO_ROOT / paths["processed_papers_file"], errors)
    scored = _load_json(REPO_ROOT / paths["candidate_file"], errors)
    selected = _load_json(REPO_ROOT / paths["selected_file"], errors)
    manifest = _load_json(REPO_ROOT / paths["manifest_file"], errors) if paths.get("manifest_file") else None
    raw = _load_json(REPO_ROOT / paths["raw_candidate_file"], errors)

    if not isinstance(papers, list) or not isinstance(scored, list) or not isinstance(selected, dict):
        errors.append("candidate source files must be data/processed actual_date papers/scored/selected artifacts")
        return
    candidate_ids = _scored_json_ids(scored)
    paper_ids = _paper_json_ids(papers)
    raw_ids = _paper_json_ids(raw) if isinstance(raw, list) else []
    featured_ids = _scored_json_ids(selected.get("featured", []))
    mention_ids = _scored_json_ids(selected.get("mentions", []))
    selected_ids = featured_ids + mention_ids

    if not candidate_ids:
        errors.append(f"candidate_file has no candidate paper IDs: {paths['candidate_file']}")
    if len(candidate_ids) != len(set(candidate_ids)):
        errors.append(f"candidate_file contains duplicate IDs: {paths['candidate_file']}")
    missing_from_candidates = [paper_id for paper_id in selected_ids if paper_id not in set(candidate_ids)]
    if missing_from_candidates:
        errors.append(f"selected papers are not from the current candidate_file: {missing_from_candidates}")
    missing_from_papers = [paper_id for paper_id in candidate_ids if paper_id not in set(paper_ids)]
    if missing_from_papers:
        errors.append(f"scored candidates are not from processed papers.json: {missing_from_papers[:10]}")
    if raw_ids and set(paper_ids) - set(raw_ids):
        errors.append("processed papers contain IDs not present in raw actual_date papers.json")

    _check_report_value(report, "candidate_count", len(candidate_ids), errors)
    _check_report_value(report, "featured_count", len(featured_ids), errors)
    _check_report_value(report, "mentions_count", len(mention_ids), errors)
    if report.get("selected_ids") and list(report.get("selected_ids") or []) != selected_ids:
        errors.append("run report selected_ids do not match selected_papers.json")
    if report.get("candidate_ids") and list(report.get("candidate_ids") or []) != candidate_ids:
        errors.append("run report candidate_ids do not match scored_papers.json")

    if isinstance(manifest, dict):
        for key, expected in {
            "publish_date": str(publish_date),
            "target_date": str(target_date),
            "actual_date": str(actual_date),
            "candidate_count": len(candidate_ids),
            "featured_count": len(featured_ids),
            "mentions_count": len(mention_ids),
        }.items():
            if str(manifest.get(key)) != str(expected):
                errors.append(f"candidate_manifest {key} mismatch: {manifest.get(key)} != {expected}")
        for key, expected_ids in {
            "candidate_ids": candidate_ids,
            "featured_ids": featured_ids,
            "mention_ids": mention_ids,
            "selected_ids": selected_ids,
        }.items():
            if list(manifest.get(key) or []) != expected_ids:
                errors.append(f"candidate_manifest {key} mismatch with candidate source files")

    for lang in ("zh", "en"):
        brief = docs.get(lang, {}).get("brief")
        source = docs.get(lang, {}).get("sources")
        for doc in (brief, source):
            if not doc:
                continue
            path, meta, body = doc
            if int(meta.get("candidate_count") or -1) != len(candidate_ids):
                errors.append(f"{path.relative_to(REPO_ROOT)} candidate_count does not match current candidate_file")
            if int(meta.get("featured_count") or -1) != len(featured_ids):
                errors.append(f"{path.relative_to(REPO_ROOT)} featured_count does not match selected_papers.json")
            if int(meta.get("mentions_count") or -1) != len(mention_ids):
                errors.append(f"{path.relative_to(REPO_ROOT)} mentions_count does not match selected_papers.json")
            parsed_ids = _source_selected_ids(body) if meta.get("page_type") == "sources" else _brief_ids(body)
            if parsed_ids != selected_ids:
                errors.append(f"{path.relative_to(REPO_ROOT)} selected IDs do not match selected_papers.json")
            extra_ids = [paper_id for paper_id in parsed_ids if paper_id not in set(selected_ids)]
            if extra_ids:
                errors.append(f"{path.relative_to(REPO_ROOT)} contains IDs outside current selected_papers.json: {extra_ids}")

    _check_no_mock_text(json.dumps({"papers": papers, "scored": scored, "selected": selected}, ensure_ascii=False), REPO_ROOT / paths["candidate_file"], publish_date, errors)


def _check_report_value(report: dict, key: str, expected: int, errors: list[str]) -> None:
    if int(report.get(key) or -1) != expected:
        errors.append(f"run report {key} mismatch: {report.get(key)} != {expected}")


def _source_paths(report: dict, actual_date: date) -> dict[str, str]:
    prefix = f"data/processed/{actual_date}"
    return {
        "raw_candidate_file": str(report.get("raw_candidate_file") or f"data/raw/{actual_date}/papers.json"),
        "processed_papers_file": str(report.get("processed_papers_file") or f"{prefix}/papers.json"),
        "candidate_file": str(report.get("candidate_file") or f"{prefix}/scored_papers.json"),
        "selected_file": str(report.get("selected_file") or f"{prefix}/selected_papers.json"),
        "manifest_file": str(report.get("candidate_manifest") or f"{prefix}/candidate_manifest.json"),
    }


def _check_processed(actual_date: date, errors: list[str]) -> None:
    path = REPO_ROOT / "data" / "processed" / str(actual_date) / "papers.json"
    payload = _load_json(path, errors)
    if not isinstance(payload, list) or not payload:
        errors.append(f"Processed papers artifact must be a non-empty list: {path.relative_to(REPO_ROOT)}")
        return
    wrong: list[str] = []
    for row in payload:
        arxiv_id = str(row.get("arxiv_id") or row.get("id") or "<missing-id>") if isinstance(row, dict) else "<non-object>"
        published_at = str(row.get("published_at") or "") if isinstance(row, dict) else ""
        if not published_at.startswith(str(actual_date)):
            wrong.append(f"{arxiv_id}:{published_at or '<missing-published_at>'}")
        if len(wrong) >= 5:
            break
    if wrong:
        errors.append(f"Processed papers must match actual_date {actual_date}; mismatches: {', '.join(wrong)}")


def _check_static(publish_date: date, docs: dict[str, dict[str, tuple[Path, dict, str]]], errors: list[str]) -> None:
    public = REPO_ROOT / "apps" / "web" / "public"
    static_paths = [public / "search-index.json", public / "sitemap.xml", public / "zh" / "feed.xml", public / "en" / "feed.xml"]
    for path in static_paths:
        if not path.exists():
            errors.append(f"Missing static artifact: {path.relative_to(REPO_ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in BAD_VISIBLE:
            if re.search(pattern, text, re.I):
                errors.append(f"Static artifact contains deprecated wording matched {pattern}: {path.relative_to(REPO_ROOT)}")
        future_slug = _first_future_slug(text, publish_date)
        if future_slug:
            errors.append(f"Static artifact contains future public issue after {publish_date}: {future_slug} in {path.relative_to(REPO_ROOT)}")
    search_path = public / "search-index.json"
    if search_path.exists():
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
    sitemap = (public / "sitemap.xml").read_text(encoding="utf-8", errors="ignore") if (public / "sitemap.xml").exists() else ""
    for lang in ("zh", "en"):
        for page_type in ("brief", "sources"):
            doc = docs.get(lang, {}).get(page_type)
            if not doc:
                continue
            if f"/{lang}/daily/{doc[1].get('slug')}/" not in sitemap:
                errors.append(f"Sitemap missing {lang}/{page_type} slug {doc[1].get('slug')}")


def _check_no_future_public_issue(publish_date: date, errors: list[str]) -> None:
    for lang in ("zh", "en"):
        for path in (REPO_ROOT / "data" / "content" / lang / "daily").glob("*.md"):
            parsed = _parse_markdown(path, errors)
            if not parsed:
                continue
            meta, _body = parsed
            if meta.get("page_type") != "brief":
                continue
            value = str(meta.get("date") or "")
            if value and value > str(publish_date):
                errors.append(f"Future public brief must not be committed before the active publish date {publish_date}: {path.relative_to(REPO_ROOT)} has date {value}")


def _check_git_diff_scope(publish_date: date, actual_date: date, errors: list[str]) -> None:
    changed: set[str] = set()
    for args in (["git", "diff", "--name-only"], ["git", "diff", "--name-only", "--cached"]):
        try:
            proc = subprocess.run(args, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        except Exception:
            return
        if proc.returncode != 0:
            return
        changed.update(line.strip() for line in proc.stdout.splitlines() if line.strip())
    disallowed = sorted(path for path in changed if not _is_allowed_generated_path(path, publish_date, actual_date))
    if disallowed:
        errors.append("Generated commit scope contains disallowed non-current files: " + ", ".join(disallowed))


def _is_allowed_generated_path(path: str, publish_date: date, actual_date: date) -> bool:
    if path.startswith("apps/web/public/"):
        return True
    if path in {f"data/reports/runs/{publish_date}.json", "data/reports/runs/last-run.json", f"data/reports/qa/{publish_date}.json"}:
        return True
    if path.startswith(f"data/raw/{actual_date}/") or path.startswith(f"data/processed/{actual_date}/"):
        return True
    for lang in ("zh", "en"):
        if path.startswith(f"data/content/{lang}/daily/{publish_date}-") and path.endswith(".md"):
            return True
    return False


def _parse_markdown(path: Path, errors: list[str]) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"Missing frontmatter: {path.relative_to(REPO_ROOT)}")
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


def _brief_ids(body: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", body)))


def _source_selected_ids(body: str) -> list[str]:
    start = re.search(r"\n##\s+(入选论文|Selected papers)\b", body)
    if start:
        body = body[start.start():]
    end = re.search(r"\n##\s+(候选池样例|Candidate pool sample)\b", body)
    if end:
        body = body[: end.start()]
    return _brief_ids(body)


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


def _check_no_mock_text(text: str, path: Path, publish_date: date, errors: list[str]) -> None:
    if str(publish_date) != "2026-06-03" and MOCK_IDS_RE.search(text):
        errors.append(f"Mock arXiv ID 2606.000xx found outside 2026-06-03 content/source: {path.relative_to(REPO_ROOT)}")
    for pattern in MOCK_VISIBLE:
        if re.search(pattern, text, re.I):
            errors.append(f"Mock fixture text matched {pattern}: {path.relative_to(REPO_ROOT)}")


def _first_future_slug(text: str, publish_date: date) -> str | None:
    for match in re.finditer(r"20\d{2}-\d{2}-\d{2}", text):
        value = match.group(0)
        if value > str(publish_date):
            return value
    return None


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
        errors.append(f"Missing JSON: {path.relative_to(REPO_ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON {path.relative_to(REPO_ROOT)}: {exc}")
    return None


def _finish(errors: list[str]) -> int:
    if errors:
        print("strict_t2_guard=failed")
        for item in errors:
            print(f"::error::{item}")
        return 1
    print("strict_t2_guard=passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
