from __future__ import annotations

import os
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def complete(self, prompt: str, *, system: str | None = None) -> str:
        raise NotImplementedError


def get_provider() -> LLMProvider:
    provider = os.environ.get("LLM_PROVIDER", "mock").lower()
    if provider in {"openai", "deepseek", "openrouter"}:
        from .openai_compatible import OpenAICompatibleProvider

        return OpenAICompatibleProvider.from_env(provider)

    from .mock import MockLLMProvider

    return MockLLMProvider()
