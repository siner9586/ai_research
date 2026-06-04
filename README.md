# Frontier Paper Radar / 前沿论文雷达

A reproducible AI paper briefing pipeline and Astro static site.

This project reproduces product capabilities and information architecture only: source-first paper collection, multi-signal scoring, daily briefs, transparent source pages, bilingual output, RSS, search, archive, topics, and scheduled deployment. It does not copy any third-party brand, site name, copy, visual design, logo, domain, trademark, or article content.

## What It Implements

- Python 3.11 data pipeline with Pydantic models.
- arXiv collection across six AI-related categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.CV`, `cs.MA`, `cs.IR`.
- Optional external enrichment for Hugging Face Daily Papers, Semantic Scholar citations, and GitHub repository signals.
- Eight scoring signal families: institution background, community recommendation, community heat, top conference, code availability, practitioner relevance, academic impact, and open-source heat.
- Tiered selection into featured papers, also-worth-watching papers, and remaining candidates.
- Daily Chinese and English Markdown briefs.
- Per-issue source pages showing every candidate, tier, total score, score breakdown, reasons, keywords, warnings, and original links.
- Static RSS feeds, sitemap, browser search index, archive pages, topic pages, and daily detail pages.
- GitHub Actions workflow for scheduled generation, tests, and Astro build.

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt -e .
.venv/bin/ai-brief mock-run --date 2026-06-03
.venv/bin/pytest -q
cd apps/web
npm install
npm run build
npm run dev
```

## Commands

```bash
ai-brief mock-run --date 2026-06-03
ai-brief run-daily --mock
ai-brief run-daily --delay-days 3
ai-brief qa --date 2026-06-03 --mock
```

`mock-run` is deterministic and does not require network access or private keys. Production `run-daily` fetches arXiv. Optional external enrichment is disabled by default; enable it with:

```bash
AI_RESEARCH_EXTERNAL_SIGNALS=1 ai-brief run-daily --delay-days 3
```

Optional API keys:

```bash
SEMANTIC_SCHOLAR_API_KEY=
GITHUB_API_TOKEN=
```

## Repository Layout

```text
configs/                         Scoring, topics, site metadata, editorial rules
packages/ai_research_brief/       Python pipeline, fetchers, scoring, rendering, QA
packages/prompts/                 Prompt templates for future LLM-assisted editing
data/raw/                         Raw collected papers
data/processed/                   Signals, scores, selected papers
data/content/{zh,en}/daily/       Generated briefs and source pages
apps/web/                         Astro static site
apps/web/public/                  Generated RSS, sitemap, search index
tests/                            Pipeline and product-scope tests
```

## Method Notes

The default cadence is T+3, so social and repository signals have time to mature. The generated source page is the audit trail: it shows not only selected papers but also remaining candidates, making ranking decisions inspectable.

Generated summaries are information triage, not final academic review. The original paper links remain the source of record.
