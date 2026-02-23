from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response, status

from .....services.players.infra.mappers import PlayerMapper
from .....services.players.use_cases import CreatePlayerUseCase, GetPlayerUseCase
from ..schemas import (
    CreatePlayerRequestDTO,
    CreatePlayerResponseDTO,
    GetPlayerResponseDTO,
)

players_router = APIRouter(prefix="/players")


@players_router.get("/{player_id}", response_model=GetPlayerResponseDTO)
@inject
async def get_player(
    player_id: int,
    use_case: FromDishka[GetPlayerUseCase],
):
    player_with_inventory_dto = await use_case.execute(player_id)
    player = PlayerMapper.to_dto(player_with_inventory_dto.player)
    inventory = player_with_inventory_dto.inventory
    return {
        "message": "successfully retrieved player data",
        "success": True,
        "player": player,
        "inventory": inventory,
    }


@players_router.post("/create", response_model=CreatePlayerResponseDTO)
@inject
async def create_player(
    dto: CreatePlayerRequestDTO,
    use_case: FromDishka[CreatePlayerUseCase],
    response: Response,
):
    player = await use_case.execute(dto.player_id, dto.username)
    player_dto = PlayerMapper.to_dto(player)
    response.status_code = status.HTTP_201_CREATED
    return {
        "message": "player created successfully",
        "success": True,
        "player": player_dto,
    }
    # "message": f"an error occurred while creating player: {str(e)}",
