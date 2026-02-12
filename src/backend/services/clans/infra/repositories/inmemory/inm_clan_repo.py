from backend.services.clans.domain.entities import Clan

from ....ports import ClanRepository


class InMemoryClanRepository(ClanRepository):
    def __init__(self):
        self.clans = []

    async def get_by_id(self, clan_id: int) -> Clan | None:
        for clan in self.clans:
            if clan.clan_id == clan_id:
                return clan
        return None

    async def get_by_name(self, clan_name: str) -> Clan | None:
        for clan in self.clans:
            if clan.clan_name == clan_name:
                return clan
        return None

    async def create(self, clan: Clan):
        self.clans.append(clan)
