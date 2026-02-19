from typing import Self

from ......shared.infra.units_of_work import SqlAlchemyUnitOfWork
from ....ports import PlayerUnitOfWork
from ...repositories.sqlal import (
    SqlAlchemyPlayerRepository,
)


class SqlAlchemyPlayerUnitOfWork(SqlAlchemyUnitOfWork, PlayerUnitOfWork):
    async def __aenter__(self) -> Self:
        self.player_repo = SqlAlchemyPlayerRepository(self.db_sess)
        return self
