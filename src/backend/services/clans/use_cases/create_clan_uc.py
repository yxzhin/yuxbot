from collections.abc import Callable

from ....shared.ports import EventBus, UseCase
from ..domain.entities import Clan
from ..ports import ClanUnitOfWork


class CreateClanUseCase(UseCase):
    def __init__(
        self,
        clan_uow_factory: Callable[[], ClanUnitOfWork],
        event_bus: EventBus,
    ):
        self.clan_uow_factory = clan_uow_factory
        self.event_bus = event_bus

    async def execute(self, clan_name: str, clan_tag: str, owner_id: int) -> Clan:  # type: ignore
        async with self.clan_uow_factory() as clan_uow:
            clan = await clan_uow.clan_service.create_clan(
                clan_name,
                clan_tag,
                owner_id,
            )
            clan_member = await clan_uow.clan_service.add_player_to_clan(
                owner_id,
                clan.clan_id,
            )

        clan_events = clan.pull_events()
        await self.event_bus.publish(clan_events)

        clan_member_events = clan_member.pull_events()
        await self.event_bus.publish(clan_member_events)

        return clan
