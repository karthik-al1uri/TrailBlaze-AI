from fastapi import FastAPI

app = FastAPI(title="TrailBlaze API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/chat/mock")
def chat_mock() -> dict[str, object]:
    return {
        "message": "Mock response from backend.",
        "sources": ["dummy-faiss-hit-1", "dummy-faiss-hit-2"],
        "itinerary_id": None,
    }
