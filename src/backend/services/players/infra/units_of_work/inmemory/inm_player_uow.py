from typing import Self

from ......shared.infra.units_of_work import InMemoryUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.inmemory import (
    InMemoryPlayerRepository,
)
from ...services import PlayerService


class InMemoryPlayerUnitOfWork(InMemoryUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = InMemoryPlayerRepository(self.inm_storage)
        self.player_service = PlayerService(self.player_repo)
        return self
