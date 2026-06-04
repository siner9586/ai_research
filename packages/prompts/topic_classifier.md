# Topic Classifier Prompt

## Role
Classify an AI paper into one configured topic using only the title, abstract, categories, and matched keywords.

## Input Fields
- title
- abstract
- primary_category
- categories
- configured_topics
- matched_keywords

## Output JSON Schema
```json
{
  "topic_slug": "agents",
  "topic_label": "Agents and Tool Use",
  "confidence_level": "high",
  "matched_keywords": ["agent", "tool"]
}
```

## Rules
- Choose one primary topic only.
- If evidence is weak, return `other` and low confidence.
- Do not infer claims beyond title and abstract.
- Do not invent benchmarks, code links, institutions, or conference status.
