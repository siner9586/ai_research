from __future__ import annotations

import json
import re
from datetime import date
from html import escape as html_escape

from ..config import REPO_ROOT, load_yaml
from ..models import BriefPaper, DailyBrief, ScoredPaper, utc_now
from ..utils.slug import slugify
from ..utils.text import first_sentence

_CODE_DATA_ZH = "代码/数据可用性需查看原文确认。"
_CODE_DATA_EN = "Code/data availability should be checked in the source paper."


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
    brief_path.write_text(_brief_markdown(brief, candidates, day, target_date, fallback_from) + "\n", encoding="utf-8")
    sources_path.write_text(
        _sources_markdown(day, lang, slug, featured, mentions, candidates, publish_date, target_date, fallback_from) + "\n",
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
    return DailyBrief(
        date=day,
        lang=lang,
        title=_brief_title(lang, featured),
        slug=slug,
        overview=labels["overview"].format(topics=topic_text),
        trend_observation=labels["trend"].format(topics=topic_text),
        featured_papers=[_brief_paper(row, lang) for row in featured],
        honorable_mentions=[_brief_paper(row, lang) for row in mentions],
        keywords=sorted({keyword for row in featured + mentions for keyword in (row.matched_keywords or [row.topic_slug])})[:14],
        sources_path=sources_path,
    )


def _brief_markdown(brief: DailyBrief, candidates: list[ScoredPaper], data_date: date, target_date: date, fallback_from: date | None) -> str:
    labels = _labels(brief.lang)
    tags = sorted({paper.topic_slug for paper in brief.featured_papers + brief.honorable_mentions if paper.topic_slug != "other"})
    lines = [
        *_frontmatter({
            "title": brief.title,
            "date": str(brief.date),
            "target_date": str(target_date),
            "actual_date": str(data_date),
            "fallback_from": str(fallback_from) if fallback_from else "",
            "lang": brief.lang,
            "slug": brief.slug,
            "summary": brief.overview,
            "tags": tags,
            "topics": tags,
            "sources_page": f"/{brief.lang}/daily/{brief.slug}-sources/",
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
        lines.extend(_paper_section(index, paper, brief.lang))
    lines.extend(["", f"## {labels['mentions_heading']}"])
    for paper in brief.honorable_mentions:
        lines.extend(_mention_lines(paper, brief.lang))
    lines.extend(["", f"## {labels['disclaimer_heading']}"])
    for item in load_yaml("editorial_rules.yaml").get("known_limits", {}).get(brief.lang, []):
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
    return "\n".join([
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
    ])


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
    focus = _focus_phrase(row, lang)
    keywords = _paper_keywords(row)
    abstract_sentence = _safe_sentence(row.paper.abstract)
    if lang == "zh":
        problem = f"{focus}这一方向中的具体研究问题"
        method = _method_signal(row, keywords, lang)
        claim = f"标题、摘要和公开信号显示：{abstract_sentence}"
        limit = _CODE_DATA_ZH
    else:
        problem = f"the concrete research problem behind {focus}"
        method = _method_signal(row, keywords, lang)
        claim = f"the title, abstract, and public signals indicate: {abstract_sentence}"
        limit = _CODE_DATA_EN
    return BriefPaper(
        arxiv_id=row.paper.arxiv_id,
        title=row.paper.title,
        short_title=focus,
        original_title=row.paper.title,
        authors=row.paper.authors,
        topic=_topic_label(row, lang),
        topic_slug=row.topic_slug,
        score=row.total_score,
        abs_url=row.paper.abs_url,
        pdf_url=row.paper.pdf_url,
        code_url=row.signal.code_url,
        why_it_matters=claim,
        problem=problem,
        method=method,
        practitioner_takeaway=claim,
        limitations=limit,
        bullets=keywords,
    )


def _paper_section(index: int, paper: BriefPaper, lang: str) -> list[str]:
    labels = _labels(lang)
    authors = ", ".join(paper.authors[:6]) if paper.authors else labels["unknown"]
    if len(paper.authors) > 6:
        authors += ", et al."
    meta_text = html_escape(f"{paper.original_title} ({authors})")
    abs_url = html_escape(paper.abs_url, quote=True)
    pdf_url = html_escape(paper.pdf_url, quote=True)
    lines = [
        "",
        f"### {index}. {paper.short_title}",
        "",
        f"<p class=\"paper-meta-line\"><span>{meta_text}</span> <a class=\"paper-meta-link\" href=\"{abs_url}\">{html_escape(paper.arxiv_id)}</a> <a class=\"paper-meta-link\" href=\"{pdf_url}\">PDF</a></p>",
        "",
        _compact_explanation(paper, lang),
    ]
    if paper.code_url:
        lines.append(f"<p class=\"paper-meta-line\"><a class=\"paper-meta-link\" href=\"{html_escape(paper.code_url, quote=True)}\">{labels['code']}</a></p>")
    return lines


def _compact_explanation(paper: BriefPaper, lang: str) -> str:
    keywords = _format_keywords(paper.bullets, lang)
    if lang == "zh":
        return f"核心：这篇论文主要解决{_trim_clause(paper.problem)}；方法上通过{_trim_clause(paper.method)}实现{paper.short_title}；主要论点是{_trim_clause(paper.practitioner_takeaway)}。关键词：{keywords}。{_CODE_DATA_ZH}"
    return f"Core idea: this paper targets {_trim_clause(paper.problem)}. It uses {_trim_clause(paper.method)} to improve {paper.short_title}. The main claim is {_trim_clause(paper.practitioner_takeaway)}. Keywords: {keywords}. {_CODE_DATA_EN}"


def _mention_lines(paper: BriefPaper, lang: str) -> list[str]:
    reason = _mention_reason(paper, lang)
    if lang == "zh":
        return [f"- [{paper.original_title}]({paper.abs_url})：{reason}"]
    return [f"- [{paper.original_title}]({paper.abs_url}): {reason}"]


def _mention_reason(paper: BriefPaper, lang: str) -> str:
    title = f"{paper.original_title} {paper.short_title} {paper.topic}".lower()
    if lang == "zh":
        if any(word in title for word in ("safety", "alignment", "jailbreak", "guardrail", "red team", "安全", "对齐")):
            return "涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。"
        if any(word in title for word in ("rag", "retrieval", "database", "检索")):
            return "涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。"
        if any(word in title for word in ("agent", "tool", "workflow", "trajectory")):
            return "涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。"
        if any(word in title for word in ("benchmark", "evaluation", "eval", "评测", "基准")):
            return "涉及任务设置、指标和失效案例，可补充模型评测与回归测试。"
        if any(word in title for word in ("inference", "serving", "latency", "cache", "quantization", "部署")):
            return "涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。"
        return f"涉及{paper.topic}中的新任务、数据或系统线索，可作为后续跟进清单的一部分。"
    if any(word in title for word in ("safety", "alignment", "jailbreak", "guardrail", "red team")):
        return "Covers model safety, guardrail routing, risk classification, or governance evaluation; useful as a safety workflow lead."
    if any(word in title for word in ("rag", "retrieval", "database")):
        return "Covers retrieval, knowledge-base QA, and evidence reliability; useful as a RAG evaluation lead."
    if any(word in title for word in ("agent", "tool", "workflow", "trajectory")):
        return "Covers tool use, execution feedback, and reusable capabilities; useful as an agent reliability lead."
    if any(word in title for word in ("benchmark", "evaluation", "eval")):
        return "Covers task design, metrics, and failure cases; useful for model evaluation and regression tests."
    if any(word in title for word in ("inference", "serving", "latency", "cache", "quantization", "deployment")):
        return "Covers inference cost, latency, throughput, and deployment constraints; useful for systems optimization."
    return f"Covers a concrete {paper.topic.lower()} signal; useful as a follow-up candidate."


def _method_signal(row: ScoredPaper, keywords: list[str], lang: str) -> str:
    keyword_text = _format_keywords(keywords, lang)
    topic = _topic_label(row, lang)
    if lang == "zh":
        code_hint = "，并带有代码或可执行资产信号" if row.signal.code_url else ""
        return f"题名、摘要和公开信号中的 {keyword_text} 等线索来组织{topic}任务、数据或评测流程{code_hint}"
    code_hint = ", with a code or executable-asset signal" if row.signal.code_url else ""
    return f"the title, abstract, and public signals around {keyword_text} to frame the {topic.lower()} task, data, or evaluation flow{code_hint}"


def _paper_keywords(row: ScoredPaper) -> list[str]:
    values: list[str] = []
    for source in (row.matched_keywords, row.signal.matched_keywords, [row.topic_slug, row.topic]):
        for item in source or []:
            clean = re.sub(r"\s+", " ", str(item)).strip()
            if clean and clean.lower() not in {v.lower() for v in values}:
                values.append(clean)
    return values[:5] or [row.topic_slug]


def _format_keywords(values: list[str], lang: str) -> str:
    clean = [re.sub(r"\s+", " ", str(value)).strip() for value in values if str(value).strip()]
    clean = list(dict.fromkeys(clean))[:4]
    if not clean:
        clean = ["AI research" if lang == "en" else "AI 研究"]
    return "、".join(clean) if lang == "zh" else ", ".join(clean)


def _safe_sentence(text: str) -> str:
    value = first_sentence(text or "") or (text or "").strip()
    return re.sub(r"\s+", " ", value).strip() or "the abstract provides a high-level signal"


def _trim_clause(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().rstrip("。.;；") or "论文题名和摘要给出的研究线索"


def _summary_table(rows: list[ScoredPaper], lang: str) -> str:
    labels = _labels(lang)
    if not rows:
        return labels["empty_table"]
    lines = [f"| {labels['rank']} | {labels['paper']} | {labels['topic']} | arXiv |", "|---:|---|---|---|"]
    for row in rows:
        lines.append(f"| {row.rank} | {_focus_phrase(row, lang)} | {_topic_label(row, lang)} | [{row.paper.arxiv_id}]({row.paper.abs_url}) |")
    return "\n".join(lines)


def _brief_title(lang: str, featured: list[ScoredPaper]) -> str:
    if not featured:
        return "今日 AI 论文简报" if lang == "zh" else "Daily AI Research Brief"
    phrases = list(dict.fromkeys(_focus_phrase(row, lang) for row in featured[:4]))[:3]
    return "、".join(phrases) if lang == "zh" else ", ".join(phrase[:1].upper() + phrase[1:] for phrase in phrases)


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
    return f"跟进{_topic_label(row, lang)}中的高分研究线索" if lang == "zh" else f"track a high-signal {_topic_label(row, lang).lower()} paper"


def _topic_label(row: ScoredPaper, lang: str) -> str:
    for topic in load_yaml("topics.yaml").get("topics", []):
        if topic.get("slug") == row.topic_slug:
            return topic.get(lang) or topic.get("en") or row.topic
    return "其他" if lang == "zh" else row.topic


def _labels(lang: str) -> dict[str, str]:
    zh = {
        "trend_heading": "今天最值得跟进的方向",
        "featured_heading": "重点论文：核心问题、方法线索与关键词",
        "mentions_heading": "其他值得关注",
        "disclaimer_heading": "阅读边界",
        "overview": "今天主要跟进：{topics}。",
        "trend": "今天的高分论文主要指向：{topics}。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。",
        "code": "代码",
        "sources_title": "内部生成记录",
        "sources_summary": "内部生成元数据：本期候选论文 {count} 篇。",
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
        "featured_heading": "Featured papers: core problem, method signal, and keywords",
        "mentions_heading": "Other papers worth tracking",
        "disclaimer_heading": "Reading boundaries",
        "overview": "Today tracks: {topics}.",
        "trend": "Today’s high-signal papers point to: {topics}. The notes below focus on the core problem, method signal, main claim, and keywords for each featured paper.",
        "code": "Code",
        "sources_title": "Internal Generation Record",
        "sources_summary": "Internal generation metadata: {count} candidate papers.",
        "sources_intro": "Internal generation record. Fetched at {fetched_at}. Generated at {generated_at}. Machine-readable details stay under data/processed and data/reports.",
        "selected_heading": "Selected papers",
        "rank": "Rank",
        "paper": "Takeaway",
        "topic": "Topic",
        "unknown": "Unknown",
        "empty_table": "None.",
    }
    return zh if lang == "zh" else en
