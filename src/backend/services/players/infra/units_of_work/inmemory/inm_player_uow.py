from typing import Self

from ......shared.infra.units_of_work import InMemoryUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.inmemory import (
    InMemoryPlayerRepository,
)


class InMemoryPlayerUnitOfWork(InMemoryUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = InMemoryPlayerRepository()
        return self
