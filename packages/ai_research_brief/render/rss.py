from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

from ..config import REPO_ROOT, site_config
from .static import _clean_generated_text, _public_briefs, _strip_markdown, read_content_documents


def build_rss(lang: str) -> Path:
    config = site_config().get("site", {})
    base_url = config.get("base_url", "").rstrip("/")
    site_name = config.get("name", {}).get(lang, "AI Research Brief")
    description = config.get("description", {}).get(lang, "")
    docs = _public_briefs(read_content_documents(lang))[:30]

    items = []
    content_open = "<" + "content" + ">"
    content_close = "</" + "content" + ">"
    for doc in docs:
        meta = doc["meta"]
        url = f"{base_url}{doc['url']}"
        source_url = str(meta.get("sources_page") or "")
        source_abs = f"{base_url}{source_url}" if source_url.startswith("/") else source_url
        pub_date = _rss_date(str(meta.get("date", "")))
        summary = _clean_generated_text(str(meta.get("summary", "")))
        if source_abs:
            summary = f"{summary} Source page: {source_abs}"
        body_text = _clean_generated_text(_strip_markdown(str(doc.get("body", ""))))
        item_content = body_text or summary
        items.append(
            "<item>"
            f"<title>{escape(str(meta.get('title', '')))}</title>"
            f"<link>{escape(url)}</link>"
            f"<guid>{escape(url)}</guid>"
            f"<description>{escape(summary)}</description>"
            f"{content_open}{escape(item_content)}{content_close}"
            f"<pubDate>{pub_date}</pubDate>"
            f"<language>{escape(lang)}</language>"
            "</item>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        f"<title>{escape(site_name)}</title>"
        f"<link>{escape(base_url + '/' + lang + '/')}</link>"
        f"<description>{escape(description)}</description>"
        + "".join(items)
        + "</channel></rss>\n"
    )
    out = REPO_ROOT / "apps" / "web" / "public" / lang / "feed.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(xml, encoding="utf-8")
    return out


def _rss_date(value: str) -> str:
    try:
        dt = datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
    except ValueError:
        dt = datetime.now(timezone.utc)
    return format_datetime(dt)
