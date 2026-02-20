from ....shared.ports import UnitOfWork
from ..ports import BaseClanService, ClanMemberRepository, ClanRepository


class ClanUnitOfWork(UnitOfWork):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository
    clan_service: BaseClanService
