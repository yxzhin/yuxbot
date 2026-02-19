from ..infra.events import DomainEvent


class BaseEntity:
    def __init__(self):
        self._events: list[DomainEvent] = []

    def pull_events(self):
        events = self._events.copy()
        self._events.clear()
        return events
