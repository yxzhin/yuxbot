from dishka import Provider, Scope, provide

from .....services.players.infra.repositories.sqlal import SqlAlchemyPlayerRepository
from .....services.players.use_cases import CreatePlayerUseCase


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_player_use_case(
        self, player_repo: SqlAlchemyPlayerRepository
    ) -> CreatePlayerUseCase:
        return CreatePlayerUseCase(player_repo)
