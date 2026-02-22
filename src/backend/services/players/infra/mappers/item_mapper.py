from ...domain.entities import Item
from ..dto import ItemDTO
from ..models import ItemModel


class ItemMapper:
    @staticmethod
    def to_domain(item: ItemModel | None) -> Item | None:
        if item is None:
            return None
        return Item(
            item_id=item.item_id,
            item_name=item.item_name,
            image_url=item.image_url,
        )

    @staticmethod
    def to_orm(item: Item | None) -> ItemModel | None:
        if item is None:
            return None
        return ItemModel(
            item_id=item.item_id,
            item_name=item.item_name,
            image_url=item.image_url,
        )

    @staticmethod
    def to_dto(item: Item | None) -> ItemDTO | None:
        if item is None:
            return None
        return ItemDTO(
            item_id=item.item_id,
            item_name=item.item_name,
            image_url=item.image_url,
        )
