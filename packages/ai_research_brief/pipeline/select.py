from __future__ import annotations


def select_papers(scored, featured_min=3, featured_max=5, mentions_min=8, mentions_max=12):
    featured = []
    used_topics = set()

    for row in scored:
        if len(featured) >= featured_max:
            break
        if row.topic_slug not in used_topics or len(featured) < featured_min:
            row.selection_tier = "featured"
            featured.append(row)
            used_topics.add(row.topic_slug)

    featured_ids = {row.paper.arxiv_id for row in featured}
    mentions = []
    for row in scored:
        if row.paper.arxiv_id in featured_ids:
            continue
        if len(mentions) >= mentions_max:
            break
        row.selection_tier = "mention"
        mentions.append(row)

    if len(mentions) < mentions_min:
        for row in scored:
            if row.paper.arxiv_id in featured_ids or row in mentions:
                continue
            row.selection_tier = "mention"
            mentions.append(row)
            if len(mentions) >= mentions_min:
                break

    return featured, mentions
