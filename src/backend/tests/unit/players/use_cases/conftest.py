import pytest

from src.backend.services.players.infra.units_of_work.inmemory import (
    InMemoryPlayerUnitOfWork,
)
from src.backend.services.players.use_cases import CreatePlayerUseCase, GetPlayerUseCase
from src.backend.shared.infra.events import InMemoryEventBus
from src.backend.shared.infra.units_of_work import InMemoryStorage


@pytest.fixture
async def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def inm_storage():
    return InMemoryStorage()


@pytest.fixture
async def player_uow_factory(inm_storage):
    return lambda: InMemoryPlayerUnitOfWork(inm_storage)


@pytest.fixture
async def create_player_uc(player_uow_factory, event_bus):
    return CreatePlayerUseCase(player_uow_factory, event_bus)


@pytest.fixture
async def get_player_uc(player_uow_factory):
    return GetPlayerUseCase(player_uow_factory)
