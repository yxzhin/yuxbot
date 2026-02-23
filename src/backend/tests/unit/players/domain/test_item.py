from uuid import UUID

from src.backend.services.players.domain.entities import Item
from src.backend.services.players.domain.events import ItemCreatedEvent


async def test_item_create_success():
    item_name = "ril73"
    image_url = "https://placehold.co/73x37"
    item = Item.create(item_name, image_url)

    assert isinstance(item.item_id, UUID)
    assert item.item_name == item_name
    assert item.image_url == image_url


async def test_item_create_emits_events():
    item = Item.create("ril73", "https://placehold.co/73x37")

    events = item.pull_events()
    assert isinstance(events, list)
    assert len(events) == 1
    assert isinstance(events[0], ItemCreatedEvent)

    assert item.pull_events() == []

    # modifying returned list shouldn't affect internal state
    events.append("ril")  # type: ignore
    assert len(item._events) == 0
