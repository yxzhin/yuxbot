import pytest

from src.backend.services.clans.infra.units_of_work.inmemory import (
    InMemoryClanUnitOfWork,
)
from src.backend.services.clans.use_cases import CreateClanUseCase
from src.backend.shared.events import InMemoryEventBus


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def clan_uow(event_bus):
    async with InMemoryClanUnitOfWork(event_bus) as inm_clan_uow:
        yield inm_clan_uow


@pytest.fixture
def create_clan_uc(clan_uow):
    return CreateClanUseCase(clan_uow)
