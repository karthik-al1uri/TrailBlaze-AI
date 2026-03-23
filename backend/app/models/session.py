"""MongoDB document models (starter)."""

from pydantic import BaseModel


class SessionModel(BaseModel):
    session_id: str
    user_id: str
    token_expiry: str
