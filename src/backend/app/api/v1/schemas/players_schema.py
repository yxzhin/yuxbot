from pydantic import BaseModel

from .....services.players.infra.dto import PlayerDTO


class CreatePlayerRequestDTO(BaseModel):
    player_id: int
    username: str


class CreatePlayerResponseDTO(BaseModel):
    message: str
    success: bool
    player: PlayerDTO | None
