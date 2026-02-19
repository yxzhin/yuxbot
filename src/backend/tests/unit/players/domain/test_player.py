from datetime import datetime

import pytest

from src.backend.services.players.domain.entities import Player
from src.backend.services.players.domain.exceptions import InsufficientBalanceError
from src.backend.services.players.domain.value_objects import Money


async def test_player_initialization():
    player = Player.create(player_id=1, username="testuser")

    assert player.player_id == 1
    assert player.username == "testuser"
    assert player.balance.amount == 0
    assert isinstance(player.created_at, datetime)

    created_at = datetime(2026, 1, 1, 12, 0, 0)
    balance = Money(1000)
    player = Player(
        player_id=42,
        username="richuser",
        balance=balance,
        created_at=created_at,
    )

    assert player.player_id == 42
    assert player.username == "richuser"
    assert player.balance.amount == 1000
    assert player.created_at == created_at


async def test_player_update_balance():
    player = Player.create(player_id=1, username="testuser")

    player.update_balance(50)
    assert player.balance.amount == 50

    player.update_balance(-30)
    assert player.balance.amount == 20

    player.update_balance(-player.balance.amount)
    assert player.balance.amount == 0

    with pytest.raises(InsufficientBalanceError):
        player.update_balance(-100)


async def test_player_set_balance():
    player = Player.create(player_id=1, username="testuser")

    player.set_balance(500)
    assert player.balance.amount == 500

    player.set_balance(0)
    assert player.balance.amount == 0

    with pytest.raises(InsufficientBalanceError):
        player.set_balance(-50)
