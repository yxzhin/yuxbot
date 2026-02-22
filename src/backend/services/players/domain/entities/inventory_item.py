from uuid import UUID

from .....shared.domain import Entity


class InventoryItem(Entity):
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
