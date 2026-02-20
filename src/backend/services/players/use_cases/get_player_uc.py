from collections.abc import Callable

from ....shared.ports import UseCase
from ..domain.entities import Player
from ..ports import PlayerUnitOfWork


class GetPlayerUseCase(UseCase):
    def __init__(self, player_uow_factory: Callable[[], PlayerUnitOfWork]) -> None:
        self.player_uow_factory = player_uow_factory

    async def execute(self, player_id: int) -> Player:  # type: ignore
        async with self.player_uow_factory() as player_uow:
            player = await player_uow.player_service.get_player(player_id)
            return player
