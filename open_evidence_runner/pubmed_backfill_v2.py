from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import Any

import pubmed_backfill as base


def text_content(node: ET.Element | None) -> str | None:
    if node is None:
        return None
    value = " ".join("".join(node.itertext()).split())
    return value or None


def extract_book_article(
    node: ET.Element, query_group: str, query_text: str
) -> dict[str, Any]:
    document = node.find("BookDocument")
    if document is None:
        raise ValueError("PubmedBookArticle has no BookDocument")

    pmid = text_content(document.find("PMID"))
    ids: dict[str, str] = {}
    for identifier in document.findall("ArticleIdList/ArticleId"):
        id_type = (identifier.attrib.get("IdType") or "").lower()
        value = text_content(identifier)
        if id_type and value:
            ids[id_type] = value

    title = text_content(document.find("ArticleTitle"))
    book_title = text_content(document.find("Book/BookTitle"))
    publisher = text_content(document.find("Book/Publisher/PublisherName"))

    abstract_parts: list[str] = []
    for abstract_node in document.findall("Abstract/AbstractText"):
        value = text_content(abstract_node)
        if not value:
            continue
        label = abstract_node.attrib.get("Label")
        abstract_parts.append(f"{label}: {value}" if label else value)

    authors: list[str] = []
    for author in document.findall("AuthorList/Author"):
        collective = text_content(author.find("CollectiveName"))
        if collective:
            authors.append(collective)
            continue
        fore = text_content(author.find("ForeName"))
        last = text_content(author.find("LastName"))
        name = " ".join(part for part in (fore, last) if part)
        if name:
            authors.append(name)

    publication_year = None
    date_candidates = [
        text_content(document.find("Book/PubDate/Year")),
        text_content(document.find("Book/PubDate/MedlineDate")),
        text_content(document.find("DateRevised/Year")),
    ]
    publication_date_text = next((value for value in date_candidates if value), None)
    if publication_date_text:
        match = re.search(r"(?:19|20)\d{2}", publication_date_text)
        publication_year = int(match.group()) if match else None

    publication_types = [
        value
        for item in document.findall("PublicationType")
        if (value := text_content(item))
    ]
    if not publication_types:
        publication_types = ["PubmedBookArticle"]

    return {
        "source_name": "PubMed",
        "source_external_id": pmid,
        "pmid": pmid,
        "pmcid": ids.get("pmc"),
        "doi_normalized": base.normalize_doi(ids.get("doi")),
        "pii": ids.get("pii"),
        "book_accession": ids.get("bookaccession"),
        "canonical_title": title or book_title,
        "abstract": "\n".join(abstract_parts) or None,
        "publication_year": publication_year,
        "publication_date_text": publication_date_text,
        "venue": book_title,
        "publisher": publisher,
        "authors": authors,
        "publication_types": publication_types,
        "mesh_terms": [],
        "languages": [],
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else None,
        "query_groups": [query_group],
        "query_texts": [query_text],
        "retrieved_at": base.utcnow(),
    }


def parse_pubmed_xml(
    payload: bytes, query_group: str, query_text: str
) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    records = [
        base.extract_article(article, query_group, query_text)
        for article in root.findall("PubmedArticle")
    ]
    records.extend(
        extract_book_article(article, query_group, query_text)
        for article in root.findall("PubmedBookArticle")
    )
    return records


base.parse_pubmed_xml = parse_pubmed_xml


if __name__ == "__main__":
    base.main()
