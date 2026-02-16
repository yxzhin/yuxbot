from collections.abc import AsyncGenerator
from typing import Any

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .....services.clans.infra.units_of_work.sqlal import SqlAlchemyClanUnitOfWork
from .....shared.events import InMemoryEventBus


class UnitOfWorkProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def clan_unit_of_work(
        self,
        db_sess: AsyncSession,
        event_bus: InMemoryEventBus,
    ) -> AsyncGenerator[SqlAlchemyClanUnitOfWork, Any]:
        async with SqlAlchemyClanUnitOfWork(db_sess, event_bus) as clan_uow:
            yield clan_uow
