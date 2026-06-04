from __future__ import annotations

import os
import re
from datetime import date

from ..config import scoring_config
from ..fetchers.github import extract_github_url, fetch_repo_signal
from ..fetchers.huggingface import fetch_daily_papers
from ..fetchers.semantic_scholar import fetch_paper_signals
from ..models import Paper, PaperSignal


MOCK_SIGNALS: dict[str, dict] = {
    "2606.00001": {"hf_daily": True, "hf_upvotes": 94, "has_code": True, "github_stars": 420, "citation_count": 78, "top_institution": True, "institutions": ["OpenAI", "Stanford"]},
    "2606.00002": {"hf_daily": True, "hf_upvotes": 38, "has_code": True, "github_stars": 180, "citation_count": 35},
    "2606.00003": {"hf_daily": True, "hf_upvotes": 26, "has_code": True, "github_stars": 96, "citation_count": 124, "top_conference": "SIGIR"},
    "2606.00004": {"hf_daily": True, "hf_upvotes": 21, "citation_count": 55, "top_conference": "CVPR"},
    "2606.00005": {"hf_daily": True, "hf_upvotes": 17, "has_code": True, "github_stars": 260, "citation_count": 44},
    "2606.00006": {"hf_upvotes": 12, "has_code": True, "github_stars": 140, "citation_count": 18},
    "2606.00007": {"hf_upvotes": 8, "has_code": True, "github_stars": 80, "top_institution": True, "institutions": ["Google"]},
    "2606.00008": {"hf_upvotes": 7, "citation_count": 210, "top_conference": "ICLR"},
    "2606.00009": {"hf_upvotes": 5, "has_code": True, "github_stars": 62},
    "2606.00010": {"hf_upvotes": 6, "top_conference": "ICCV", "citation_count": 28},
    "2606.00011": {"hf_upvotes": 14, "has_code": True, "github_stars": 155},
    "2606.00012": {"hf_upvotes": 11, "citation_count": 60, "top_conference": "NeurIPS"},
    "2606.00013": {"hf_upvotes": 10, "has_code": True, "github_stars": 120},
    "2606.00014": {"hf_upvotes": 9, "top_conference": "ACL", "citation_count": 22},
    "2606.00015": {"hf_upvotes": 13, "has_code": True, "github_stars": 112},
    "2606.00016": {"hf_upvotes": 4, "has_code": True, "github_stars": 51},
    "2606.00017": {"hf_upvotes": 16, "citation_count": 90, "top_conference": "AAAI"},
    "2606.00018": {"hf_upvotes": 6, "citation_count": 510, "top_conference": "ICML"},
}


def build_signals(papers: list[Paper], day: date, mock: bool = False) -> dict[str, PaperSignal]:
    config = scoring_config()
    signals = {paper.arxiv_id: _base_signal(paper, config) for paper in papers}

    if mock:
        for arxiv_id, patch in MOCK_SIGNALS.items():
            if arxiv_id in signals:
                _apply_patch(signals[arxiv_id], patch, source="mock")
        return signals

    if os.environ.get("AI_RESEARCH_EXTERNAL_SIGNALS", "0") != "1":
        for signal in signals.values():
            signal.warnings.append("External signal enrichment disabled; set AI_RESEARCH_EXTERNAL_SIGNALS=1 to enable.")
        return signals

    hf_signals = fetch_daily_papers(day)
    for arxiv_id, patch in hf_signals.items():
        if arxiv_id in signals:
            _apply_patch(signals[arxiv_id], patch, source="huggingface")

    semantic_signals = fetch_paper_signals(list(signals))
    for arxiv_id, patch in semantic_signals.items():
        if arxiv_id in signals:
            _apply_patch(signals[arxiv_id], patch, source="semantic_scholar")

    for paper in papers:
        signal = signals[paper.arxiv_id]
        repo = extract_github_url(f"{paper.title} {paper.abstract}")
        if not repo:
            continue
        signal.has_code = True
        signal.code_url = repo
        signal.code_source = "paper_text"
        signal.signal_sources["code"] = "paper_text"
        _apply_patch(signal, fetch_repo_signal(repo), source="github")

    return signals


def _base_signal(paper: Paper, config: dict) -> PaperSignal:
    text = f"{paper.title} {paper.abstract}"
    lowered = text.lower()
    signal = PaperSignal(arxiv_id=paper.arxiv_id)

    for institution in config.get("top_institutions", []):
        if _contains_name(lowered, institution):
            signal.top_institution = True
            signal.institutions.append(institution)
            signal.signal_sources["institution_background"] = "paper_text"

    for conference in config.get("top_conferences", []):
        if conference.lower() in lowered:
            signal.top_conference = conference
            signal.signal_sources["top_conference"] = "paper_text"
            break

    if any(phrase in lowered for phrase in ("github.com/", "code is available", "code available", "open-source code", "released code", "repository")):
        signal.has_code = True
        signal.code_source = "paper_text"
        signal.signal_sources["code"] = "paper_text"

    signal.matched_keywords = [
        keyword
        for keyword in config.get("practitioner_keywords", [])
        if keyword.lower() in lowered
    ]
    return signal


def _apply_patch(signal: PaperSignal, patch: dict, source: str) -> None:
    for key, value in patch.items():
        if hasattr(signal, key):
            setattr(signal, key, value)
            signal.signal_sources[key] = source
    if signal.has_code and not signal.code_source:
        signal.code_source = source


def _contains_name(lowered_text: str, name: str) -> bool:
    needle = name.lower()
    if len(needle) <= 4 or needle.isupper():
        return re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", lowered_text) is not None
    return needle in lowered_text
