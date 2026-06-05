from __future__ import annotations

import json
import re
from datetime import date
from functools import lru_cache
from html import escape as html_escape

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
    overview = labels["overview"].format(topics=topic_text)
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
    lines.extend(["", f"## {labels['disclaimer_heading']}"])
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
            "tags": ["internal"],
            "topics": ["internal"],
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
        labels["sources_intro"].format(generated_at=generated_at, fetched_at=fetched_at),
        "",
        f"## {labels['selected_heading']}",
        "",
        _summary_table(featured + mentions, lang),
    ]
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
        why = f"{focus}。{_verification_sentence(row, lang, abstract_sentence)}"
        problem = f"{focus}在真实研究或工程场景中仍不稳定、不透明或成本较高。"
        method = "重点看论文如何设计数据、评测、训练或系统流程。"
        takeaway = "优先核查任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论能否迁移到实际系统。"
        limitations = "这是 arXiv 预印本简报，只能作为跟进线索；结论、实验细节和可复现性仍需阅读全文确认。"
    else:
        why = f"{focus}. {_verification_sentence(row, lang, abstract_sentence)}"
        problem = f"{focus} remains unreliable, opaque, costly, or hard to evaluate in real research and engineering workflows."
        method = "Inspect how the paper sets up data, evaluation, training, or systems design before trusting the claim."
        takeaway = "Verify whether the task setup is realistic, whether code or data are available, whether the evaluation covers complex scenarios, and whether the result can transfer into real systems."
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
    authors = ", ".join(paper.authors[:6]) if paper.authors else labels["unknown"]
    if len(paper.authors) > 6:
        authors += ", et al."
    explanation = _compact_explanation(paper, lang)
    meta_text = html_escape(f"{paper.original_title} ({authors})")
    abs_url = html_escape(paper.abs_url, quote=True)
    pdf_url = html_escape(paper.pdf_url, quote=True)
    lines = [
        "",
        f"### {index}. {paper.short_title}",
        "",
        f"<p class=\"paper-meta-line\"><span>{meta_text}</span> <a class=\"paper-meta-link\" href=\"{abs_url}\">{html_escape(paper.arxiv_id)}</a> <a class=\"paper-meta-link\" href=\"{pdf_url}\">PDF</a></p>",
        "",
        explanation,
    ]
    if paper.code_url:
        code_url = html_escape(paper.code_url, quote=True)
        lines.append(f"<p class=\"paper-meta-line\"><a class=\"paper-meta-link\" href=\"{code_url}\">{labels['code']}</a></p>")
    return lines


def _mention_lines(paper: BriefPaper, lang: str) -> list[str]:
    if lang == "zh":
        reason = _mention_reason(paper, lang)
        return [f"- [{paper.original_title}]({paper.abs_url})：{reason}"]
    reason = _mention_reason(paper, lang)
    return [f"- [{paper.original_title}]({paper.abs_url}): {reason}"]


def _compact_explanation(paper: BriefPaper, lang: str) -> str:
    why = _clean_note(paper.why_it_matters, lang)
    follow = _clean_note(paper.practitioner_takeaway, lang)
    if lang == "zh":
        return f"{why} 重点核验：{follow}"
    return f"{why} Verify whether {follow[0].lower() + follow[1:] if follow else 'the task setup is realistic and the evidence transfers to real workflows'}"


def _mention_reason(paper: BriefPaper, lang: str) -> str:
    title = f"{paper.original_title} {paper.short_title} {paper.topic}".lower()
    if lang == "zh":
        if any(word in title for word in ("safety", "alignment", "jailbreak", "guardrail", "red team", "安全", "对齐")):
            return "关注模型安全、护栏路由、风险分类或治理评测，适合跟进安全评测与治理工具链。"
        if any(word in title for word in ("rag", "retrieval", "database", "检索")):
            return "关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。"
        if any(word in title for word in ("agent", "tool", "workflow", "trajectory")):
            return "关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。"
        if any(word in title for word in ("benchmark", "evaluation", "eval", "评测", "基准")):
            return "关注任务设置、指标和失效案例，适合补充模型评测与回归测试。"
        if any(word in title for word in ("inference", "serving", "latency", "cache", "quantization", "部署")):
            return "关注推理成本、延迟、吞吐和部署约束，适合跟进系统优化。"
        return f"关注{paper.topic}中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。"
    if any(word in title for word in ("safety", "alignment", "jailbreak", "guardrail", "red team")):
        return "Tracks model safety, guardrail routing, risk classification, or governance evaluation; useful for safety and policy workflows."
    if any(word in title for word in ("rag", "retrieval", "database")):
        return "Tracks retrieval, knowledge-base QA, and evidence reliability; useful for RAG evaluation and enterprise knowledge systems."
    if any(word in title for word in ("agent", "tool", "workflow", "trajectory")):
        return "Tracks tool use, execution feedback, and reusable capabilities; useful for agent workflow reliability."
    if any(word in title for word in ("benchmark", "evaluation", "eval")):
        return "Tracks task design, metrics, and failure cases; useful for model evaluation and regression testing."
    if any(word in title for word in ("inference", "serving", "latency", "cache", "quantization", "deployment")):
        return "Tracks inference cost, latency, throughput, and deployment constraints; useful for systems optimization."
    return f"Tracks a concrete {paper.topic.lower()} signal; useful for deciding whether the full paper deserves follow-up."


