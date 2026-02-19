import pytest

from src.backend.services.clans.infra.units_of_work.inmemory import (
    InMemoryClanUnitOfWork,
)
from src.backend.services.clans.use_cases import CreateClanUseCase
from src.backend.shared.infra.events import InMemoryEventBus


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def clan_uow(event_bus):
    return lambda: InMemoryClanUnitOfWork()


@pytest.fixture
def create_clan_uc(clan_uow, event_bus):
    return CreateClanUseCase(clan_uow, event_bus)
