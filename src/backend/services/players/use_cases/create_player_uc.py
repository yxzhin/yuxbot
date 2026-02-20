from collections.abc import Callable

from ....shared.ports import EventBus, UseCase
from ..domain.entities import Player
from ..ports import PlayerUnitOfWork


class CreatePlayerUseCase(UseCase):
    def __init__(
        self,
        player_uow_factory: Callable[[], PlayerUnitOfWork],
        event_bus: EventBus,
    ):
        self.player_uow_factory = player_uow_factory
        self.event_bus = event_bus

    async def execute(self, player_id: int, username: str) -> Player:  # type: ignore
        async with self.player_uow_factory() as player_uow:
            player = await player_uow.player_service.create_player(player_id, username)

        player_events = player.pull_events()
        await self.event_bus.publish(player_events)

        return player
