from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ....domain.entities import InventoryItem
from ....ports import InventoryItemRepository
from ...mappers import InventoryItemMapper
from ...models import InventoryItemModel


class SqlAlchemyInventoryItemRepository(InventoryItemRepository):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None:
        query = await self.db_sess.execute(
            select(InventoryItemModel).where(
                InventoryItemModel.inventory_item_id == inventory_item_id
            )
        )
        result = query.scalar_one_or_none()
        inventory_item = InventoryItemMapper.to_domain(result)
        return inventory_item

    async def get_by_player_id(self, player_id: int) -> list[InventoryItem]:
        query = await self.db_sess.execute(
            select(InventoryItemModel).where(InventoryItemModel.player_id == player_id)
        )
        result = query.scalars().all()
        inventory_items = [
            InventoryItemMapper.to_domain(inventory_item) for inventory_item in result
        ]
        return inventory_items  # type: ignore

    async def save(self, inventory_item: InventoryItem) -> None:
        query = await self.db_sess.execute(
            select(InventoryItemModel).where(
                InventoryItemModel.inventory_item_id == inventory_item.inventory_item_id
            )
        )
        result = query.scalar_one_or_none()

        if result is None:
            item_model = InventoryItemMapper.to_orm(inventory_item)
            self.db_sess.add(item_model)
            await self.db_sess.flush()
            return

        query = await self.db_sess.execute(
            update(InventoryItemModel)
            .where(
                InventoryItemModel.inventory_item_id == inventory_item.inventory_item_id
            )
            .values(
                player_id=inventory_item.player_id,
                item_id=inventory_item.item_id,
                item_amount=inventory_item.item_amount,
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db_sess.flush()

    async def delete(self, inventory_item: InventoryItem) -> None:
        await self.db_sess.execute(
            delete(InventoryItemModel).where(
                InventoryItemModel.inventory_item_id == inventory_item.inventory_item_id
            )
        )
        await self.db_sess.flush()
