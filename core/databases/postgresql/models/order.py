from typing import Optional, TYPE_CHECKING

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .profile import Profile
    from .thing import Thing


class Order(Base):
    company: Mapped[Optional[str]]
    insurance: Mapped[Optional[int]]
    comment: Mapped[Optional[str]] = mapped_column(Text)

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    profile: Mapped["Profile"] = relationship(back_populates="orders")

    thing_id: Mapped[int] = mapped_column(ForeignKey("things.id"))
    thing: Mapped["Thing"] = relationship(back_populates="orders")
