from typing import Self

from ......shared.infra.units_of_work import InMemoryUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.inmemory import (
    InMemoryInventoryItemRepository,
    InMemoryItemRepository,
    InMemoryPlayerRepository,
)
from ...services import InventoryService, PlayerService


class InMemoryPlayerUnitOfWork(InMemoryUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = InMemoryPlayerRepository(self.inm_storage)
        self.player_service = PlayerService(self.player_repo)
        self.item_repo = InMemoryItemRepository(self.inm_storage)
        self.inventory_item_repo = InMemoryInventoryItemRepository(self.inm_storage)
        self.inventory_service = InventoryService(
            self.item_repo, self.inventory_item_repo
        )
        return self
