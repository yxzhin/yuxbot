from datetime import datetime
from typing import Self
from uuid import UUID, uuid4

from .....shared.domain import Aggregate
from ..events import ClanCreatedEvent, ClanMemberJoinedEvent
from ..value_objects import ClanName, ClanTag
from .clan_member import ClanMember


class Clan(Aggregate):
    def __init__(
        self,
        clan_id: UUID,
        clan_name: ClanName,
        clan_tag: ClanTag,
        owner_id: int,
        created_at: datetime,
    ):
        super().__init__()
        self.clan_id = clan_id
        self.clan_name = clan_name
        self.clan_tag = clan_tag
        self.owner_id = owner_id
        self.created_at = created_at

    @classmethod
    def create(  # type: ignore
        cls,
        clan_name: str,
        clan_tag: str,
        owner_id: int,
    ) -> Self:
        clan_id = uuid4()
        created_at = datetime.now()
        clan_name_ = ClanName(clan_name)
        clan_tag_ = ClanTag(clan_tag)
        clan = cls(clan_id, clan_name_, clan_tag_, owner_id, created_at)
        event = ClanCreatedEvent.new(
            clan_name=clan_name,
            clan_tag=clan_tag,
            owner_id=owner_id,
        )
        clan._events.append(event)
        return clan

    def add_member(self, player_id: int) -> ClanMember:
        clan_member_id = uuid4()
        joined_at = datetime.now()
        clan_member = ClanMember(
            clan_member_id=clan_member_id,
            player_id=player_id,
            clan_id=self.clan_id,
            joined_at=joined_at,
        )
        event = ClanMemberJoinedEvent.new(
            player_id=player_id,
            clan_name=self.clan_name,
        )
        self._events.append(event)
        return clan_member
