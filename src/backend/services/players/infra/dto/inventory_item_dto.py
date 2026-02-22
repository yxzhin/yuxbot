from uuid import UUID

from pydantic import BaseModel


class InventoryItemDTO(BaseModel):
    inventory_item_id: UUID
    player_id: int
    item_id: UUID
    item_amount: int
