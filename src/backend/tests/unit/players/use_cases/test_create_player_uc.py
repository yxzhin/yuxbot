import pytest

from src.backend.services.players.domain.exceptions import PlayerAlreadyExistsError


async def test_create_player_successfully(create_player_uc):
    player = await create_player_uc.execute(73, "ril73")

    assert player.player_id == 73
    assert player.username == "ril73"
    assert player.balance.amount == 0
    assert player.created_at is not None


async def test_create_player_with_duplicate_id_raises(create_player_uc):
    await create_player_uc.execute(73, "ril73")

    with pytest.raises(PlayerAlreadyExistsError):
        await create_player_uc.execute(73, "ril37")
