from __future__ import annotations

import json
from datetime import date
from functools import lru_cache
from pathlib import Path

from ..config import REPO_ROOT, load_yaml
from ..llm import get_provider
from ..models import BriefPaper, DailyBrief, ScoredPaper, utc_now
from ..utils.slug import slugify
from ..utils.text import first_sentence


def render_daily_markdown(
    day: date,
    lang: str,
    featured: list[ScoredPaper],
    mentions: list[ScoredPaper],
    candidates: list[ScoredPaper],
) -> tuple[list[str], str]:
    content_dir = REPO_ROOT / "data" / "content" / lang / "daily"
    content_dir.mkdir(parents=True, exist_ok=True)

    base_title = featured[0].paper.title if featured else "AI research brief"
    slug = f"{day}-{slugify(base_title, max_words=7)}"
    brief_path = content_dir / f"{slug}.md"
    sources_path = content_dir / f"{slug}-sources.md"
    brief = build_daily_brief(day, lang, slug, str(sources_path.relative_to(REPO_ROOT)), featured, mentions, candidates)

    brief_path.write_text(_brief_markdown(brief, candidates) + "\n", encoding="utf-8")
    sources_path.write_text(_sources_markdown(day, lang, slug, featured, mentions, candidates) + "\n", encoding="utf-8")
    return [str(brief_path), str(sources_path)], slug


def build_daily_brief(
    day: date,
    lang: str,
    slug: str,
    sources_path: str,
    featured: list[ScoredPaper],
    mentions: list[ScoredPaper],
    candidates: list[ScoredPaper],
) -> DailyBrief:
    labels = _labels(lang)
    topic_names = [_topic_label(row, lang) for row in featured[:3]]
    overview = labels["overview"].format(
        candidates=len(candidates),
        featured=len(featured),
        mentions=len(mentions),
        topics="、".join(topic_names) if lang == "zh" else ", ".join(topic_names),
    )
    trend = labels["trend"].format(
        topics="、".join(topic_names) if lang == "zh" else ", ".join(topic_names),
    )
    title = _brief_title(lang, featured)
    keywords = sorted({keyword for row in featured + mentions for keyword in (row.matched_keywords or [row.topic_slug])})[:14]
    return DailyBrief(
        date=day,
        lang=lang,
        title=title,
        slug=slug,
        overview=overview,
        trend_observation=trend,
        featured_papers=[_brief_paper(row, lang) for row in featured],
        honorable_mentions=[_brief_paper(row, lang) for row in mentions],
        keywords=keywords,
        sources_path=sources_path,
    )


def _brief_markdown(brief: DailyBrief, candidates: list[ScoredPaper]) -> str:
    lang = brief.lang
    labels = _labels(lang)
    tags = sorted({paper.topic_slug for paper in brief.featured_papers + brief.honorable_mentions if paper.topic_slug != "other"})
    summary = brief.overview
    lines = [
        *_frontmatter({
            "title": brief.title,
            "date": str(brief.date),
            "lang": lang,
            "slug": brief.slug,
            "summary": summary,
            "tags": tags,
            "topics": tags,
            "sources_page": f"/{lang}/daily/{brief.slug}-sources/",
            "generated_at": brief.generated_at.isoformat(),
            "page_type": "brief",
            "candidate_count": len(candidates),
            "featured_count": len(brief.featured_papers),
            "mentions_count": len(brief.honorable_mentions),
        }),
        "",
        f"# {brief.title}",
        "",
        f"**{labels['date']}**: {brief.date}",
        "",
        f"## {labels['overview_heading']}",
        "",
        brief.overview,
        "",
        f"## {labels['trend_heading']}",
        "",
        brief.trend_observation,
        "",
        f"## {labels['featured_heading']}",
    ]

    for index, paper in enumerate(brief.featured_papers, start=1):
        lines.extend(_paper_section(index, paper, lang, featured=True))

    lines.extend(["", f"## {labels['mentions_heading']}"])
    for paper in brief.honorable_mentions:
        lines.extend(_mention_lines(paper, lang))

    lines.extend([
        "",
        f"## {labels['keywords_heading']}",
        "",
        ", ".join(brief.keywords) if brief.keywords else labels["no_keywords"],
        "",
        f"## {labels['sources_heading']}",
        "",
        labels["sources_sentence"].format(url=f"/{lang}/daily/{brief.slug}-sources/"),
        "",
        f"## {labels['disclaimer_heading']}",
    ])
    for item in load_yaml("editorial_rules.yaml").get("known_limits", {}).get(lang, []):
        lines.append(f"- {item}")
    return "\n".join(lines)


