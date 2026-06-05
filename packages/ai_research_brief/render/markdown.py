from __future__ import annotations

import json
from datetime import date
from functools import lru_cache

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
    target_date: date | None = None,
    fallback_from: date | None = None,
    publish_date: date | None = None,
) -> tuple[list[str], str]:
    content_dir = REPO_ROOT / "data" / "content" / lang / "daily"
    content_dir.mkdir(parents=True, exist_ok=True)
    target_date = target_date or day
    publish_date = publish_date or day
    base_title = featured[0].paper.title if featured else "AI research brief"
    slug = f"{publish_date}-{slugify(base_title, max_words=7)}"
    brief_path = content_dir / f"{slug}.md"
    sources_path = content_dir / f"{slug}-sources.md"
    brief = build_daily_brief(publish_date, lang, slug, str(sources_path.relative_to(REPO_ROOT)), featured, mentions, candidates)
    brief_path.write_text(
        _brief_markdown(brief, candidates, data_date=day, target_date=target_date, fallback_from=fallback_from) + "\n",
        encoding="utf-8",
    )
    sources_path.write_text(
        _sources_markdown(
            day,
            lang,
            slug,
            featured,
            mentions,
            candidates,
            publish_date=publish_date,
            target_date=target_date,
            fallback_from=fallback_from,
        ) + "\n",
        encoding="utf-8",
    )
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
    focus_names = [_focus_phrase(row, lang) for row in featured[:3]]
    topic_text = "、".join(focus_names) if lang == "zh" else ", ".join(focus_names)
    overview = labels["overview"].format(
        candidates=len(candidates),
        featured=len(featured),
        mentions=len(mentions),
        topics=topic_text,
    )
    trend = labels["trend"].format(topics=topic_text)
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


