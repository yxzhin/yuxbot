from ......shared.infra.units_of_work import InMemoryStorage, InMemoryUnitOfWork
from ....ports import ClanUnitOfWork
from ...repositories.inmemory import (
    InMemoryClanMemberRepository,
    InMemoryClanRepository,
)
from ...services import ClanService


class InMemoryClanUnitOfWork(InMemoryUnitOfWork, ClanUnitOfWork):
    def __init__(self, inm_storage: InMemoryStorage):
        super().__init__(inm_storage)
        self.clan_repo = InMemoryClanRepository(self.inm_storage)
        self.clan_member_repo = InMemoryClanMemberRepository(self.inm_storage)
        self.clan_service = ClanService(self.clan_repo, self.clan_member_repo)
