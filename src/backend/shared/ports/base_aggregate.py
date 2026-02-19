from abc import ABC, abstractmethod
from typing import Self

from .base_entity import BaseEntity


class BaseAggregate(BaseEntity, ABC):
    @classmethod
    @abstractmethod
    def create(cls) -> Self: ...
