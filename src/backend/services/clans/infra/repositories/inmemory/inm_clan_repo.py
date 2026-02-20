from string import whitespace
from uuid import UUID

from src.backend.services.clans.domain.entities import Clan

from ......shared.infra.units_of_work import InMemoryStorage
from ....ports import ClanRepository


class InMemoryClanRepository(ClanRepository):
    def __init__(self, inm_storage: InMemoryStorage):
        self.inm_storage = inm_storage

    async def get_by_id(self, clan_id: UUID) -> Clan | None:
        for clan in self.inm_storage.clans:
            if clan.clan_id == clan_id:
                return clan
        return None

    async def get_by_name(self, clan_name: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_name = clan_name.translate(trans)
        for clan in self.inm_storage.clans:
            if clan.clan_name.value == clan_name:
                return clan
        return None

    async def get_by_tag(self, clan_tag: str) -> Clan | None:
        trans = str.maketrans("", "", whitespace)
        clan_tag = clan_tag.upper().translate(trans)
        for clan in self.inm_storage.clans:
            if clan.clan_tag.value == clan_tag:
                return clan
        return None

    async def get_by_owner_id(self, owner_id: int) -> Clan | None:
        for clan in self.inm_storage.clans:
            if clan.owner_id == owner_id:
                return clan
        return None

    async def save(self, clan: Clan) -> None:
        for clan_ in self.inm_storage.clans:
            if clan_.clan_id == clan.clan_id:
                index = self.inm_storage.clans.index(clan)
                self.inm_storage.clans[index] = clan
                return

        self.inm_storage.clans.append(clan)
        return
