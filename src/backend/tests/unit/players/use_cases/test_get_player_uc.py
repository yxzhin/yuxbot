import pytest

from src.backend.services.players.domain.exceptions import PlayerNotFoundError


async def test_get_player_successfully(create_player_uc, get_player_uc):
    create_player = await create_player_uc.execute(73, "ril73")

    get_player = await get_player_uc.execute(73)

    assert get_player.player_id == create_player.player_id
    assert get_player.username == create_player.username
    assert get_player.balance == create_player.balance
    assert get_player.created_at == create_player.created_at


async def test_get_player_with_nonexistent_id_raises(get_player_uc):
    with pytest.raises(PlayerNotFoundError):
        await get_player_uc.execute(-73)
