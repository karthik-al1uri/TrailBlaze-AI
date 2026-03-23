"""Task 1 demo: hardcoded query -> embeddings -> dummy FAISS -> synthesized response."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ai_rag.src.vector.faiss_index import query_dummy_index


def fake_embedding(text: str) -> list[float]:
    # Deterministic placeholder embedding for skeleton development.
    base = [float((ord(ch) % 31) / 31.0) for ch in text[:24]]
    return base + [0.0] * max(0, 24 - len(base))


def synthesize_response(query: str, contexts: list[str]) -> str:
    joined = " | ".join(contexts)
    return f"Query: {query}\nGrounded summary: {joined}"


def main() -> None:
    query = "Find a trail near Boulder with shade and low lightning risk."
    embedding = fake_embedding(query)
    hits = query_dummy_index(embedding, top_k=3)
    response = synthesize_response(query, [hit.text for hit in hits])
    print(response)


if __name__ == "__main__":
    main()
