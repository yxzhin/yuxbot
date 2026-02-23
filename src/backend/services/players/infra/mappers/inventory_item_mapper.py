from ...domain.entities import InventoryItem
from ...domain.value_objects import ItemAmount
from ..dto import InventoryItemDTO
from ..models import InventoryItemModel


class InventoryItemMapper:
    @staticmethod
    def to_domain(inventory_item: InventoryItemModel | None) -> InventoryItem | None:
        if inventory_item is None:
            return None
        return InventoryItem(
            inventory_item_id=inventory_item.inventory_item_id,
            player_id=inventory_item.player_id,
            item_id=inventory_item.item_id,
            item_amount=ItemAmount(inventory_item.item_amount),
        )

    @staticmethod
    def to_orm(inventory_item: InventoryItem | None) -> InventoryItemModel | None:
        if inventory_item is None:
            return None
        return InventoryItemModel(
            inventory_item_id=inventory_item.inventory_item_id,
            player_id=inventory_item.player_id,
            item_id=inventory_item.item_id,
            item_amount=inventory_item.item_amount.amount,
        )

    @staticmethod
    def to_dto(inventory_item: InventoryItem | None) -> InventoryItemDTO | None:
        if inventory_item is None:
            return None
        return InventoryItemDTO(
            inventory_item_id=inventory_item.inventory_item_id,
            player_id=inventory_item.player_id,
            item_id=inventory_item.item_id,
            item_amount=inventory_item.item_amount.amount,
        )
