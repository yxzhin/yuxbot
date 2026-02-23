from src.backend.services.players.domain.entities import Item


async def test_save_inserts_new_item(item_repo_factory):
    item_repo = item_repo_factory()

    item = Item.create("ril73", "https://placehold.co/73x37")

    await item_repo.save(item)

    get_item = await item_repo.get_by_id(item.item_id)

    assert isinstance(get_item, Item)
    assert get_item.item_name == item.item_name
    assert get_item.image_url == item.image_url


async def test_save_updates_existing_item(item_repo_factory):
    item_repo = item_repo_factory()

    item = Item.create("ril73", "https://placehold.co/73x37")

    await item_repo.save(item)

    item_name = "ril37"
    image_url = "https://placehold.co/37x73"

    item.item_name = item_name
    item.image_url = image_url

    await item_repo.save(item)

    get_item = await item_repo.get_by_id(item.item_id)

    assert get_item.item_name == item_name
    assert get_item.image_url == image_url


async def test_get_item_by_name(item_repo_factory):
    item_repo = item_repo_factory()

    item = Item.create("ril73", "https://placehold.co/73x37")

    await item_repo.save(item)

    get_item = await item_repo.get_by_name("ril73")

    assert isinstance(get_item, Item)
    assert get_item.item_id == item.item_id


async def test_get_nonexistent_item_returns_none(item_repo_factory):
    item_repo = item_repo_factory()

    assert await item_repo.get_by_id(73) is None
    assert await item_repo.get_by_name("ril73") is None
