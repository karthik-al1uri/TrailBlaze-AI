"""
RAG retriever module.
Wraps FAISS similarity search and formats retrieved context for LLM consumption.
"""

from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


def retrieve_context(faiss_index: FAISS, query: str, top_k: int = 3) -> List[Document]:
    """Retrieve top-k trail documents relevant to the user query."""
    return faiss_index.similarity_search(query, k=top_k)


def format_context(documents: List[Document]) -> str:
    """
    Format retrieved documents into a single context string
    suitable for injection into an LLM prompt.
    """
    if not documents:
        return "No relevant trail information found."

    sections = []
    for i, doc in enumerate(documents, 1):
        meta = doc.metadata
        header = f"Trail {i}: {meta.get('name', 'Unknown')}"
        location = f"  Location: {meta.get('location', 'N/A')}"
        difficulty = f"  Difficulty: {meta.get('difficulty', 'N/A')}"
        distance = f"  Distance: {meta.get('distance_miles', 'N/A')} miles"
        elevation = f"  Elevation Gain: {meta.get('elevation_gain_ft', 'N/A')} ft"
        detail = f"  Details: {doc.page_content}"
        sections.append(
            "\n".join([header, location, difficulty, distance, elevation, detail])
        )

    return "\n\n".join(sections)
