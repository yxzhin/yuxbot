import pytest

from src.backend.services.clans.infra.repositories.sqlal import (
    SqlAlchemyClanMemberRepository,
    SqlAlchemyClanRepository,
)


@pytest.fixture
async def clan_repo(db_sess):
    return SqlAlchemyClanRepository(db_sess)


@pytest.fixture
async def clan_member_repo(db_sess):
    return SqlAlchemyClanMemberRepository(db_sess)
