from pydantic import BaseModel

from .....services.clans.infra.dto import ClanDTO
from .....shared.infra.dto import BaseResponseDTO


class CreateClanRequestDTO(BaseModel):
    clan_name: str
    clan_tag: str
    owner_id: int


class CreateClanResponseDTO(BaseResponseDTO):
    clan: ClanDTO | None
