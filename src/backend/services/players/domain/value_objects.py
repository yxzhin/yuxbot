from dataclasses import dataclass

from .exceptions import InsufficientAmountError


@dataclass
class Money:
    amount: int

    def __post_init__(self):
        if self.amount < 0:
            raise InsufficientAmountError("balance cannot be negative")


@dataclass
class ItemAmount:
    amount: int

    def __post_init__(self):
        if self.amount < 1:
            raise InsufficientAmountError("item amount cannot be lesser than 1")
