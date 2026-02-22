from datetime import datetime
from uuid import UUID

from src.backend.services.clans.domain.entities import Clan
from src.backend.services.clans.domain.events import (
    ClanCreatedEvent,
    ClanMemberJoinedEvent,
)


async def test_clan_create_successfully():
    clan = Clan.create("ril73", "73", 73)

    assert isinstance(clan.clan_id, UUID)
    assert clan.clan_name.value == "ril73"
    assert clan.clan_tag.value == "73"
    assert clan.owner_id == 73
    assert isinstance(clan.created_at, datetime)


async def test_clan_create_emits_events():
    clan = Clan.create("ril37", "37", 37)

    events = clan.pull_events()
    assert isinstance(events, list)
    assert len(events) == 1
    assert isinstance(events[0], ClanCreatedEvent)

    assert clan.pull_events() == []

    # modifying returned list shouldn't affect internal state
    events.append("ril")  # type: ignore
    assert len(clan._events) == 0


async def test_clan_add_member_successfully():
    clan = Clan.create("ril73", "73", 73)
    clan_member = clan.add_member(73)

    assert isinstance(clan_member.clan_member_id, UUID)
    assert clan_member.player_id == 73
    assert clan_member.clan_id == clan.clan_id
    assert isinstance(clan_member.joined_at, datetime)

    events = clan.pull_events()
    assert len(events) == 2
    assert isinstance(events[1], ClanMemberJoinedEvent)
