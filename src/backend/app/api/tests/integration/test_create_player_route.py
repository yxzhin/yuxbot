async def test_create_player_success(create_player):
    result = await create_player(player_id=1, username="test_player")

    assert result is not None
    assert result["player_id"] == 1
    assert result["username"] == "test_player"
    assert result["balance"] >= 0
    assert result["created_at"] is not None


async def test_create_player_response_has_correct_schema(httpx_client):
    payload = {
        "player_id": 150,
        "username": "schema_test",
    }

    response = await httpx_client.post("/players/create", json=payload)

    assert response.status_code == 201
    json_data = response.json()

    assert "message" in json_data
    assert "success" in json_data
    assert "player" in json_data

    assert isinstance(json_data["message"], str)
    assert isinstance(json_data["success"], bool)
    assert json_data["success"] is True

    player = json_data["player"]
    assert player["player_id"] == 150
    assert player["username"] == "schema_test"
    assert isinstance(player["balance"], int)
    assert "created_at" in player


async def test_create_player_sequential_creation(create_player):
    players = []
    for i in range(1, 6):
        player = await create_player(player_id=i, username=f"sequential_player_{i}")
        players.append(player)

    assert len(players) == 5
    for i, player in enumerate(players, start=1):
        assert player["player_id"] == i
        assert player["username"] == f"sequential_player_{i}"
