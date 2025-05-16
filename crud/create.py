from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import create_record
from core.databases.postgresql.models import TgUser, Profile, Thing, Order
from core.databases.postgresql.models.schemas import (
    TgUserSm,
    ProfileSm,
    ThingSm,
    OrderSm,
)


async def create_user(
    session: AsyncSession,
    tg_id: int,
    first_name: str,
    last_name: str | None,
    username: str | None,
    active: bool = True,
) -> TgUserSm:
    return await create_record(
        session=session,
        model=TgUser,
        schema=TgUserSm,
        tg_id=tg_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        active=active,
    )


async def create_profile(
    session: AsyncSession,
    first_name: str,
    last_name: str,
    patronymic: str | None,
    phone: int,
    tg_user_tg_id: int,
) -> ProfileSm:
    return await create_record(
        session=session,
        model=Profile,
        schema=ProfileSm,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        phone=phone,
        tg_user_tg_id=tg_user_tg_id,
    )


async def create_thing(
    session: AsyncSession,
    name: str,
    quality: str,
    bio: str | None,
    price: int,
    link: str | None,
) -> ThingSm:
    return await create_record(
        session=session,
        model=Thing,
        schema=ThingSm,
        name=name,
        quality=quality,
        bio=bio,
        price=price,
        link=link,
    )


async def create_order(
    session: AsyncSession,
    company: str | None,
    insurance: int | None,
    comment: str | None,
    profile_id: int,
    thing_id: int,
) -> OrderSm:
    return await create_record(
        session=session,
        model=Order,
        schema=OrderSm,
        company=company,
        insurance=insurance,
        comment=comment,
        profile_id=profile_id,
        thing_id=thing_id,
    )
