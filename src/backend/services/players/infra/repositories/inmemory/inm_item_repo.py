from uuid import UUID

from ......shared.infra.units_of_work import InMemoryStorage
from ....domain.entities import Item
from ....ports import ItemRepository


class InMemoryItemRepository(ItemRepository):
    def __init__(self, inm_storage: InMemoryStorage):
        self.inm_storage = inm_storage

    async def get_by_id(self, item_id: UUID) -> Item | None:
        for item in self.inm_storage.items:
            if item.item_id == item_id:
                return item
        return None

    async def get_by_name(self, item_name: str) -> Item | None:
        for item in self.inm_storage.items:
            if item.item_name == item_name:
                return item
        return None

    async def save(self, item: Item) -> None:
        for item_ in self.inm_storage.items:
            if item_.item_id == item.item_id:
                index = self.inm_storage.items.index(item)
                self.inm_storage.items[index] = item
                return
        self.inm_storage.items.append(item)
        return
