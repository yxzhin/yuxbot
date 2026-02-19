import pytest

from src.backend.services.players.domain.exceptions import InsufficientBalanceError
from src.backend.services.players.domain.value_objects import Money


def test_money_positive_ok():
    m = Money(73)
    assert m.amount == 73


def test_money_negative_raises():
    with pytest.raises(InsufficientBalanceError):
        Money(-73)
