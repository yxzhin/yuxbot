from traceback import print_exc
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from ...ports import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess
        self._nested_ctx: AsyncSessionTransaction | None = None

    async def __aenter__(self) -> Self:
        self._nested_ctx = self.db_sess.begin_nested()
        await self._nested_ctx.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            await self._nested_ctx.__aexit__(exc_type, exc, tb)  # type: ignore
        finally:
            await super().__aexit__(exc_type, exc, tb)

    async def _commit(self) -> None:
        if self._nested_ctx is not None:
            await self.db_sess.flush()
            await self._nested_ctx.__aexit__(None, None, None)
            self._nested_ctx = None
            print("[SqlAlchemy UoW] db session committed")

    async def _rollback(self) -> None:
        if self._nested_ctx is not None:
            await self._nested_ctx.__aexit__(BaseException, BaseException(), None)
            self._nested_ctx = None
            print(
                "[SqlAlchemy UoW] warning: an exception occurred. db session rolled back"
            )
            print_exc()
