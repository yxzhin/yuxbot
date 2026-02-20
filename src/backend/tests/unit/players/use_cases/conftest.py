from asyncio import get_event_loop

import pytest

from src.backend.services.players.infra.units_of_work.inmemory import (
    InMemoryPlayerUnitOfWork,
)
from src.backend.services.players.use_cases import CreatePlayerUseCase
from src.backend.shared.infra.events import InMemoryEventBus
from src.backend.shared.infra.units_of_work import InMemoryStorage


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
def inm_storage():
    return InMemoryStorage()


@pytest.fixture
async def player_uow_factory(inm_storage):
    return lambda: InMemoryPlayerUnitOfWork(inm_storage)


@pytest.fixture
def create_player_uc(player_uow_factory, event_bus):
    async def _create_player_uc():
        return CreatePlayerUseCase(player_uow_factory, event_bus)

    return get_event_loop().run_until_complete(_create_player_uc())
