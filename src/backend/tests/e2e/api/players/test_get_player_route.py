async def test_create_and_get_player_successfully(create_player, get_player):
    player_id = 73
    username = "ril73"

    create_player = await create_player(player_id, username)

    result = await get_player(player_id)
    get_player = result[0]
    inventory = result[1]

    assert get_player["player_id"] == create_player["player_id"]
    assert get_player["username"] == create_player["username"]
    assert get_player["balance"] == create_player["balance"]
    assert get_player["created_at"] == create_player["created_at"]
    assert isinstance(inventory, list)
    assert len(inventory) == 0
