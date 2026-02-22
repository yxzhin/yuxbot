from typing import Self

from ......shared.infra.units_of_work import SqlAlchemyUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.sqlal import (
    SqlAlchemyInventoryItemRepository,
    SqlAlchemyItemRepository,
    SqlAlchemyPlayerRepository,
)
from ...services import InventoryService, PlayerService


class SqlAlchemyPlayerUnitOfWork(SqlAlchemyUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = SqlAlchemyPlayerRepository(self.db_sess)
        self.player_service = PlayerService(self.player_repo)
        self.item_repo = SqlAlchemyItemRepository(self.db_sess)
        self.inventory_item_repo = SqlAlchemyInventoryItemRepository(self.db_sess)
        self.inventory_service = InventoryService(
            self.item_repo, self.inventory_item_repo
        )
        return self
