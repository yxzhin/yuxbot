from abc import ABC, abstractmethod
from uuid import UUID

from ..domain.entities import InventoryItem


class InventoryItemRepository(ABC):
    @abstractmethod
    async def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None: ...

    @abstractmethod
    async def get_by_player_id(self, player_id: int) -> list[InventoryItem]: ...

    @abstractmethod
    async def save(self, inventory_item: InventoryItem) -> None: ...

    @abstractmethod
    async def delete(self, inventory_item: InventoryItem) -> None: ...
