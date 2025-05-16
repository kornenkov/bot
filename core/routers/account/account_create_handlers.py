from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.keyboards.skip_kb import build_skip_kb
from core.keyboards.phone_kb import build_phone_kb

from core.states.account_create_states import AccountCreate

from core.extra.validators import valid_phone_filter
from core.extra.functions import register_profile


router = Router(name=__name__)


@router.message(
    AccountCreate.CREATE_LAST_NAME,
    F.text,
)
async def process_last_name(
    message: types.Message,
    state: FSMContext,
) -> None:
    last_name = message.text
    await state.update_data(last_name=last_name)
    await state.set_state(AccountCreate.CREATE_FIRST_NAME)
    await message.answer(text="укажите имя")


@router.message(
    AccountCreate.CREATE_FIRST_NAME,
    F.text,
)
async def process_first_name(
    message: types.Message,
    state: FSMContext,
) -> None:
    first_name = message.text
    await state.update_data(first_name=first_name)
    await state.set_state(AccountCreate.CREATE_PATRONYMIC)
    await message.reply(
        text="напишите отчество (при наличии)",
        reply_markup=build_skip_kb(),
    )


@router.message(
    AccountCreate.CREATE_PATRONYMIC,
    F.text,
)
async def process_patronymic(
    message: types.Message,
    state: FSMContext,
) -> None:
    patronymic = message.text if message.text != "пропустить" else None
    await state.update_data(patronymic=patronymic)
    await state.set_state(AccountCreate.CREATE_PHONE)
    await message.reply(
        text="отправьте свой номер телефона. нажмите на кнопку/напишите вручную",
        reply_markup=build_phone_kb(),
    )


@router.message(
    AccountCreate.CREATE_PHONE,
    F.cast(valid_phone_filter).as_(
        "phone",
    ),
)
async def process_phone(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
    phone: str,
):
    await state.update_data(phone=int(phone))
    await register_profile(
        message=message,
        state=state,
        session=session,
    )
