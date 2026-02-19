from typing import Self

from ......shared.infra.units_of_work import InMemoryUnitOfWork
from ....ports import ClanUnitOfWork
from ...repositories.inmemory import (
    InMemoryClanMemberRepository,
    InMemoryClanRepository,
)


class InMemoryClanUnitOfWork(InMemoryUnitOfWork, ClanUnitOfWork):
    async def __aenter__(self) -> Self:
        self.clan_repo = InMemoryClanRepository()
        self.clan_member_repo = InMemoryClanMemberRepository()
        return self
