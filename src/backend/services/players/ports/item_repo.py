from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import Item


class ItemRepository(ABC):
    @abstractmethod
    async def get_by_id(self, item_id: UUID) -> Item | None: ...

    @abstractmethod
    async def get_by_name(self, item_name: str) -> Item | None: ...

    @abstractmethod
    async def save(self, item: Item) -> None: ...
