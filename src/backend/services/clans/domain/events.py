from dataclasses import dataclass

from ....shared.domain import DomainEvent


@dataclass(slots=True)
class ClanCreatedEvent(DomainEvent):
    clan_name: str
    clan_tag: str
    owner_id: int


@dataclass(slots=True)
class ClanMemberJoinedEvent(DomainEvent):
    player_id: int
    clan_name: str
