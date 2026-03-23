"""LangGraph routing skeleton for vector and weather agents."""

from typing import TypedDict


class AgentState(TypedDict):
    query: str
    route: str
    context: str
    response: str


def route_query(query: str) -> str:
    lowered = query.lower()
    if "weather" in lowered or "rain" in lowered or "storm" in lowered:
        return "weather"
    return "vector"
