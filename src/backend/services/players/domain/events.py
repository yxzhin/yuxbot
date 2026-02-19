from dataclasses import dataclass
from datetime import datetime

from ....shared.infra.events import DomainEvent
from .value_objects import Money


@dataclass(slots=True)
class PlayerCreatedEvent(DomainEvent):
    player_id: int
    username: str
    balance: Money
    created_at: datetime
