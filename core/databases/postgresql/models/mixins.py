from sqlalchemy import String
from sqlalchemy.orm import (
    declared_attr,
    mapped_column,
    Mapped,
)


class PrimaryKeyMixin:
    _id_index = False

    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(
            primary_key=True,
            autoincrement=True,
            index=cls._id_index,
        )


class FullNameMixin:
    _last_name_nullable = None

    @declared_attr
    def first_name(cls) -> Mapped[str]:
        return mapped_column(String)

    @declared_attr
    def last_name(cls) -> Mapped[str]:
        return mapped_column(
            String,
            nullable=cls._last_name_nullable,
        )
