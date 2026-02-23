from uuid import UUID, uuid4

import pytest

from src.backend.services.players.domain.entities import Player
from src.backend.services.players.domain.exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from src.backend.services.players.infra.services import InventoryService


@pytest.fixture
async def inventory_service(item_repo, inventory_item_repo):
    return InventoryService(item_repo, inventory_item_repo)


async def test_create_and_get_item_successfully(inventory_service):
    item_name = "ril73"
    image_url = "https://placehold.co/73x37"
    item = await inventory_service.create_item(item_name, image_url)

    get_item = await inventory_service.get_item(item.item_id)

    assert get_item.item_name == item.item_name
    assert get_item.image_url == item.image_url


async def test_create_item_with_duplicate_name_raises(inventory_service):
    item_name = "ril73"

    await inventory_service.create_item(item_name, "https://placehold.co/73x37")

    with pytest.raises(ItemAlreadyExistsError):
        await inventory_service.create_item(item_name, "https://placehold.co/37x73")


async def test_get_nonexistent_item_raises(inventory_service):
    with pytest.raises(ItemNotFoundError):
        await inventory_service.get_item(uuid4())


async def test_add_new_inventory_item(inventory_service):
    player = Player.create(73, "ril73")
    item = await inventory_service.create_item("ril73", "https://placehold.co/73x37")

    item_amount = 73

    inventory_item = await inventory_service.add_inventory_item(
        player, item, item_amount
    )

    assert isinstance(inventory_item.inventory_item_id, UUID)
    assert inventory_item.player_id == player.player_id
    assert inventory_item.item_id == item.item_id
    assert inventory_item.item_amount.amount == item_amount


async def test_add_existing_inventory_item_increases_amount(inventory_service):
    player = Player.create(73, "ril73")
    item = await inventory_service.create_item("ril73", "https://placehold.co/73x37")

    item_amount = 73

    await inventory_service.add_inventory_item(player, item, item_amount)
    await inventory_service.add_inventory_item(player, item, item_amount)
    inventory_item = await inventory_service.add_inventory_item(
        player, item, item_amount
    )

    assert inventory_item.item_amount.amount == item_amount * 3


async def test_inventory_item_deletes_if_lesser_than_one(inventory_service):
    player = Player.create(73, "ril73")
    item = await inventory_service.create_item("ril73", "https://placehold.co/73x37")

    item_amount = 73

    await inventory_service.add_inventory_item(player, item, item_amount)

    inventory_item = await inventory_service.add_inventory_item(
        player, item, -item_amount
    )

    assert inventory_item is None


async def test_get_inventory_items(inventory_service):
    player = Player.create(73, "ril73")
    item = await inventory_service.create_item("ril73", "https://placehold.co/73x37")

    item_amount = 73

    inventory_item = await inventory_service.add_inventory_item(
        player, item, item_amount
    )

    inventory_items = await inventory_service.get_inventory_items(player)

    assert isinstance(inventory_items, list)
    assert len(inventory_items) == 1
    assert inventory_items[0].inventory_item_id == inventory_item.inventory_item_id

    await inventory_service.add_inventory_item(player, item, -item_amount)

    assert await inventory_service.get_inventory_items(player) == []
