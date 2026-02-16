from ..domain.entities import Clan, ClanMember
from ..domain.exceptions import ClanAlreadyExistsError
from ..ports import ClanUnitOfWork


class CreateClanUseCase:
    def __init__(self, clan_uow: ClanUnitOfWork):
        self.clan_uow = clan_uow

    async def execute(self, clan_name: str, clan_tag: str, owner_id: int) -> Clan:
        existing = await self.clan_uow.clan_repo.get_by_name(clan_name)
        if existing:
            raise ClanAlreadyExistsError("clan name already taken")

        existing = await self.clan_uow.clan_repo.get_by_tag(clan_tag)
        if existing:
            raise ClanAlreadyExistsError("clan tag already taken")

        existing = await self.clan_uow.clan_repo.get_by_owner_id(owner_id)
        if existing:
            raise ClanAlreadyExistsError("this player is already an owner of a clan")

        clan = Clan.create(
            clan_name=clan_name,
            clan_tag=clan_tag,
            owner_id=owner_id,
        )

        clan_member = ClanMember.create(
            player_id=clan.owner_id,
            clan_id=clan.clan_id,
        )

        for ev in clan.pull_events():
            await self.clan_uow.collect_event(ev)

        for ev in clan_member.pull_events():
            await self.clan_uow.collect_event(ev)

        await self.clan_uow.clan_repo.save(clan)
        await self.clan_uow.clan_member_repo.save(clan_member)

        return clan
