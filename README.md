# TrailBlaze AI

Smart Colorado outdoor guide: trail discovery with RAG over reviews and condition reports, plus weather-aware safety context.

## Stack (planned)

- **Cloud:** AWS
- **Source control:** GitHub
- **Agile:** Trello

## Repository layout

| Path | Purpose |
|------|---------|
| `backend/` | API, RAG pipeline, orchestration |
| `frontend/` | Web UI (to be added) |
| `infra/` | IaC, deployment configs |
| `docs/` | Design notes, ADRs |
| `data/` | Local samples only — **do not commit** scraped data or secrets |

## Quick start (backend)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Environment

Copy `.env.example` to `.env` and fill in keys. Never commit `.env`.

## License

TBD (team decision).
