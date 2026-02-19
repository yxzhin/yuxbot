from abc import ABC, abstractmethod
from typing import Self

from .entity import Entity


class Aggregate(Entity, ABC):
    @classmethod
    @abstractmethod
    def create(cls) -> Self: ...
