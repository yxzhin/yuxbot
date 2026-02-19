from ....shared.ports import BaseUnitOfWork
from ..ports import ClanMemberRepository, ClanRepository


class ClanUnitOfWork(BaseUnitOfWork):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository
