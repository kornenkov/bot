from typing import Optional, Set, TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .order import Order


class Thing(Base):
    name: Mapped[str] = mapped_column(unique=True)
    quality: Mapped[str]
    bio: Mapped[Optional[str]] = mapped_column(Text)
    price: Mapped[int]
    link: Mapped[Optional[str]] = mapped_column(unique=True)

    orders: Mapped[Optional[Set["Order"]]] = relationship(
        back_populates="thing",
        cascade="all, delete-orphan",
    )
