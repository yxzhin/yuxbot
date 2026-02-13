from datetime import datetime

from pydantic import BaseModel


class PlayerDTO(BaseModel):
    player_id: int
    username: str
    balance: int
    created_at: datetime
