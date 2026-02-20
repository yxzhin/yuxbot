from ...domain.entities import Player
from ...domain.exceptions import PlayerAlreadyExistsError, PlayerNotFoundError
from ...ports import BasePlayerService, PlayerRepository


class PlayerService(BasePlayerService):
    def __init__(self, player_repo: PlayerRepository):
        self.player_repo = player_repo

    async def create_player(self, player_id: int, username: str) -> Player:
        existing = await self.player_repo.get_by_id(player_id)
        if existing:
            raise PlayerAlreadyExistsError("player already exists")

        player = Player.create(
            player_id=player_id,
            username=username,
        )

        await self.player_repo.save(player)

        return player

    async def get_player(self, player_id: int) -> Player:
        player = await self.player_repo.get_by_id(player_id)
        if player is None:
            raise PlayerNotFoundError("player with given id not found")
        return player
