def classify_topic(title: str, abstract: str):
    text = (title + ' ' + abstract).lower()
    if 'agent' in text or 'tool' in text:
        return 'Agents', ['agent']
    if 'retrieval' in text or 'rag' in text:
        return 'RAG', ['retrieval']
    if 'inference' in text or 'cache' in text:
        return 'LLM Inference', ['inference']
    if 'safety' in text:
        return 'Safety', ['safety']
    if 'code' in text:
        return 'Code Models', ['code']
    if 'benchmark' in text:
        return 'Evaluation', ['benchmark']
    return 'Other', []
