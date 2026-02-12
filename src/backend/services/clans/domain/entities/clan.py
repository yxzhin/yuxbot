from datetime import datetime

from ..value_objects import ClanName, ClanTag


class Clan:
    def __init__(
        self,
        clan_id: int,
        clan_name: ClanName,
        clan_tag: ClanTag,
        owner_id: int,
        created_at: datetime | None = None,
    ):
        self.clan_id = clan_id
        self.clan_name = clan_name
        self.clan_tag = clan_tag
        self.owner_id = owner_id
        self.created_at = created_at or datetime.now()
