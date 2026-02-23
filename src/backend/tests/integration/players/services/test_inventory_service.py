import pytest

from src.backend.services.players.infra.services import InventoryService


@pytest.fixture
async def inventory_service_factory(item_repo_factory, inventory_item_repo_factory):
    return lambda: InventoryService(item_repo_factory(), inventory_item_repo_factory())
