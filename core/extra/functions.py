from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.formatting import (
    Text,
    Code,
    PhoneNumber,
    as_marked_list,
    Bold,
    as_line,
)

from asyncio import sleep
from typing import TypeVar, Optional, Union, Any

from sqlalchemy.ext.asyncio import AsyncSession

from core.databases.postgresql.models.schemas import AccountSm
from core.keyboards.inline_keyboards.close_kb import build_close_kb

from crud.create import create_profile


P = TypeVar("P")
E = TypeVar("E", bound=Text)


def chunks(
    population: list[P],
    step: int,
) -> list[list[P]]:
    return [
        population[i : i + step]
        for i in range(
            0,
            len(population),
            step,
        )
    ]


async def report_fault(
    message: types.Message,
    entity: str,
) -> None:
    await message.reply(
        text=f"ошибка. отправьте {entity} текстом",
        reply_markup=build_close_kb(),
    )


async def send_temporal_message(
    message: types.Message,
    text: str,
    timeout: int | float = 2.5,
    reply_markup: Optional[
        Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
        ]
    ] = build_close_kb(),
):
    target_message = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )
    await sleep(timeout)
    try:
        await target_message.delete()
    except TelegramBadRequest:
        pass


def create_line(
    key: str,
    value: Union[str, int],
    envelope: type[E] = Bold,
    sep: str = ": ",
    end: str = "",
) -> Text:
    return as_line(
        key,
        envelope(value),
        sep=sep,
        end=end,
    )


def show_account(
    account: AccountSm,
) -> dict[str, Any]:
    fields = (
        (
            "фио",
            account.full_name,
        ),
        ("телефон", account.phone, PhoneNumber),
        ("тг имя", account.tg_user.tg_full_name),
        ("тг айди", account.tg_user_tg_id),
        ("юзернейм", account.tg_user.username or "нет", Code),
    )
    return as_marked_list(
        *(
            create_line(
                *field,
            )
            for field in fields
        ),
    ).as_kwargs()


async def register_profile(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    await create_profile(
        session=session,
        **await state.get_data(),
        tg_user_tg_id=message.from_user.id,
    )
    await state.clear()
    await message.answer(
        text="супер! вы успешно зарегистрированы",
        reply_markup=types.ReplyKeyboardRemove(),
    )
