from pydantic import BaseModel

from .....services.players.infra.dto import InventoryItemDTO, PlayerDTO
from .....shared.infra.dto import BaseResponseDTO


class GetPlayerResponseDTO(BaseResponseDTO):
    player: PlayerDTO
    inventory: list[InventoryItemDTO]


class CreatePlayerRequestDTO(BaseModel):
    player_id: int
    username: str


class CreatePlayerResponseDTO(BaseResponseDTO):
    player: PlayerDTO | None
