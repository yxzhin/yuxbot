from ..domain.entities import Player
from ..domain.exceptions import PlayerAlreadyExistsError
from ..ports import PlayerRepository


class CreatePlayerUseCase:
    def __init__(self, repo: PlayerRepository):
        self.repo = repo

    async def execute(self, player_id: int, username: str) -> Player:
        existing = await self.repo.get_by_id(player_id)
        if existing:
            raise PlayerAlreadyExistsError("player already exists")

        player = Player(
            player_id=player_id,
            username=username,
        )
        await self.repo.create(player)
        return player
