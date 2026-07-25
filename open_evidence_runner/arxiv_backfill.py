from __future__ import annotations

import argparse
import csv
import gzip
import json
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

API = "https://export.arxiv.org/api/query"
PAGE_SIZE = 500
CATEGORIES = "(cat:cs.AI OR cat:cs.CL OR cat:cs.CV OR cat:cs.HC OR cat:cs.LG OR cat:cs.SE OR cat:stat.ML OR cat:econ.EM OR cat:q-fin.*)"
QUERIES = {
    "Q01_XAI_FAITHFULNESS": '(all:"explanation faithfulness" OR all:"explanation fidelity" OR all:"attribution faithfulness" OR all:"explanation infidelity")',
    "Q02_XAI_STABILITY": '(all:"explanation stability" OR all:"explanation robustness" OR all:"attribution stability" OR all:"attribution robustness")',
    "Q03_XAI_COMPLETENESS": '(all:"explanation completeness" OR all:"explanation sufficiency" OR all:"explanation coverage" OR all:"completeness explainable AI")',
    "Q04_XAI_MECHANISTIC_ALIGNMENT": '(all:"mechanistic interpretability" OR all:"mechanistic alignment" OR all:"plausibility faithfulness" OR all:"plausibility-faithfulness gap")',
    "Q05_HUMAN_AI_RELIANCE": '(all:"appropriate reliance" OR all:overreliance OR all:underreliance OR all:"human AI reliance")',
    "Q06_ALGORITHMIC_ADVICE": '(all:"algorithmic advice" OR all:"AI advice" OR all:"advice taking" OR all:"artificial intelligence advice")',
    "Q07_AUTOMATION_BIAS": '(all:"automation bias" OR all:"error induction" OR all:"automation induced error")',
    "Q08_TRUST_CALIBRATION": '(all:"trust calibration" OR all:"calibrated trust" OR all:"trust in AI")',
    "Q09_PROFESSIONAL_DECISION": '(all:"AI assisted decision" OR all:"AI decision support" OR all:"professional decision")',
    "Q10_MANAGEMENT_ORGANIZATION": '(all:management OR all:managerial OR all:organizational OR all:governance) AND (all:AI OR all:"artificial intelligence") AND (all:decision OR all:explanation)',
    "Q11_TRANSFORMER_EXPLANATION": '(all:Transformer OR all:BERT OR all:GPT OR all:"attention rollout") AND (all:explanation OR all:attribution)',
    "Q12_LLM_EXPLANATION": '(all:"large language model" OR all:LLM) AND (all:"explanation faithfulness" OR all:explanation OR all:rationale)',
    "Q13_OPEN_DATA_REPLICATION": '(all:"participant level data" OR all:"trial level data" OR all:"replication package" OR all:"open data") AND (all:XAI OR all:"human AI" OR all:"explainable AI")',
    "Q14_CHINESE_XAI": '(all:可解释人工智能 OR all:解释忠实性 OR all:解释稳定性 OR all:解释偏差)',
    "Q15_CHINESE_HUMAN_AI": '(all:人机决策 OR all:算法建议 OR all:自动化偏差 OR all:适当依赖 OR all:信任校准)',
}
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
    "arxiv": "http://arxiv.org/schemas/atom",
}
ARXIV_ID = re.compile(r"(?:abs/|pdf/)([^/?#]+?)(?:\.pdf)?$")


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_text(text: str | None) -> str | None:
    if text is None:
        return None
    return " ".join(text.split())


def make_session() -> requests.Session:
    retry = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=3,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/1.0 research", "Accept": "application/atom+xml"})
    return session


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_entry(entry: ET.Element, year: int, query_group: str, query_text: str) -> dict[str, Any]:
    entry_url = clean_text(entry.findtext("atom:id", namespaces=NS)) or ""
    match = ARXIV_ID.search(entry_url)
    versioned_id = match.group(1) if match else entry_url.rsplit("/", 1)[-1]
    base_id = re.sub(r"v\d+$", "", versioned_id)
    authors = [clean_text(author.findtext("atom:name", namespaces=NS)) for author in entry.findall("atom:author", NS)]
    categories = [node.attrib.get("term") for node in entry.findall("atom:category", NS) if node.attrib.get("term")]
    links = {node.attrib.get("rel", "alternate"): node.attrib.get("href") for node in entry.findall("atom:link", NS) if node.attrib.get("href")}
    pdf_url = next((node.attrib.get("href") for node in entry.findall("atom:link", NS) if node.attrib.get("type") == "application/pdf"), None)
    doi = clean_text(entry.findtext("arxiv:doi", namespaces=NS))
    journal_ref = clean_text(entry.findtext("arxiv:journal_ref", namespaces=NS))
    primary = entry.find("arxiv:primary_category", NS)
    return {
        "source_name": "arXiv",
        "source_external_id": base_id,
        "arxiv_id": base_id,
        "arxiv_versioned_id": versioned_id,
        "doi_normalized": doi.lower() if doi else None,
        "canonical_title": clean_text(entry.findtext("atom:title", namespaces=NS)) or "",
        "abstract": clean_text(entry.findtext("atom:summary", namespaces=NS)),
        "publication_date": clean_text(entry.findtext("atom:published", namespaces=NS)),
        "updated_date": clean_text(entry.findtext("atom:updated", namespaces=NS)),
        "publication_year": year,
        "work_type": "preprint",
        "language": None,
        "venue": journal_ref or "arXiv",
        "publisher": "arXiv",
        "authors": [a for a in authors if a],
        "landing_url": entry_url,
        "oa_pdf_url": pdf_url,
        "is_oa": True,
        "oa_status": "green",
        "license": None,
        "categories": categories,
        "primary_category": primary.attrib.get("term") if primary is not None else None,
        "links": links,
        "query_groups": [query_group],
        "query_texts": [query_text],
    }


