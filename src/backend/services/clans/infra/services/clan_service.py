from uuid import UUID

from ...domain.entities import Clan, ClanMember
from ...domain.exceptions import ClanAlreadyExistsError, PlayerAlreadyInClanError
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

    async def add_player_to_clan(self, player_id: int, clan_id: UUID):
        existing = await self.clan_member_repo.get_by_player_id(player_id)
        if existing is not None:
            raise PlayerAlreadyInClanError("this player is already a member of a clan")

        clan_member = ClanMember.create(
            player_id=player_id,
            clan_id=clan_id,
        )

        await self.clan_member_repo.save(clan_member)

        return clan_member
