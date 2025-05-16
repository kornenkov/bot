from typing import Optional, Set, TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.databases.postgresql.models.base import Base

from .mixins import FullNameMixin


if TYPE_CHECKING:
    from .tg_user import TgUser
    from .order import Order


class Profile(Base, FullNameMixin):
    _last_name_nullable = False

    patronymic: Mapped[Optional[str]]
    phone: Mapped[str] = mapped_column(
        BigInteger,
        unique=True,
    )

    tg_user_tg_id: Mapped[int] = mapped_column(
        ForeignKey("tgusers.tg_id"),
        unique=True,
    )
    tg_user: Mapped["TgUser"] = relationship(back_populates="profile")

    orders: Mapped[Optional[Set["Order"]]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )
