import re


def slugify(text: str, max_words: int = 8) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    parts = [p for p in text.split('-') if p]
    return '-'.join(parts[:max_words]) or 'untitled'
