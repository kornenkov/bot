from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.databases.postgresql.models.base import Base

from .mixins import FullNameMixin


if TYPE_CHECKING:
    from .profile import Profile


class TgUser(Base, FullNameMixin):
    _last_name_nullable = True

    tg_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
    )
    username: Mapped[Optional[str]]
    active: Mapped[Optional[bool]] = mapped_column(
        Boolean,
        default=True,
    )
    profile: Mapped["Profile"] = relationship(
        back_populates="tg_user",
        uselist=False,
        cascade="all, delete-orphan",
    )
