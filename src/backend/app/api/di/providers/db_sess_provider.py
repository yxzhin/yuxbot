from collections.abc import AsyncGenerator
from typing import Any

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .....shared.utils import Database


class DBSessionProvider(Provider):
    """Провайдер для внедрения сессий базы данных в приложение."""

    def __init__(self, db_sess: AsyncSession | None = None):
        super().__init__()
        self._db_sess = db_sess

    @provide(scope=Scope.REQUEST)
    async def db_sess(self) -> AsyncGenerator[AsyncSession, Any]:
        """
        Предоставляет асинхронную сессию базы данных для каждого запроса.
        Используется внутри контекстного менеджера async with.
        """
        if self._db_sess:
            yield self._db_sess
        else:
            async with Database.get_session() as session:
                yield session
