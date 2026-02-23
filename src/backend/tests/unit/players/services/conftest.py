import pytest

from src.backend.services.players.infra.repositories.inmemory import (
    InMemoryInventoryItemRepository,
    InMemoryItemRepository,
    InMemoryPlayerRepository,
)
from src.backend.shared.infra.units_of_work import InMemoryStorage


@pytest.fixture
async def inm_storage():
    return InMemoryStorage()


@pytest.fixture
async def player_repo(inm_storage):
    return InMemoryPlayerRepository(inm_storage)


@pytest.fixture
async def item_repo(inm_storage):
    return InMemoryItemRepository(inm_storage)


@pytest.fixture
async def inventory_item_repo(inm_storage):
    return InMemoryInventoryItemRepository(inm_storage)
