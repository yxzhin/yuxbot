from datetime import datetime
from uuid import UUID, uuid4

from .....shared.events import DomainEvent
from ..events import ClanMemberCreatedEvent


class ClanMember:
    def __init__(
        self,
        clan_member_id: UUID,
        player_id: int,
        clan_id: UUID,
        joined_at: datetime,
    ):
        self.clan_member_id = clan_member_id
        self.player_id = player_id
        self.clan_id = clan_id
        self.joined_at = joined_at
        self._events: list[DomainEvent] = []

    @classmethod
    def create(
        cls,
        player_id: int,
        clan_id: UUID,
    ) -> "ClanMember":
        clan_member_id = uuid4()
        joined_at = datetime.now()
        clan_member = cls(clan_member_id, player_id, clan_id, joined_at)
        event = ClanMemberCreatedEvent.new(
            clan_member_id=clan_member_id,
            player_id=player_id,
            clan_id=clan_id,
        )
        clan_member._events.append(event)
        return clan_member

    def pull_events(self):
        events = self._events.copy()
        self._events.clear()
        return events
