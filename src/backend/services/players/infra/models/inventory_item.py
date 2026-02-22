from uuid import UUID

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID as UUIDPG

from .....shared.utils import Base


class InventoryItemModel(Base):
    __tablename__ = "inventory_items"

    inventory_item_id: Mapped[UUID] = mapped_column(
        UUIDPG(as_uuid=True),
        primary_key=True,
    )
    player_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=False,
    )
    item_id: Mapped[UUID] = mapped_column(
        ForeignKey("items.item_id"),
        unique=True,
        nullable=False,
    )
    item_amount: Mapped[int] = mapped_column(
        Integer(),
        nullable=False,
    )