def _brief_markdown(
    brief: DailyBrief,
    candidates: list[ScoredPaper],
    data_date: date,
    target_date: date,
    fallback_from: date | None,
) -> str:
    lang = brief.lang
    labels = _labels(lang)
    tags = sorted({paper.topic_slug for paper in brief.featured_papers + brief.honorable_mentions if paper.topic_slug != "other"})
    summary = brief.overview
    lines = [
        *_frontmatter({
            "title": brief.title,
            "date": str(brief.date),
            "target_date": str(target_date),
            "actual_date": str(data_date),
            "fallback_from": str(fallback_from) if fallback_from else "",
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
    publish_date: date,
    target_date: date,
    fallback_from: date | None,
) -> str:
    labels = _labels(lang)
    generated_at = utc_now().isoformat()
    fetched_at = min((row.paper.fetched_at for row in candidates), default=utc_now()).isoformat()
    lines = [
        *_frontmatter({
            "title": labels["sources_title"],
            "date": str(publish_date),
            "target_date": str(target_date),
            "actual_date": str(day),
            "fallback_from": str(fallback_from) if fallback_from else "",
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
    focus = _focus_phrase(row, lang)
    llm_payload = _llm_payload(row, lang)
    if lang == "zh":
        why = f"重点是：{focus}。摘要中的直接线索是：{abstract_sentence}"
        problem = f"它要解决的问题是：{focus}在真实研究或工程场景中仍不稳定、不透明或成本较高。"
        method = "方法线索来自标题、摘要和公开元数据；重点看论文如何设计数据、评测、训练或系统流程。"
        takeaway = "从业者可先核查是否有代码/数据、评测是否贴近真实场景，以及方案是否能迁移到自己的模型或业务链路。"
        limitations = "这是 arXiv 预印本简报，只能作为跟进线索；结论、实验细节和可复现性仍需阅读全文确认。"
    else:
        why = f"Core idea: {focus}. The abstract signal is: {abstract_sentence}"
        problem = f"The paper targets a concrete bottleneck: {focus} is still unreliable, opaque, costly, or hard to evaluate in real research and engineering workflows."
        method = "The method note is constrained to the title, abstract, and metadata; inspect how the paper sets up data, evaluation, training, or systems design before trusting the claim."
        takeaway = "First check whether code or data exist, whether the evaluation matches real use, and whether the idea can transfer into your model, RAG, agent, or deployment stack."
        limitations = "This is an arXiv preprint triage note. Treat it as a follow-up lead, not as peer-reviewed validation or production evidence."
    if llm_payload:
        why = llm_payload.get("why_it_matters") or why
        problem = llm_payload.get("problem") or problem
        method = llm_payload.get("method") or method
        takeaway = llm_payload.get("practitioner_takeaway") or takeaway
        limitations = llm_payload.get("limitations") or limitations
    return BriefPaper(
        arxiv_id=row.paper.arxiv_id,
        title=title,
        short_title=focus,
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
        bullets=llm_payload.get("bullets") if isinstance(llm_payload.get("bullets"), list) else [
            f"一句话：{focus}。" if lang == "zh" else f"One-line read: {focus}.",
            "看点：任务、数据、评测或系统收益是否清楚。" if lang == "zh" else "Look for whether the task, data, evaluation, or system gain is explicit.",
            "核验：优先打开原文确认实验设置、基线和代码/数据是否可用。" if lang == "zh" else "Verify the setup, baselines, and code/data availability in the paper.",
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
    title = paper.short_title
    if lang == "zh":
        return [f"- [{title}]({paper.abs_url}) - {paper.topic}，score {paper.score}。{labels['mention_reason']} {paper.why_it_matters}"]
    return [f"- [{title}]({paper.abs_url}) - {paper.topic}, score {paper.score}. {labels['mention_reason']} {paper.why_it_matters}"]


def _summary_table(rows: list[ScoredPaper], lang: str) -> str:
    labels = _labels(lang)
    if not rows:
        return labels["empty_table"]
    lines = [
        f"| {labels['rank']} | {labels['paper']} | {labels['topic']} | Score | arXiv |",
        "|---:|---|---|---:|---|",
    ]
    for row in rows:
        title = _focus_phrase(row, lang)
        lines.append(f"| {row.rank} | {title} | {_topic_label(row, lang)} | {row.total_score} | [{row.paper.arxiv_id}]({row.paper.abs_url}) |")
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
    display_title = _focus_phrase(row, lang)
    return [
        "",
        f"### #{row.rank} {display_title}",
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
    first = _focus_phrase(featured[0], lang)
    rest = [_focus_phrase(row, lang) for row in featured[1:3]]
    if lang == "zh":
        if rest:
            return f"今日重点：{first}；另含{'、'.join(rest)}"
        return f"今日重点：{first}"
    if rest:
        return f"Today's focus: {first}; also {', '.join(rest)}"
    return f"Today's focus: {first}"


def _focus_phrase(row: ScoredPaper, lang: str) -> str:
    text = f"{row.paper.title} {row.paper.abstract}".lower()
    rules = [
        (("agent", "tool", "trajectory"), "让 Agent 更可靠地调用工具和复用技能", "make agents use tools and reusable skills more reliably"),
        (("reason", "planning", "verifier", "math"), "提升模型推理、规划和验证能力", "improve model reasoning, planning, and verification"),
        (("rag", "retrieval", "database", "index"), "提升 RAG 检索和知识库问答可靠性", "make RAG retrieval and knowledge-base QA more reliable"),
        (("multimodal", "vision-language", "vlm", "chart", "document"), "增强多模态模型理解图表和文档的能力", "strengthen multimodal understanding of charts, documents, and visual evidence"),
        (("code", "program", "execution", "repair", "api"), "提升代码生成、执行反馈和自动修复能力", "improve code generation, execution feedback, and automated repair"),
        (("diffusion", "image", "render", "visual"), "改进图像生成、视觉理解和可控渲染", "improve image generation, visual understanding, and controllable rendering"),
        (("video", "temporal", "motion", "frame"), "评测视频生成的时间一致性和运动真实感", "test temporal consistency and motion realism in video generation"),
        (("safety", "alignment", "jailbreak", "guardrail", "red team"), "识别并缓解模型安全、越狱和对齐风险", "identify and reduce safety, jailbreak, and alignment risks"),
        (("speech", "audio", "voice", "sound"), "扩展语音、音频和声音场景的 AI 能力", "extend AI capabilities across speech, audio, and sound tasks"),
        (("robot", "embodied", "manipulation", "navigation"), "把模型能力落到机器人和具身任务", "bring model capabilities into robotics and embodied tasks"),
        (("interpret", "attribution", "mechanistic", "representation"), "解释模型内部表征和行为归因", "explain internal representations and behavioral attribution"),
        (("benchmark", "evaluation", "eval", "dataset", "metric"), "用新基准和评测方法暴露模型短板", "use benchmarks and evaluations to expose model weaknesses"),
        (("data", "synthetic", "curation", "deduplication"), "改进训练数据筛选、合成和去重流程", "improve training-data curation, synthesis, and deduplication"),
        (("inference", "serving", "latency", "throughput", "cache", "quantization"), "降低推理成本并提升部署效率", "reduce inference cost and improve deployment efficiency"),
    ]
    for keys, zh_desc, en_desc in rules:
        if any(key in text for key in keys):
            return zh_desc if lang == "zh" else en_desc
    if lang == "zh":
        return f"跟进{_topic_label(row, lang)}中的高分研究线索"
    return f"track a high-signal {_topic_label(row, lang).lower()} paper"


def _topic_label(row: ScoredPaper, lang: str) -> str:
    for topic in load_yaml("topics.yaml").get("topics", []):
        if topic.get("slug") == row.topic_slug:
            return topic.get(lang) or topic.get("en") or row.topic
    return "其他" if lang == "zh" else row.topic


def _labels(lang: str) -> dict[str, str]:
    zh = {
        "overview_heading": "一眼看懂本期",
        "trend_heading": "今天最值得跟进的方向",
        "featured_heading": "重点论文：题目、看点与核验线索",
        "mentions_heading": "其他值得关注",
        "keywords_heading": "今日关键词",
        "sources_heading": "来源页链接",
        "disclaimer_heading": "阅读边界",
        "overview": "本期从 {candidates} 篇候选论文中筛出 {featured} 篇重点论文和 {mentions} 篇补充关注论文。重点不是泛泛列主题，而是围绕：{topics}。",
        "trend": "今天的高分论文主要指向：{topics}。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。",
        "sources_sentence": "完整候选池、评分规则摘要和每篇 score breakdown 见 [来源透明页]({url})。",
        "original_title": "原始论文标题",
        "authors": "作者/机构",
        "topic": "归类",
        "code": "代码链接",
        "why": "一句话看点",
        "problem": "它想解决什么",
        "method": "大致怎么做",
        "takeaway": "可以怎样跟进",
        "limits": "注意事项",
        "bullets": "快速判断",
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
        "paper": "看点",
        "unknown": "未知",
        "empty_table": "无。",
        "no_keywords": "无明确关键词。",
    }
    en = {
        "overview_heading": "Quick read",
        "trend_heading": "What is worth tracking today",
        "featured_heading": "Featured papers: title, takeaway, and verification trail",
        "mentions_heading": "Other papers worth tracking",
        "keywords_heading": "Keywords",
        "sources_heading": "Source page",
        "disclaimer_heading": "Reading boundaries",
        "overview": "This issue filters {featured} featured papers and {mentions} additional picks from {candidates} candidates. Rather than broad topic labels, the focus is: {topics}.",
        "trend": "Today’s high-signal papers point to: {topics}. Open the original paper, check the abstract, evaluation setup, and code/data availability before deciding whether to reproduce or adopt the idea.",
        "sources_sentence": "See the [source transparency page]({url}) for the full candidate pool, scoring summary, and per-paper score breakdown.",
        "original_title": "Original paper title",
        "authors": "Authors / institutions",
        "topic": "Category",
        "code": "Code link",
        "why": "One-line takeaway",
        "problem": "Problem it targets",
        "method": "How it appears to work",
        "takeaway": "How to follow up",
        "limits": "Cautions",
        "bullets": "Fast checks",
        "mention_reason": "Why track:",
        "sources_title": "Sources and Scoring",
        "sources_summary": "Source and scoring log for {count} candidate papers",
        "sources_intro": "This page exposes sources and scores for {count} candidate papers. Fetched at {fetched_at}. Generated at {generated_at}. Featured: {featured}; additional picks: {mentions}.",
        "scoring_rules_heading": "Scoring rule summary",
        "scoring_rules": "The score combines institution background, HF Daily Papers, HF upvotes, conference signal, code availability, practitioner keywords, Semantic Scholar citations, GitHub heat, arXiv category weight, novelty/duplicate penalties, recent topic repetition penalties, and safety/ethics/governance keywords. Optional external signals remain empty when APIs are unavailable.",
        "featured_table_heading": "Featured paper table",
        "mentions_table_heading": "Additional paper table",
        "all_candidates_heading": "Full candidate scores",
        "rank": "Rank",
        "paper": "Takeaway",
        "unknown": "Unknown",
        "empty_table": "None.",
        "no_keywords": "No explicit keywords.",
    }
    return zh if lang == "zh" else en
