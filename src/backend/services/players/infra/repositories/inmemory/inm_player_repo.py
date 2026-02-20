from ......shared.infra.units_of_work import InMemoryStorage
from ....domain.entities import Player
from ....ports import PlayerRepository


class InMemoryPlayerRepository(PlayerRepository):
    def __init__(self, inm_storage: InMemoryStorage):
        self.inm_storage = inm_storage

    async def get_by_id(self, player_id: int) -> Player | None:
        for player in self.inm_storage.players:
            if player.player_id == player_id:
                return player
        return None

    async def get_by_username(self, username: str) -> Player | None:
        for player in self.inm_storage.players:
            if player.username == username:
                return player
        return None

    async def save(self, player: Player) -> None:
        for player_ in self.inm_storage.players:
            if player_.player_id == player.player_id:
                index = self.inm_storage.players.index(player)
                self.inm_storage.players[index] = player
                return
        self.inm_storage.players.append(player)
        return
