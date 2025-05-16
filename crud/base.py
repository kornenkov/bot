from typing import TypeVar, Generator, Any

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.databases.postgresql.models import Base
from core.databases.postgresql.models.schemas import BaseSm


M = TypeVar("M", bound=Base)
S = TypeVar("S", bound=BaseSm)


async def create_record(
    session: AsyncSession,
    model: type[M],
    schema: type[S],
    **kwargs: Any,
) -> S:
    async with session.begin():
        record = model(**kwargs)
        session.add(record)
    await session.commit()
    return schema.model_validate(record)


async def get_record(
    session: AsyncSession,
    model: type[M],
    schema: type[S],
    ft_field: str,
    ft_value: Any,
) -> S | None:
    async with session.begin():
        stmt = select(model).filter(getattr(model, ft_field) == ft_value)
        record: M | None = await session.scalar(stmt)
    if record is None:
        return record
    return schema.model_validate(record)


async def update_record(
    session: AsyncSession,
    model: type[M],
    ft_field: str,
    ft_value: int | str,
    ud_mapping: dict[str, Any],
) -> None:
    async with session.begin():
        stmt = (
            update(model)
            .filter(getattr(model, ft_field) == ft_value)
            .values(ud_mapping)
        )
        await session.execute(stmt)


async def get_all_records(
    session: AsyncSession,
    model: type[M],
    schema: type[S],
) -> Generator[S]:
    async with session.begin():
        stmt = select(model)
        records: Generator[S] = (
            schema.model_validate(record) for record in await session.scalars(stmt)
        )
    return records


async def get_record_by_tg_id(
    session: AsyncSession,
    model: type[M],
    schema: type[S],
    field: str,
    tg_id: int,
) -> S:
    return await get_record(
        session=session,
        model=model,
        schema=schema,
        ft_field=field,
        ft_value=tg_id,
    )
