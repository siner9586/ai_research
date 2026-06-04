from ..config import scoring_config
from ..models import PaperSignal, ScoredPaper
from .topics import classify_topic


def score_papers(papers, signals):
    config = scoring_config()
    weights = config.get("weights", {})
    thresholds = config.get("thresholds", {})
    rows = []
    for paper in papers:
        sig = signals[paper.arxiv_id]
        text = (paper.title + ' ' + paper.abstract).lower()
        score = 0
        parts = {}
        reasons = []

        if sig.top_institution:
            value = int(weights.get("institution_background", 3))
            parts["institution_background"] = value
            reasons.append("Top institution signal" + (f": {', '.join(sig.institutions)}" if sig.institutions else ""))
            score += value

        if sig.hf_daily:
            value = int(weights.get("hf_daily", 3))
            parts['hf_daily'] = value
            reasons.append("Included by HF Daily Papers")
            score += value

        if sig.hf_upvotes >= int(thresholds.get("hf_upvotes_viral", 80)):
            value = int(weights.get("hf_upvotes_viral", 5))
            parts['hf_upvotes'] = value
            reasons.append(f"HF community heat: {sig.hf_upvotes} upvotes")
            score += value
        elif sig.hf_upvotes >= int(thresholds.get("hf_upvotes_high", 25)):
            value = int(weights.get("hf_upvotes_high", 4))
            parts['hf_upvotes'] = value
            reasons.append(f"HF community heat: {sig.hf_upvotes} upvotes")
            score += value
        elif sig.hf_upvotes >= int(thresholds.get("hf_upvotes_mid", 10)):
            value = int(weights.get("hf_upvotes_mid", 3))
            parts['hf_upvotes'] = value
            reasons.append(f"HF community heat: {sig.hf_upvotes} upvotes")
            score += value
        elif sig.hf_upvotes >= int(thresholds.get("hf_upvotes_low", 1)):
            value = int(weights.get("hf_upvotes_low", 1))
            parts['hf_upvotes'] = value
            reasons.append(f"Early HF votes: {sig.hf_upvotes}")
            score += value

        if sig.top_conference:
            value = int(weights.get("top_conference", 3))
            parts["top_conference"] = value
            reasons.append(f"Top conference signal: {sig.top_conference}")
            score += value

        if sig.has_code:
            value = int(weights.get("code_available", 2))
            parts['code_available'] = value
            reasons.append("Code or executable artifact signal")
            score += value

        if sig.github_stars >= int(thresholds.get("github_stars", 100)) or sig.github_trending:
            value = int(weights.get("open_source_heat", 2))
            parts['open_source_heat'] = value
            reasons.append(f"Open-source heat: {sig.github_stars} stars")
            score += value

        if sig.citation_count >= int(thresholds.get("citation_high", 500)):
            value = int(weights.get("citation_high", 3))
            parts["citation_count"] = value
            reasons.append(f"Academic impact signal: {sig.citation_count} citations")
            score += value
        elif sig.citation_count >= int(thresholds.get("citation_mid", 100)):
            value = int(weights.get("citation_mid", 2))
            parts["citation_count"] = value
            reasons.append(f"Academic impact signal: {sig.citation_count} citations")
            score += value
        elif sig.citation_count >= int(thresholds.get("citation_low", 20)):
            value = int(weights.get("citation_low", 1))
            parts["citation_count"] = value
            reasons.append(f"Early citation signal: {sig.citation_count} citations")
            score += value

        keywords = [w for w in config.get("practitioner_keywords", []) if w.lower() in text]
        if keywords:
            value = min(int(weights.get("practitioner_relevance", 4)), len(keywords))
            parts['practitioner_relevance'] = value
            reasons.append(f"Practitioner keywords: {', '.join(keywords[:6])}")
            score += value

        topic, topic_slug, hits = classify_topic(paper.title, paper.abstract)
        rows.append(ScoredPaper(
            paper=paper,
            signal=sig,
            total_score=score,
            score_breakdown=parts,
            score_reasons=reasons,
            selected_reason='; '.join(reasons) or 'arXiv category relevance',
            matched_keywords=list(dict.fromkeys(keywords + sig.matched_keywords + hits)),
            topic=topic,
            topic_slug=topic_slug,
            confidence_level='high' if score >= 10 else 'medium' if score >= 5 else 'low',
        ))

    rows = sorted(rows, key=lambda x: (x.total_score, x.paper.published_at), reverse=True)
    for index, row in enumerate(rows, start=1):
        row.rank = index
    return rows
