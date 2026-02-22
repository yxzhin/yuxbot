from uuid import UUID

from ......shared.infra.units_of_work import InMemoryStorage
from ....domain.entities import InventoryItem
from ....ports import InventoryItemRepository


class InMemoryInventoryItemRepository(InventoryItemRepository):
    def __init__(self, inm_storage: InMemoryStorage):
        self.inm_storage = inm_storage

    async def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None:
        for inventory_item in self.inm_storage.inventory_items:
            if inventory_item.inventory_item_id == inventory_item_id:
                return inventory_item
        return None

    async def get_by_player_id(self, player_id: int) -> list[InventoryItem]:
        return [
            inventory_item
            for inventory_item in self.inm_storage.inventory_items
            if inventory_item.player_id == player_id
        ]

    async def save(self, inventory_item: InventoryItem) -> None:
        for inventory_item_ in self.inm_storage.inventory_items:
            if inventory_item_.inventory_item_id == inventory_item.inventory_item_id:
                index = self.inm_storage.inventory_items.index(inventory_item)
                self.inm_storage.inventory_items[index] = inventory_item
                return
        self.inm_storage.inventory_items.append(inventory_item)
        return
