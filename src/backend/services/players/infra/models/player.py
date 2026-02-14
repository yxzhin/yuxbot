from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.utils import Base
from ...domain.value_objects import Money
from ..type_mappers import MoneyTypeMapper


class PlayerModel(Base):
    __tablename__ = "players"

    player_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )
    balance: Mapped[Money] = mapped_column(
        MoneyTypeMapper,
        default=0,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
