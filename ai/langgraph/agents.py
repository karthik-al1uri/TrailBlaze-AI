"""
LangGraph agent nodes for TrailBlaze AI.
Each function takes a TrailBlazeState and returns a partial state update.
"""

import os
from typing import Dict, Any

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from ai.langgraph.state import TrailBlazeState


def _get_llm() -> ChatOpenAI:
    """Return a ChatOpenAI instance using env config."""
    model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
    return ChatOpenAI(model=model, temperature=0)


# ---------------------------------------------------------------------------
# Node 1: Router — classifies the query intent
# ---------------------------------------------------------------------------

def router_agent(state: TrailBlazeState) -> Dict[str, Any]:
    """
    Classify the user query to determine routing.
    Returns route: 'trail', 'weather', or 'both'.
    """
    llm = _get_llm()
    messages = [
        SystemMessage(content=(
            "You are a query classifier for a Colorado trail assistant. "
            "Classify the user query into exactly one category:\n"
            "- 'trail' if the user is asking about trail recommendations, difficulty, distance, scenery, or reviews.\n"
            "- 'weather' if the user is asking only about weather, lightning risk, or conditions.\n"
            "- 'both' if the query involves trail selection AND weather/conditions.\n"
            "Respond with ONLY one word: trail, weather, or both."
        )),
        HumanMessage(content=state["user_query"]),
    ]
    response = llm.invoke(messages)
    route = response.content.strip().lower()

    if route not in ("trail", "weather", "both"):
        route = "both"

    return {"route": route}


# ---------------------------------------------------------------------------
# Node 2: Vector retrieval agent — searches FAISS for relevant trails
# ---------------------------------------------------------------------------

def vector_agent(state: TrailBlazeState, faiss_index) -> Dict[str, Any]:
    """
    Retrieve trail documents from FAISS and format them as context.
    This is a factory-style node; the graph builder wraps it with the index.
    """
    from ai.rag.retriever import retrieve_context, format_context

    docs = retrieve_context(faiss_index, state["user_query"], top_k=3)
    context = format_context(docs)
    return {"retrieved_docs": docs, "trail_context": context}


# ---------------------------------------------------------------------------
# Node 3: Weather agent — provides weather context (simulated for Task 1)
# ---------------------------------------------------------------------------

def weather_agent(state: TrailBlazeState) -> Dict[str, Any]:
    """
    Provide weather context for the user query.
    In Task 1 this is simulated; in later tasks it will call a live API.
    """
    llm = _get_llm()
    messages = [
        SystemMessage(content=(
            "You are a weather information agent for Colorado outdoor activities. "
            "Based on the user query, provide a brief simulated weather summary for "
            "the relevant Colorado area. Include temperature, sky conditions, wind, "
            "and any safety notes (e.g. lightning risk). Keep it to 2-3 sentences. "
            "Note: this is simulated data for development purposes."
        )),
        HumanMessage(content=state["user_query"]),
    ]
    response = llm.invoke(messages)
    return {"weather_context": response.content.strip()}


# ---------------------------------------------------------------------------
# Node 4: Synthesizer — combines all context into a final answer
# ---------------------------------------------------------------------------

def synthesizer_agent(state: TrailBlazeState) -> Dict[str, Any]:
    """
    Synthesize a final grounded answer from trail and weather context.
    """
    llm = _get_llm()

    context_parts = []
    if state.get("trail_context"):
        context_parts.append(f"TRAIL INFORMATION:\n{state['trail_context']}")
    if state.get("weather_context"):
        context_parts.append(f"WEATHER CONTEXT:\n{state['weather_context']}")

    combined_context = "\n\n".join(context_parts) if context_parts else "No context available."

    messages = [
        SystemMessage(content=(
            "You are TrailBlaze AI, an intelligent Colorado trail planning assistant. "
            "Answer the user's question using ONLY the provided context. "
            "Be specific, cite trail names and details, and provide actionable recommendations. "
            "If weather information is available, incorporate safety advice. "
            "If the context does not contain enough information, say so honestly. "
            "Keep your response concise and well-structured."
        )),
        HumanMessage(content=(
            f"User Question: {state['user_query']}\n\n"
            f"Context:\n{combined_context}"
        )),
    ]
    response = llm.invoke(messages)
    return {"answer": response.content.strip()}
