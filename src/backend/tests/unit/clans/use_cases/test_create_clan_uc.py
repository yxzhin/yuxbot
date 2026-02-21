from datetime import datetime
from uuid import UUID

import pytest

from src.backend.services.clans.domain.exceptions import (
    ClanAlreadyExistsError,
    PlayerAlreadyInClanError,
)


async def test_create_clan_successfully(create_player_uc, create_clan_uc):
    player_id = 73
    username = "ril73"
    player = await create_player_uc.execute(player_id, username)

    clan_name = "ril37"
    clan_tag = "73"
    clan = await create_clan_uc.execute(clan_name, clan_tag, player.player_id)

    assert isinstance(clan.clan_id, UUID)
    assert clan.clan_name.value == clan_name
    assert clan.clan_tag.value == clan_tag
    assert clan.owner_id == player.player_id
    assert isinstance(clan.created_at, datetime)


async def test_create_clan_creates_owner_as_clan_member(
    create_player_uc, create_clan_uc, get_clan_members_uc
):
    player_id = 73
    username = "ril73"
    player = await create_player_uc.execute(player_id, username)

    clan_name = "ril37"
    clan_tag = "73"
    clan = await create_clan_uc.execute(clan_name, clan_tag, player.player_id)

    clan_members = await get_clan_members_uc.execute(clan.clan_id)

    assert any(
        clan_member.player_id == player.player_id for clan_member in clan_members
    )


async def test_create_clan_raises_error_if_clan_name_exists(
    create_player_uc, create_clan_uc
):
    player_id = 73
    username = "ril73"
    player = await create_player_uc.execute(player_id, username)

    player_id2 = 37
    username2 = "ril37"
    player2 = await create_player_uc.execute(player_id2, username2)

    clan_name = "ril73"
    clan_tag = "73"
    await create_clan_uc.execute(clan_name, clan_tag, player.player_id)

    with pytest.raises(ClanAlreadyExistsError, match="clan name already taken"):
        await create_clan_uc.execute(clan_name, "37", player2.player_id)


async def test_create_clan_raises_error_if_clan_tag_exists(
    create_player_uc, create_clan_uc
):
    player_id = 73
    username = "ril73"
    player = await create_player_uc.execute(player_id, username)

    player_id2 = 37
    username2 = "ril37"
    player2 = await create_player_uc.execute(player_id2, username2)

    clan_name = "ril73"
    clan_tag = "73"
    await create_clan_uc.execute(clan_name, clan_tag, player.player_id)

    with pytest.raises(ClanAlreadyExistsError, match="clan tag already taken"):
        await create_clan_uc.execute("ril37", clan_tag, player2.player_id)


async def test_create_clan_raises_error_if_owner_already_owns_clan(
    create_player_uc, create_clan_uc
):
    player_id = 73
    username = "ril73"
    player = await create_player_uc.execute(player_id, username)

    clan_name = "ril73"
    clan_tag = "73"
    await create_clan_uc.execute(clan_name, clan_tag, player.player_id)

    with pytest.raises(
        PlayerAlreadyInClanError, match="this player is already a member of a clan"
    ):
        await create_clan_uc.execute("ril37", "37", player.player_id)
