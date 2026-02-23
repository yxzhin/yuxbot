import pytest

from src.backend.services.players.domain.exceptions import InsufficientAmountError
from src.backend.services.players.domain.value_objects import ItemAmount


def test_item_amount_positive_ok():
    item_amount = ItemAmount(73)
    assert item_amount.amount == 73


def test_item_amount_lesser_than_1_raises():
    with pytest.raises(InsufficientAmountError):
        ItemAmount(0)
