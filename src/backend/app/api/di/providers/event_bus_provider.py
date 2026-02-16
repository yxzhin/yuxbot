from dishka import Provider, Scope, provide

from .....services.clans.domain.events import ClanCreatedEvent, ClanMemberCreatedEvent
from .....shared.events import InMemoryEventBus
from .....shared.utils import StructuredLogger


async def clan_created_event(event):
    StructuredLogger.info(f"clan created: {event}")


async def clan_member_created_event(event):
    StructuredLogger.info(f"clan member created: {event}")


class EventBusProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def event_bus(self) -> InMemoryEventBus:
        event_bus = InMemoryEventBus()
        event_bus.register(ClanCreatedEvent, clan_created_event)
        event_bus.register(ClanMemberCreatedEvent, clan_member_created_event)
        return event_bus
