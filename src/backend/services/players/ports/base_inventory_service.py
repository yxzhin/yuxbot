from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import InventoryItem, Item, Player
from .inventory_item_repo import InventoryItemRepository
from .item_repo import ItemRepository


class BaseInventoryService(ABC):
    item_repo: ItemRepository
    inventory_item_repo: InventoryItemRepository

    @abstractmethod
    async def create_item(self, item_name: str, image_url: str) -> Item: ...

    @abstractmethod
    async def get_item(self, item_id: UUID) -> Item: ...

    @abstractmethod
    async def add_inventory_item(
        self, player: Player, item: Item, item_amount: int
    ) -> InventoryItem | None: ...

    @abstractmethod
    async def get_inventory_items(self, player: Player) -> list[InventoryItem]: ...
