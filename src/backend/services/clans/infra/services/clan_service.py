from uuid import UUID

from ...domain.entities import Clan, ClanMember
from ...domain.exceptions import (
    ClanAlreadyExistsError,
    ClanNotFoundError,
    PlayerAlreadyInClanError,
)
from ...ports import BaseClanService, ClanMemberRepository, ClanRepository


class ClanService(BaseClanService):
    def __init__(
        self,
        clan_repo: ClanRepository,
        clan_member_repo: ClanMemberRepository,
    ):
        self.clan_repo = clan_repo
        self.clan_member_repo = clan_member_repo

    async def create_clan(self, clan_name: str, clan_tag: str, owner_id: int) -> Clan:
        existing = await self.clan_repo.get_by_name(clan_name)
        if existing is not None:
            raise ClanAlreadyExistsError("clan name already taken")

        existing = await self.clan_repo.get_by_tag(clan_tag)
        if existing is not None:
            raise ClanAlreadyExistsError("clan tag already taken")

        existing = await self.clan_repo.get_by_owner_id(owner_id)
        if existing is not None:
            raise ClanAlreadyExistsError("this player is already an owner of a clan")

        existing = await self.clan_member_repo.get_by_player_id(owner_id)  # type: ignore
        if existing is not None:
            raise PlayerAlreadyInClanError("this player is already a member of a clan")

        clan = Clan.create(
            clan_name=clan_name,
            clan_tag=clan_tag,
            owner_id=owner_id,
        )

        await self.clan_repo.save(clan)

        return clan

    async def add_player_to_clan(self, player_id: int, clan: Clan) -> ClanMember:
        existing = await self.clan_member_repo.get_by_player_id(player_id)
        if existing is not None:
            raise PlayerAlreadyInClanError("this player is already a member of a clan")

        clan_member = clan.add_member(player_id)

        await self.clan_member_repo.save(clan_member)

        return clan_member

    async def get_clan_by_id(self, clan_id: UUID) -> Clan:
        clan = await self.clan_repo.get_by_id(clan_id)
        if clan is None:
            raise ClanNotFoundError("clan with given id not found")
        return clan

    async def get_clan_members(self, clan: Clan) -> list[ClanMember]:
        clan_members = await self.clan_member_repo.get_by_clan_id(clan.clan_id)
        return clan_members
