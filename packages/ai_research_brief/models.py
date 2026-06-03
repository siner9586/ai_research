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
    github_stars: int = 0
    github_forks: int = 0
    citation_count: int = 0
    top_institution: bool = False
    top_conference: str | None = None
    matched_keywords: list[str] = []
    extra: dict = {}

class ScoredPaper(BaseModel):
    paper: Paper
    signal: PaperSignal
    total_score: int
    score_breakdown: dict[str, int]
    selected_reason: str
    matched_keywords: list[str]
    topic: str
    confidence_level: str

class QAReport(BaseModel):
    date: date
    passed: bool
    warnings: list[str]
    errors: list[str]
    checked_files: list[str]
    generated_at: datetime = Field(default_factory=datetime.utcnow)
