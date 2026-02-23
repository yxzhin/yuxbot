import pytest

from src.backend.services.clans.infra.repositories.inmemory import (
    InMemoryClanMemberRepository,
    InMemoryClanRepository,
)
from src.backend.shared.infra.units_of_work import InMemoryStorage


@pytest.fixture
async def inm_storage():
    return InMemoryStorage()


@pytest.fixture
async def clan_repo(inm_storage):
    return InMemoryClanRepository(inm_storage)


@pytest.fixture
async def clan_member_repo(inm_storage):
    return InMemoryClanMemberRepository(inm_storage)
