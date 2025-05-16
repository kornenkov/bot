from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from core.databases.postgresql.models import TgUser, Profile

from .base import update_record


async def update_tg_user(
    session: AsyncSession,
    tg_id: int,
    ud_mapping: dict[str, Any],
) -> None:
    async with session.begin():
        await update_record(
            session=session,
            model=TgUser,
            ft_field="tg_id",
            ft_value=tg_id,
            ud_mapping=ud_mapping,
        )


async def update_profile(
    session: AsyncSession,
    tg_user_tg_id: int,
    ud_mapping: dict[str, Any],
) -> None:
    await update_record(
        session=session,
        model=Profile,
        ft_field="tg_user_tg_id",
        ft_value=tg_user_tg_id,
        ud_mapping=ud_mapping,
    )
