from uuid import uuid4

import pytest

from src.backend.services.clans.domain.exceptions import (
    ClanAlreadyExistsError,
    ClanNotFoundError,
    PlayerAlreadyInClanError,
)
from src.backend.services.clans.infra.services import ClanService


@pytest.fixture
async def clan_service(clan_repo, clan_member_repo):
    return ClanService(clan_repo, clan_member_repo)


async def test_create_and_get_clan_successfully(clan_service):
    clan_name = "ril37"
    clan_tag = "73"
    owner_id = 73
    clan = await clan_service.create_clan(clan_name, clan_tag, owner_id)

    get_clan = await clan_service.get_clan_by_id(clan.clan_id)

    assert get_clan.clan_name.value == clan.clan_name.value
    assert get_clan.clan_tag.value == clan.clan_tag.value
    assert get_clan.owner_id == clan.owner_id
    assert get_clan.created_at == clan.created_at


async def test_create_clan_raises_error_if_clan_name_exists(clan_service):
    clan_name = "ril73"
    await clan_service.create_clan(clan_name, "73", 73)

    with pytest.raises(ClanAlreadyExistsError, match="clan name already taken"):
        await clan_service.create_clan(clan_name, "37", 37)


async def test_create_clan_raises_error_if_clan_tag_exists(clan_service):
    clan_tag = "73"
    await clan_service.create_clan("ril73", clan_tag, 73)

    with pytest.raises(ClanAlreadyExistsError, match="clan tag already taken"):
        await clan_service.create_clan("ril37", clan_tag, 37)


async def test_create_clan_raises_error_if_owner_already_owns_clan(clan_service):
    owner_id = 73
    await clan_service.create_clan("ril73", "73", owner_id)

    with pytest.raises(
        ClanAlreadyExistsError, match="this player is already an owner of a clan"
    ):
        await clan_service.create_clan("ril37", "37", owner_id)


async def test_create_and_get_clan_members_successfully(clan_service):
    clan_name = "ril37"
    clan_tag = "73"
    owner_id = 73
    clan = await clan_service.create_clan(clan_name, clan_tag, owner_id)

    clan_member = await clan_service.add_player_to_clan(37, clan)

    get_clan_members = await clan_service.get_clan_members(clan)

    assert isinstance(get_clan_members, list)
    assert len(get_clan_members) == 1

    get_clan_member = get_clan_members[0]

    assert clan_member.clan_member_id == get_clan_member.clan_member_id
    assert clan_member.player_id == get_clan_member.player_id


async def test_add_duplicate_clan_member_raises(clan_service):
    clan_name = "ril37"
    clan_tag = "73"
    owner_id = 73
    clan = await clan_service.create_clan(clan_name, clan_tag, owner_id)

    player_id = 37
    await clan_service.add_player_to_clan(player_id, clan)

    with pytest.raises(
        PlayerAlreadyInClanError, match="this player is already a member of a clan"
    ):
        await clan_service.add_player_to_clan(player_id, clan)


async def test_get_nonexistent_clan_raises(clan_service):
    with pytest.raises(ClanNotFoundError):
        await clan_service.get_clan_by_id(uuid4())
