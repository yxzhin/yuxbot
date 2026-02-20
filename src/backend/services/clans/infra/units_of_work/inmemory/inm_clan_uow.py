from typing import Self

from ......shared.infra.units_of_work import InMemoryUnitOfWork
from ....ports import ClanUnitOfWork
from ...repositories.inmemory import (
    InMemoryClanMemberRepository,
    InMemoryClanRepository,
)
from ...services import ClanService


class InMemoryClanUnitOfWork(InMemoryUnitOfWork, ClanUnitOfWork):
    async def __aenter__(self) -> Self:
        self.clan_repo = InMemoryClanRepository(self.inm_storage)
        self.clan_member_repo = InMemoryClanMemberRepository(self.inm_storage)
        self.clan_service = ClanService(self.clan_repo, self.clan_member_repo)
        return self
