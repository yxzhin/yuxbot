from .domain_event import DomainEvent


class Entity:
    def __init__(self):
        self._events: list[DomainEvent] = []

    def pull_events(self):
        events = self._events.copy()
        self._events.clear()
        return events
