from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ClanDTO(BaseModel):
    clan_id: UUID
    clan_name: str
    clan_tag: str
    owner_id: int
    created_at: datetime
