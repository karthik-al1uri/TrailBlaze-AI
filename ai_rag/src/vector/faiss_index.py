"""Vector index abstraction placeholder."""

from dataclasses import dataclass


@dataclass
class SearchResult:
    text: str
    score: float


def query_dummy_index(_: list[float], top_k: int = 3) -> list[SearchResult]:
    samples = [
        SearchResult("Trail has moderate shade and creek crossings.", 0.91),
        SearchResult("Afternoon storms are common above tree line.", 0.87),
        SearchResult("Parking is limited after 8 AM on weekends.", 0.79),
    ]
    return samples[:top_k]
