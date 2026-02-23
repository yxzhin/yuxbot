import pytest

from src.backend.services.players.infra.repositories.sqlal import (
    SqlAlchemyInventoryItemRepository,
    SqlAlchemyItemRepository,
    SqlAlchemyPlayerRepository,
)


@pytest.fixture
async def player_repo(db_sess):
    return SqlAlchemyPlayerRepository(db_sess)


@pytest.fixture
async def item_repo(db_sess):
    return SqlAlchemyItemRepository(db_sess)


@pytest.fixture
async def inventory_item_repo(db_sess):
    return SqlAlchemyInventoryItemRepository(db_sess)
