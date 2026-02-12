from abc import ABC, abstractmethod

from ..domain.entities import ClanMember


class ClanMemberRepository(ABC):
    @abstractmethod
    async def get_by_id(self, clan_member_id: int) -> ClanMember | None: ...

    @abstractmethod
    async def get_by_player_id(self, player_id: int) -> ClanMember | None: ...

    @abstractmethod
    async def get_by_clan_id(self, clan_id: int) -> ClanMember | None: ...

    @abstractmethod
    async def create(self, clan_member: ClanMember): ...
