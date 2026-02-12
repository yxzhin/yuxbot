from abc import ABC, abstractmethod

from ..ports import ClanMemberRepository, ClanRepository


class ClanUnitOfWork(ABC):
    clan_repo: ClanRepository
    clan_member_repo: ClanMemberRepository

    @abstractmethod
    async def __aenter__(self) -> "ClanUnitOfWork": ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb) -> None: ...

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...
