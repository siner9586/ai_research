from datetime import datetime, date
from pydantic import BaseModel, Field

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
    fetched_at: datetime = Field(default_factory=datetime.utcnow)

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
    github_trending: bool = False
    citation_count: int = 0
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
    generated_at: datetime = Field(default_factory=datetime.utcnow)

class QAReport(BaseModel):
    date: date
    passed: bool
    warnings: list[str]
    errors: list[str]
    checked_files: list[str]
    generated_at: datetime = Field(default_factory=datetime.utcnow)
