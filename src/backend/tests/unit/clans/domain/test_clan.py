from datetime import datetime
from uuid import UUID, uuid4

import pytest

from src.backend.services.clans.domain.entities.clan import Clan
from src.backend.services.clans.domain.events import ClanCreatedEvent
from src.backend.services.clans.domain.exceptions import (
    InvalidClanNameLengthError,
    InvalidClanTagLengthError,
    InvalidClanTagValueError,
)
from src.backend.services.clans.domain.value_objects import ClanName, ClanTag


async def test_clan_initialization():
    clan_id = uuid4()
    clan_name = ClanName("TestClan")
    clan_tag = ClanTag("test")
    owner_id = 123
    created_at = datetime.now()

    clan = Clan(clan_id, clan_name, clan_tag, owner_id, created_at)

    assert clan.clan_id == clan_id
    assert clan.clan_name == clan_name
    assert clan.clan_tag == clan_tag
    assert clan.owner_id == owner_id
    assert clan.created_at == created_at
    assert clan._events == []


async def test_clan_events_list_initialized_empty():
    clan = Clan(uuid4(), ClanName("Test"), ClanTag("test"), 1, datetime.now())
    assert isinstance(clan._events, list)
    assert len(clan._events) == 0


async def test_create_clan_with_valid_data():
    clan_name = "TestClan"
    clan_tag = "test"
    owner_id = 123

    clan = Clan.create(clan_name, clan_tag, owner_id)

    assert clan.clan_name.value == clan_name
    assert clan.clan_tag.value == clan_tag.upper()
    assert clan.owner_id == owner_id
    assert clan.clan_id is not None
    assert clan.created_at is not None
    assert len(clan._events) == 1
    event = clan._events[0]
    assert isinstance(event, ClanCreatedEvent)
    UUID(event.event_id)


async def test_clan_name_too_short_raises_error():
    with pytest.raises(InvalidClanNameLengthError):
        Clan.create("ab", "test", 123)


async def test_clan_name_too_long_raises_error():
    long_name = "a" * 31
    with pytest.raises(InvalidClanNameLengthError):
        Clan.create(long_name, "test", 123)


async def test_clan_name_with_whitespace_is_trimmed():
    clan = Clan.create("Test Clan", "test", 123)
    # ClanName removes whitespace
    assert clan.clan_name.value == "TestClan"


async def test_clan_name_minimum_length():
    clan = Clan.create("abc", "test", 123)
    assert clan.clan_name.value == "abc"


async def test_clan_name_maximum_length():
    name = "a" * 30
    clan = Clan.create(name, "test", 123)
    assert clan.clan_name.value == name


async def test_clan_tag_too_short_raises_error():
    with pytest.raises(InvalidClanTagLengthError):
        Clan.create("TestClan", "a", 123)


async def test_clan_tag_too_long_raises_error():
    long_tag = "a" * 7
    with pytest.raises(InvalidClanTagLengthError):
        Clan.create("TestClan", long_tag, 123)


async def test_clan_tag_with_whitespace_is_trimmed():
    clan = Clan.create("TestClan", "te st", 123)
    assert clan.clan_tag.value == "TEST"


async def test_clan_tag_is_capitalized():
    clan = Clan.create("TestClan", "test", 123)
    assert clan.clan_tag.value == "TEST"


async def test_clan_tag_non_ascii_raises_error():
    with pytest.raises(InvalidClanTagValueError):
        Clan.create("TestClan", "tëst", 123)


async def test_clan_tag_minimum_length():
    clan = Clan.create("TestClan", "ab", 123)
    assert len(clan.clan_tag.value) == 2


async def test_clan_tag_maximum_length():
    tag = "a" * 6
    clan = Clan.create("TestClan", tag, 123)
    assert len(clan.clan_tag.value) == 6


async def test_pull_events_returns_events():
    clan = Clan.create("TestClan", "test", 123)
    events = clan.pull_events()

    assert len(events) == 1
    assert isinstance(events[0], ClanCreatedEvent)


async def test_pull_events_clears_events_list():
    clan = Clan.create("TestClan", "test", 123)
    clan.pull_events()

    assert len(clan._events) == 0


async def test_pull_events_multiple_times():
    clan = Clan.create("TestClan", "test", 123)
    first_pull = clan.pull_events()
    second_pull = clan.pull_events()

    assert len(first_pull) == 1
    assert len(second_pull) == 0


async def test_pull_events_returns_copy_of_events():
    clan = Clan.create("TestClan", "test", 123)
    events = clan.pull_events()

    # modifying returned list shouldn't affect internal state
    events.append("something")  # type: ignore
    assert len(clan._events) == 0
