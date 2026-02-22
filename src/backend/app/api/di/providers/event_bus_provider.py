from dishka import Provider, Scope, provide

from .....services.clans.domain.events import ClanCreatedEvent, ClanMemberJoinedEvent
from .....services.players.domain.events import PlayerCreatedEvent
from .....shared.infra.events import InMemoryEventBus
from .....shared.utils import StructuredLogger


async def player_created_event(event):
    StructuredLogger.info(f"player created: {event}")


async def clan_created_event(event):
    StructuredLogger.info(f"clan created: {event}")


async def clan_member_joined_event(event):
    StructuredLogger.info(f"clan member joined: {event}")


class EventBusProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def event_bus(self) -> InMemoryEventBus:
        event_bus = InMemoryEventBus()
        event_bus.register(ClanCreatedEvent, clan_created_event)
        event_bus.register(ClanMemberJoinedEvent, clan_member_joined_event)
        event_bus.register(PlayerCreatedEvent, player_created_event)
        return event_bus