def _verification_sentence(row: ScoredPaper, lang: str, abstract_sentence: str) -> str:
    topic = _topic_label(row, lang)
    if lang == "zh":
        return (
            f"这篇论文值得跟进，因为{topic}仍需要更真实的任务、更可靠的评测和更清楚的可复现资产。"
        )
    return (
        f"The paper is worth tracking because {topic.lower()} still needs realistic tasks, reliable evaluation, and clearer reproducible assets."
    )


def _clean_note(text: str, lang: str) -> str:
    value = re.sub(r"\s+", " ", text or "").strip()
    value = re.sub(r"^(重点在于|重点是|Core idea|Why track)\s*[:：]\s*", "", value, flags=re.I)
    value = re.sub(r"(摘要给出的直接线索是|摘要中的直接线索是|The abstract signal is)\s*[:：]\s*", "", value, flags=re.I)
    value = re.sub(r"^(It matters because|It targets a verifiable AI research question\.?)\s*", "", value, flags=re.I)
    if not value:
        return "优先阅读全文核验任务、数据、评测和代码资产。" if lang == "zh" else "Check the full paper for task design, data, evaluation, and code assets."
    return value[0].upper() + value[1:] if lang == "en" else value


def _summary_table(rows: list[ScoredPaper], lang: str) -> str:
    labels = _labels(lang)
    if not rows:
        return labels["empty_table"]
    lines = [
        f"| {labels['rank']} | {labels['paper']} | {labels['topic']} | arXiv |",
        "|---:|---|---|---|",
    ]
    for row in rows:
        title = _focus_phrase(row, lang)
        lines.append(f"| {row.rank} | {title} | {_topic_label(row, lang)} | [{row.paper.arxiv_id}]({row.paper.abs_url}) |")
    return "\n".join(lines)


def _brief_title(lang: str, featured: list[ScoredPaper]) -> str:
    if not featured:
        return "今日 AI 论文简报" if lang == "zh" else "Daily AI Research Brief"
    phrases = list(dict.fromkeys(_focus_phrase(row, lang) for row in featured[:4]))
    phrases = phrases[:3]
    if lang == "zh":
        return "、".join(phrases)
    return ", ".join(phrase[:1].upper() + phrase[1:] for phrase in phrases)


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
        "trend_heading": "今天最值得跟进的方向",
        "featured_heading": "重点论文：题目、看点与核验线索",
        "mentions_heading": "其他值得关注",
        "disclaimer_heading": "阅读边界",
        "overview": "今天主要跟进：{topics}。",
        "trend": "今天的高分论文主要指向：{topics}。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。",
        "code": "代码",
        "sources_title": "内部生成记录",
        "sources_summary": "内部生成元数据",
        "sources_intro": "内部生成记录。抓取时间 {fetched_at}，生成时间 {generated_at}；机器可读明细保留在 data/processed 与 data/reports。",
        "selected_heading": "入选论文",
        "rank": "排名",
        "paper": "看点",
        "topic": "主题",
        "unknown": "未知",
        "empty_table": "无。",
    }
    en = {
        "trend_heading": "What is worth tracking today",
        "featured_heading": "Featured papers: title, takeaway, and verification trail",
        "mentions_heading": "Other papers worth tracking",
        "disclaimer_heading": "Reading boundaries",
        "overview": "Today tracks: {topics}.",
        "trend": "Today’s high-signal papers point to: {topics}. Open the original paper, check the abstract, evaluation setup, and code/data availability before deciding whether to reproduce or adopt the idea.",
        "code": "Code",
        "sources_title": "Internal Generation Record",
        "sources_summary": "Internal generation metadata",
        "sources_intro": "Internal generation record. Fetched at {fetched_at}. Generated at {generated_at}. Machine-readable details stay under data/processed and data/reports.",
        "selected_heading": "Selected papers",
        "rank": "Rank",
        "paper": "Takeaway",
        "topic": "Topic",
        "unknown": "Unknown",
        "empty_table": "None.",
    }
    return zh if lang == "zh" else en
