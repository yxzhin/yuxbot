from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response, status

from .....services.players.infra.mappers import PlayerMapper
from .....services.players.use_cases import CreatePlayerUseCase
from .....shared.utils import StructuredLogger
from ..schemas import CreatePlayerRequestDTO, CreatePlayerResponseDTO

players_router = APIRouter(prefix="/players")


@players_router.post("/create", response_model=CreatePlayerResponseDTO)
@inject
async def create_player(
    dto: CreatePlayerRequestDTO,
    use_case: FromDishka[CreatePlayerUseCase],
    response: Response,
):
    try:
        player = await use_case.execute(dto.player_id, dto.username)
        player_dto = PlayerMapper.to_dto(player)
        response.status_code = status.HTTP_201_CREATED
        return {
            "message": "player created successfully",
            "success": True,
            "player": player_dto,
        }
    except Exception as e:
        StructuredLogger.exception(str(e))
        return {
            "message": f"an error occurred while creating player: {str(e)}",
            "success": False,
            "player": None,
        }
