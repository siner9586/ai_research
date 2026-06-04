from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.config import REPO_ROOT, site_config, topics_config
from ai_research_brief.pipeline.dedupe import dedupe_papers
from ai_research_brief.pipeline.run_daily import run_daily
from ai_research_brief.utils.slug import slugify
from datetime import date
import json


def test_slug():
    assert slugify('Self Evolving Agents') == 'self-evolving-agents'


def test_mock_papers():
    assert len(mock_papers()) >= 3


def test_dedupe():
    p = mock_papers()
    assert len(dedupe_papers(p + p)) == len(p)


def test_run_daily():
    r = run_daily(date(2026, 6, 3), mock=True)
    assert r['qa_passed'] is True
    assert r['featured'] >= 3


def test_configured_product_scope():
    assert REPO_ROOT.name == 'ai_research'
    assert len(site_config()['pipeline']['arxiv_categories']) == 6
    assert len(topics_config()['topics']) == 15


def test_run_daily_generates_transparent_static_artifacts():
    r = run_daily(date(2026, 6, 3), mock=True)
    generated = '\n'.join(r['generated'])
    assert 'feed.xml' in generated
    assert 'search-index.json' in generated
    assert 'sitemap.xml' in generated

    source = REPO_ROOT / 'data/content/zh/daily/2026-06-03-self-evolving-agents-for-tool-use-skills-sources.md'
    text = source.read_text(encoding='utf-8')
    assert text.count('Score breakdown:') == r['papers']
    assert 'Tier: candidate' in text
    assert 'Top institution signal: OpenAI, Stanford' in text

    rows = json.loads((REPO_ROOT / 'apps/web/public/search-index.json').read_text(encoding='utf-8'))
    assert {row['type'] for row in rows} >= {'brief', 'sources'}
    assert {row['lang'] for row in rows} >= {'zh', 'en'}
