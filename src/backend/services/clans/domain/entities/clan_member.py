from datetime import datetime


class ClanMember:
    def __init__(
        self,
        clan_member_id: int,
        player_id: int,
        clan_id: int,
        joined_at: datetime | None = None,
    ):
        self.clan_member_id = clan_member_id
        self.player_id = player_id
        self.clan_id = clan_id
        self.joined_at = joined_at or datetime.now()
