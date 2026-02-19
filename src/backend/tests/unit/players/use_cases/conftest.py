import pytest

from src.backend.services.players.infra.units_of_work.inmemory import (
    InMemoryPlayerUnitOfWork,
)
from src.backend.services.players.use_cases import CreatePlayerUseCase
from src.backend.shared.infra.events import InMemoryEventBus


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def player_uow_factory():
    return lambda: InMemoryPlayerUnitOfWork()


@pytest.fixture
def create_player_uc(player_uow_factory, event_bus):
    return CreatePlayerUseCase(player_uow_factory, event_bus)
