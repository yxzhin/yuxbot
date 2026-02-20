from ....shared.ports import UnitOfWork
from ..ports import BasePlayerService, PlayerRepository


class PlayerUnitOfWork(UnitOfWork):
    player_repo: PlayerRepository
    player_service: BasePlayerService
