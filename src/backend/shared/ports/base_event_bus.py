from abc import ABC, abstractmethod
from collections.abc import Iterable

from ..infra.events import DomainEvent


class BaseEventBus(ABC):
    @abstractmethod
    async def publish(self, events: Iterable[DomainEvent]) -> None: ...
