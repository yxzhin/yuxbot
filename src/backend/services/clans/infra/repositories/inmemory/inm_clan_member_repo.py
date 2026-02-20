from uuid import UUID

from src.backend.services.clans.domain.entities import ClanMember

from ......shared.infra.units_of_work import InMemoryStorage
from ....ports import ClanMemberRepository


class InMemoryClanMemberRepository(ClanMemberRepository):
    def __init__(self, inm_storage: InMemoryStorage) -> None:
        self.inm_storage = inm_storage

    async def get_by_id(self, clan_member_id: UUID) -> ClanMember | None:
        for clan_member in self.inm_storage.clan_members:
            if clan_member.clan_member_id == clan_member_id:
                return clan_member
        return None

    async def get_by_player_id(self, player_id: int) -> ClanMember | None:
        for clan_member in self.inm_storage.clan_members:
            if clan_member.player_id == player_id:
                return clan_member
        return None

    async def get_by_clan_id(self, clan_id: UUID) -> ClanMember | None:
        for clan_member in self.inm_storage.clan_members:
            if clan_member.clan_id == clan_id:
                return clan_member
        return None

    async def save(self, clan_member: ClanMember) -> None:
        for clan_member_ in self.inm_storage.clan_members:
            if clan_member_.clan_member_id == clan_member.clan_member_id:
                index = self.inm_storage.clan_members.index(clan_member)
                self.inm_storage.clan_members[index] = clan_member
                return

        self.inm_storage.clan_members.append(clan_member)
        return
