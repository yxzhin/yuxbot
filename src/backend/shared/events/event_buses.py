from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Callable, Iterable

from . import DomainEvent


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: Iterable[DomainEvent]) -> None: ...


class InMemoryEventBus(EventBus):
    def __init__(self):
        self.handlers: dict[
            type[DomainEvent],
            list[Callable],
        ] = defaultdict(list)

    def register(self, event_type: type[DomainEvent], handler: Callable):
        self.handlers[event_type].append(handler)

    async def publish(self, events: Iterable[DomainEvent]) -> None:
        for event in events:
            for handler in self.handlers[type(event)]:
                await handler(event)


# //@TODO: other event bus implementations
