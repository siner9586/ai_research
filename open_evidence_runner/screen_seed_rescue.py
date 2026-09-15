from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import re
import sqlite3
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)
ARXIV_PREFIX = re.compile(r"^(?:arxiv:\s*|https?://arxiv\.org/(?:abs|pdf)/)", re.I)

PATTERNS = {
    "ai": r"\b(?:artificial intelligence|machine learning|deep learning|neural network|neural model|transformer|bert|roberta|gpt|large language model|llm|algorithmic|automated decision|automation|decision support|human[- ]ai|human[- ]robot|robotic|ai)\b|人工智能|机器学习|深度学习|神经网络|大语言模型|人机|算法",
    "explanation": r"\b(?:explainable|explanation|explanations|interpretability|interpretable|attribution|saliency|shap|lime|integrated gradients|counterfactual|rationale|feature importance|attention rollout|mechanistic interpretability)\b|可解释|解释|归因|反事实",
    "ebi": r"\b(?:faithfulness|fidelity|infidelity|stability|robustness|sensitivity[- ]?n|comprehensiveness|sufficiency|completeness|explanation uncertainty|mechanistic alignment|causal alignment|plausibility[- ]faithfulness|attribution disagreement|simulatability|predict model behavior)\b|解释忠实|解释稳定|解释完整|解释敏感|机制对齐|归因一致",
    "behavior": r"\b(?:appropriate reliance|overreliance|underreliance|reliance|trust|trust calibration|calibrated trust|automation bias|advice taking|algorithm aversion|algorithm appreciation|algorithmic advice|ai advice|decision switching|verification|delegation|decision making|decision-making|decision performance|human[- ]ai collaboration|team performance|user study)\b|适当依赖|过度依赖|依赖不足|信任|自动化偏差|算法建议|算法厌恶|算法欣赏|采纳|复核|授权|决策",
    "human": r"\b(?:human|humans|participant|participants|user|users|respondent|respondents|worker|workers|clinician|clinicians|physician|physicians|patient|patients|manager|managers|professional|professionals|expert|experts|student|students|crowdworker|mturk|prolific)\b|参与者|受试者|用户|管理者|专业人员|医生|患者|学生|人类",
    "study": r"\b(?:experiment|experimental|randomized|randomised|trial|study|studies|survey|user study|human subjects|between-subjects|within-subjects)\b|实验|随机|研究|调查",
    "domain": r"\b(?:management|managerial|organization|organizational|executive|professional|audit|accounting|bankruptcy|credit|finance|financial|investment|marketing|operations|supply chain|forecasting|hiring|recruitment|healthcare|medical|clinical|legal|judicial|risk management|intelligence analyst|symptom checker|prescribing|diagnosis|screening)\b|管理|组织|审计|会计|破产|信贷|金融|投资|营销|运营|供应链|预测|招聘|医疗|临床|法律|司法|风险",
    "resource": r"\b(?:participant[- ]level data|trial[- ]level data|raw data|open data|dataset|data availability|code availability|replication package|preregistration|osf|zenodo|github|dataverse|figshare|dryad|openicpsr)\b|开放数据|参与者级数据|试次级数据|复现包|代码",
}


