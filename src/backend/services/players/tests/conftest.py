import pytest

from src.backend.services.players.infra.repositories.inmemory import (
    InMemoryPlayerRepository,
)
from src.backend.services.players.use_cases import CreatePlayerUseCase


@pytest.fixture
def player_repo():
    return InMemoryPlayerRepository()


@pytest.fixture
def create_player_uc(player_repo):
    return CreatePlayerUseCase(player_repo)
