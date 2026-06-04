from __future__ import annotations

import os
import re

import httpx


GITHUB_URL_RE = re.compile(r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")


def extract_github_url(text: str) -> str | None:
    match = GITHUB_URL_RE.search(text)
    return match.group(0).rstrip(".") if match else None


def fetch_repo_signal(repo_url: str, timeout: float = 8.0) -> dict:
    match = re.search(r"github\.com/([^/\s]+)/([^/\s#?]+)", repo_url)
    if not match:
        return {}
    owner, repo = match.groups()
    headers = {"User-Agent": "frontier-paper-radar/0.1"}
    if os.environ.get("GITHUB_API_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_API_TOKEN']}"
    try:
        response = httpx.get(f"https://api.github.com/repos/{owner}/{repo}", timeout=timeout, headers=headers)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return {}
    return {
        "github_stars": int(payload.get("stargazers_count") or 0),
        "github_forks": int(payload.get("forks_count") or 0),
    }
