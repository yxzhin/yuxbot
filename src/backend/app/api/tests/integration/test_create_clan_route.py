from httpx import AsyncClient


async def test_create_clan_success(httpx_client: AsyncClient, create_player):
    # create player first (owner of the clan)
    await create_player(123, "test_user")

    response = await httpx_client.post(
        "/clans/create",
        json={
            "clan_name": "TestClan",
            "clan_tag": "test",
            "owner_id": 123,
        },
    )

    assert response.status_code == 201
    data = response.json()

    assert data["success"] is True
    assert data["message"] == "clan created successfully"
    assert data["clan"] is not None

    clan = data["clan"]
    assert clan["clan_name"] == "TestClan"
    assert clan["clan_tag"] == "TEST"
    assert clan["owner_id"] == 123
    assert "clan_id" in clan
    assert "created_at" in clan


async def test_create_clan_with_whitespace_in_name(create_player, create_clan):
    await create_player(125, "test_user3")
    clan = await create_clan("    Test  Clan  ", "test", 125)
    assert clan["clan_name"] == "TestClan"


async def test_create_clan_tag_capitalization(create_player, create_clan):
    await create_player(126, "test_user4")
    clan = await create_clan("AnotherClan", "abc", 126)
    assert clan["clan_tag"] == "ABC"


async def test_create_clan_duplicate_name_error(
    httpx_client: AsyncClient, create_player, create_clan
):
    await create_player(127, "user1")
    await create_player(128, "user2")

    # create first clan
    await create_clan("UniqueClan", "uniq", 127)

    # try to create second clan with same name
    response2 = await httpx_client.post(
        "/clans/create",
        json={
            "clan_name": "UniqueClan",
            "clan_tag": "diff",
            "owner_id": 128,
        },
    )

    assert response2.status_code != 201
    data = response2.json()
    assert data["success"] is False
    assert "already taken" in data["message"].lower()


async def test_create_clan_duplicate_tag_error(
    httpx_client: AsyncClient, create_player, create_clan
):
    await create_player(129, "user3")
    await create_player(130, "user4")

    # create first clan
    await create_clan("FirstClan", "uniq", 129)

    # try to create second clan with same tag
    response2 = await httpx_client.post(
        "/clans/create",
        json={
            "clan_name": "SecondClan",
            "clan_tag": "uniq",
            "owner_id": 130,
        },
    )

    assert response2.status_code != 201
    data = response2.json()
    assert data["success"] is False
    assert "already taken" in data["message"].lower()


async def test_create_clan_owner_already_has_clan(
    httpx_client: AsyncClient, create_player, create_clan
):
    await create_player(131, "user5")

    # create first clan
    await create_clan("OwnersClan", "owne", 131)

    # try to create second clan with same owner
    response2 = await httpx_client.post(
        "/clans/create",
        json={
            "clan_name": "SecondClansForOwner",
            "clan_tag": "scfo",
            "owner_id": 131,
        },
    )

    assert response2.status_code != 201
    data = response2.json()
    assert data["success"] is False
    assert "already" in data["message"].lower()


async def test_create_clan_ownership_reflected_in_response(
    httpx_client: AsyncClient, create_player, create_clan
):
    owner_id = 145
    await create_player(owner_id, "user17")
    clan = await create_clan("OwnedClan", "ownd", owner_id)
    assert clan["owner_id"] == owner_id
