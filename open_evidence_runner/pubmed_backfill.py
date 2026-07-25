from __future__ import annotations

import argparse
import calendar
import csv
import gzip
import hashlib
import json
import os
import random
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
BATCH_SIZE = 200
MAX_HISTORY_COUNT = 9000
DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_gzip_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as handle:
        handle.write(payload)


def normalize_doi(value: str | None) -> str | None:
    if not value or not value.strip():
        return None
    return DOI_PREFIX.sub("", value).strip().lower() or None


def text_content(node: ET.Element | None) -> str | None:
    if node is None:
        return None
    text = "".join(node.itertext())
    normalized = " ".join(text.split())
    return normalized or None


def make_session() -> requests.Session:
    retry = Retry(
        total=10,
        connect=10,
        read=10,
        status=10,
        backoff_factor=2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "POST"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {
            "User-Agent": "ExplainabilityBiasOpenEvidence/1.0 PubMed systematic review",
            "Accept": "application/json, application/xml, text/xml",
        }
    )
    return session


def common_params() -> dict[str, str]:
    params = {
        "tool": os.getenv("NCBI_TOOL", "ExplainabilityBiasOpenEvidence"),
        "email": os.getenv("NCBI_EMAIL", "open-evidence@example.invalid"),
    }
    api_key = os.getenv("NCBI_API_KEY")
    if api_key:
        params["api_key"] = api_key
    return params


def polite_sleep() -> None:
    delay = 0.12 if os.getenv("NCBI_API_KEY") else 0.42
    time.sleep(delay + random.random() * 0.08)


def date_term(query: str, start_date: str, end_date: str) -> str:
    return (
        f"({query}) AND (\"{start_date}\"[Date - Publication] : "
        f"\"{end_date}\"[Date - Publication])"
    )


def yearly_window(year: int) -> tuple[str, str, str]:
    return f"{year}-year", f"{year}/01/01", f"{year}/12/31"


def monthly_windows(year: int) -> list[tuple[str, str, str]]:
    windows = []
    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]
        windows.append(
            (
                f"{year}-{month:02d}",
                f"{year}/{month:02d}/01",
                f"{year}/{month:02d}/{last_day:02d}",
            )
        )
    return windows


