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

    async def save(self, player: Player) -> None:
        for player_ in self.players:
            if player_.player_id == player.player_id:
                index = self.players.index(player)
                self.players[index] = player
                return
        self.players.append(player)
        return
