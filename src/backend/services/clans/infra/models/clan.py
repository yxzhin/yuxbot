from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.db import Base
from ...domain.value_objects import ClanName, ClanTag
from ..mappers import ClanNameMapper, ClanTagMapper


class ClanModel(Base):
    __tablename__ = "clans"

    clan_id: Mapped[int] = mapped_column(primary_key=True)
    clan_name: Mapped[ClanName] = mapped_column(
        ClanNameMapper,
        unique=True,
    )
    clan_tag: Mapped[ClanTag] = mapped_column(
        ClanTagMapper,
        unique=True,
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
