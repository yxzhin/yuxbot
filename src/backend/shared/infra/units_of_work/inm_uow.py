from traceback import print_exc

from ...ports import BaseUnitOfWork


class InMemoryUnitOfWork(BaseUnitOfWork):
    async def _commit(self) -> None:
        print("[InMemory UoW] committed")

    async def _rollback(self) -> None:
        print("[InMemory UoW] warning: an exception occurred.")
        print_exc()
