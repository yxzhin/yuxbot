from datetime import datetime
from typing import Self

from .....shared.ports import BaseAggregate
from ..events import PlayerCreatedEvent
from ..value_objects import Money


class Player(BaseAggregate):
    def __init__(
        self,
        player_id: int,
        username: str,
        balance: Money,
        created_at: datetime,
    ):
        super().__init__()
        self.player_id = player_id
        self.username = username
        self.balance = balance
        self.created_at = created_at

    @classmethod
    def create(
        cls,
        player_id: int,
        username: str,
    ) -> Self:
        balance = Money(0)
        created_at = datetime.now()
        player = cls(player_id, username, balance, created_at)
        event = PlayerCreatedEvent.new(
            player_id=player_id,
            username=username,
            balance=balance,
            created_at=created_at,
        )
        player._events.append(event)
        return player

    def update_balance(self, delta: int):
        new = self.balance.amount + delta
        self.balance = Money(new)

    def set_balance(self, new: int):
        self.balance = Money(new)
