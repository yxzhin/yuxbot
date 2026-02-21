from collections.abc import Callable
from uuid import UUID

from ....shared.ports import UseCase
from ..domain.entities import ClanMember
from ..ports import ClanUnitOfWork


class GetClanMembersUseCase(UseCase):
    def __init__(self, clan_uow_factory: Callable[[], ClanUnitOfWork]):
        self.clan_uow_factory = clan_uow_factory

    async def execute(self, clan_id: UUID) -> list[ClanMember]:  # type: ignore
        async with self.clan_uow_factory() as clan_uow:
            clan = await clan_uow.clan_service.get_clan_by_id(clan_id)
            clan_members = await clan_uow.clan_service.get_clan_members(clan)
            return clan_members
