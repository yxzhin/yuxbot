from sqlalchemy import select
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

    async def create(self, player: Player):
        player_model = PlayerMapper.to_orm(player)
        self.db_sess.add(player_model)
        await self.db_sess.flush()
