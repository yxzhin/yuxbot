import pytest

from src.backend.services.players.domain.exceptions import PlayerNotFoundError


async def test_get_player_successfully(create_player_uc, get_player_uc):
    player_id = 73

    create_player = await create_player_uc.execute(player_id, "ril73")

    get_player = await get_player_uc.execute(player_id)
    player = get_player.player
    inventory = get_player.inventory

    assert player.player_id == create_player.player_id
    assert player.username == create_player.username
    assert player.balance == create_player.balance
    assert player.created_at == create_player.created_at
    assert isinstance(inventory, list)
    assert len(inventory) == 0


async def test_get_player_with_nonexistent_id_raises(get_player_uc):
    with pytest.raises(PlayerNotFoundError):
        await get_player_uc.execute(-73)
