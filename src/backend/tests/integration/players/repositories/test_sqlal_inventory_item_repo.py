from uuid import uuid4

from src.backend.services.players.domain.entities import InventoryItem
from src.backend.services.players.domain.value_objects import ItemAmount


async def test_save_inserts_new_inventory_item(inventory_item_repo):
    inventory_item = InventoryItem.create(73, uuid4(), 73)

    await inventory_item_repo.save(inventory_item)

    get_inventory_item = await inventory_item_repo.get_by_id(
        inventory_item.inventory_item_id
    )

    assert isinstance(get_inventory_item, InventoryItem)
    assert get_inventory_item.item_id == inventory_item.item_id
    assert get_inventory_item.item_amount == inventory_item.item_amount


async def test_save_updates_existing_inventory_item(inventory_item_repo):
    inventory_item = InventoryItem.create(73, uuid4(), 73)

    await inventory_item_repo.save(inventory_item)

    player_id = 37
    item_id = uuid4()
    item_amount = ItemAmount(37)

    inventory_item.player_id = player_id
    inventory_item.item_id = item_id
    inventory_item.item_amount = item_amount

    await inventory_item_repo.save(inventory_item)

    get_inventory_item = await inventory_item_repo.get_by_id(
        inventory_item.inventory_item_id
    )

    assert get_inventory_item.player_id == player_id
    assert get_inventory_item.item_id == item_id
    assert get_inventory_item.item_amount.amount == item_amount.amount


async def test_get_inventory_items_by_player_id(inventory_item_repo):
    player_id = 73

    inventory_item = InventoryItem.create(player_id, uuid4(), 73)

    await inventory_item_repo.save(inventory_item)

    get_inventory_items = await inventory_item_repo.get_by_player_id(player_id)

    assert isinstance(get_inventory_items, list)
    assert len(get_inventory_items) == 1
    assert get_inventory_items[0].inventory_item_id == inventory_item.inventory_item_id


async def test_get_nonexistent_inventory_item_returns_none(inventory_item_repo):
    assert await inventory_item_repo.get_by_id(73) is None
    assert await inventory_item_repo.get_by_player_id(73) == []


async def test_delete_inventory_item(inventory_item_repo):
    inventory_item = InventoryItem.create(73, uuid4(), 73)

    await inventory_item_repo.save(inventory_item)

    await inventory_item_repo.delete(inventory_item)

    get_inventory_item = await inventory_item_repo.get_by_id(
        inventory_item.inventory_item_id
    )

    assert get_inventory_item is None
