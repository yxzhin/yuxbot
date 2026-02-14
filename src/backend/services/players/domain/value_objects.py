from dataclasses import dataclass

from .exceptions import InsufficientBalanceError


@dataclass
class Money:
    amount: int

    def __post_init__(self):
        if self.amount < 0:
            raise InsufficientBalanceError("balance cannot be negative")
