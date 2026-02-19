from traceback import print_exc

from sqlalchemy.ext.asyncio import AsyncSession

from ...ports import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, db_sess: AsyncSession):
        self.db_sess = db_sess

    async def _commit(self) -> None:
        await self.db_sess.commit()
        print("[SqlAlchemy UoW] db session committed")

    async def _rollback(self) -> None:
        # await self.db_sess.rollback() # sqlalchemy should rollback automatically if an exception is raised
        print("[SqlAlchemy UoW] warning: an exception occurred. db session rolled back")
        print_exc()