def _sources_markdown(
    day: date,
    lang: str,
    slug: str,
    featured: list[ScoredPaper],
    mentions: list[ScoredPaper],
    candidates: list[ScoredPaper],
) -> str:
    labels = _labels(lang)
    generated_at = utc_now().isoformat()
    fetched_at = min((row.paper.fetched_at for row in candidates), default=utc_now()).isoformat()
    lines = [
        *_frontmatter({
            "title": labels["sources_title"],
            "date": str(day),
            "lang": lang,
            "slug": f"{slug}-sources",
            "summary": labels["sources_summary"].format(count=len(candidates)),
            "tags": ["sources", "scoring"],
            "topics": ["sources"],
            "brief_page": f"/{lang}/daily/{slug}/",
            "generated_at": generated_at,
            "page_type": "sources",
            "candidate_count": len(candidates),
            "featured_count": len(featured),
            "mentions_count": len(mentions),
        }),
        "",
        f"# {labels['sources_title']}",
        "",
        labels["sources_intro"].format(
            count=len(candidates),
            featured=len(featured),
            mentions=len(mentions),
            generated_at=generated_at,
            fetched_at=fetched_at,
        ),
        "",
        f"## {labels['scoring_rules_heading']}",
        "",
        labels["scoring_rules"],
        "",
        f"## {labels['featured_table_heading']}",
        "",
        _summary_table(featured, lang),
        "",
        f"## {labels['mentions_table_heading']}",
        "",
        _summary_table(mentions, lang),
        "",
        f"## {labels['all_candidates_heading']}",
    ]
    for row in candidates:
        lines.extend(_source_block(row, lang))
    return "\n".join(lines)


def _frontmatter(values: dict) -> list[str]:
    lines = ["---"]
    for key, value in values.items():
        if isinstance(value, str):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        elif isinstance(value, list):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return lines


def _brief_paper(row: ScoredPaper, lang: str) -> BriefPaper:
    abstract_sentence = first_sentence(row.paper.abstract)
    title = row.paper.title
    llm_payload = _llm_payload(row, lang)
    if lang == "zh":
        why = f"它聚焦 {_topic_label(row, lang)}，并在摘要中明确处理 {abstract_sentence}"
        problem = f"问题是：{abstract_sentence}"
        method = "方法线索来自摘要和公开元数据；在未阅读全文前，只把它视为可进一步核验的研究方向。"
        takeaway = "从业者可关注其中的数据、评测、部署或工作流设计是否能迁移到自己的系统。"
        limitations = "这是 arXiv 预印本简报，不代表结论已被同行评审确认；具体实验细节需阅读原文。"
    else:
        why = f"It is relevant to {_topic_label(row, lang)} and the abstract states: {abstract_sentence}"
        problem = f"The paper targets this problem signal: {abstract_sentence}"
        method = "The method summary is inferred from the abstract and metadata; full claims should be checked in the paper."
        takeaway = "Practitioners can inspect whether the data, evaluation, deployment, or workflow idea transfers to their own systems."
        limitations = "This is an arXiv preprint brief, not a peer-reviewed confirmation; read the paper for experimental details."
    if llm_payload:
        why = llm_payload.get("why_it_matters") or why
        problem = llm_payload.get("problem") or problem
        method = llm_payload.get("method") or method
        takeaway = llm_payload.get("practitioner_takeaway") or takeaway
        limitations = llm_payload.get("limitations") or limitations
    return BriefPaper(
        arxiv_id=row.paper.arxiv_id,
        title=title,
        short_title=title,
        original_title=title,
        authors=row.paper.authors,
        topic=_topic_label(row, lang),
        topic_slug=row.topic_slug,
        score=row.total_score,
        abs_url=row.paper.abs_url,
        pdf_url=row.paper.pdf_url,
        code_url=row.signal.code_url,
        why_it_matters=why,
        problem=problem,
        method=method,
        practitioner_takeaway=takeaway,
        limitations=limitations,
        bullets=(llm_payload.get("bullets") if llm_payload else None) or [
            row.selected_reason,
            f"{_topic_label(row, lang)} / score {row.total_score}",
            "Source links are kept with the original arXiv record.",
        ],
    )


def _llm_payload(row: ScoredPaper, lang: str) -> dict:
    prompt = "\n".join([
        "OUTPUT_JSON",
        f"lang={lang}",
        f"title={row.paper.title}",
        f"abstract={row.paper.abstract}",
        f"topic={_topic_label(row, lang)}",
        f"score_breakdown={json.dumps(row.score_breakdown, ensure_ascii=False)}",
        f"code_url={row.signal.code_url or ''}",
        "Return JSON keys: why_it_matters, problem, method, practitioner_takeaway, limitations, bullets.",
        "Do not fabricate code links, peer-review status, or conclusions absent from the abstract.",
    ])
    try:
        text = _provider().complete(prompt)
        payload = json.loads(text)
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


