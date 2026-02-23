import pytest

from src.backend.services.players.infra.services import PlayerService


@pytest.fixture
async def player_service_factory(player_repo_factory):
    return lambda: PlayerService(player_repo_factory())
