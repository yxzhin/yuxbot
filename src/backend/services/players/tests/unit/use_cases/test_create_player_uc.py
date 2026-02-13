import pytest

from src.backend.services.players.domain.exceptions import PlayerAlreadyExistsError


async def test_create_player_successfully(create_player_uc):
    player = await create_player_uc.execute(player_id=1, username="testuser")

    assert player.player_id == 1
    assert player.username == "testuser"
    assert player.balance.amount == 0
    assert player.created_at is not None


async def test_create_player_with_duplicate_id(create_player_uc):
    await create_player_uc.execute(player_id=1, username="user1")

    with pytest.raises(PlayerAlreadyExistsError):
        await create_player_uc.execute(player_id=1, username="user2")
