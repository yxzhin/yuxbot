from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import Clan


class ClanRepository(ABC):
    @abstractmethod
    async def get_by_id(self, clan_id: UUID) -> Clan | None: ...

    @abstractmethod
    async def get_by_name(self, clan_name: str) -> Clan | None: ...

    @abstractmethod
    async def get_by_tag(self, clan_tag: str) -> Clan | None: ...

    @abstractmethod
    async def get_by_owner_id(self, owner_id: int) -> Clan | None: ...

    @abstractmethod
    async def save(self, clan: Clan) -> None: ...
