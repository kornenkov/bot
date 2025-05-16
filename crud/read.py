from typing import Generator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.databases.postgresql.models import TgUser, Profile
from core.databases.postgresql.models.schemas import (
    TgUserSm,
    ProfileSm,
    AccountSm,
)
from crud.base import get_all_records, get_record_by_tg_id


async def get_user_by_tg_id(
    session: AsyncSession,
    tg_id: int,
) -> TgUserSm | None:
    return await get_record_by_tg_id(
        session=session,
        model=TgUser,
        schema=TgUserSm,
        field="tg_id",
        tg_id=tg_id,
    )


async def get_profile_by_tg_id(
    session: AsyncSession,
    tg_id: int,
) -> ProfileSm | None:
    return await get_record_by_tg_id(
        session=session,
        model=Profile,
        schema=ProfileSm,
        field="tg_user_tg_id",
        tg_id=tg_id,
    )


async def get_all_tg_users(
    session: AsyncSession,
) -> Generator[TgUserSm]:
    return await get_all_records(
        session=session,
        model=TgUser,
        schema=TgUserSm,
    )


async def get_user_and_profile_by_tg_id(
    session: AsyncSession,
    tg_id: int,
) -> AccountSm | None:
    async with session.begin():
        stmt = (
            select(Profile)
            .options(joinedload(Profile.tg_user))
            .where(Profile.tg_user_tg_id == tg_id)
        )
        account = await session.scalar(stmt)
    if account is None:
        return None
    return AccountSm.model_validate(account)
