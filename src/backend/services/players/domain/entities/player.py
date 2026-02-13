from datetime import datetime

from ..value_objects import Money


class Player:
    def __init__(
        self,
        player_id: int,
        username: str,
        balance: Money = Money(0),
        created_at: datetime | None = None,
    ):
        self.player_id = player_id
        self.username = username
        self.balance = balance
        self.created_at = created_at or datetime.now()

    def update_balance(self, delta: int):
        new = self.balance.amount + delta
        self.balance = Money(new)

    def set_balance(self, new: int):
        self.balance = Money(new)
