import pytest

from src.backend.services.players.infra.repositories.sqlal import (
    SqlAlchemyInventoryItemRepository,
    SqlAlchemyItemRepository,
    SqlAlchemyPlayerRepository,
)


@pytest.fixture
async def player_repo_factory(db_sess):
    return lambda: SqlAlchemyPlayerRepository(db_sess)


@pytest.fixture
async def item_repo_factory(db_sess):
    return lambda: SqlAlchemyItemRepository(db_sess)


@pytest.fixture
async def inventory_item_repo_factory(db_sess):
    return lambda: SqlAlchemyInventoryItemRepository(db_sess)
