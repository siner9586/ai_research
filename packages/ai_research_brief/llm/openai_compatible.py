from __future__ import annotations

import os

import httpx

from .base import LLMProvider


class OpenAICompatibleProvider(LLMProvider):
    def __init__(self, api_key: str | None, base_url: str, model: str):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model

    @classmethod
    def from_env(cls, provider: str) -> "OpenAICompatibleProvider":
        if provider == "deepseek":
            api_key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
            base_url = os.environ.get("OPENAI_BASE_URL") or "https://api.deepseek.com"
            model = os.environ.get("OPENAI_MODEL") or "deepseek-chat"
        elif provider == "openrouter":
            api_key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
            base_url = os.environ.get("OPENAI_BASE_URL") or "https://openrouter.ai/api/v1"
            model = os.environ.get("OPENAI_MODEL") or "openai/gpt-4o-mini"
        else:
            api_key = os.environ.get("OPENAI_API_KEY")
            base_url = os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1"
            model = os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"
        return cls(api_key, base_url, model)

    def complete(self, prompt: str, *, system: str | None = None) -> str:
        if not self.api_key:
            raise RuntimeError("LLM provider selected but API key is missing")
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        response = httpx.post(
            f"{self.base_url}/chat/completions",
            timeout=45,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            json={"model": self.model, "messages": messages, "temperature": 0.2},
        )
        response.raise_for_status()
        payload = response.json()
        return payload["choices"][0]["message"]["content"]
