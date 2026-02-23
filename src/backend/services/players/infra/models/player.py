from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.utils import Base


class PlayerModel(Base):
    __tablename__ = "players"

    player_id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        unique=True,
    )
    username: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    balance: Mapped[int] = mapped_column(
        Integer(),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
