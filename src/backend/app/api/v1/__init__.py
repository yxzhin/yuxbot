from fastapi import APIRouter

from .routers import *

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(players_router)
