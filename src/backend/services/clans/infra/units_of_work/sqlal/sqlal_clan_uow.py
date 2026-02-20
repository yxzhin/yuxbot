from typing import Self

from ......shared.infra.units_of_work import SqlAlchemyUnitOfWork
from ....ports import ClanUnitOfWork
from ...repositories.sqlal import (
    SqlAlchemyClanMemberRepository,
    SqlAlchemyClanRepository,
)
from ...services import ClanService


class SqlAlchemyClanUnitOfWork(SqlAlchemyUnitOfWork, ClanUnitOfWork):
    async def __aenter__(self) -> Self:
        self.clan_repo = SqlAlchemyClanRepository(self.db_sess)
        self.clan_member_repo = SqlAlchemyClanMemberRepository(self.db_sess)
        self.clan_service = ClanService(self.clan_repo, self.clan_member_repo)
        return self
