from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any

AI = re.compile(r"\b(artificial intelligence|ai\b|algorithm(ic)?|machine learning|deep learning|neural network|automation|automated|model)\b", re.I)
XAI = re.compile(r"\b(explainable ai|xai\b|explanation(s)?|explainability|interpretability|interpretable|attribution|saliency|rationale|counterfactual|shap\b|lime\b|attention rollout|feature importance|mechanistic interpretability)\b", re.I)
QUALITY = re.compile(r"\b(faithful(ness)?|fidelity|infidelity|stability|robust(ness)?|sensitivity|completeness|comprehensiveness|sufficiency|uncertainty|mechanistic|causal alignment|plausibility|explanation quality|evaluation metric|benchmark|misleading|deceptive|deception|manipulat(e|ing|ion)|leakage)\b", re.I)
TRANSFORMER = re.compile(r"\b(transformer|bert\b|gpt\b|large language model|llm\b|attention)\b", re.I)
HUMAN = re.compile(r"\b(human|participant(s)?|user(s)?|person|people|layperson|expert(s)?|clinician(s)?|physician(s)?|manager(s)?|worker(s)?|student(s)?)\b", re.I)
DECISION = re.compile(r"\b(decision(-| )?making|decision support|judg(e)?ment|recommendation|advice|diagnos(is|tic)|forecast(ing)?|classification choice|choice|select(ion)?|adopt(ion)?|accept(ance)?|reject(ion)?|delegate|verification|verify|review)\b", re.I)
RELIANCE = re.compile(r"\b(reliance|rely|overreliance|underreliance|appropriate reliance|trust|calibrat(ed|ion)|automation bias|algorithm aversion|algorithm appreciation|advice taking|weight of advice|switch(ing)?|compliance|dependence|delegation)\b", re.I)
EMPIRICAL = re.compile(r"\b(experiment(al)?|randomi[sz]ed|user study|human study|online study|survey experiment|between[- ]subjects|within[- ]subjects|participants? (were|was|completed|recruited)|sample of|n\s*=\s*\d+|mturk|prolific)\b", re.I)
PROFESSIONAL = re.compile(r"\b(manager(ial)?|executive|organization(al)?|audit(or|ing)?|account(ing|ant)?|bankruptcy|credit|finance|financial|investment|marketing|operation(s|al)?|supply chain|forecasting|hiring|recruitment|healthcare|clinical|medical|legal|lawyer|judge|risk management|professional)\b", re.I)
OPEN_RESOURCE = re.compile(r"\b(dataset|data set|open data|repository|github|osf|zenodo|mendeley data|dataverse|figshare|dryad|replication package|participant[- ]level|trial[- ]level|code available|source code)\b", re.I)
GOVERNANCE = re.compile(r"\b(governance|accountability|responsibility|responsible ai|audit trail|contestability|oversight|escalation|incident|harm|risk management|regulation|regulatory|liability|human override)\b", re.I)
SIMULATABILITY = re.compile(r"\b(simulatability|simulate model|predict(ing)? (the )?model( behavior)?|model predictability|mental model|understand(ing)? (the )?(model|system)|debug(ging)?|detect(ing)? errors?)\b", re.I)
IRRELEVANT_TECH = re.compile(r"\b(image enhancement|noise removal|object detection|segmentation|wireless network|internet of things|power system|wind turbine|railway|crop disease|traffic flow)\b", re.I)

JSON_FIELDS = {"corpus_layers": [], "reasons": [], "evidence": []}


def blank(value: Any) -> bool:
    return value is None or str(value).strip() in {"", "nan", "NaN", "None", "null"}


