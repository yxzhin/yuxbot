from datetime import datetime
from uuid import UUID


async def test_create_clan_successfully(create_player, create_clan):
    player_id = 73
    username = "ril73"

    player = await create_player(player_id, username)

    clan_name = "ril73"
    clan_tag = "73"

    clan = await create_clan(clan_name, clan_tag, player["player_id"])

    assert UUID(clan["clan_id"])
    assert clan["clan_name"] == clan_name
    assert clan["clan_tag"] == clan_tag
    assert clan["owner_id"] == player["player_id"]
    assert datetime.fromisoformat(clan["created_at"])


async def test_create_clan_sequential_creation(create_player, create_clan):
    players = []
    for i in range(1, 6):
        player = await create_player(i, f"ril{i}")
        players.append(player)

    clans = []
    for i in range(1, 6):
        clan = await create_clan(f"ril{i}", str(i) * 3, i)
        clans.append(clan)

    assert len(clans) == 5
    for i, clan in enumerate(clans, start=1):
        assert clan["clan_name"] == f"ril{i}"
        assert clan["clan_tag"] == str(i) * 3
        assert clan["owner_id"] == i
