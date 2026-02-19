from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ....domain.entities import Player
from ....ports import PlayerRepository
from ...mappers import PlayerMapper
from ...models import PlayerModel


class SqlAlchemyPlayerRepository(PlayerRepository):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def get_by_id(self, player_id: int) -> Player | None:
        query = await self.db_sess.execute(
            select(PlayerModel).where(PlayerModel.player_id == player_id)
        )
        result = query.scalar_one_or_none()
        player = PlayerMapper.to_domain(result)
        return player

    async def get_by_username(self, username: str) -> Player | None:
        query = await self.db_sess.execute(
            select(PlayerModel).where(PlayerModel.username == username)
        )
        result = query.scalar_one_or_none()
        player = PlayerMapper.to_domain(result)
        return player

    async def save(self, player: Player) -> None:
        query = await self.db_sess.execute(
            select(PlayerModel).where(PlayerModel.player_id == player.player_id)
        )
        result = query.scalar_one_or_none()

        if result is None:
            player_model = PlayerMapper.to_orm(player)
            self.db_sess.add(player_model)
            await self.db_sess.flush()
            return

        query = await self.db_sess.execute(
            update(PlayerModel)
            .where(PlayerModel.player_id == player.player_id)
            .values(
                username=player.username,
                balance=player.balance,
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db_sess.flush()