def load_csv_gz(path: Path) -> list[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv_gz(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            encoded = dict(row)
            for field in JSON_FIELDS:
                if field in encoded:
                    encoded[field] = json.dumps(encoded[field], ensure_ascii=False, separators=(",", ":"))
            writer.writerow(encoded)


def classify(title: str, abstract: str, year: int | None) -> dict[str, Any]:
    text = re.sub(r"\s+", " ", f"{title or ''} {abstract or ''}")
    signals = {
        "ai": bool(AI.search(text)),
        "xai": bool(XAI.search(text)),
        "quality": bool(QUALITY.search(text)),
        "transformer": bool(TRANSFORMER.search(text)),
        "human": bool(HUMAN.search(text)),
        "decision": bool(DECISION.search(text)),
        "reliance": bool(RELIANCE.search(text)),
        "empirical": bool(EMPIRICAL.search(text)),
        "professional": bool(PROFESSIONAL.search(text)),
        "open_resource": bool(OPEN_RESOURCE.search(text)),
        "governance": bool(GOVERNANCE.search(text)),
        "simulatability": bool(SIMULATABILITY.search(text)),
    }
    layers: list[str] = []
    reasons: list[str] = []
    if signals["xai"] and signals["quality"] and (signals["ai"] or signals["transformer"]):
        layers.append("C")
        reasons.append("technical_xai_quality")
    elif signals["xai"] and signals["transformer"]:
        layers.append("C?")
        reasons.append("technical_xai_transformer_partial")
    if signals["ai"] and signals["human"] and ((signals["decision"] and signals["reliance"]) or signals["simulatability"]) and signals["empirical"]:
        layers.append("B")
        reasons.append("human_ai_behavior_experiment")
    elif signals["ai"] and ((signals["human"] and ((signals["decision"] and signals["reliance"]) or signals["simulatability"])) or signals["reliance"]):
        layers.append("B?")
        reasons.append("human_ai_behavior_partial")
    if signals["professional"] and signals["ai"] and (signals["human"] or signals["reliance"]) and (signals["decision"] or signals["simulatability"] or signals["xai"]):
        layers.append("D")
        reasons.append("professional_decision_context")
    if signals["open_resource"] and (signals["xai"] or signals["reliance"]) and (signals["human"] or signals["transformer"]):
        layers.append("A")
        reasons.append("open_resource_signal")
    if signals["governance"] and signals["ai"] and (signals["xai"] or signals["reliance"]):
        layers.append("F")
        reasons.append("governance_signal")

    in_scope_year = year is not None and 2018 <= year <= 2026
    strong = any(layer in {"B", "C", "D"} for layer in layers)
    partial = any(layer.endswith("?") for layer in layers) or any(layer in {"A", "F"} for layer in layers)
    irrelevant_penalty = bool(IRRELEVANT_TECH.search(text)) and not any(
        signals[key] for key in ("quality", "reliance", "empirical", "open_resource", "simulatability")
    )
    if not in_scope_year:
        decision = "exclude"
        confidence = 0.99
        exclusion_code = "OUT_OF_PROTOCOL_YEAR"
        reasons.append("outside_2018_2026_window")
    elif strong and not irrelevant_penalty:
        decision = "include"
        confidence = 0.86
        exclusion_code = None
    elif partial and not irrelevant_penalty:
        decision = "uncertain"
        confidence = 0.66
        exclusion_code = None
    else:
        decision = "exclude"
        confidence = 0.84
        exclusion_code = "INSUFFICIENT_TARGET_CONSTRUCT_INTERSECTION"
        reasons.append("insufficient_target_construct_intersection")

    return {
        "decision": decision,
        "corpus_layers": layers,
        "reasons": reasons,
        "exclusion_code": exclusion_code,
        "evidence": [key for key, present in signals.items() if present],
        "confidence": confidence,
        "requires_adjudication": decision == "uncertain",
        "technical_score": sum(signals[key] for key in ("ai", "xai", "quality", "transformer")),
        "behavior_score": sum(signals[key] for key in ("ai", "human", "decision", "reliance", "empirical", "simulatability")),
        "professional_score": sum(signals[key] for key in ("professional", "ai", "human", "decision", "reliance", "empirical", "simulatability")),
        "resource_score": sum(signals[key] for key in ("open_resource", "xai", "reliance", "human", "transformer")),
        "governance_score": sum(signals[key] for key in ("governance", "ai", "xai", "reliance", "professional")),
    }


def multiclass_kappa(first: list[str], second: list[str]) -> float:
    labels = ["include", "uncertain", "exclude"]
    n = len(first)
    if not n:
        return 0.0
    observed = sum(a == b for a, b in zip(first, second)) / n
    first_counts = Counter(first)
    second_counts = Counter(second)
    expected = sum((first_counts[label] / n) * (second_counts[label] / n) for label in labels)
    return (observed - expected) / (1 - expected) if expected < 1 else 1.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--first-decisions", type=Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--reviewer", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    candidates = load_csv_gz(args.candidates)
    first_rows = load_csv_gz(args.first_decisions)
    first_by_id = {row["candidate_id"]: row for row in first_rows}
    if len(first_by_id) != len(first_rows):
        raise RuntimeError("Duplicate first-pass candidate_id")

    decisions: list[dict[str, Any]] = []
    comparisons: list[dict[str, Any]] = []
    for candidate in candidates:
        candidate_id = candidate["candidate_id"]
        first = first_by_id.get(candidate_id)
        if first is None:
            raise RuntimeError(f"Missing first-pass decision for {candidate_id}")
        year = None if blank(candidate.get("publication_year")) else int(float(candidate["publication_year"]))
        second = classify(candidate.get("canonical_title", ""), candidate.get("abstract", ""), year)
        agreement = first["decision"] == second["decision"]
        adjudication = (not agreement) or first["decision"] == "uncertain" or second["decision"] == "uncertain"
        decision_row = {
            "candidate_id": candidate_id,
            "screening_stage": "title_abstract_independent_rule_v2",
            "reviewer": args.reviewer,
            **second,
            "requires_adjudication": adjudication,
            "run_id": "independent-screen-v2-20260724",
        }
        decisions.append(decision_row)
        comparisons.append({
            "candidate_id": candidate_id,
            "source": args.source,
            "canonical_title": candidate.get("canonical_title"),
            "publication_year": year,
            "decision_v1": first["decision"],
            "decision_v2": second["decision"],
            "agreement": agreement,
            "requires_adjudication": adjudication,
            "corpus_layers": second["corpus_layers"],
            "reasons": second["reasons"],
            "confidence_v2": second["confidence"],
        })

    decision_fields = [
        "candidate_id", "screening_stage", "reviewer", "decision", "corpus_layers", "reasons",
        "exclusion_code", "evidence", "confidence", "requires_adjudication", "technical_score",
        "behavior_score", "professional_score", "resource_score", "governance_score", "run_id",
    ]
    comparison_fields = [
        "candidate_id", "source", "canonical_title", "publication_year", "decision_v1", "decision_v2",
        "agreement", "requires_adjudication", "corpus_layers", "reasons", "confidence_v2",
    ]
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv_gz(args.output / "screening_decisions_independent_v2.csv.gz", decisions, decision_fields)
    write_csv_gz(args.output / "screening_comparison_and_adjudication.csv.gz", comparisons, comparison_fields)
    adjudication = [row for row in comparisons if row["requires_adjudication"]]
    write_csv_gz(args.output / "adjudication_queue.csv.gz", adjudication, comparison_fields)

    first_values = [row["decision_v1"] for row in comparisons]
    second_values = [row["decision_v2"] for row in comparisons]
    summary = {
        "source": args.source,
        "reviewer_v2": args.reviewer,
        "records": len(comparisons),
        "first_counts": dict(Counter(first_values)),
        "second_counts": dict(Counter(second_values)),
        "agreement_count": sum(row["agreement"] for row in comparisons),
        "agreement_rate": sum(row["agreement"] for row in comparisons) / len(comparisons),
        "cohen_kappa_three_class": multiclass_kappa(first_values, second_values),
        "adjudication_count": len(adjudication),
        "adjudication_rate": len(adjudication) / len(comparisons),
        "out_of_protocol_year_count": sum(row.get("exclusion_code") == "OUT_OF_PROTOCOL_YEAR" for row in decisions),
        "independence_note": "The v2 classifier does not read or use the v1 decision when assigning its decision.",
        "final_inclusion_note": "No machine decision is promoted directly to final inclusion; disagreements and uncertain records require adjudication/full-text review.",
        "completed": True,
    }
    (args.output / "independent_screen_v2_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
