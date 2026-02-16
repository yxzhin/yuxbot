from dataclasses import dataclass
from uuid import UUID

from ....shared.events import DomainEvent


@dataclass(slots=True)
class ClanCreatedEvent(DomainEvent):
    clan_id: UUID
    clan_name: str
    clan_tag: str
    owner_id: int


@dataclass(slots=True)
class ClanMemberCreatedEvent(DomainEvent):
    clan_member_id: UUID
    player_id: int
    clan_id: UUID
