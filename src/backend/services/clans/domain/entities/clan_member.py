from datetime import datetime
from typing import Self
from uuid import UUID, uuid4

from .....shared.domain import EntityFactory


class ClanMember(EntityFactory):
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

    @classmethod
    def create(  # type: ignore
        cls,
        player_id: int,
        clan_id: UUID,
    ) -> Self:
        clan_member_id = uuid4()
        joined_at = datetime.now()
        clan_member = cls(clan_member_id, player_id, clan_id, joined_at)
        return clan_member