@lru_cache(maxsize=1)
def _provider():
    return get_provider()


def _paper_section(index: int, paper: BriefPaper, lang: str, featured: bool = True) -> list[str]:
    labels = _labels(lang)
    lines = [
        "",
        f"### {index}. {paper.short_title}",
        "",
        f"- {labels['original_title']}: {paper.original_title}",
        f"- {labels['authors']}: {', '.join(paper.authors) if paper.authors else labels['unknown']}",
        f"- {labels['topic']}: {paper.topic}",
        f"- arXiv: [{paper.arxiv_id}]({paper.abs_url})",
        f"- PDF: [PDF]({paper.pdf_url})",
    ]
    if paper.code_url:
        lines.append(f"- {labels['code']}: [{paper.code_url}]({paper.code_url})")
    lines.extend([
        f"- {labels['why']}: {paper.why_it_matters}",
        f"- {labels['problem']}: {paper.problem}",
        f"- {labels['method']}: {paper.method}",
        f"- {labels['takeaway']}: {paper.practitioner_takeaway}",
        f"- {labels['limits']}: {paper.limitations}",
        f"- {labels['bullets']}:",
    ])
    for bullet in paper.bullets[:3]:
        lines.append(f"  - {bullet}")
    return lines


def _mention_lines(paper: BriefPaper, lang: str) -> list[str]:
    labels = _labels(lang)
    return [
        f"- [{paper.original_title}]({paper.abs_url}) - {paper.topic}, score {paper.score}. {labels['mention_reason']} {paper.why_it_matters}",
    ]


def _summary_table(rows: list[ScoredPaper], lang: str) -> str:
    labels = _labels(lang)
    if not rows:
        return labels["empty_table"]
    lines = [
        f"| {labels['rank']} | {labels['paper']} | {labels['topic']} | Score | arXiv |",
        "|---:|---|---|---:|---|",
    ]
    for row in rows:
        lines.append(f"| {row.rank} | {row.paper.title} | {_topic_label(row, lang)} | {row.total_score} | [{row.paper.arxiv_id}]({row.paper.abs_url}) |")
    return "\n".join(lines)


def _source_block(row: ScoredPaper, lang: str) -> list[str]:
    labels = _labels(lang)
    signal = row.signal
    signals = []
    if signal.hf_daily:
        signals.append(f"HF Daily ({signal.hf_upvotes} upvotes)")
    if signal.code_url:
        signals.append(f"Code: {signal.code_url}")
    elif signal.has_code:
        signals.append("Code signal present, URL not verified")
    if signal.github_stars:
        signals.append(f"GitHub {signal.github_stars} stars / {signal.github_forks} forks")
    if signal.citation_count:
        signals.append(f"Semantic Scholar {signal.citation_count} citations")
    if signal.top_conference:
        signals.append(signal.top_conference)
    if signal.top_institution:
        signals.append(", ".join(signal.institutions) or "top institution")
    warnings = "; ".join(signal.warnings) if signal.warnings else "none"
    return [
        "",
        f"### #{row.rank} {row.paper.title}",
        "",
        f"- Tier: {row.selection_tier}",
        f"- Score: {row.total_score}",
        f"- Topic: {_topic_label(row, lang)}",
        f"- Original title: {row.paper.title}",
        f"- Authors: {', '.join(row.paper.authors) if row.paper.authors else labels['unknown']}",
        f"- arXiv: [{row.paper.arxiv_id}]({row.paper.abs_url})",
        f"- PDF: [PDF]({row.paper.pdf_url})",
        f"- Code URL: {signal.code_url or 'none verified'}",
        f"- Score breakdown: {json.dumps(row.score_breakdown, ensure_ascii=False, sort_keys=True)}",
        f"- Selected reason: {row.selected_reason}",
        f"- Matched keywords: {', '.join(row.matched_keywords) if row.matched_keywords else 'none'}",
        f"- Signals: {', '.join(signals) if signals else 'arXiv metadata only'}",
        f"- Warnings: {warnings}",
    ]


def _brief_title(lang: str, featured: list[ScoredPaper]) -> str:
    if not featured:
        return "今日 AI 论文简报" if lang == "zh" else "Daily AI Research Brief"
    topics = []
    for row in featured:
        label = _topic_label(row, lang)
        if label not in topics:
            topics.append(label)
    if lang == "zh":
        return f"AI 研究简报：{ '、'.join(topics[:3]) }"
    return f"AI Research Brief: {', '.join(topics[:3])}"


