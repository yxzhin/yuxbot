from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class DomainEvent:
    event_id: str
    occurred_at: datetime

    @classmethod
    def new(cls, **kwargs):
        return cls(event_id=str(uuid4()), occurred_at=datetime.now(), **kwargs)
