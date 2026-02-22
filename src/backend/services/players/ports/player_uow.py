from ....shared.ports import UnitOfWork
from ..ports import (
    BaseInventoryService,
    BasePlayerService,
    InventoryItemRepository,
    ItemRepository,
    PlayerRepository,
)


class PlayerUnitOfWork(UnitOfWork):
    player_repo: PlayerRepository
    player_service: BasePlayerService
    item_repo: ItemRepository
    inventory_item_repo: InventoryItemRepository
    inventory_service: BaseInventoryService
