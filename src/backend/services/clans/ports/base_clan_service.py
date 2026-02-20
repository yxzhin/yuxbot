from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import Clan, ClanMember
from .clan_member_repo import ClanMemberRepository
from .clan_repo import ClanRepository


class BaseClanService(ABC):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository

    @abstractmethod
    async def create_clan(
        self, clan_name: str, clan_tag: str, owner_id: int
    ) -> Clan: ...

    @abstractmethod
    async def add_player_to_clan(self, player_id: int, clan_id: UUID) -> ClanMember: ...
