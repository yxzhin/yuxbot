from string import whitespace
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.services.clans.domain.entities import Clan

from ....ports import ClanRepository
from ...mappers import ClanMapper
from ...models import ClanModel


class SqlAlchemyClanRepository(ClanRepository):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def get_by_id(self, clan_id: UUID) -> Clan | None:
        query = await self.db_sess.execute(
            select(ClanModel).where(ClanModel.clan_id == clan_id)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def get_by_name(self, clan_name: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_name = clan_name.translate(trans)
        query = await self.db_sess.execute(
            select(ClanModel).where(ClanModel.clan_name == clan_name)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def get_by_tag(self, clan_tag: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_tag = clan_tag.upper().translate(trans)
        query = await self.db_sess.execute(
            select(ClanModel).where(ClanModel.clan_tag == clan_tag)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def get_by_owner_id(self, owner_id: int) -> Clan | None:
        query = await self.db_sess.execute(
            select(ClanModel).where(ClanModel.owner_id == owner_id)
        )
        result = query.scalar_one_or_none()
        clan = ClanMapper.to_domain(result)
        return clan

    async def save(self, clan: Clan) -> None:
        query = await self.db_sess.execute(
            select(ClanModel).where(ClanModel.clan_id == clan.clan_id)
        )
        result = query.scalar_one_or_none()

        if result is None:
            clan_model = ClanMapper.to_orm(clan)
            self.db_sess.add(clan_model)
            await self.db_sess.flush()
            return

        query = await self.db_sess.execute(
            update(ClanModel)
            .where(ClanModel.clan_id == clan.clan_id)
            .values(
                clan_name=clan.clan_name.value,
                clan_tag=clan.clan_tag.value,
                owner_id=clan.owner_id,
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db_sess.flush()
