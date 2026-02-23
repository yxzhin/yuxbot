from uuid import uuid4

import pytest

from src.backend.services.clans.domain.entities import Clan, ClanMember
from src.backend.services.clans.infra.units_of_work.sqlal import (
    SqlAlchemyClanUnitOfWork,
)


@pytest.fixture
async def clan_uow_factory(db_sess):
    return lambda: SqlAlchemyClanUnitOfWork(db_sess)


async def test_uow_commit_persists_data(
    clan_uow_factory, clan_repo_factory, clan_member_repo_factory
):
    async with clan_uow_factory() as clan_uow:
        clan = Clan.create("ril73", "73", 73)
        await clan_uow.clan_repo.save(clan)
        clan_member = ClanMember.create(73, uuid4())
        await clan_uow.clan_member_repo.save(clan_member)

    clan_repo = clan_repo_factory()
    get_clan = await clan_repo.get_by_id(clan.clan_id)
    assert isinstance(get_clan, Clan)

    clan_member_repo = clan_member_repo_factory()
    get_clan_member = await clan_member_repo.get_by_id(clan_member.clan_member_id)
    assert isinstance(get_clan_member, ClanMember)


async def test_uow_rollback_on_exception(
    clan_uow_factory, clan_repo_factory, clan_member_repo_factory
):
    class TestError(BaseException):
        pass

    with pytest.raises(TestError):
        async with clan_uow_factory() as clan_uow:
            clan = Clan.create("ril73", "73", 73)
            await clan_uow.clan_repo.save(clan)
            clan_member = ClanMember.create(73, uuid4())
            await clan_uow.clan_member_repo.save(clan_member)
            raise TestError()

    clan_repo = clan_repo_factory()
    get_clan = await clan_repo.get_by_id(clan.clan_id)
    assert get_clan is None

    clan_member_repo = clan_member_repo_factory()
    get_clan_member = await clan_member_repo.get_by_id(clan_member.clan_member_id)
    assert get_clan_member is None
