from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.db import Base


class ClanMemberModel(Base):
    __tablename__ = "clan_members"

    clan_member_id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=False,
        unique=True,
    )
    clan_id: Mapped[int] = mapped_column(
        ForeignKey("clans.clan_id"),
        nullable=False,
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
