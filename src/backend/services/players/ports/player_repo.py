from abc import ABC, abstractmethod

from ..domain.entities import Player


class PlayerRepository(ABC):
    @abstractmethod
    async def get_by_id(self, player_id: int) -> Player | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> Player | None: ...

    @abstractmethod
    async def save(self, player: Player) -> None: ...
