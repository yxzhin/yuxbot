from datetime import datetime

import pytest

from src.backend.services.players.domain.entities import Player
from src.backend.services.players.domain.events import PlayerCreatedEvent
from src.backend.services.players.domain.exceptions import InsufficientBalanceError


async def test_player_create_success():
    player = Player.create(73, "ril73")

    assert player.player_id == 73
    assert player.username == "ril73"
    assert player.balance.amount == 0
    assert isinstance(player.created_at, datetime)


async def test_player_create_emits_events():
    player = Player.create(37, "ril37")

    events = player.pull_events()
    assert isinstance(events, list)
    assert len(events) == 1
    assert isinstance(events[0], PlayerCreatedEvent)

    assert player.pull_events() == []

    # modifying returned list shouldn't affect internal state
    events.append("ril")  # type: ignore
    assert len(player._events) == 0


async def test_player_update_balance():
    player = Player.create(73, "ril73")

    player.update_balance(50)
    assert player.balance.amount == 50

    player.update_balance(-30)
    assert player.balance.amount == 20

    player.update_balance(-player.balance.amount)
    assert player.balance.amount == 0

    with pytest.raises(InsufficientBalanceError):
        player.update_balance(-100)


async def test_player_set_balance():
    player = Player.create(73, "ril73")

    player.set_balance(500)
    assert player.balance.amount == 500

    player.set_balance(0)
    assert player.balance.amount == 0

    with pytest.raises(InsufficientBalanceError):
        player.set_balance(-50)
