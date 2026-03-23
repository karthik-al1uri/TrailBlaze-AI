from pydantic import BaseModel


class ItineraryModel(BaseModel):
    user_id: str
    trail_ids: list[str]
    notes: str | None = None
