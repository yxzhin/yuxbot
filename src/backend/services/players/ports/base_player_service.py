from abc import ABC, abstractmethod

from ..domain.entities import Player
from .player_repo import PlayerRepository


class BasePlayerService(ABC):
    player_repo: PlayerRepository

    @abstractmethod
    async def create_player(self, player_id: int, username: str) -> Player: ...

    @abstractmethod
    async def get_player(self, player_id: int) -> Player: ...
