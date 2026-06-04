from __future__ import annotations

from pathlib import Path

from .static import build_search_index


def render_search_index() -> Path:
    return build_search_index()
