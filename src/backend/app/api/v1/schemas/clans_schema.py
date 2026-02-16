from pydantic import BaseModel

from .....services.clans.infra.dto import ClanDTO


class CreateClanRequestDTO(BaseModel):
    clan_name: str
    clan_tag: str
    owner_id: int


class CreateClanResponseDTO(BaseModel):
    message: str
    success: bool
    clan: ClanDTO | None
