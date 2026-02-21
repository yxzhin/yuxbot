from datetime import datetime

import pytest

from src.backend.services.players.domain.exceptions import PlayerAlreadyExistsError


async def test_create_player_successfully(create_player_uc):
    player_id = 73
    username = "ril73"

    player = await create_player_uc.execute(player_id, username)

    assert player.player_id == player_id
    assert player.username == username
    assert player.balance.amount == 0
    assert isinstance(player.created_at, datetime)


async def test_create_player_with_duplicate_id_raises(create_player_uc):
    player_id = 73

    await create_player_uc.execute(player_id, "ril73")

    with pytest.raises(PlayerAlreadyExistsError):
        await create_player_uc.execute(player_id, "ril37")
