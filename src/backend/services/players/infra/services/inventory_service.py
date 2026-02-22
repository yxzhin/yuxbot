from uuid import UUID

from ...domain.entities import InventoryItem, Item, Player
from ...domain.exceptions import ItemAlreadyExistsError, ItemNotFoundError
from ...ports import BaseInventoryService, InventoryItemRepository, ItemRepository


class InventoryService(BaseInventoryService):
    def __init__(
        self, item_repo: ItemRepository, inventory_item_repo: InventoryItemRepository
    ):
        self.item_repo = item_repo
        self.inventory_item_repo = inventory_item_repo

    async def create_item(self, item_name: str, image_url: str) -> Item:
        existing = await self.item_repo.get_by_name(item_name)
        if existing:
            raise ItemAlreadyExistsError("item already exists")

        item = Item.create(
            item_name=item_name,
            image_url=image_url,
        )

        await self.item_repo.save(item)

        return item

    async def get_item(self, item_id: UUID) -> Item:
        item = await self.item_repo.get_by_id(item_id)
        if item is None:
            raise ItemNotFoundError("item with given id not found")
        return item

    async def add_inventory_item(
        self, player: Player, item: Item, item_amount: int
    ) -> InventoryItem | None:
        inventory_items = await self.inventory_item_repo.get_by_player_id(
            player.player_id
        )

        for inventory_item in inventory_items:
            if inventory_item.item_id == item.item_id:
                new_amount = inventory_item.item_amount + item_amount
                if new_amount < 0:
                    await self.inventory_item_repo.delete(inventory_item)
                    return None

                await self.inventory_item_repo.save(inventory_item)
                return inventory_item

        inventory_item = InventoryItem.create(
            player_id=player.player_id,
            item_id=item.item_id,
            item_amount=item_amount,
        )
        return inventory_item

    async def get_inventory_items(self, player: Player) -> list[InventoryItem]:
        inventory_items = await self.inventory_item_repo.get_by_player_id(
            player.player_id
        )
        return inventory_items
