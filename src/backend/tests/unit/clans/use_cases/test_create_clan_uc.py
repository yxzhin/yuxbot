from src.backend.services.clans.domain.entities import Clan
from src.backend.services.clans.use_cases import CreateClanUseCase


async def test_create_clan_successfully(create_clan_uc: CreateClanUseCase):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    clan = await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    assert isinstance(clan, Clan)
    assert clan.clan_name.value == clan_name
    assert clan.clan_tag.value == clan_tag.upper()
    assert clan.owner_id == owner_id
    assert clan.clan_id is not None
    assert clan.created_at is not None


"""
async def test_create_clan_creates_owner_as_clan_member(
    create_clan_uc: CreateClanUseCase,
):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    clan = await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # verify clan member was created with correct owner
    clan_member = await create_clan_uc.clan_uow.clan_member_repo.get_by_player_id(
        owner_id
    )
    assert isinstance(clan_member, ClanMember)
    assert clan_member.player_id == owner_id
    assert clan_member.clan_id == clan.clan_id
    assert clan_member.clan_member_id is not None
    assert clan_member.joined_at is not None
"""


"""
async def test_create_clan_raises_error_if_clan_name_exists(
    create_clan_uc: CreateClanUseCase,
):
    clan_name = "   Test Clan "
    clan_tag = "test"
    owner_id = 123

    # create first clan
    await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # try to create another clan with same name
    with pytest.raises(ClanAlreadyExistsError, match="clan name already taken"):
        await create_clan_uc.execute(clan_name, "other", 456)
"""


"""
async def test_create_clan_raises_error_if_clan_tag_exists(
    create_clan_uc: CreateClanUseCase,
):
    clan_name = "TestClan"
    clan_tag = " tes t  "
    owner_id = 123

    # create first clan
    await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # try to create another clan with same tag
    with pytest.raises(ClanAlreadyExistsError, match="clan tag already taken"):
        await create_clan_uc.execute("OtherClan", clan_tag, 456)
"""


"""
async def test_create_clan_raises_error_if_owner_already_owns_clan(
    create_clan_uc: CreateClanUseCase,
):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    # create first clan
    await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # try to create another clan with same owner
    with pytest.raises(
        ClanAlreadyExistsError, match="this player is already an owner of a clan"
    ):
        await create_clan_uc.execute("AnotherClan", "other", owner_id)


async def test_create_clan_persists_events(create_clan_uc: CreateClanUseCase):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    clan = await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # verify events were collected (would be in event bus)
    # since we're using InMemoryEventBus, we can check it was called
    assert clan is not None
"""


"""
async def test_create_clan_persists_clan(create_clan_uc: CreateClanUseCase):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    clan = await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # verify clan was saved
    saved_clan = await create_clan_uc.clan_uow.clan_repo.get_by_name(clan_name)
    assert saved_clan is not None
    assert saved_clan.clan_id == clan.clan_id
"""


"""
async def test_create_clan_case_insensitive_tag_comparison(
    create_clan_uc: CreateClanUseCase,
):
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    # create first clan
    await create_clan_uc.execute(clan_name, clan_tag, owner_id)

    # try to create another clan with same tag but different case
    with pytest.raises(ClanAlreadyExistsError, match="clan tag already taken"):
        await create_clan_uc.execute("OtherClan", "TEST", 456)
"""


"""
async def test_create_clan_multiple_clans_different_names_and_owners(
    create_clan_uc: CreateClanUseCase,
):
    clan1 = await create_clan_uc.execute("Clan1", "tag1", 123)
    clan2 = await create_clan_uc.execute("Clan2", "tag2", 456)
    clan3 = await create_clan_uc.execute("Clan3", "tag3", 789)

    assert clan1.clan_id != clan2.clan_id
    assert clan2.clan_id != clan3.clan_id
    assert clan1.owner_id != clan2.owner_id
    assert clan2.owner_id != clan3.owner_id

    # verify all clans can be retrieved
    saved_clan1 = await create_clan_uc.clan_uow.clan_repo.get_by_name("Clan1")
    saved_clan2 = await create_clan_uc.clan_uow.clan_repo.get_by_name("Clan2")
    saved_clan3 = await create_clan_uc.clan_uow.clan_repo.get_by_name("Clan3")

    assert saved_clan1 is not None
    assert saved_clan2 is not None
    assert saved_clan3 is not None
"""
