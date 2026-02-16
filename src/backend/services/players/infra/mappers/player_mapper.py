from ...domain.entities import Player
from ...domain.value_objects import Money
from ..dto import PlayerDTO
from ..models import PlayerModel


class PlayerMapper:
    @staticmethod
    def to_domain(player: PlayerModel | None) -> Player | None:
        if player is None:
            return None
        return Player(
            player_id=player.player_id,
            username=player.username,
            balance=Money(player.balance),
            created_at=player.created_at,
        )

    @staticmethod
    def to_orm(player: Player | None) -> PlayerModel | None:
        if player is None:
            return None
        return PlayerModel(
            player_id=player.player_id,
            username=player.username,
            balance=player.balance.amount,
            created_at=player.created_at,
        )

    @staticmethod
    def to_dto(player: Player | None) -> PlayerDTO | None:
        if player is None:
            return None
        return PlayerDTO(
            player_id=player.player_id,
            username=player.username,
            balance=player.balance.amount,
            created_at=player.created_at,
        )
