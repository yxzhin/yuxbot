from typing import Self
from uuid import UUID, uuid4

from .....shared.domain import EntityFactory
from ..events import InventoryItemAddedEvent
from ..exceptions import InsufficientInventoryItemAmountError


class InventoryItem(EntityFactory):
    def __init__(
        self,
        inventory_item_id: UUID,
        player_id: int,
        item_id: UUID,
        item_amount: int,
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
        if item_amount < 1:
            raise InsufficientInventoryItemAmountError(
                "inventory item amount must be equal to or greater than 1"
            )
        inventory_item_id = uuid4()
        inventory_item = cls(inventory_item_id, player_id, item_id, item_amount)
        event = InventoryItemAddedEvent.new(
            player_id=player_id,
            item_id=item_id,
            item_amount=item_amount,
        )
        inventory_item._events.append(event)
        return inventory_item
