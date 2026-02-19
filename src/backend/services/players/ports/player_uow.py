from ....shared.ports import BaseUnitOfWork
from ..ports import PlayerRepository


class PlayerUnitOfWork(BaseUnitOfWork):
    player_repo: PlayerRepository
