from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.services.clans.domain.entities import ClanMember

from ....ports import ClanMemberRepository
from ...mappers import ClanMemberMapper
from ...models import ClanMemberModel


class SqlAlchemyClanMemberRepository(ClanMemberRepository):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def get_by_id(self, clan_member_id: UUID) -> ClanMember | None:
        query = await self.db_sess.execute(
            select(ClanMemberModel).where(
                ClanMemberModel.clan_member_id == clan_member_id
            )
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def get_by_player_id(self, player_id: int) -> ClanMember | None:
        query = await self.db_sess.execute(
            select(ClanMemberModel).where(ClanMemberModel.player_id == player_id)
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def get_by_clan_id(self, clan_id: UUID) -> ClanMember | None:
        query = await self.db_sess.execute(
            select(ClanMemberModel).where(ClanMemberModel.clan_id == clan_id)
        )
        result = query.scalar_one_or_none()
        clan_member = ClanMemberMapper.to_domain(result)
        return clan_member

    async def save(self, clan_member: ClanMember) -> None:
        query = await self.db_sess.execute(
            select(ClanMemberModel).where(
                ClanMemberModel.clan_member_id == clan_member.clan_member_id
            )
        )
        result = query.scalar_one_or_none()

        if result is None:
            clan_member_model = ClanMemberMapper.to_orm(clan_member)
            self.db_sess.add(clan_member_model)
            await self.db_sess.flush()
            return

        query = await self.db_sess.execute(
            update(ClanMemberModel)
            .where(ClanMemberModel.clan_member_id == clan_member.clan_member_id)
            .values(
                player_id=clan_member.player_id,
                clan_id=clan_member.clan_id,
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db_sess.flush()
