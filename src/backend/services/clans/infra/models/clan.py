from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as UUIDPG
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.utils import Base


class ClanModel(Base):
    __tablename__ = "clans"

    clan_id: Mapped[UUID] = mapped_column(
        UUIDPG(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    clan_name: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )
    clan_tag: Mapped[str] = mapped_column(
        String(6),
        unique=True,
        nullable=False,
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        unique=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
