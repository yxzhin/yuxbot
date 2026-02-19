from collections.abc import Callable

from ....shared.ports import EventBus, UseCase
from ..domain.entities import Player
from ..domain.exceptions import PlayerAlreadyExistsError
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
            existing = await player_uow.player_repo.get_by_id(player_id)
            if existing:
                raise PlayerAlreadyExistsError("player already exists")

            player = Player.create(
                player_id=player_id,
                username=username,
            )
            await player_uow.player_repo.save(player)

        player_events = player.pull_events()
        await self.event_bus.publish(player_events)

        return player