def _topic_label(row: ScoredPaper, lang: str) -> str:
    for topic in load_yaml("topics.yaml").get("topics", []):
        if topic.get("slug") == row.topic_slug:
            return topic.get(lang) or topic.get("en") or row.topic
    return "其他" if lang == "zh" else row.topic


def _labels(lang: str) -> dict[str, str]:
    zh = {
        "date": "日期",
        "overview_heading": "今日概览",
        "trend_heading": "今日趋势观察",
        "featured_heading": "重点论文",
        "mentions_heading": "也值得关注",
        "keywords_heading": "今日关键词",
        "sources_heading": "来源页链接",
        "disclaimer_heading": "阅读边界",
        "overview": "本期从 {candidates} 篇候选论文中筛出 {featured} 篇重点论文和 {mentions} 篇也值得关注论文，主要覆盖 {topics}。",
        "trend": "今天的高分论文集中在 {topics}。这些信号更适合作为选题和工程跟进线索，而不是对论文结论的最终背书。",
        "sources_sentence": "完整候选池、评分规则摘要和每篇 score breakdown 见 [来源透明页]({url})。",
        "original_title": "原始论文标题",
        "authors": "作者/机构",
        "topic": "主题",
        "code": "代码链接",
        "why": "为什么重要",
        "problem": "它解决了什么问题",
        "method": "方法简述",
        "takeaway": "从业者启发",
        "limits": "局限与风险",
        "bullets": "三条要点",
        "mention_reason": "关注理由：",
        "sources_title": "论文来源与评分",
        "sources_summary": "候选池 {count} 篇论文的来源与评分记录",
        "sources_intro": "本页公开 {count} 篇候选论文的来源与评分。抓取时间：{fetched_at}。生成时间：{generated_at}。其中重点论文 {featured} 篇，也值得关注 {mentions} 篇。",
        "scoring_rules_heading": "评分规则摘要",
        "scoring_rules": "评分综合机构背景、HF Daily Papers、HF upvotes、顶会信息、代码、从业者关键词、Semantic Scholar 引用、GitHub 热度、arXiv 分类权重、新颖性/重复惩罚、最近主题重复惩罚，以及安全/伦理/治理关键词。外部 API 不可用时对应信号留空。",
        "featured_table_heading": "重点论文表格",
        "mentions_table_heading": "也值得关注论文表格",
        "all_candidates_heading": "完整候选评分",
        "rank": "排名",
        "paper": "论文",
        "unknown": "未知",
        "empty_table": "无。",
        "no_keywords": "无明确关键词。",
    }
    en = {
        "date": "Date",
        "overview_heading": "Overview",
        "trend_heading": "Trend Observation",
        "featured_heading": "Featured Papers",
        "mentions_heading": "Honorable Mentions",
        "keywords_heading": "Keywords",
        "sources_heading": "Source Page",
        "disclaimer_heading": "Reading Boundaries",
        "overview": "This issue selects {featured} featured papers and {mentions} honorable mentions from {candidates} candidates, mainly covering {topics}.",
        "trend": "High-scoring papers today cluster around {topics}. Treat these as research and engineering follow-up signals, not final validation of the claims.",
        "sources_sentence": "See the [source transparency page]({url}) for the full candidate pool, scoring summary, and per-paper score breakdown.",
        "original_title": "Original paper title",
        "authors": "Authors / institutions",
        "topic": "Topic",
        "code": "Code link",
        "why": "Why it matters",
        "problem": "Problem addressed",
        "method": "Method sketch",
        "takeaway": "Practitioner takeaway",
        "limits": "Limitations and risks",
        "bullets": "Three notes",
        "mention_reason": "Why track:",
        "sources_title": "Sources and Scoring",
        "sources_summary": "Source and scoring log for {count} candidate papers",
        "sources_intro": "This page exposes sources and scores for {count} candidate papers. Fetched at {fetched_at}. Generated at {generated_at}. Featured: {featured}; honorable mentions: {mentions}.",
        "scoring_rules_heading": "Scoring Rule Summary",
        "scoring_rules": "The score combines institution background, HF Daily Papers, HF upvotes, conference signal, code availability, practitioner keywords, Semantic Scholar citations, GitHub heat, arXiv category weight, novelty/duplicate penalties, recent topic repetition penalties, and safety/ethics/governance keywords. Optional external signals remain empty when APIs are unavailable.",
        "featured_table_heading": "Featured Paper Table",
        "mentions_table_heading": "Honorable Mention Table",
        "all_candidates_heading": "Full Candidate Scores",
        "rank": "Rank",
        "paper": "Paper",
        "unknown": "Unknown",
        "empty_table": "None.",
        "no_keywords": "No explicit keywords.",
    }
    return zh if lang == "zh" else en