def normalize_doi(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    return DOI_PREFIX.sub("", value.strip()).lower() or None


def normalize_arxiv(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = ARXIV_PREFIX.sub("", value.strip())
    text = re.sub(r"\.pdf$", "", text, flags=re.I)
    return re.sub(r"v\d+$", "", text, flags=re.I).lower() or None


def normalize_title(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    value = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(re.sub(r"[\W_]+", " ", value, flags=re.UNICODE).split())


def find_one(root: Path, name: str) -> Path:
    matches = list(root.rglob(name))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one {name}, found {len(matches)} under {root}")
    return matches[0]


def json_string(value: Any, empty: Any) -> str:
    if isinstance(value, type(empty)):
        return json.dumps(value, ensure_ascii=False)
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return json.dumps(empty, ensure_ascii=False)
    return json.dumps(value, ensure_ascii=False)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_frame(path: Path) -> pd.DataFrame:
    return pd.read_json(path, lines=True, compression="gzip")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--original-root", type=Path, required=True)
    parser.add_argument("--rescue-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    original_path = find_one(args.original_root, "semantic_scholar_all_paper_master.jsonl.gz")
    rescue_path = find_one(args.rescue_root, "semantic_scholar_seed_rescue_master.jsonl.gz")
    original = load_frame(original_path)
    rescue = load_frame(rescue_path)

    original["doi_norm"] = original["doi_normalized"].map(normalize_doi)
    original["arxiv_norm"] = original["arxiv_id"].map(normalize_arxiv)
    original["title_norm"] = original["canonical_title"].map(normalize_title)
    original_s2 = set(original["s2_paper_id"].dropna().astype(str).str.lower())
    original_doi = set(original["doi_norm"].dropna())
    original_arxiv = set(original["arxiv_norm"].dropna())
    original_title = set(original.loc[original["title_norm"].ne(""), "title_norm"])

    rescue["doi_norm"] = rescue["doi_normalized"].map(normalize_doi)
    rescue["arxiv_norm"] = rescue["arxiv_id"].map(normalize_arxiv)
    rescue["title_norm"] = rescue["canonical_title"].map(normalize_title)
    duplicate_reason = np.select(
        [
            rescue["s2_paper_id"].fillna("").astype(str).str.lower().isin(original_s2),
            rescue["doi_norm"].notna() & rescue["doi_norm"].isin(original_doi),
            rescue["arxiv_norm"].notna() & rescue["arxiv_norm"].isin(original_arxiv),
            rescue["title_norm"].ne("") & rescue["title_norm"].isin(original_title),
        ],
        ["s2_paper_id", "doi", "arxiv_id", "normalized_title"],
        default="",
    )
    rescue["duplicate_reason"] = duplicate_reason
    new = rescue[rescue["duplicate_reason"].eq("")].copy()

    text = (new["canonical_title"].fillna("") + "\n" + new["abstract"].fillna("")).astype(str)
    signals = pd.DataFrame(
        {
            name: text.str.contains(pattern, case=False, regex=True, na=False)
            for name, pattern in PATTERNS.items()
        },
        index=new.index,
    )
    layer_a = signals.ai & signals.behavior & signals.human & signals.study
    layer_b = signals.explanation & signals.behavior & signals.human & signals.study
    layer_c = signals.explanation & signals.ebi & signals.ai
    layer_d = signals.domain & signals.ai & (signals.behavior | signals.explanation) & (signals.human | signals.study)
    include = layer_a | layer_b | layer_c | layer_d
    uncertain = (~include) & (
        (signals.ai & (signals.explanation | signals.behavior | signals.ebi | signals.domain))
        | (signals.explanation & signals.behavior)
    )
    decision = np.where(include, "include", np.where(uncertain, "uncertain", "exclude"))
    layer_matrix = np.column_stack([layer_a, layer_b, layer_c, layer_d])
    labels = np.array(["A", "B", "C", "D"])
    layers = [json.dumps(labels[row].tolist()) for row in layer_matrix]
    signal_count = signals.sum(axis=1).to_numpy()
    confidence = np.where(
        include,
        np.minimum(0.98, 0.68 + 0.05 * layer_matrix.sum(axis=1) + 0.025 * signal_count),
        np.where(uncertain, np.minimum(0.82, 0.50 + 0.04 * signal_count), np.where(signal_count == 0, 0.92, 0.78)),
    )

    candidate_id = np.where(
        new["doi_norm"].notna(),
        "doi:" + new["doi_norm"].fillna(""),
        np.where(
            new["arxiv_norm"].notna(),
            "arxiv:" + new["arxiv_norm"].fillna(""),
            np.where(
                new["s2_paper_id"].notna(),
                "s2:" + new["s2_paper_id"].fillna("").astype(str).str.lower(),
                "title:" + new["title_norm"],
            ),
        ),
    )
    new["candidate_id"] = candidate_id

    candidates = pd.DataFrame(
        {
            "candidate_id": new.candidate_id,
            "source_name": "Semantic Scholar rescue",
            "source_external_id": new.source_external_id,
            "canonical_title": new.canonical_title,
            "abstract": new.abstract,
            "publication_date": new.publication_date,
            "publication_year": new.publication_year,
            "work_type": new.work_type.map(lambda x: json_string(x, [])),
            "language": new.language,
            "venue": new.venue,
            "publisher": new.publisher,
            "doi_normalized": new.doi_norm,
            "arxiv_id": new.arxiv_norm,
            "s2_paper_id": new.s2_paper_id,
            "pmid": new.pmid,
            "openalex_id": None,
            "authors": new.authors.map(lambda x: json_string(x, [])),
            "query_groups": new.query_groups.map(lambda x: json_string(x, [])),
            "query_texts": new.query_texts.map(lambda x: json_string(x, [])),
            "source_url": new.url,
            "is_oa": new.is_oa,
            "oa_pdf_url": new.oa_pdf_url,
            "oa_status": new.oa_status,
            "license": new.license,
            "citation_count": new.citation_count,
            "reference_count": new.reference_count,
            "fields_of_study": new.fields_of_study.map(lambda x: json_string(x, [])),
            "external_ids": new.external_ids.map(lambda x: json_string(x, {})),
            "fulltext_status": "not_assessed",
            "source_api_status": "official_supplemental_search_completed",
            "import_batch_id": "s2-rescue-20260724",
        },
        index=new.index,
    )

    evidence = []
    reasons = []
    for row_index, (state, title, abstract) in enumerate(
        zip(decision, new.canonical_title.fillna("").astype(str), new.abstract.fillna("").astype(str))
    ):
        active = signals.columns[signals.iloc[row_index].to_numpy()].tolist()
        reasons.append(json.dumps(["signals:" + ",".join(active)], ensure_ascii=False))
        items = [{"claim": "title", "quote_or_paraphrase": title[:500]}]
        if state != "exclude" and abstract:
            items.append({"claim": "abstract", "quote_or_paraphrase": abstract[:500]})
        evidence.append(json.dumps(items, ensure_ascii=False))

    screening = pd.DataFrame(
        {
            "candidate_id": new.candidate_id,
            "screening_stage": "title_abstract_machine_v2",
            "reviewer": "deterministic_layered_recall_v2",
            "decision": decision,
            "corpus_layers": layers,
            "reasons": reasons,
            "exclusion_code": np.where(decision == "exclude", "NO_SUBSTANTIVE_LINK", None),
            "evidence": evidence,
            "confidence": np.round(confidence, 3),
            "requires_adjudication": decision == "uncertain",
            "technical_score": signals.explanation.astype(int) + signals.ebi.astype(int),
            "behavior_score": signals.behavior.astype(int) + signals.human.astype(int) + signals.study.astype(int),
            "professional_score": signals.domain.astype(int),
            "resource_score": signals.resource.astype(int),
            "governance_score": (signals.behavior & signals.domain).astype(int),
            "run_id": "s2-rescue-screen-20260724",
        },
        index=new.index,
    )

    selected = screening.decision.ne("exclude")
    outputs = {
        "candidate_records_s2_rescue.csv.gz": candidates,
        "screening_decisions_s2_rescue.csv.gz": screening,
        "candidate_records_selected.csv.gz": candidates[selected],
        "screening_decisions_selected.csv.gz": screening[selected],
    }
    for file_name, frame in outputs.items():
        frame.to_csv(args.output / file_name, index=False, compression="gzip")

    sqlite_path = args.output / "s2_rescue_selected.sqlite"
    with sqlite3.connect(sqlite_path) as connection:
        candidates[selected].to_sql("candidate_records", connection, index=False, chunksize=1000)
        screening[selected].to_sql("screening_decisions", connection, index=False, chunksize=1000)
        connection.execute("CREATE UNIQUE INDEX ux_candidate_id ON candidate_records(candidate_id)")
        connection.execute("CREATE INDEX ix_screen_decision ON screening_decisions(decision)")
        connection.execute("CREATE INDEX ix_publication_year ON candidate_records(publication_year)")

    duplicate_counts = Counter(rescue.loc[rescue.duplicate_reason.ne(""), "duplicate_reason"])
    query_counts = Counter(value for values in new.query_groups for value in (values if isinstance(values, list) else []))
    summary = {
        "run_id": "s2-rescue-normalize-screen-20260724",
        "original_unique_records": int(len(original)),
        "rescue_unique_records": int(len(rescue)),
        "duplicates_against_original": int(sum(duplicate_counts.values())),
        "duplicate_match_methods": {key: int(value) for key, value in duplicate_counts.items()},
        "new_unique_candidates": int(len(candidates)),
        "screening_status": {key: int(value) for key, value in screening.decision.value_counts().items()},
        "selected_for_candidate_import": int(selected.sum()),
        "corpus_layers": {
            "A": int(layer_a.sum()),
            "B": int(layer_b.sum()),
            "C": int(layer_c.sum()),
            "D": int(layer_d.sum()),
        },
        "query_record_counts": {key: int(value) for key, value in query_counts.items()},
        "screening_method": "deterministic_layered_recall_v2",
        "second_review_status": "pending",
        "integrity_note": "Rescue candidates remain separate from original official partition counts and require independent screening and adjudication.",
    }
    summary_path = args.output / "normalization_screening_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    files = sorted(path for path in args.output.iterdir() if path.is_file())
    (args.output / "sha256sums.txt").write_text(
        "".join(f"{file_sha256(path)}  {path.name}\n" for path in files), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
