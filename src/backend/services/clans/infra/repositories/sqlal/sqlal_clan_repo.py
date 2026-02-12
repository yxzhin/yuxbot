from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.clans.domain.entities import Clan

from ....ports import ClanRepository
from ...mappers import ClanMapper
from ...models import ClanModel


class SqlAlchemyClanRepository(ClanRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, clan_id: int) -> Clan | None:
        query = await self.session.execute(
            select(ClanModel).where(ClanModel.clan_id == clan_id)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def get_by_name(self, clan_name: str) -> Clan | None:
        query = await self.session.execute(
            select(ClanModel).where(ClanModel.clan_name == clan_name)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def create(self, clan: Clan):
        clan_model = ClanMapper.to_orm(clan)
        self.session.add(clan_model)
        await self.session.flush()
