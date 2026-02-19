from pydantic import BaseModel

from .....services.players.infra.dto import PlayerDTO
from .....shared.infra.dto import BaseResponseDTO


class GetPlayerResponseDTO(BaseResponseDTO):
    player: PlayerDTO | None


class CreatePlayerRequestDTO(BaseModel):
    player_id: int
    username: str


class CreatePlayerResponseDTO(BaseResponseDTO):
    player: PlayerDTO | None
