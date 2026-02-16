from abc import ABC, abstractmethod
from typing import Self

from ....shared.events import DomainEvent
from ..ports import ClanMemberRepository, ClanRepository


class ClanUnitOfWork(ABC):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository

    @abstractmethod
    async def __aenter__(self) -> Self: ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb) -> None: ...

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...

    @abstractmethod
    async def collect_event(self, event: DomainEvent) -> None: ...
