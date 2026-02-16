from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .....services.players.infra.repositories.sqlal import SqlAlchemyPlayerRepository


class RepositoryProvider(Provider):
    """Провайдер для внедрения репозиториев в приложение."""

    @provide(scope=Scope.REQUEST)
    async def player_repository(
        self, db_sess: AsyncSession
    ) -> SqlAlchemyPlayerRepository:
        """Предоставляет репозиторий пользователей, используя сессию базы данных."""
        return SqlAlchemyPlayerRepository(db_sess)
