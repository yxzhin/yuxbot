from collections.abc import Callable

from ....shared.ports import UseCase
from ..domain.entities import Player
from ..domain.exceptions import PlayerNotFoundError
from ..ports import PlayerUnitOfWork


class GetPlayerUseCase(UseCase):
    def __init__(self, player_uow_factory: Callable[[], PlayerUnitOfWork]) -> None:
        self.player_uow_factory = player_uow_factory

    async def execute(self, player_id: int) -> Player:  # type: ignore
        async with self.player_uow_factory() as player_uow:
            player = await player_uow.player_repo.get_by_id(player_id)
            if player is None:
                raise PlayerNotFoundError("player with given id not found")

            return player
