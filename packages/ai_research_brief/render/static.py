from __future__ import annotations

import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from ..config import REPO_ROOT, site_config, topics_config


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
BRIEF_TITLE_PREFIX_RE = re.compile(r"^今日重点[:：]\s*")


def read_content_documents(lang: str | None = None) -> list[dict]:
    root = REPO_ROOT / "data" / "content"
    pattern = f"{lang}/daily/*.md" if lang else "*/daily/*.md"
    docs = []
    for path in sorted(root.glob(pattern), reverse=True):
        match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        meta = _parse_frontmatter(match.group(1))
        body = match.group(2)
        doc_lang = meta.get("lang") or path.parts[-3]
        slug = meta.get("slug") or path.stem
        docs.append({
            "path": path,
            "meta": meta,
            "body": body,
            "lang": doc_lang,
            "slug": slug,
            "url": f"/{doc_lang}/daily/{slug}/",
        })
    docs.sort(key=lambda doc: (str(doc["meta"].get("date", "")), doc["slug"]), reverse=True)
    return docs


def build_search_index() -> Path:
    rows = []
    for doc in read_content_documents():
        meta = doc["meta"]
        text = _strip_markdown(doc["body"])
        rows.append({
            "title": _clean_title(meta.get("title", "")),
            "date": meta.get("date", ""),
            "lang": doc["lang"],
            "url": doc["url"],
            "summary": meta.get("summary", ""),
            "tags": meta.get("tags", []),
            "topics": meta.get("topics", meta.get("tags", [])),
            "authors": _extract_authors(doc["body"]),
            "content_excerpt": _clean_title(text[:800]),
            "type": meta.get("page_type", "page"),
            "text": _clean_title(text[:5000]),
        })
    out = REPO_ROOT / "apps" / "web" / "public" / "search-index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def build_sitemap() -> Path:
    base_url = site_config().get("site", {}).get("base_url", "").rstrip("/")
    static_paths = [
        "/",
        "/zh/",
        "/en/",
        "/zh/archive/",
        "/en/archive/",
        "/zh/search/",
        "/en/search/",
        "/zh/topics/",
        "/en/topics/",
        "/zh/methodology/",
        "/en/methodology/",
        "/zh/privacy/",
        "/en/privacy/",
        "/zh/whatsnew/",
        "/en/whatsnew/",
    ]
    topic_paths = []
    for lang in ("zh", "en"):
        for topic in topics_config().get("topics", []):
            topic_paths.append(f"/{lang}/topics/{topic['slug']}/")
    urls = static_paths + topic_paths + [doc["url"] for doc in read_content_documents()]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in dict.fromkeys(urls):
        xml += f"  <url><loc>{escape(base_url + url)}</loc></url>\n"
    xml += "</urlset>\n"
    out = REPO_ROOT / "apps" / "web" / "public" / "sitemap.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(xml, encoding="utf-8")
    return out


def _parse_frontmatter(text: str) -> dict:
    meta = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            meta[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            if value.isdigit():
                meta[key.strip()] = int(value)
            else:
                meta[key.strip()] = value.strip('"')
    return meta


def _strip_markdown(text: str) -> str:
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[#*_`>-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _clean_title(text: str) -> str:
    return BRIEF_TITLE_PREFIX_RE.sub("", str(text or "")).strip()


def _extract_authors(markdown: str) -> list[str]:
    authors: list[str] = []
    for match in re.finditer(r"(?:Authors / institutions|作者/机构|Authors):\s*([^\n]+)", markdown):
        value = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", match.group(1)).strip()
        if value and value.lower() not in {"unknown", "未知"}:
            authors.extend([part.strip() for part in value.split(",") if part.strip()])
    return list(dict.fromkeys(authors))[:20]
