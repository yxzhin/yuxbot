from ....domain.entities import Player
from ....ports import PlayerRepository


class InMemoryPlayerRepository(PlayerRepository):
    def __init__(self):
        self.players = []

    async def get_by_id(self, player_id: int) -> Player | None:
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    async def get_by_username(self, username: str) -> Player | None:
        for player in self.players:
            if player.username == username:
                return player
        return None

    async def create(self, player: Player):
        self.players.append(player)
