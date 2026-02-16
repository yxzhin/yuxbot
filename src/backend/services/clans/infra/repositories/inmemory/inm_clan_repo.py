from string import whitespace
from uuid import UUID

from src.backend.services.clans.domain.entities import Clan

from ....ports import ClanRepository


class InMemoryClanRepository(ClanRepository):
    def __init__(self):
        self.clans: list[Clan] = []

    async def get_by_id(self, clan_id: UUID) -> Clan | None:
        for clan in self.clans:
            if clan.clan_id == clan_id:
                return clan
        return None

    async def get_by_name(self, clan_name: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_name = clan_name.translate(trans)
        for clan in self.clans:
            if clan.clan_name.value == clan_name:
                return clan
        return None

    async def get_by_tag(self, clan_tag: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_tag = clan_tag.upper().translate(trans)
        for clan in self.clans:
            if clan.clan_tag.value == clan_tag:
                return clan
        return None

    async def get_by_owner_id(self, owner_id: int) -> Clan | None:
        for clan in self.clans:
            if clan.owner_id == owner_id:
                return clan
        return None

    async def save(self, clan: Clan) -> None:
        for clan_ in self.clans:
            if clan_.clan_id == clan.clan_id:
                index = self.clans.index(clan)
                self.clans[index] = clan
                return

        self.clans.append(clan)
        return
