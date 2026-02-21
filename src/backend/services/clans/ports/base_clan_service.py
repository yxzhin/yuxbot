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
    async def add_player_to_clan(self, player_id: int, clan: Clan) -> ClanMember: ...

    @abstractmethod
    async def get_clan_by_id(self, clan_id: UUID) -> Clan: ...

    @abstractmethod
    async def get_clan_members(self, clan: Clan) -> list[ClanMember]: ...
