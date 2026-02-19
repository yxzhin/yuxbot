from abc import ABC, abstractmethod
from collections.abc import Iterable

from ..domain import DomainEvent


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: Iterable[DomainEvent]) -> None: ...
