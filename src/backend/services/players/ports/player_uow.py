from ....shared.ports import UnitOfWork
from ..ports import PlayerRepository


class PlayerUnitOfWork(UnitOfWork):
    player_repo: PlayerRepository
