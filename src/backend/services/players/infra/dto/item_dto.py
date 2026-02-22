from uuid import UUID

from pydantic import BaseModel


class ItemDTO(BaseModel):
    item_id: UUID
    item_name: str
    image_url: str
