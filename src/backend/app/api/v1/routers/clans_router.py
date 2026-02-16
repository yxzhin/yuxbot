from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response, status

from .....services.clans.infra.mappers import ClanMapper
from .....services.clans.use_cases import CreateClanUseCase
from .....shared.utils import StructuredLogger
from ..schemas import CreateClanRequestDTO, CreateClanResponseDTO

clans_router = APIRouter(prefix="/clans")


@clans_router.post("/create", response_model=CreateClanResponseDTO)
@inject
async def create_clan(
    dto: CreateClanRequestDTO,
    use_case: FromDishka[CreateClanUseCase],
    response: Response,
):
    try:
        clan = await use_case.execute(dto.clan_name, dto.clan_tag, dto.owner_id)
        clan_dto = ClanMapper.to_dto(clan)
        response.status_code = status.HTTP_201_CREATED
        return {
            "message": "clan created successfully",
            "success": True,
            "clan": clan_dto,
        }
    except Exception as e:
        StructuredLogger.exception(str(e))
        return {
            "message": f"an error occurred while creating clan: {str(e)}",
            "success": False,
            "clan": None,
        }
