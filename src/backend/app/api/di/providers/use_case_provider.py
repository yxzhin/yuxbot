from collections.abc import Callable

from dishka import Provider, Scope, provide

from .....services.clans.infra.units_of_work.sqlal import SqlAlchemyClanUnitOfWork
from .....services.clans.use_cases import CreateClanUseCase
from .....services.players.infra.units_of_work.sqlal import SqlAlchemyPlayerUnitOfWork
from .....services.players.use_cases import CreatePlayerUseCase, GetPlayerUseCase
from .....shared.infra.events import InMemoryEventBus


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_player_use_case(
        self,
        player_uow_factory: Callable[[], SqlAlchemyPlayerUnitOfWork],
    ) -> GetPlayerUseCase:
        return GetPlayerUseCase(player_uow_factory)

    @provide(scope=Scope.REQUEST)
    async def create_player_use_case(
        self,
        player_uow_factory: Callable[[], SqlAlchemyPlayerUnitOfWork],
        event_bus: InMemoryEventBus,
    ) -> CreatePlayerUseCase:
        return CreatePlayerUseCase(player_uow_factory, event_bus)

    @provide(scope=Scope.REQUEST)
    async def create_clan_use_case(
        self,
        clan_uow_factory: Callable[[], SqlAlchemyClanUnitOfWork],
        event_bus: InMemoryEventBus,
    ) -> CreateClanUseCase:
        return CreateClanUseCase(clan_uow_factory, event_bus)
