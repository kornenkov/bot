from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.databases.postgresql.models import TgUser
from core.keyboards.inline_keyboards.start_kb import build_start_kb
from core.keyboards.inline_keyboards.close_kb import build_close_kb

from core.states.account_create_states import AccountCreate
from crud.base import update_record

from crud.read import get_user_by_tg_id, get_profile_by_tg_id
from crud.create import create_user


router = Router(name=__name__)


@router.message(CommandStart())
async def process_start(
    message: types.Message,
    session: AsyncSession,
):
    user = await get_user_by_tg_id(
        session=session,
        tg_id=message.from_user.id,
    )
    if not user:
        user = await create_user(
            session=session,
            tg_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            active=True,
        )
    if not user.active:
        user.active = True
        await session.commit()
    await message.react(
        reaction=[
            types.ReactionTypeEmoji(
                emoji="❤",
            ),
        ],
        is_big=True,
    )
    await message.reply(
        text=f"рад видеть, <b>{user.first_name}</b>!",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await message.answer(
        text="меню",
        reply_markup=build_start_kb(),
    )


@router.message(Command("help"))
async def process_help(message: types.Message):
    await message.answer(
        text="взаимодействие с ботом происходит посредством инлайн-кнопок. также предусмотрена защита от спама. нашли баг? пишите, исправлю!",
        reply_markup=build_close_kb(),
    )


@router.message(Command("cancel"))
async def process_cancel(
    message: types.Message,
    state: FSMContext,
):
    if await state.get_state() is None:
        return
    await state.clear()
    await message.reply(
        text="прервано",
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Command("account"))
async def process_account_create(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    profile = await get_profile_by_tg_id(
        session=session,
        tg_id=message.from_user.id,
    )
    if profile:
        await message.answer(
            text="Вы уже зарегистрированы",
            show_alert=True,
        )
        return
    await message.answer(text="введите фамилию")
    await state.set_state(AccountCreate.CREATE_LAST_NAME)
