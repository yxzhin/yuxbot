from uuid import UUID

from src.backend.services.clans.domain.entities import ClanMember

from ....ports import ClanMemberRepository


class InMemoryClanMemberRepository(ClanMemberRepository):
    def __init__(self) -> None:
        self.clan_members: list[ClanMember] = []

    async def get_by_id(self, clan_member_id: UUID) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.clan_member_id == clan_member_id:
                return clan_member
        return None

    async def get_by_player_id(self, player_id: int) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.player_id == player_id:
                return clan_member
        return None

    async def get_by_clan_id(self, clan_id: UUID) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.clan_id == clan_id:
                return clan_member
        return None

    async def save(self, clan_member: ClanMember) -> None:
        for clan_member_ in self.clan_members:
            if clan_member_.clan_member_id == clan_member.clan_member_id:
                index = self.clan_members.index(clan_member)
                self.clan_members[index] = clan_member
                return

        self.clan_members.append(clan_member)
        return
