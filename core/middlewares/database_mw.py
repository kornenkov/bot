from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import Callable, Any, Awaitable, Dict

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from core.databases.postgresql.pg_helper import pg_helper


class DatabaseMw(BaseMiddleware):
    def __init__(
        self,
        session_factory: async_sessionmaker[AsyncSession],
    ) -> None:
        self.__session_factory = session_factory

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        async with self.__session_factory() as session:
            data["session"] = session
        return await handler(event, data)


database_mw = DatabaseMw(pg_helper.session_factory)
