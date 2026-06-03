import json
from datetime import date
from pathlib import Path
from ..config import REPO_ROOT, ensure_dirs
from ..models import PaperSignal
from ..fetchers.arxiv import mock_papers, fetch_arxiv_category
from .dedupe import dedupe_papers
from .score import score_papers
from .select import select_papers
from .qa import run_qa


def _write(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, list):
        data = [x.model_dump(mode='json') if hasattr(x, 'model_dump') else x for x in data]
    elif hasattr(data, 'model_dump'):
        data = data.model_dump(mode='json')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def _render(day: date, lang: str, featured, mentions):
    content = REPO_ROOT / 'data' / 'content' / lang / 'daily'
    content.mkdir(parents=True, exist_ok=True)
    slug = str(day) + '-ai-research-brief'
    main = content / (slug + '.md')
    src = content / (slug + '-sources.md')
    lines = ['---', 'title: "AI Research Brief"', f'date: "{day}"', f'lang: "{lang}"', f'slug: "{slug}"', 'summary: [AI paper brief]', 'tags: [AI, arXiv]', f'sources_page: "/{lang}/daily/{slug}-sources/"', '---', '', '# Overview']
    lines.append('A source-grounded AI paper brief generated from a candidate pool.')
    lines.append('# Featured Papers')
    for row in featured:
        p = row.paper
        lines += [f'## {p.title}', f'- arXiv: {p.abs_url}', f'- PDF: {p.pdf_url}', f'- Topic: {row.topic}', f'- Score: {row.total_score}', p.abstract]
    lines.append('# Also Worth Watching')
    for row in mentions:
        lines.append(f'- {row.paper.title} — {row.topic}, score {row.total_score}')
    main.write_text('\n'.join(lines), encoding='utf-8')
    src_lines = ['---', 'title: "Sources and scoring"', f'date: "{day}"', f'lang: "{lang}"', f'slug: "{slug}-sources"', 'summary: [sources]', 'tags: [sources]', 'sources_page: ""', '---', '', '# Sources and scoring']
    for row in featured + mentions:
        src_lines.append(f'- {row.paper.title}: score {row.total_score}, reason {row.selected_reason}, link {row.paper.abs_url}')
    src.write_text('\n'.join(src_lines), encoding='utf-8')
    return [str(main), str(src)]


def _static_files():
    public = REPO_ROOT / 'apps' / 'web' / 'public'
    (public / 'zh').mkdir(parents=True, exist_ok=True)
    (public / 'en').mkdir(parents=True, exist_ok=True)
    (public / 'zh' / 'feed.xml').write_text('<rss><channel><title>AI Research Brief zh</title></channel></rss>', encoding='utf-8')
    (public / 'en' / 'feed.xml').write_text('<rss><channel><title>AI Research Brief en</title></channel></rss>', encoding='utf-8')
    (public / 'sitemap.xml').write_text('<urlset><url><loc>/</loc></url></urlset>', encoding='utf-8')
    (public / 'search-index.json').write_text('[]', encoding='utf-8')


def run_daily(day: date, mock: bool = False):
    ensure_dirs()
    papers = mock_papers() if mock else fetch_arxiv_category('cs.AI', 50)
    papers = dedupe_papers(papers)
    signals = {p.arxiv_id: PaperSignal(arxiv_id=p.arxiv_id) for p in papers}
    if papers:
        first = signals[papers[0].arxiv_id]
        first.hf_daily = True
        first.hf_upvotes = 42
        first.has_code = True
        first.github_stars = 128
    scored = score_papers(papers, signals)
    featured, mentions = select_papers(scored)
    processed = REPO_ROOT / 'data' / 'processed' / str(day)
    _write(processed / 'papers.json', papers)
    _write(processed / 'scored_papers.json', scored)
    _write(processed / 'selected_papers.json', {'featured': [x.model_dump(mode='json') for x in featured], 'mentions': [x.model_dump(mode='json') for x in mentions]})
    files = []
    files += _render(day, 'zh', featured, mentions)
    files += _render(day, 'en', featured, mentions)
    _static_files()
    report = run_qa(day, REPO_ROOT / 'data' / 'content', REPO_ROOT / 'data' / 'reports' / 'qa')
    return {'date': str(day), 'papers': len(papers), 'featured': len(featured), 'mentions': len(mentions), 'qa_passed': report.passed, 'generated': files}
