"""
Shared state definition for the TrailBlaze AI LangGraph execution.
All agents read from and write to this typed state dict.
"""

from typing import TypedDict, List, Optional

from langchain_core.documents import Document


class TrailBlazeState(TypedDict):
    """State passed through the LangGraph nodes."""

    # User's original natural-language query
    user_query: str

    # Routing decision: which agents should handle the query
    route: Optional[str]  # "trail", "weather", "both"

    # Retrieved trail documents from FAISS
    retrieved_docs: List[Document]

    # Formatted context string built from retrieved docs
    trail_context: str

    # Weather context (simulated for Task 1)
    weather_context: str

    # Final synthesized answer
    answer: str
