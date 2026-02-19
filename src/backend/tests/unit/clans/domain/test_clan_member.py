from datetime import datetime
from uuid import UUID, uuid4

from src.backend.services.clans.domain.entities import ClanMember
from src.backend.services.clans.domain.events import ClanMemberCreatedEvent


async def test_clan_member_create_success():
    clan_member = ClanMember.create(73, uuid4())

    assert isinstance(clan_member.clan_member_id, UUID)
    assert clan_member.player_id == 73
    assert isinstance(clan_member.clan_id, UUID)
    assert isinstance(clan_member.joined_at, datetime)


async def test_clan_member_create_emits_events():
    clan_member = ClanMember.create(37, uuid4())

    events = clan_member.pull_events()
    assert isinstance(events, list)
    assert len(events) == 1
    assert isinstance(events[0], ClanMemberCreatedEvent)

    assert clan_member.pull_events() == []

    # modifying returned list shouldn't affect internal state
    events.append("ril")  # type: ignore
    assert len(clan_member._events) == 0
