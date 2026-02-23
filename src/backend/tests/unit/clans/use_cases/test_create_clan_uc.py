from datetime import datetime
from uuid import UUID


async def test_create_clan_successfully(create_clan_uc):
    clan_name = "ril37"
    clan_tag = "73"
    owner_id = 73
    clan = await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    assert isinstance(clan.clan_id, UUID)
    assert clan.clan_name.value == clan_name
    assert clan.clan_tag.value == clan_tag
    assert clan.owner_id == owner_id
    assert isinstance(clan.created_at, datetime)


async def test_create_clan_creates_owner_as_clan_member(
    create_clan_uc, get_clan_members_uc
):
    clan_name = "ril37"
    clan_tag = "73"
    owner_id = 73
    clan = await create_clan_uc.execute(clan_name, clan_tag, 73)

    clan_members = await get_clan_members_uc.execute(clan.clan_id)

    assert any(clan_member.player_id == owner_id for clan_member in clan_members)
