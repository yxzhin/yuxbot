from collections.abc import Callable

from ....shared.ports import BaseEventBus, BaseUseCase
from ..domain.entities import Clan, ClanMember
from ..domain.exceptions import ClanAlreadyExistsError
from ..ports import ClanUnitOfWork


class CreateClanUseCase(BaseUseCase):
    def __init__(
        self,
        clan_uow_factory: Callable[[], ClanUnitOfWork],
        event_bus: BaseEventBus,
    ):
        self.clan_uow_factory = clan_uow_factory
        self.event_bus = event_bus

    async def execute(self, clan_name: str, clan_tag: str, owner_id: int) -> Clan:
        async with self.clan_uow_factory() as clan_uow:
            existing = await clan_uow.clan_repo.get_by_name(clan_name)
            if existing:
                raise ClanAlreadyExistsError("clan name already taken")

            existing = await clan_uow.clan_repo.get_by_tag(clan_tag)
            if existing:
                raise ClanAlreadyExistsError("clan tag already taken")

            existing = await clan_uow.clan_repo.get_by_owner_id(owner_id)
            if existing:
                raise ClanAlreadyExistsError(
                    "this player is already an owner of a clan"
                )

            clan = Clan.create(
                clan_name=clan_name,
                clan_tag=clan_tag,
                owner_id=owner_id,
            )

            clan_member = ClanMember.create(
                player_id=clan.owner_id,
                clan_id=clan.clan_id,
            )

            await clan_uow.clan_repo.save(clan)
            await clan_uow.clan_member_repo.save(clan_member)

        clan_events = clan.pull_events()
        await self.event_bus.publish(clan_events)

        clan_member_events = clan_member.pull_events()
        await self.event_bus.publish(clan_member_events)

        return clan
