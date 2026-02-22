from typing import Self
from uuid import UUID, uuid4

from .....shared.domain import Aggregate
from ..events import ItemCreatedEvent


class Item(Aggregate):
    def __init__(
        self,
        item_id: UUID,
        item_name: str,
        image_url: str,
    ):
        super().__init__()
        self.item_id = item_id
        self.item_name = item_name
        self.image_url = image_url

    @classmethod
    def create(  # type: ignore
        cls,
        item_name: str,
        image_url: str,
    ) -> Self:
        item_id = uuid4()
        item = cls(item_id, item_name, image_url)
        event = ItemCreatedEvent.new(
            item_name=item_name,
            image_url=image_url,
        )
        item._events.append(event)
        return item
