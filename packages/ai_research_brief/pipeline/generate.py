from __future__ import annotations

from datetime import date

from .run_daily import generate_stage


def generate_content(day: date, lang: str | None = None):
    return generate_stage(day, lang=lang)
