from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from ..config import REPO_ROOT, load_yaml
from ..models import ScoredPaper
from ..utils.slug import slugify


def render_daily_markdown(
    day: date,
    lang: str,
    featured: list[ScoredPaper],
    mentions: list[ScoredPaper],
    candidates: list[ScoredPaper],
) -> tuple[list[str], str]:
    content_dir = REPO_ROOT / "data" / "content" / lang / "daily"
    content_dir.mkdir(parents=True, exist_ok=True)

    base_title = featured[0].paper.title if featured else "AI paper signals"
    slug = f"{day}-{slugify(base_title, max_words=7)}"
    brief_path = content_dir / f"{slug}.md"
    sources_path = content_dir / f"{slug}-sources.md"
    site = load_yaml("site.yml").get("site", {})
    site_name = site.get("name", {}).get(lang, "Frontier Paper Radar")

    brief_title = _brief_title(lang, featured)
    summary = _brief_summary(lang, featured, len(candidates))
    tags = sorted({row.topic_slug for row in featured + mentions if row.topic_slug != "other"})

    brief = [
        *_frontmatter({
            "title": brief_title,
            "date": str(day),
            "lang": lang,
            "slug": slug,
            "page_type": "brief",
            "site_name": site_name,
            "summary": summary,
            "tags": tags,
            "sources_page": f"/{lang}/daily/{slug}-sources/",
            "candidate_count": len(candidates),
            "featured_count": len(featured),
            "mentions_count": len(mentions),
        }),
        "",
        f"# {brief_title}",
        "",
        summary,
        "",
        _label(lang, "featured_heading"),
    ]

    for index, row in enumerate(featured, start=1):
        brief.extend(_paper_block(index, row, lang, featured=True))

    brief.extend(["", _label(lang, "mentions_heading")])
    for row in mentions:
        brief.append(f"- [{row.paper.title}]({row.paper.abs_url}) - {_topic_label(row, lang)}, score {row.total_score}. {_short_reason(row, lang)}")

    brief.extend([
        "",
        _label(lang, "source_heading"),
        "",
        _label(lang, "source_note").format(
            count=len(candidates),
            url=f"/{lang}/daily/{slug}-sources/",
        ),
        "",
        _label(lang, "limits_heading"),
    ])
    for item in load_yaml("editorial_rules.yml").get("known_limits", {}).get(lang, []):
        brief.append(f"- {item}")

    brief_path.write_text("\n".join(brief) + "\n", encoding="utf-8")

    sources = [
        *_frontmatter({
            "title": _label(lang, "sources_title"),
            "date": str(day),
            "lang": lang,
            "slug": f"{slug}-sources",
            "page_type": "sources",
            "site_name": site_name,
            "summary": _label(lang, "sources_summary").format(count=len(candidates)),
            "tags": ["sources", "scoring"],
            "brief_page": f"/{lang}/daily/{slug}/",
            "candidate_count": len(candidates),
            "featured_count": len(featured),
            "mentions_count": len(mentions),
        }),
        "",
        f"# {_label(lang, 'sources_title')}",
        "",
        _label(lang, "sources_intro").format(
            candidate_count=len(candidates),
            featured_count=len(featured),
            mentions_count=len(mentions),
        ),
    ]

    for row in candidates:
        sources.extend(_source_block(row, lang))

    sources_path.write_text("\n".join(sources) + "\n", encoding="utf-8")
    return [str(brief_path), str(sources_path)], slug


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


def _paper_block(index: int, row: ScoredPaper, lang: str, featured: bool = False) -> list[str]:
    heading = f"## {index}. {row.paper.title}" if featured else f"### {row.paper.title}"
    return [
        "",
        heading,
        "",
        f"- {_label(lang, 'topic')}: {_topic_label(row, lang)}",
        f"- {_label(lang, 'score')}: {row.total_score} ({row.confidence_level})",
        f"- arXiv: [{row.paper.arxiv_id}]({row.paper.abs_url})",
        f"- PDF: [download]({row.paper.pdf_url})",
        f"- {_label(lang, 'why')}: {_short_reason(row, lang)}",
        "",
        _interpretation(row, lang),
    ]


