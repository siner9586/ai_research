from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Paper(BaseModel):
    id: str
    arxiv_id: str
    title: str
    abstract: str
    authors: list[str]
    primary_category: str
    categories: list[str]
    published_at: datetime
    updated_at: datetime
    abs_url: str
    pdf_url: str
    source: str = 'arxiv'
    fetched_at: datetime = Field(default_factory=utc_now)

class PaperSignal(BaseModel):
    arxiv_id: str
    hf_daily: bool = False
    hf_upvotes: int = 0
    hf_url: str | None = None
    has_code: bool = False
    code_url: str | None = None
    code_source: str | None = None
    github_stars: int = 0
    github_forks: int = 0
    repo_updated_at: datetime | None = None
    github_trending: bool = False
    semantic_scholar_id: str | None = None
    citation_count: int = 0
    influential_citation_count: int = 0
    fields_of_study: list[str] = Field(default_factory=list)
    external_ids: dict[str, Any] = Field(default_factory=dict)
    top_institution: bool = False
    institutions: list[str] = Field(default_factory=list)
    top_conference: str | None = None
    matched_keywords: list[str] = Field(default_factory=list)
    signal_sources: dict[str, str] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)
    extra: dict = Field(default_factory=dict)

class ScoredPaper(BaseModel):
    paper: Paper
    signal: PaperSignal
    total_score: int
    score_breakdown: dict[str, int]
    score_reasons: list[str] = Field(default_factory=list)
    selected_reason: str
    matched_keywords: list[str]
    topic: str
    topic_slug: str = "other"
    confidence_level: str
    selection_tier: str = "candidate"
    rank: int = 0

class BriefPaper(BaseModel):
    arxiv_id: str
    title: str
    short_title: str
    original_title: str
    authors: list[str]
    topic: str
    topic_slug: str
    score: int
    abs_url: str
    pdf_url: str
    code_url: str | None = None
    why_it_matters: str
    problem: str
    method: str
    practitioner_takeaway: str
    limitations: str
    bullets: list[str] = Field(default_factory=list)


class DailyBrief(BaseModel):
    date: date
    lang: str
    title: str
    slug: str
    overview: str
    trend_observation: str
    featured_papers: list[BriefPaper] = Field(default_factory=list)
    honorable_mentions: list[BriefPaper] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    sources_path: str
    generated_at: datetime = Field(default_factory=utc_now)


class DailyBriefMeta(BaseModel):
    date: date
    slug: str
    lang: str
    title: str
    summary: str
    candidate_count: int
    featured_count: int
    mentions_count: int
    sources_page: str
    generated_at: datetime = Field(default_factory=utc_now)

class QAReport(BaseModel):
    date: date
    passed: bool
    warnings: list[str]
    errors: list[str]
    checked_files: list[str]
    generated_at: datetime = Field(default_factory=utc_now)
