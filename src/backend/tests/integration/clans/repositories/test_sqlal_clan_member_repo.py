from uuid import uuid4

from src.backend.services.clans.domain.entities import ClanMember


async def test_save_inserts_new_clan_member(clan_member_repo_factory):
    clan_member_repo = clan_member_repo_factory()

    clan_member = ClanMember.create(73, uuid4())

    await clan_member_repo.save(clan_member)

    get_clan_member = await clan_member_repo.get_by_id(clan_member.clan_member_id)

    assert isinstance(get_clan_member, ClanMember)
    assert get_clan_member.clan_member_id == clan_member.clan_member_id
    assert get_clan_member.player_id == clan_member.player_id
    assert get_clan_member.clan_id == clan_member.clan_id
    assert get_clan_member.joined_at == clan_member.joined_at


async def test_save_updates_existing_clan_member(clan_member_repo_factory):
    clan_member_repo = clan_member_repo_factory()

    clan_member = ClanMember.create(73, uuid4())

    await clan_member_repo.save(clan_member)

    player_id = 37
    clan_id = uuid4()

    clan_member.player_id = player_id
    clan_member.clan_id = clan_id

    await clan_member_repo.save(clan_member)

    get_clan_member = await clan_member_repo.get_by_id(clan_member.clan_member_id)

    assert get_clan_member.player_id == player_id
    assert get_clan_member.clan_id == clan_id


async def test_get_clan_member_by_player_id(clan_member_repo_factory):
    clan_member_repo = clan_member_repo_factory()

    clan_member = ClanMember.create(73, uuid4())

    await clan_member_repo.save(clan_member)

    get_clan_member = await clan_member_repo.get_by_player_id(73)

    assert isinstance(get_clan_member, ClanMember)
    assert get_clan_member.clan_member_id == clan_member.clan_member_id


async def test_get_clan_members_by_clan_id(clan_member_repo_factory):
    clan_member_repo = clan_member_repo_factory()

    clan_id = uuid4()

    clan_member = ClanMember.create(73, clan_id)

    await clan_member_repo.save(clan_member)

    get_clan_members = await clan_member_repo.get_by_clan_id(clan_id)

    assert isinstance(get_clan_members, list)
    assert len(get_clan_members) == 1
    assert get_clan_members[0].clan_member_id == clan_member.clan_member_id


async def test_get_nonexistent_clan_member_returns_none(clan_member_repo_factory):
    clan_member_repo = clan_member_repo_factory()

    assert await clan_member_repo.get_by_id(73) is None
    assert await clan_member_repo.get_by_player_id(73) is None
    assert await clan_member_repo.get_by_clan_id(uuid4()) == []
