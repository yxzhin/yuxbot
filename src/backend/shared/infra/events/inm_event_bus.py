from collections import defaultdict
from collections.abc import Awaitable, Callable, Iterable
from traceback import print_exc

from ...domain import DomainEvent
from ...ports import EventBus

Handler = Callable[[DomainEvent], Awaitable[None]]


class InMemoryEventBus(EventBus):
    def __init__(self):
        self.handlers: dict[type[DomainEvent], list[Handler]] = defaultdict(list)

    def register(self, event_type: type[DomainEvent], handler: Handler):
        self.handlers[event_type].append(handler)

    async def publish(self, events: Iterable[DomainEvent]) -> None:
        for event in events:
            for etype, handlers in self.handlers.items():
                if isinstance(event, etype):
                    for handler in handlers:
                        try:
                            await handler(event)
                        except Exception:
                            # log but continue
                            print(
                                f"[InMemoryEventBus] warning: an exception occurred during {handler}"
                            )
                            print_exc()


# //@TODO: other event bus implementations
