from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as UUIDPG
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.utils import Base


class ClanMemberModel(Base):
    __tablename__ = "clan_members"

    clan_member_id: Mapped[UUID] = mapped_column(
        UUIDPG(as_uuid=True), primary_key=True, default=uuid4
    )
    player_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=False,
        unique=True,
    )
    clan_id: Mapped[UUID] = mapped_column(
        ForeignKey("clans.clan_id"),
        nullable=False,
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
