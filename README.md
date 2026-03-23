# TrailBlaze AI

TrailBlaze AI is a smart Colorado outdoor guide that combines trail metadata, weather context,
and review retrieval to answer natural-language trail questions.

## Project Skeleton

This repository is organized by delivery phase:

- `ai_rag/` - LangGraph routing, embeddings, FAISS retrieval, and Task 1 demo script.
- `etl/` - Scrapers, COTREX ingestion placeholders, and text cleaning/chunking pipeline.
- `data/` - Data contracts and storage layout for staged and processed datasets.
- `backend/` - FastAPI service with mock endpoints and starter Mongo models.
- `frontend/` - Next.js/React/Tailwind/Mapbox application shell placeholders.
- `infra/` - Dockerfiles and CI/CD workflow baseline.
- `integration/` - End-to-end acceptance criteria and smoke test scaffold.
- `assets/project-charter/` - Formal project charter and milestone checklist.

## Quick Start

- Backend mock API:
  - `pip install -r backend/requirements.txt`
  - `uvicorn backend.app.main:app --reload`
- RAG smoke demo:
  - `python3 ai_rag/scripts/demo_rag_pipeline.py`
