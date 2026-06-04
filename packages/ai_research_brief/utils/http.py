from __future__ import annotations

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential


DEFAULT_USER_AGENT = "ai-research-brief/0.1 (+https://github.com/siner9586/ai_research)"


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
def get_text(url: str, timeout: float = 30.0, headers: dict[str, str] | None = None) -> str:
    request_headers = {"User-Agent": DEFAULT_USER_AGENT}
    if headers:
        request_headers.update(headers)
    response = httpx.get(url, timeout=timeout, follow_redirects=True, headers=request_headers)
    response.raise_for_status()
    return response.text


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
def get_json(url: str, timeout: float = 15.0, headers: dict[str, str] | None = None):
    request_headers = {"User-Agent": DEFAULT_USER_AGENT}
    if headers:
        request_headers.update(headers)
    response = httpx.get(url, timeout=timeout, follow_redirects=True, headers=request_headers)
    response.raise_for_status()
    return response.json()