def build_search_query(year: int, body: str) -> str:
    end = "202607242359" if year == 2026 else f"{year}12312359"
    date_range = f"submittedDate:[{year}01010000 TO {end}]"
    return f"({body}) AND {CATEGORIES} AND {date_range}"


def crawl_query(session: requests.Session, root: Path, year: int, query_group: str, body: str, deadline: float) -> dict[str, Any]:
    checkpoint = root / "checkpoints" / str(year) / f"{query_group}.json"
    prior = json.loads(checkpoint.read_text(encoding="utf-8")) if checkpoint.exists() else {}
    if prior.get("completed") and prior.get("result"):
        return prior["result"]

    start = int(prior.get("start", 0))
    pages = int(prior.get("pages", 0))
    records = int(prior.get("records", 0))
    total = prior.get("total")
    started = utcnow()
    completed = False
    error = None
    search_query = build_search_query(year, body)
    output = root / "normalized" / "arxiv" / str(year) / f"{query_group}.jsonl.gz"

    while time.monotonic() < deadline:
        response = session.get(
            API,
            params={
                "search_query": search_query,
                "start": start,
                "max_results": PAGE_SIZE,
                "sortBy": "submittedDate",
                "sortOrder": "ascending",
            },
            timeout=(30, 180),
        )
        if response.status_code != 200:
            error = f"http_{response.status_code}:{response.text[:500]}"
            break
        raw = response.content
        pages += 1
        raw_path = root / "raw" / "arxiv" / str(year) / query_group / f"page_{pages:06d}.xml.gz"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(raw_path, "wb") as handle:
            handle.write(raw)
        try:
            feed = ET.fromstring(raw)
        except ET.ParseError as exc:
            error = f"invalid_atom:{exc}"
            break
        total_text = feed.findtext("opensearch:totalResults", default="0", namespaces=NS)
        total = int(total_text or 0)
        entries = feed.findall("atom:entry", NS)
        output.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(output, "at", encoding="utf-8") as handle:
            for entry in entries:
                handle.write(json.dumps(parse_entry(entry, year, query_group, search_query), ensure_ascii=False) + "\n")
        records += len(entries)
        start += len(entries)
        completed = not entries or start >= total
        save_json(checkpoint, {"start": start, "pages": pages, "records": records, "total": total, "completed": completed, "updated_at": utcnow()})
        if completed:
            break
        time.sleep(3.2 + random.random() * 0.8)

    if not completed and not error:
        error = "workflow_deadline_reached"
    result = {
        "query_group": query_group,
        "query_text": search_query,
        "pages_completed": pages,
        "records_found": records,
        "total_results": total,
        "cursor_start": 0,
        "cursor_end": start,
        "completed": completed,
        "started_at": started,
        "finished_at": utcnow(),
        "error": error,
    }
    save_json(checkpoint, {"start": start, "pages": pages, "records": records, "total": total, "completed": completed, "result": result, "updated_at": utcnow()})
    return result


def merge_year(root: Path, year: int) -> tuple[int, Path]:
    records: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "normalized" / "arxiv" / str(year)).glob("Q*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = item["arxiv_id"]
                if key in records:
                    records[key]["query_groups"] = sorted(set(records[key]["query_groups"]) | set(item["query_groups"]))
                    records[key]["query_texts"] = sorted(set(records[key]["query_texts"]) | set(item["query_texts"]))
                    if (item.get("updated_date") or "") > (records[key].get("updated_date") or ""):
                        keep_groups = records[key]["query_groups"]
                        keep_queries = records[key]["query_texts"]
                        records[key] = item
                        records[key]["query_groups"] = keep_groups
                        records[key]["query_texts"] = keep_queries
                else:
                    records[key] = item
    output = root / "normalized" / "arxiv" / str(year) / "paper_master_arxiv.jsonl.gz"
    output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        for key in sorted(records):
            handle.write(json.dumps(records[key], ensure_ascii=False) + "\n")
    return len(records), output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--hours", type=float, default=5.5)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started = utcnow()
    deadline = time.monotonic() + args.hours * 3600
    session = make_session()
    results = []
    for query_group, body in QUERIES.items():
        result = crawl_query(session, args.output, args.year, query_group, body, deadline)
        results.append(result)
        if result["error"] == "workflow_deadline_reached":
            break

    unique_records, master = merge_year(args.output, args.year)
    manifest = args.output / "manifests" / f"arxiv_{args.year}_search_queries.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    completed = len(results) == len(QUERIES) and all(item["completed"] for item in results)
    summary = {
        "run_id": f"arxiv-{args.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "arXiv",
        "year": args.year,
        "query_groups_expected": len(QUERIES),
        "query_groups_attempted": len(results),
        "query_groups_completed": sum(bool(item["completed"]) for item in results),
        "pages_completed": sum(int(item["pages_completed"]) for item in results),
        "raw_records": sum(int(item["records_found"]) for item in results),
        "unique_records": unique_records,
        "completed": completed,
        "started_at": started,
        "finished_at": utcnow(),
        "errors": [item for item in results if item["error"]],
        "master_path": str(master.relative_to(args.output)),
        "manifest_path": str(manifest.relative_to(args.output)),
    }
    summary_path = args.output / "completion" / f"arxiv_{args.year}_summary.json"
    save_json(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
