from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from ......shared.events import DomainEvent, EventBus
from ......shared.utils import StructuredLogger
from ....ports import ClanUnitOfWork
from ...repositories.sqlal import (
    SqlAlchemyClanMemberRepository,
    SqlAlchemyClanRepository,
)


class SqlAlchemyClanUnitOfWork(ClanUnitOfWork):
    def __init__(
        self,
        db_sess: AsyncSession,
        event_bus: EventBus | None = None,
    ):
        self.db_sess = db_sess
        self.clan_repo: SqlAlchemyClanRepository | None = None  # type: ignore
        self.clan_member_repo: SqlAlchemyClanMemberRepository | None = None  # type: ignore
        self.event_bus = event_bus
        self._pending_events: list[DomainEvent] = []

    async def __aenter__(self) -> Self:
        self.clan_repo = SqlAlchemyClanRepository(self.db_sess)
        self.clan_member_repo = SqlAlchemyClanMemberRepository(self.db_sess)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            if exc_type:
                await self.rollback()
                StructuredLogger.exception(
                    "an exception occurred in SqlAlchemyClanUnitOfWork. performing db session rollback"
                )
            else:
                await self.commit()
        finally:
            await self.db_sess.close()

    async def commit(self) -> None:
        await self.db_sess.commit()
        if self.event_bus and self._pending_events:
            await self.event_bus.publish(self._pending_events)
            self._pending_events.clear()

    async def rollback(self) -> None:
        await self.db_sess.rollback()
        self._pending_events.clear()

    async def collect_event(self, event: DomainEvent) -> None:
        self._pending_events.append(event)
