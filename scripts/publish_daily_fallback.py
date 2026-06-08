from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.render.rss import build_rss
from ai_research_brief.render.static import build_search_index, build_sitemap

TZ = ZoneInfo("Asia/Shanghai")


def main() -> None:
    publish_date = datetime.now(TZ).date().isoformat()
    generated_at = datetime.now(timezone.utc).isoformat()
    slug = f"{publish_date}-generation-status-and-source-availability"
    for lang in ("zh", "en"):
        daily_dir = REPO_ROOT / "data" / "content" / lang / "daily"
        daily_dir.mkdir(parents=True, exist_ok=True)
        existing = [p for p in daily_dir.glob(f"{publish_date}-*.md") if not p.stem.endswith("-sources")]
        if existing:
            print(f"{lang}: issue already exists for {publish_date}, skip fallback")
            continue
        if lang == "zh":
            title = "自动生成状态与数据源可用性说明"
            summary = "今日自动生成流程未取得足够稳定的上游论文数据，已发布透明状态页；系统会在后续补偿任务中继续尝试生成正式简报。"
            brief_body = f"""---
title: {title!r}
date: {publish_date!r}
target_date: ""
actual_date: ""
fallback_from: ""
lang: "zh"
slug: {slug!r}
summary: {summary!r}
tags: ["status"]
topics: ["status"]
sources_page: "/zh/daily/{slug}-sources/"
generated_at: {generated_at!r}
page_type: "brief"
candidate_count: 0
featured_count: 0
mentions_count: 0
---

# {title}

## 今日状态

{summary}

这不是论文质量结论，也不会编造论文、代码链接、数据链接或同行评审状态。页面保留当天日期，避免站点日更断档；后续补偿任务若成功取得有效候选，会重新生成正式简报并替换本状态页。

## 建议阅读

- 可以先查看归档页中的最近一期有效简报。
- 可以稍后刷新本站，等待补偿任务完成。
- 来源页记录了本次降级发布的元数据。
"""
            source_body = f"""---
title: "内部生成状态记录"
date: {publish_date!r}
target_date: ""
actual_date: ""
fallback_from: ""
lang: "zh"
slug: "{slug}-sources"
summary: "降级发布记录"
tags: ["internal", "status"]
topics: ["internal", "status"]
brief_page: "/zh/daily/{slug}/"
generated_at: {generated_at!r}
page_type: "sources"
candidate_count: 0
featured_count: 0
mentions_count: 0
---

# 内部生成状态记录

本页说明：正式抓取或生成流程未能在当前运行中产出稳定候选，因此发布透明状态页作为日更兜底。后续补偿任务仍会继续尝试正式生成。
"""
        else:
            title = "Generation status and source availability note"
            summary = "The daily pipeline did not obtain a stable upstream paper set, so a transparent status page was published while catch-up jobs keep retrying."
            brief_body = f"""---
title: {title!r}
date: {publish_date!r}
target_date: ""
actual_date: ""
fallback_from: ""
lang: "en"
slug: {slug!r}
summary: {summary!r}
tags: ["status"]
topics: ["status"]
sources_page: "/en/daily/{slug}-sources/"
generated_at: {generated_at!r}
page_type: "brief"
candidate_count: 0
featured_count: 0
mentions_count: 0
---

# {title}

## Status

{summary}

This page does not invent paper claims, code links, datasets, or peer-review status. It keeps the publication date live while the catch-up workflow continues to retry the full brief generation. If a later retry obtains a stable candidate set, the formal brief can replace this status page.

## Suggested reading

- Check the archive for the latest full brief.
- Refresh the site later after catch-up jobs complete.
- The source page records this degraded publication state.
"""
            source_body = f"""---
title: "Internal generation status record"
date: {publish_date!r}
target_date: ""
actual_date: ""
fallback_from: ""
lang: "en"
slug: "{slug}-sources"
summary: "Fallback publication record"
tags: ["internal", "status"]
topics: ["internal", "status"]
brief_page: "/en/daily/{slug}/"
generated_at: {generated_at!r}
page_type: "sources"
candidate_count: 0
featured_count: 0
mentions_count: 0
---

# Internal generation status record

The full upstream fetch or generation pipeline did not produce a stable candidate set in this run, so this transparent status page was published as a daily fallback. Catch-up jobs will keep retrying the full generation path.
"""
        (daily_dir / f"{slug}.md").write_text(brief_body, encoding="utf-8")
        (daily_dir / f"{slug}-sources.md").write_text(source_body, encoding="utf-8")
        print(f"{lang}: wrote fallback issue {slug}")
    build_rss("zh")
    build_rss("en")
    build_search_index()
    build_sitemap()


if __name__ == "__main__":
    main()
