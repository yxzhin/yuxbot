from ....shared.ports import UnitOfWork
from ..ports import ClanMemberRepository, ClanRepository


class ClanUnitOfWork(UnitOfWork):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository
