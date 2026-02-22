from abc import ABC, abstractmethod
from typing import Self

from .entity import Entity


class EntityFactory(Entity, ABC):
    @classmethod
    @abstractmethod
    def create(cls) -> Self: ...
