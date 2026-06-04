from __future__ import annotations

from pathlib import Path

from ..config import REPO_ROOT


PROMPT_DIR = REPO_ROOT / "packages" / "prompts"


def load_prompt(name: str) -> str:
    path = PROMPT_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")
