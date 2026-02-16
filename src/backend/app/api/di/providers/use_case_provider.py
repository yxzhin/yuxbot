from dishka import Provider, Scope, provide

from .....services.clans.infra.units_of_work.sqlal import SqlAlchemyClanUnitOfWork
from .....services.clans.use_cases import CreateClanUseCase
from .....services.players.infra.repositories.sqlal import SqlAlchemyPlayerRepository
from .....services.players.use_cases import CreatePlayerUseCase


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def create_player_use_case(
        self, player_repo: SqlAlchemyPlayerRepository
    ) -> CreatePlayerUseCase:
        return CreatePlayerUseCase(player_repo)

    @provide(scope=Scope.REQUEST)
    async def create_clan_use_case(
        self, clan_uow: SqlAlchemyClanUnitOfWork
    ) -> CreateClanUseCase:
        return CreateClanUseCase(clan_uow)
