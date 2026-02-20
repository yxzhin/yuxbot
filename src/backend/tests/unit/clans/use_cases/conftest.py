import pytest

from src.backend.services.clans.infra.units_of_work.inmemory import (
    InMemoryClanUnitOfWork,
)
from src.backend.services.clans.use_cases import CreateClanUseCase
from src.backend.shared.infra.events import InMemoryEventBus
from src.backend.shared.infra.units_of_work import InMemoryStorage


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
def inm_storage():
    return InMemoryStorage()


@pytest.fixture
async def clan_uow_factory(inm_storage):
    return lambda: InMemoryClanUnitOfWork(inm_storage)


@pytest.fixture
def create_clan_uc(clan_uow_factory, event_bus):
    return CreateClanUseCase(clan_uow_factory, event_bus)
