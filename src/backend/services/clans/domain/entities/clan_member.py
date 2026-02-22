from datetime import datetime
from uuid import UUID

from .....shared.domain import Entity


class ClanMember(Entity):
    def __init__(
        self,
        clan_member_id: UUID,
        player_id: int,
        clan_id: UUID,
        joined_at: datetime,
    ):
        super().__init__()
        self.clan_member_id = clan_member_id
        self.player_id = player_id
        self.clan_id = clan_id
        self.joined_at = joined_at
