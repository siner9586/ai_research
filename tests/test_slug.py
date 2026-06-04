from ai_research_brief.utils.slug import slugify


def test_slugify_ascii_title():
    assert slugify("Self Evolving Agents for Tool Use Skills") == "self-evolving-agents-for-tool-use-skills"


def test_slugify_empty_title():
    assert slugify("!!!") == "untitled"
