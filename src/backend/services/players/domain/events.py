from dataclasses import dataclass
from uuid import UUID

from ....shared.domain import DomainEvent


@dataclass(slots=True)
class PlayerCreatedEvent(DomainEvent):
    player_id: int
    username: str


@dataclass(slots=True)
class ItemCreatedEvent(DomainEvent):
    item_name: str
    image_url: str


@dataclass(slots=True)
class InventoryItemAddedEvent(DomainEvent):
    player_id: int
    item_id: UUID
    item_amount: int
