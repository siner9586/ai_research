from ..models import PaperSignal, ScoredPaper
from .topics import classify_topic


def score_papers(papers, signals):
    rows = []
    for paper in papers:
        sig = signals[paper.arxiv_id]
        text = (paper.title + ' ' + paper.abstract).lower()
        score = 0
        parts = {}
        if sig.hf_daily:
            parts['hf_daily'] = 3
            score += 3
        if sig.hf_upvotes >= 25:
            parts['hf_upvotes'] = 4
            score += 4
        elif sig.hf_upvotes >= 10:
            parts['hf_upvotes'] = 3
            score += 3
        if sig.has_code:
            parts['has_code'] = 2
            score += 2
        if sig.github_stars >= 100:
            parts['github_stars'] = 2
            score += 2
        keywords = [w for w in ['agent','tool','rag','retrieval','inference','benchmark','evaluation','code','safety','multimodal'] if w in text]
        if keywords:
            parts['keywords'] = min(4, len(keywords))
            score += parts['keywords']
        topic, hits = classify_topic(paper.title, paper.abstract)
        rows.append(ScoredPaper(paper=paper, signal=sig, total_score=score, score_breakdown=parts, selected_reason=', '.join(parts.keys()) or 'arxiv relevance', matched_keywords=list(dict.fromkeys(keywords + hits)), topic=topic, confidence_level='high' if score >= 7 else 'medium' if score >= 4 else 'low'))
    return sorted(rows, key=lambda x: x.total_score, reverse=True)