def esearch(
    session: requests.Session,
    query: str,
    start_date: str,
    end_date: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    params: dict[str, Any] = {
        "db": "pubmed",
        "term": date_term(query, start_date, end_date),
        "usehistory": "y",
        "retmax": 0,
        "retmode": "json",
        **common_params(),
    }
    response = session.post(ESEARCH, data=params, timeout=(30, 180))
    if response.status_code != 200:
        raise RuntimeError(f"esearch_http_{response.status_code}:{response.text[:500]}")
    payload = response.json()
    result = payload.get("esearchresult") or {}
    parsed = {
        "count": int(result.get("count") or 0),
        "query_key": result.get("querykey"),
        "webenv": result.get("webenv"),
        "query_translation": result.get("querytranslation"),
        "warning_list": result.get("warninglist") or {},
        "error_list": result.get("errorlist") or {},
    }
    return payload, parsed


def extract_article(article: ET.Element, query_group: str, query_text: str) -> dict[str, Any]:
    citation = article.find("MedlineCitation")
    pubmed_data = article.find("PubmedData")
    article_node = citation.find("Article") if citation is not None else None
    pmid = text_content(citation.find("PMID")) if citation is not None else None
    title = text_content(article_node.find("ArticleTitle")) if article_node is not None else None

    abstract_parts: list[str] = []
    if article_node is not None:
        for node in article_node.findall("Abstract/AbstractText"):
            value = text_content(node)
            if value:
                label = node.attrib.get("Label")
                abstract_parts.append(f"{label}: {value}" if label else value)

    authors: list[str] = []
    if article_node is not None:
        for author in article_node.findall("AuthorList/Author"):
            collective = text_content(author.find("CollectiveName"))
            if collective:
                authors.append(collective)
                continue
            fore = text_content(author.find("ForeName"))
            last = text_content(author.find("LastName"))
            name = " ".join(part for part in (fore, last) if part)
            if name:
                authors.append(name)

    ids: dict[str, str] = {}
    if pubmed_data is not None:
        for node in pubmed_data.findall("ArticleIdList/ArticleId"):
            value = text_content(node)
            id_type = (node.attrib.get("IdType") or "").lower()
            if value and id_type:
                ids[id_type] = value

    journal = text_content(article_node.find("Journal/Title")) if article_node is not None else None
    journal_issue = article_node.find("Journal/JournalIssue") if article_node is not None else None
    pub_date = journal_issue.find("PubDate") if journal_issue is not None else None
    year_text = text_content(pub_date.find("Year")) if pub_date is not None else None
    medline_date = text_content(pub_date.find("MedlineDate")) if pub_date is not None else None
    publication_year = int(year_text) if year_text and year_text.isdigit() else None
    if publication_year is None and medline_date:
        match = re.search(r"(?:19|20)\d{2}", medline_date)
        publication_year = int(match.group()) if match else None

    publication_types = []
    if article_node is not None:
        publication_types = [
            value
            for node in article_node.findall("PublicationTypeList/PublicationType")
            if (value := text_content(node))
        ]
    mesh_terms = []
    if citation is not None:
        mesh_terms = [
            value
            for node in citation.findall("MeshHeadingList/MeshHeading/DescriptorName")
            if (value := text_content(node))
        ]
    languages = []
    if article_node is not None:
        languages = [
            value
            for node in article_node.findall("Language")
            if (value := text_content(node))
        ]

    return {
        "source_name": "PubMed",
        "source_external_id": pmid,
        "pmid": pmid,
        "pmcid": ids.get("pmc"),
        "doi_normalized": normalize_doi(ids.get("doi")),
        "pii": ids.get("pii"),
        "canonical_title": title,
        "abstract": "\n".join(abstract_parts) or None,
        "publication_year": publication_year,
        "publication_date_text": medline_date or year_text,
        "venue": journal,
        "authors": authors,
        "publication_types": publication_types,
        "mesh_terms": mesh_terms,
        "languages": languages,
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else None,
        "query_groups": [query_group],
        "query_texts": [query_text],
        "retrieved_at": utcnow(),
    }


def parse_pubmed_xml(payload: bytes, query_group: str, query_text: str) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    return [extract_article(node, query_group, query_text) for node in root.findall("PubmedArticle")]


def fetch_history(
    session: requests.Session,
    root: Path,
    year: int,
    query_group: str,
    query_text: str,
    window_name: str,
    count: int,
    query_key: str,
    webenv: str,
) -> tuple[int, int]:
    folder = root / "normalized" / "pubmed" / str(year) / query_group
    output = folder / f"{window_name}.jsonl.gz"
    pages = 0
    records = 0
    with gzip.open(output, "wt", encoding="utf-8") as normalized:
        for retstart in range(0, count, BATCH_SIZE):
            params: dict[str, Any] = {
                "db": "pubmed",
                "query_key": query_key,
                "WebEnv": webenv,
                "retstart": retstart,
                "retmax": BATCH_SIZE,
                "retmode": "xml",
                **common_params(),
            }
            response = session.post(EFETCH, data=params, timeout=(30, 240))
            if response.status_code != 200:
                raise RuntimeError(
                    f"efetch_http_{response.status_code}:{response.text[:500]}"
                )
            pages += 1
            raw_path = (
                root
                / "raw"
                / "pubmed"
                / str(year)
                / query_group
                / window_name
                / f"batch_{pages:06d}.xml.gz"
            )
            write_gzip_bytes(raw_path, response.content)
            items = parse_pubmed_xml(response.content, query_group, query_text)
            for item in items:
                normalized.write(json.dumps(item, ensure_ascii=False) + "\n")
            records += len(items)
            polite_sleep()
    return pages, records


def process_window(
    session: requests.Session,
    root: Path,
    year: int,
    query_group: str,
    query_text: str,
    window: tuple[str, str, str],
) -> dict[str, Any]:
    window_name, start_date, end_date = window
    checkpoint = root / "checkpoints" / "pubmed" / str(year) / query_group / f"{window_name}.json"
    if checkpoint.exists():
        previous = json.loads(checkpoint.read_text(encoding="utf-8"))
        if previous.get("completed"):
            return previous

    started_at = utcnow()
    raw_search, search = esearch(session, query_text, start_date, end_date)
    search_path = (
        root
        / "raw"
        / "pubmed"
        / str(year)
        / query_group
        / window_name
        / "esearch.json"
    )
    save_json(search_path, raw_search)
    polite_sleep()
    count = int(search["count"])
    if count > MAX_HISTORY_COUNT:
        result = {
            "window": window_name,
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "pages_completed": 0,
            "records_found": 0,
            "completed": False,
            "error": "window_exceeds_9000_requires_finer_partition",
            "query_translation": search.get("query_translation"),
            "started_at": started_at,
            "finished_at": utcnow(),
        }
        save_json(checkpoint, result)
        return result
    if count == 0:
        result = {
            "window": window_name,
            "start_date": start_date,
            "end_date": end_date,
            "count": 0,
            "pages_completed": 0,
            "records_found": 0,
            "completed": True,
            "error": None,
            "query_translation": search.get("query_translation"),
            "started_at": started_at,
            "finished_at": utcnow(),
        }
        save_json(checkpoint, result)
        return result
    if not search.get("query_key") or not search.get("webenv"):
        raise RuntimeError("esearch_history_missing_query_key_or_webenv")
    pages, records = fetch_history(
        session,
        root,
        year,
        query_group,
        query_text,
        window_name,
        count,
        str(search["query_key"]),
        str(search["webenv"]),
    )
    result = {
        "window": window_name,
        "start_date": start_date,
        "end_date": end_date,
        "count": count,
        "pages_completed": pages,
        "records_found": records,
        "completed": records == count,
        "error": None if records == count else "record_count_mismatch",
        "query_translation": search.get("query_translation"),
        "started_at": started_at,
        "finished_at": utcnow(),
    }
    save_json(checkpoint, result)
    return result


def process_query(
    session: requests.Session,
    root: Path,
    year: int,
    query_group: str,
    query_text: str,
) -> dict[str, Any]:
    full_window = yearly_window(year)
    _, start_date, end_date = full_window
    preview_raw, preview = esearch(session, query_text, start_date, end_date)
    preview_path = root / "raw" / "pubmed" / str(year) / query_group / "year_preview_esearch.json"
    save_json(preview_path, preview_raw)
    polite_sleep()
    windows = monthly_windows(year) if int(preview["count"]) > MAX_HISTORY_COUNT else [full_window]
    window_results = [
        process_window(session, root, year, query_group, query_text, window)
        for window in windows
    ]
    return {
        "query_group": query_group,
        "query_text": query_text,
        "year_preview_count": int(preview["count"]),
        "partition_mode": "monthly" if len(windows) == 12 else "yearly",
        "windows_expected": len(windows),
        "windows_completed": sum(bool(item["completed"]) for item in window_results),
        "pages_completed": sum(int(item["pages_completed"]) for item in window_results),
        "records_found": sum(int(item["records_found"]) for item in window_results),
        "completed": all(item["completed"] for item in window_results),
        "errors": [item for item in window_results if item["error"]],
    }


def merge_year(root: Path, year: int) -> tuple[int, Path]:
    records: dict[str, dict[str, Any]] = {}
    base = root / "normalized" / "pubmed" / str(year)
    for path in sorted(base.rglob("*.jsonl.gz")):
        if path.name == "paper_master_pubmed.jsonl.gz":
            continue
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = item.get("pmid") or item.get("doi_normalized") or hashlib.sha256(
                    json.dumps(item, sort_keys=True).encode("utf-8")
                ).hexdigest()
                if key in records:
                    records[key]["query_groups"] = sorted(
                        set(records[key].get("query_groups") or [])
                        | set(item.get("query_groups") or [])
                    )
                    records[key]["query_texts"] = sorted(
                        set(records[key].get("query_texts") or [])
                        | set(item.get("query_texts") or [])
                    )
                    for field in ("abstract", "doi_normalized", "pmcid", "mesh_terms"):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    output = base / "paper_master_pubmed.jsonl.gz"
    output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        for key in sorted(records):
            handle.write(json.dumps(records[key], ensure_ascii=False) + "\n")
    return len(records), output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--queries", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    queries = json.loads(args.queries.read_text(encoding="utf-8"))
    if not isinstance(queries, dict) or not queries:
        raise SystemExit("query configuration is empty")

    started_at = utcnow()
    session = make_session()
    results = []
    for query_group, query_text in queries.items():
        try:
            results.append(
                process_query(session, args.output, args.year, query_group, query_text)
            )
        except Exception as exc:
            results.append(
                {
                    "query_group": query_group,
                    "query_text": query_text,
                    "completed": False,
                    "pages_completed": 0,
                    "records_found": 0,
                    "errors": [{"error": f"{type(exc).__name__}:{exc}"}],
                }
            )

    unique_records, master = merge_year(args.output, args.year)
    manifest = args.output / "manifests" / f"pubmed_{args.year}_search_queries.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = [
            "query_group",
            "query_text",
            "year_preview_count",
            "partition_mode",
            "windows_expected",
            "windows_completed",
            "pages_completed",
            "records_found",
            "completed",
            "errors",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in results:
            copy = dict(row)
            copy["errors"] = json.dumps(copy.get("errors") or [], ensure_ascii=False)
            writer.writerow(copy)

    completed = len(results) == len(queries) and all(item.get("completed") for item in results)
    summary = {
        "run_id": f"pubmed-{args.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "PubMed",
        "year": args.year,
        "query_groups_expected": len(queries),
        "query_groups_completed": sum(bool(item.get("completed")) for item in results),
        "pages_completed": sum(int(item.get("pages_completed") or 0) for item in results),
        "raw_records": sum(int(item.get("records_found") or 0) for item in results),
        "unique_records": unique_records,
        "completed": completed,
        "started_at": started_at,
        "finished_at": utcnow(),
        "errors": [item for item in results if item.get("errors")],
        "master_path": str(master.relative_to(args.output)),
        "official_end_evidence": "ESearch count matched by EFetch records for every yearly or monthly window",
    }
    save_json(args.output / "completion" / f"pubmed_{args.year}.json", summary)
    if not completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
