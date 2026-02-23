import pytest

from src.backend.services.players.domain.exceptions import (
    PlayerAlreadyExistsError,
    PlayerNotFoundError,
)
from src.backend.services.players.infra.services import PlayerService


@pytest.fixture
async def player_service(player_repo):
    return PlayerService(player_repo)


async def test_create_and_get_player_successfully(player_service):
    player_id = 73
    username = "ril73"
    player = await player_service.create_player(player_id, username)

    get_player = await player_service.get_player(player.player_id)

    assert get_player.username == player.username
    assert get_player.balance.amount == player.balance.amount
    assert get_player.created_at == player.created_at


async def test_create_player_with_duplicate_id_raises(player_service):
    player_id = 73

    await player_service.create_player(player_id, "ril73")

    with pytest.raises(PlayerAlreadyExistsError):
        await player_service.create_player(player_id, "ril37")


async def test_get_nonexistent_player_raises(player_service):
    with pytest.raises(PlayerNotFoundError):
        await player_service.get_player(73)
