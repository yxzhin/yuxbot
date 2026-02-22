from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID as UUIDPG

from .....shared.utils import Base


class ItemModel(Base):
    __tablename__ = "items"

    item_id: Mapped[UUID] = mapped_column(
        UUIDPG(as_uuid=True),
        primary_key=True,
    )
    item_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    image_url: Mapped[str] = mapped_column(
        String(2083),  # standard max length for URLs
        nullable=False,
    )
