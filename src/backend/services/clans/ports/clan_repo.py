from abc import ABC, abstractmethod

from ..domain.entities import Clan


class ClanRepository(ABC):
    @abstractmethod
    async def get_by_id(self, clan_id: int) -> Clan | None: ...

    @abstractmethod
    async def get_by_name(self, clan_name: str) -> Clan | None: ...

    @abstractmethod
    async def create(self, clan: Clan): ...
