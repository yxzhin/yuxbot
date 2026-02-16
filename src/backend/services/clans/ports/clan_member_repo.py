from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import ClanMember


class ClanMemberRepository(ABC):
    @abstractmethod
    async def get_by_id(self, clan_member_id: UUID) -> ClanMember | None: ...

    @abstractmethod
    async def get_by_player_id(self, player_id: int) -> ClanMember | None: ...

    @abstractmethod
    async def get_by_clan_id(self, clan_id: UUID) -> ClanMember | None: ...

    @abstractmethod
    async def save(self, clan_member: ClanMember) -> None: ...
