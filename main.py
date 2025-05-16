import logging
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from core.routers import router as main_router

from core.middlewares.database_mw import database_mw
from core.middlewares.throttling_mw import throttling_mw

from core.configs.bot_config import bot_config


def configure_logging(
    level=logging.INFO,
) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


async def main() -> None:
    bot = Bot(
        token=bot_config.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            protect_content=True,
            link_preview_is_disabled=True,
        ),
    )
    dp = Dispatcher(name=__name__)

    dp.include_router(router=main_router)

    dp.message.middleware(database_mw)
    dp.message.outer_middleware(throttling_mw)

    dp.callback_query.middleware(database_mw)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    configure_logging()
    asyncio.run(main())
