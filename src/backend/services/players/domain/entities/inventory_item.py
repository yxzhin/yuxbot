from typing import Self
from uuid import UUID, uuid4

from .....shared.domain import EntityFactory
from ..events import InventoryItemAddedEvent
from ..value_objects import ItemAmount


class InventoryItem(EntityFactory):
    def __init__(
        self,
        inventory_item_id: UUID,
        player_id: int,
        item_id: UUID,
        item_amount: ItemAmount,
    ):
        super().__init__()
        self.inventory_item_id = inventory_item_id
        self.player_id = player_id
        self.item_id = item_id
        self.item_amount = item_amount

    @classmethod
    def create(  # type: ignore
        cls,
        player_id: int,
        item_id: UUID,
        item_amount: int,
    ) -> Self:
        inventory_item_id = uuid4()
        item_amount_ = ItemAmount(item_amount)
        inventory_item = cls(inventory_item_id, player_id, item_id, item_amount_)
        event = InventoryItemAddedEvent.new(
            player_id=player_id,
            item_id=item_id,
            item_amount=item_amount,
        )
        inventory_item._events.append(event)
        return inventory_item
