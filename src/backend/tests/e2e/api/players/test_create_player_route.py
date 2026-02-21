from datetime import datetime


async def test_create_player_successfully(create_player):
    player_id = 73
    username = "ril73"

    player = await create_player(player_id, username)

    assert player["player_id"] == player_id
    assert player["username"] == username
    assert player["balance"] == 0
    assert datetime.fromisoformat(player["created_at"])


async def test_create_player_sequential_creation(create_player):
    players = []
    for i in range(1, 6):
        player = await create_player(i, f"ril{i}")
        players.append(player)

    assert len(players) == 5
    for i, player in enumerate(players, start=1):
        assert player["player_id"] == i
        assert player["username"] == f"ril{i}"
