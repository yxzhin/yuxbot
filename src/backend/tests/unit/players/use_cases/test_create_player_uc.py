from datetime import datetime


async def test_create_player_successfully(create_player_uc):
    player_id = 73
    username = "ril73"

    player = await create_player_uc.execute(player_id, username)

    assert player.player_id == player_id
    assert player.username == username
    assert player.balance.amount == 0
    assert isinstance(player.created_at, datetime)
