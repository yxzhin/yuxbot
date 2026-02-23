import pytest

from src.backend.services.clans.infra.services import ClanService


@pytest.fixture
async def clan_service_factory(clan_repo_factory, clan_member_repo_factory):
    return lambda: ClanService(clan_repo_factory(), clan_member_repo_factory())
