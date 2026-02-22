from dataclasses import dataclass
from uuid import UUID

from ....shared.domain import DomainEvent
from .value_objects import ClanName, ClanTag


@dataclass(slots=True)
class ClanCreatedEvent(DomainEvent):
    clan_name: ClanName
    clan_tag: ClanTag
    owner_id: int


@dataclass(slots=True)
class ClanMemberJoinedEvent(DomainEvent):
    player_id: int
    clan_id: UUID
