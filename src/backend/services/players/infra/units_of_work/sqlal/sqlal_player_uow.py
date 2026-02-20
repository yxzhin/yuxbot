from typing import Self

from ......shared.infra.units_of_work import SqlAlchemyUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.sqlal import (
    SqlAlchemyPlayerRepository,
)
from ...services import PlayerService


class SqlAlchemyPlayerUnitOfWork(SqlAlchemyUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = SqlAlchemyPlayerRepository(self.db_sess)
        self.player_service = PlayerService(self.player_repo)
        return self
