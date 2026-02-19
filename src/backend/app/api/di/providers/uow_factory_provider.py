from collections.abc import Callable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .....services.clans.infra.units_of_work.sqlal import SqlAlchemyClanUnitOfWork
from .....services.players.infra.units_of_work.sqlal import SqlAlchemyPlayerUnitOfWork


class UnitOfWorkFactoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def clan_uow_factory(
        self,
        db_sess: AsyncSession,
    ) -> Callable[[], SqlAlchemyClanUnitOfWork]:
        return lambda: SqlAlchemyClanUnitOfWork(db_sess)

    @provide(scope=Scope.REQUEST)
    async def player_uow_factory(
        self,
        db_sess: AsyncSession,
    ) -> Callable[[], SqlAlchemyPlayerUnitOfWork]:
        return lambda: SqlAlchemyPlayerUnitOfWork(db_sess)
