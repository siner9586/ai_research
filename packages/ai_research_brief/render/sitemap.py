from __future__ import annotations

from pathlib import Path

from .static import build_sitemap


def render_sitemap() -> Path:
    return build_sitemap()
