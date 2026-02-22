import pytest

from src.backend.services.clans.domain.entities import Clan
from src.backend.services.clans.domain.value_objects import ClanName, ClanTag


async def test_save_inserts_new_clan(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan = Clan.create("ril73", "73", 73)

    await clan_repo.save(clan)

    get_clan = await clan_repo.get_by_id(clan.clan_id)

    assert isinstance(get_clan, Clan)
    assert get_clan.clan_id == clan.clan_id
    assert get_clan.clan_name.value == clan.clan_name.value
    assert get_clan.clan_tag.value == clan.clan_tag.value
    assert get_clan.created_at == clan.created_at


async def test_save_updates_existing_clan(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan = Clan.create("ril73", "73", 73)

    await clan_repo.save(clan)

    owner_id = 37
    clan_name = "ril73"
    clan_tag = "73"

    clan.owner_id = owner_id
    clan.clan_name = ClanName(clan_name)
    clan.clan_tag = ClanTag(clan_tag)

    await clan_repo.save(clan)

    get_clan = await clan_repo.get_by_id(clan.clan_id)

    assert get_clan.owner_id == owner_id
    assert get_clan.clan_name.value == clan_name
    assert get_clan.clan_tag.value == clan_tag


async def test_get_clan_by_name_whitespace_removal(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan = Clan.create("ril73", "73", 73)

    await clan_repo.save(clan)

    get_clan = await clan_repo.get_by_name("   ril73 \t \n ")

    assert isinstance(get_clan, Clan)
    assert get_clan.clan_id == clan.clan_id


async def test_get_clan_by_tag_whitespace_removal_and_upper(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan = Clan.create("ril73", "ril73", 73)

    await clan_repo.save(clan)

    get_clan = await clan_repo.get_by_tag("   ril73 \t \n ")

    assert isinstance(get_clan, Clan)
    assert get_clan.clan_id == clan.clan_id


async def test_get_clan_by_owner_id(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan = Clan.create("ril73", "ril73", 73)

    await clan_repo.save(clan)

    get_clan = await clan_repo.get_by_owner_id(73)

    assert isinstance(get_clan, Clan)
    assert get_clan.clan_id == clan.clan_id


async def test_get_nonexistent_clan_returns_none(clan_repo_factory):
    clan_repo = clan_repo_factory()

    assert await clan_repo.get_by_id(73) is None
    assert await clan_repo.get_by_name("ril73") is None
    assert await clan_repo.get_by_tag("73") is None
    assert await clan_repo.get_by_owner_id(73) is None


async def test_clan_unique_constraint(clan_repo_factory):
    clan_repo = clan_repo_factory()

    clan1 = Clan.create("ril73", "73", 73)
    await clan_repo.save(clan1)

    clan2 = Clan.create("ril73", "37", 37)
    with pytest.raises(Exception):  # noqa: B017
        await clan_repo.save(clan2)

    clan3 = Clan.create("ril37", "73", 37)
    with pytest.raises(Exception):  # noqa: B017
        await clan_repo.save(clan3)

    clan4 = Clan.create("ril37", "37", 73)
    with pytest.raises(Exception):  # noqa: B017
        await clan_repo.save(clan4)
