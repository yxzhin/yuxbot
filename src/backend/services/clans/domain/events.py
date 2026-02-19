from dataclasses import dataclass
from uuid import UUID

from ....shared.infra.events import DomainEvent
from .value_objects import ClanName, ClanTag


@dataclass(slots=True)
class ClanCreatedEvent(DomainEvent):
    clan_id: UUID
    clan_name: ClanName
    clan_tag: ClanTag
    owner_id: int


@dataclass(slots=True)
class ClanMemberCreatedEvent(DomainEvent):
    clan_member_id: UUID
    player_id: int
    clan_id: UUID
