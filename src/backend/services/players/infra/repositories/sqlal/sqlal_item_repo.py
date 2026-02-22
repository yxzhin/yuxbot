from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ....domain.entities import Item
from ....ports import ItemRepository
from ...mappers import ItemMapper
from ...models import ItemModel


class SqlAlchemyItemRepository(ItemRepository):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def get_by_id(self, item_id: UUID) -> Item | None:
        query = await self.db_sess.execute(
            select(ItemModel).where(ItemModel.item_id == item_id)
        )
        result = query.scalar_one_or_none()
        item = ItemMapper.to_domain(result)
        return item

    async def get_by_name(self, item_name: str) -> Item | None:
        query = await self.db_sess.execute(
            select(ItemModel).where(ItemModel.item_name == item_name)
        )
        result = query.scalar_one_or_none()
        item = ItemMapper.to_domain(result)
        return item

    async def save(self, item: Item) -> None:
        query = await self.db_sess.execute(
            select(ItemModel).where(ItemModel.item_id == item.item_id)
        )
        result = query.scalar_one_or_none()

        if result is None:
            item_model = ItemMapper.to_orm(item)
            self.db_sess.add(item_model)
            await self.db_sess.flush()
            return

        query = await self.db_sess.execute(
            update(ItemModel)
            .where(ItemModel.item_id == item.item_id)
            .values(
                item_name=item.item_name,
                image_url=item.image_url,
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db_sess.flush()
