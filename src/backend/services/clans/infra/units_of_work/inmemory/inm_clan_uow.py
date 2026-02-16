from typing import Self

from ......shared.events import DomainEvent, EventBus
from ....ports import ClanUnitOfWork
from ...repositories.inmemory import (
    InMemoryClanMemberRepository,
    InMemoryClanRepository,
)


class InMemoryClanUnitOfWork(ClanUnitOfWork):
    def __init__(self, event_bus: EventBus | None = None):
        self.clan_repo: InMemoryClanRepository | None = None  # type: ignore
        self.clan_member_repo: InMemoryClanMemberRepository | None = None  # type: ignore
        self.event_bus = event_bus
        self._pending_events: list[DomainEvent] = []

    async def __aenter__(self) -> Self:
        self.clan_repo = InMemoryClanRepository()
        self.clan_member_repo = InMemoryClanMemberRepository()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        if self.event_bus and self._pending_events:
            await self.event_bus.publish(self._pending_events)
            self._pending_events.clear()

    async def rollback(self) -> None:
        self._pending_events.clear()

    async def collect_event(self, event: DomainEvent) -> None:
        self._pending_events.append(event)
