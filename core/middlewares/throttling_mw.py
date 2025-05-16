from aiogram import BaseMiddleware
from aiogram.types import Message

from redis.asyncio import Redis

from typing import Callable, Any, Awaitable, Dict
from datetime import datetime
from operator import sub

from core.databases.redis.rd_helper import rd_helper


class ThrottlingMw(BaseMiddleware):
    __warning_alert = "подозрительная активность. попробуйте еще раз через {} c."

    def __init__(
        self,
        redis: Redis,
        permitted_rate: int = 2,
    ) -> None:
        self.__redis_instance = redis
        self.__permitted_rate = permitted_rate

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        user = await self.__redis_instance.hgetall(name=user_id)
        current_time = datetime.now().isoformat()
        if not user:
            await self.__create_user(
                user_id=user_id,
                current_time=current_time,
            )
        else:
            if (
                self.__calculate_event_interval(
                    dispatch_time=user["dispatch_time"],
                    current_time=current_time,
                )
                < self.__permitted_rate
            ):
                match user["is_notified"]:
                    case "0":
                        await event.reply(
                            text=self.__warning_alert.format(
                                self.__permitted_rate,
                            )
                        )
                        await self.__update_user(
                            user_id=user_id,
                            mapping={
                                "is_notified": "1",
                            },
                        )
                return
            await self.__update_user(
                user_id=user_id,
                mapping={
                    "dispatch_time": current_time,
                    "is_notified": "0",
                },
            )
        return await handler(event, data)

    async def __create_user(
        self,
        user_id: int,
        current_time: str,
    ) -> None:
        await self.__redis_instance.hset(
            name=user_id,
            mapping={
                "dispatch_time": current_time,
                "is_notified": "0",
            },
        )

    async def __update_user(
        self,
        user_id: int,
        mapping: Dict[str, str],
    ) -> None:
        await self.__redis_instance.hset(
            name=user_id,
            mapping=mapping,
        )

    @staticmethod
    def __calculate_event_interval(
        dispatch_time: str,
        current_time: str,
    ) -> int:
        return sub(
            *map(
                datetime.fromisoformat,
                (
                    current_time,
                    dispatch_time,
                ),
            )
        ).total_seconds()


throttling_mw = ThrottlingMw(redis=rd_helper.redis_session)
