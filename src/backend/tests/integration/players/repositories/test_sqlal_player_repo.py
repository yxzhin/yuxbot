from src.backend.services.players.domain.entities import Player
from src.backend.services.players.domain.value_objects import Money


async def test_save_inserts_new_player(player_repo):
    player = Player.create(73, "ril73")

    await player_repo.save(player)

    get_player = await player_repo.get_by_id(player.player_id)

    assert isinstance(get_player, Player)
    assert get_player.player_id == player.player_id
    assert get_player.username == player.username
    assert get_player.balance.amount == get_player.balance.amount
    assert get_player.created_at == player.created_at


async def test_save_updates_existing_player(player_repo):
    player = Player.create(73, "ril73")

    await player_repo.save(player)

    username = "ril37"
    balance = Money(737)

    player.username = username
    player.balance = balance

    await player_repo.save(player)

    get_player = await player_repo.get_by_id(player.player_id)

    assert get_player.username == username
    assert get_player.balance.amount == balance.amount


async def test_get_player_by_username(player_repo):
    player = Player.create(73, "ril73")

    await player_repo.save(player)

    get_player = await player_repo.get_by_username("ril73")

    assert isinstance(get_player, Player)
    assert get_player.player_id == player.player_id


async def test_get_nonexistent_player_returns_none(player_repo):
    assert await player_repo.get_by_id(73) is None
    assert await player_repo.get_by_username("ril73") is None
