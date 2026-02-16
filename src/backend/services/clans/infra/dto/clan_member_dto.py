from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ClanMemberDTO(BaseModel):
    clan_member_id: UUID
    player_id: int
    clan_id: UUID
    joined_at: datetime
