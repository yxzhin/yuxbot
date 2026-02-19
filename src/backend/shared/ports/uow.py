from abc import ABC, abstractmethod
from typing import Self


class UnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self) -> Self: ...

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if exc_type is None:
            await self._commit()
        else:
            await self._rollback()

    @abstractmethod
    async def _commit(self) -> None: ...

    @abstractmethod
    async def _rollback(self) -> None: ...
