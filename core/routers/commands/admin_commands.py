from aiogram import Router, Bot, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramForbiddenError

from sqlalchemy.ext.asyncio import AsyncSession

from crud.read import get_all_tg_users

router = Router(name=__name__)


@router.message(Command("ad"))
async def process_admin_command(
    message: types.Message,
    bot: Bot,
    session: AsyncSession,
):
    await message.reply(text="начинаю рассылку!")
    for tg_user in await get_all_tg_users(session=session):
        try:
            if tg_user.active:
                await bot.send_message(
                    chat_id=tg_user.tg_id,
                    text=f"салют, <b>{tg_user.tg_full_name}</b>! подпишись на @dmallwww",
                )
        except TelegramForbiddenError:
            pass
        else:
            await message.answer("сообщение отправлено!")
    await message.answer(text="готово.")
