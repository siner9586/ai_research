def select_papers(scored, featured_max=5, mentions_max=15):
    featured = scored[:featured_max]
    mentions = scored[featured_max:featured_max+mentions_max]
    return featured, mentions
