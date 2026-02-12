from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.clans.domain.entities import ClanMember

from ....ports import ClanMemberRepository
from ...mappers import ClanMemberMapper
from ...models import ClanMemberModel


class SqlAlchemyClanMemberRepository(ClanMemberRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, clan_member_id: int) -> ClanMember | None:
        query = await self.session.execute(
            select(ClanMemberModel).where(
                ClanMemberModel.clan_member_id == clan_member_id
            )
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def get_by_player_id(self, player_id: int) -> ClanMember | None:
        query = await self.session.execute(
            select(ClanMemberModel).where(ClanMemberModel.player_id == player_id)
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def get_by_clan_id(self, clan_id: int) -> ClanMember | None:
        query = await self.session.execute(
            select(ClanMemberModel).where(ClanMemberModel.clan_id == clan_id)
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def create(self, clan_member: ClanMember):
        clan_member_model = ClanMemberMapper.to_orm(clan_member)
        self.session.add(clan_member_model)
        await self.session.flush()
