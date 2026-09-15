from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
LIMIT = 1000
FIELDS = (
    "paperId,corpusId,externalIds,title,abstract,venue,year,publicationDate,authors,"
    "citationCount,referenceCount,isOpenAccess,openAccessPdf,fieldsOfStudy,"
    "s2FieldsOfStudy,publicationTypes,journal,url"
)
QUERIES = {
    "Q01_XAI_FAITHFULNESS": '("explanation faithfulness" | "explanation fidelity" | "attribution faithfulness" | "explanation infidelity")',
    "Q02_XAI_STABILITY": '("explanation stability" | "explanation robustness" | "attribution stability" | "attribution robustness")',
    "Q03_XAI_COMPLETENESS": '("explanation completeness" | "explanation sufficiency" | "explanation coverage" | (completeness + "explainable AI"))',
    "Q04_XAI_MECHANISTIC_ALIGNMENT": '("mechanistic interpretability" | "mechanistic alignment" | "plausibility faithfulness" | "plausibility-faithfulness gap")',
    "Q05_HUMAN_AI_RELIANCE": '(("appropriate reliance" | overreliance | underreliance | "human AI reliance") + AI)',
    "Q06_ALGORITHMIC_ADVICE": '("algorithmic advice" | "AI advice" | ("advice taking" + algorithm) | "artificial intelligence advice")',
    "Q07_AUTOMATION_BIAS": '("automation bias" | ("error induction" + AI) | "automation induced error")',
    "Q08_TRUST_CALIBRATION": '(("trust calibration" | "calibrated trust" | "trust in AI") + AI)',
    "Q09_PROFESSIONAL_DECISION": '(("AI assisted decision" | "AI decision support") + (professional | medical | legal | finance))',
    "Q10_MANAGEMENT_ORGANIZATION": '((management | managerial | organizational | governance) + (AI | "artificial intelligence") + (decision | explanation | "decision support"))',
    "Q11_TRANSFORMER_EXPLANATION": '((Transformer | BERT | GPT | "attention rollout") + (explanation | attribution))',
    "Q12_LLM_EXPLANATION": '(("large language model" | LLM) + ("explanation faithfulness" | explanation | rationale))',
    "Q13_OPEN_DATA_REPLICATION": '(("participant level data" | "trial level data" | "replication package" | "open data") + (XAI | "human AI" | "explainable AI"))',
    "Q14_CHINESE_XAI": '(可解释人工智能 | 解释忠实性 | 解释稳定性 | 解释偏差)',
    "Q15_CHINESE_HUMAN_AI": '(人机决策 | 算法建议 | 自动化偏差 | 适当依赖 | 信任校准)',
}
DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_doi(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    return DOI_PREFIX.sub("", value).strip().lower()


def make_session() -> requests.Session:
    retry = Retry(
        total=10,
        connect=10,
        read=10,
        status=10,
        backoff_factor=2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    headers = {
        "User-Agent": "ExplainabilityBiasOpenEvidence/1.0 research",
        "Accept": "application/json",
    }
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key
    session.headers.update(headers)
    return session


def dump_json_gz(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False)


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_paper(item: dict[str, Any], year: int, query_group: str, query_text: str) -> dict[str, Any]:
    external = item.get("externalIds") or {}
    oa = item.get("openAccessPdf") or {}
    authors = [a.get("name") for a in item.get("authors") or [] if a.get("name")]
    journal = item.get("journal") or {}
    return {
        "source_name": "Semantic Scholar",
        "source_external_id": item.get("paperId")
        or str(item.get("corpusId"))
        or hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest(),
        "s2_paper_id": item.get("paperId"),
        "corpus_id": item.get("corpusId"),
        "doi_normalized": normalize_doi(external.get("DOI")),
        "arxiv_id": external.get("ArXiv"),
        "pmid": external.get("PubMed"),
        "openalex_id": external.get("MAG"),
        "canonical_title": " ".join((item.get("title") or "").split()),
        "abstract": item.get("abstract"),
        "publication_date": item.get("publicationDate"),
        "publication_year": item.get("year") or year,
        "work_type": item.get("publicationTypes") or [],
        "language": None,
        "venue": item.get("venue") or journal.get("name"),
        "publisher": None,
        "authors": authors,
        "url": item.get("url"),
        "is_oa": item.get("isOpenAccess"),
        "oa_pdf_url": oa.get("url"),
        "oa_status": item.get("isOpenAccess"),
        "license": oa.get("status"),
        "citation_count": item.get("citationCount"),
        "reference_count": item.get("referenceCount"),
        "fields_of_study": item.get("fieldsOfStudy") or [],
        "s2_fields_of_study": item.get("s2FieldsOfStudy") or [],
        "external_ids": external,
        "query_groups": [query_group],
        "query_texts": [query_text],
    }


def crawl_query(
    session: requests.Session,
    root: Path,
    year: int,
    query_group: str,
    query_text: str,
    deadline: float,
) -> dict[str, Any]:
    checkpoint = root / "checkpoints" / str(year) / f"{query_group}.json"
    prior = json.loads(checkpoint.read_text(encoding="utf-8")) if checkpoint.exists() else {}
    if prior.get("completed") and prior.get("result"):
        return prior["result"]

    token = prior.get("token")
    pages = int(prior.get("pages", 0))
    records = int(prior.get("records", 0))
    started = utcnow()
    completed = False
    error = None
    output = root / "normalized" / "semantic_scholar" / str(year) / f"{query_group}.jsonl.gz"

    while time.monotonic() < deadline:
        params: dict[str, Any] = {
            "query": query_text,
            "year": str(year),
            "fields": FIELDS,
            "limit": LIMIT,
        }
        if token:
            params["token"] = token
        response = session.get(API, params=params, timeout=(30, 180))
        if response.status_code != 200:
            error = f"http_{response.status_code}:{response.text[:500]}"
            break
        try:
            payload = response.json()
        except ValueError as exc:
            error = f"invalid_json:{exc}"
            break

        data = payload.get("data") or []
        pages += 1
        dump_json_gz(
            root / "raw" / "semantic_scholar" / str(year) / query_group / f"page_{pages:06d}.json.gz",
            payload,
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(output, "at", encoding="utf-8") as handle:
            for item in data:
                handle.write(json.dumps(normalize_paper(item, year, query_group, query_text), ensure_ascii=False) + "\n")
        records += len(data)
        next_token = payload.get("token")
        completed = not next_token or not data
        save_json(
            checkpoint,
            {
                "token": next_token,
                "pages": pages,
                "records": records,
                "completed": completed,
                "updated_at": utcnow(),
            },
        )
        if completed:
            token = next_token or "END_NO_TOKEN"
            break
        if next_token == token:
            error = "repeated_token"
            break
        token = next_token
        time.sleep(1.2 + random.random() * 0.5)

    if not completed and not error:
        error = "workflow_deadline_reached"
    result = {
        "query_group": query_group,
        "query_text": query_text,
        "pages_completed": pages,
        "records_found": records,
        "cursor_start": None,
        "cursor_end": token,
        "completed": completed,
        "started_at": started,
        "finished_at": utcnow(),
        "error": error,
    }
    save_json(
        checkpoint,
        {
            "token": token,
            "pages": pages,
            "records": records,
            "completed": completed,
            "result": result,
            "updated_at": utcnow(),
        },
    )
    return result


def merge_year(root: Path, year: int) -> tuple[int, Path]:
    records: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "normalized" / "semantic_scholar" / str(year)).glob("Q*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = item.get("doi_normalized") or item.get("s2_paper_id") or item["source_external_id"]
                if key in records:
                    records[key]["query_groups"] = sorted(set(records[key]["query_groups"]) | set(item["query_groups"]))
                    records[key]["query_texts"] = sorted(set(records[key]["query_texts"]) | set(item["query_texts"]))
                    for field in ("abstract", "oa_pdf_url", "venue", "authors"):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    output = root / "normalized" / "semantic_scholar" / str(year) / "paper_master_semantic_scholar.jsonl.gz"
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
    for query_group, query_text in QUERIES.items():
        result = crawl_query(session, args.output, args.year, query_group, query_text, deadline)
        results.append(result)
        if result["error"] == "workflow_deadline_reached":
            break

    unique_records, master = merge_year(args.output, args.year)
    manifest = args.output / "manifests" / f"semantic_scholar_{args.year}_search_queries.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    completed = len(results) == len(QUERIES) and all(item["completed"] for item in results)
    summary = {
        "run_id": f"semantic-scholar-{args.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "Semantic Scholar",
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
    summary_path = args.output / "completion" / f"semantic_scholar_{args.year}_summary.json"
    save_json(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