def _source_block(row: ScoredPaper, lang: str) -> list[str]:
    reasons = row.score_reasons or [row.selected_reason]
    signal_bits = []
    signal = row.signal
    if signal.hf_daily:
        signal_bits.append(f"HF Daily ({signal.hf_upvotes} upvotes)")
    if signal.has_code:
        signal_bits.append("code")
    if signal.github_stars:
        signal_bits.append(f"GitHub {signal.github_stars} stars")
    if signal.citation_count:
        signal_bits.append(f"{signal.citation_count} citations")
    if signal.top_conference:
        signal_bits.append(signal.top_conference)
    if signal.top_institution:
        signal_bits.append(", ".join(signal.institutions) or "top institution")
    warnings = "; ".join(signal.warnings)
    return [
        "",
        f"## #{row.rank} {row.paper.title}",
        "",
        f"- Tier: {row.selection_tier}",
        f"- Score: {row.total_score}",
        f"- Topic: {_topic_label(row, lang)}",
        f"- arXiv: [{row.paper.arxiv_id}]({row.paper.abs_url})",
        f"- PDF: [download]({row.paper.pdf_url})",
        f"- Score breakdown: {json.dumps(row.score_breakdown, ensure_ascii=False)}",
        f"- Reasons: {'; '.join(reasons)}",
        f"- Signals: {', '.join(signal_bits) if signal_bits else 'arXiv metadata only'}",
        f"- Matched keywords: {', '.join(row.matched_keywords) if row.matched_keywords else 'none'}",
        f"- Warnings: {warnings}" if warnings else "- Warnings: none",
    ]


def _brief_title(lang: str, featured: list[ScoredPaper]) -> str:
    if not featured:
        return "今日论文信号" if lang == "zh" else "Today in AI Papers"
    first = _topic_label(featured[0], lang)
    second = _topic_label(featured[1], lang) if len(featured) > 1 else featured[0].paper.title
    return f"{first}、{second} 等方向值得跟进" if lang == "zh" else f"{first}, {second}, and other signals to track"


def _brief_summary(lang: str, featured: list[ScoredPaper], count: int) -> str:
    titles = "；".join(row.paper.title for row in featured[:3])
    if lang == "zh":
        return f"本期从 {count} 篇候选论文中筛出 {len(featured)} 篇重点关注。核心线索包括：{titles}。"
    return f"This issue selects {len(featured)} featured papers from {count} candidates. Main signals: {titles}."


def _interpretation(row: ScoredPaper, lang: str) -> str:
    abstract = row.paper.abstract.strip()
    first_sentence = abstract.split(". ")[0].strip()
    topic = _topic_label(row, lang)
    if lang == "zh":
        return f"这篇论文值得关注，因为它把问题落在 **{topic}** 方向，并且摘要显示：{first_sentence}。当前判断基于公开元数据和摘要，完整结论仍应以原论文为准。"
    return f"This paper is worth tracking because it lands in **{topic}** and the abstract indicates: {first_sentence}. The assessment is based on public metadata and the abstract; the original paper remains authoritative."


def _short_reason(row: ScoredPaper, lang: str) -> str:
    if row.score_reasons:
        return row.score_reasons[0]
    return "评分来自 arXiv 相关性" if lang == "zh" else "Score comes from arXiv relevance"


def _label(lang: str, key: str) -> str:
    labels = {
        "zh": {
            "featured_heading": "## 重点关注",
            "mentions_heading": "## 也值得关注",
            "source_heading": "## 来源透明",
            "source_note": "本期候选池共 {count} 篇，完整评分、入选层级和未入选候选见 [来源页]({url})。",
            "limits_heading": "## 已知局限",
            "sources_title": "论文来源与评分",
            "sources_summary": "候选池 {count} 篇论文的评分记录",
            "sources_intro": "本页公开本期 {candidate_count} 篇候选论文的评分记录，其中重点关注 {featured_count} 篇，也值得关注 {mentions_count} 篇。",
            "topic": "方向",
            "score": "评分",
            "why": "入选理由",
        },
        "en": {
            "featured_heading": "## Featured Papers",
            "mentions_heading": "## Also Worth Watching",
            "source_heading": "## Source Transparency",
            "source_note": "The candidate pool contains {count} papers. Full scoring, tiers, and non-selected candidates are available on the [source page]({url}).",
            "limits_heading": "## Known Limits",
            "sources_title": "Sources and Scoring",
            "sources_summary": "Scoring log for {count} candidate papers",
            "sources_intro": "This page exposes the scoring log for {candidate_count} candidate papers: {featured_count} featured and {mentions_count} also worth watching.",
            "topic": "Topic",
            "score": "Score",
            "why": "Why selected",
        },
    }
    return labels[lang][key]


def _topic_label(row: ScoredPaper, lang: str) -> str:
    for topic in load_yaml("topics.yml").get("topics", []):
        if topic.get("slug") == row.topic_slug:
            return topic.get(lang) or topic.get("en") or row.topic
    return "其他" if lang == "zh" else row.topic
