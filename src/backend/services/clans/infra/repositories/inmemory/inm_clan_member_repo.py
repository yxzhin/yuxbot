from backend.services.clans.domain.entities import ClanMember

from ....ports import ClanMemberRepository


class InMemoryClanMemberRepository(ClanMemberRepository):
    def __init__(self) -> None:
        self.clan_members: list[ClanMember] = []

    async def get_by_id(self, clan_member_id: int) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.clan_member_id == clan_member_id:
                return clan_member
        return None

    async def get_by_player_id(self, player_id: int) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.player_id == player_id:
                return clan_member
        return None

    async def get_by_clan_id(self, clan_id: int) -> ClanMember | None:
        for clan_member in self.clan_members:
            if clan_member.clan_id == clan_id:
                return clan_member
        return None

    async def create(self, clan_member: ClanMember):
        self.clan_members.append(clan_member)
