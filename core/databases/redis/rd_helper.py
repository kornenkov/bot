from redis.asyncio import Redis

from core.databases.shared.mixins import SingletonMixin
from core.configs.bot_config import bot_config


class RdHelper(SingletonMixin):
    def __init__(
        self,
        encoding: str = "utf-8",
        decode_responses: bool = False,
    ) -> None:
        self.redis_session = Redis(
            host=bot_config.rd.rd_host,
            port=bot_config.rd.rd_port,
            db=bot_config.rd.rd_db,
            encoding=encoding,
            decode_responses=decode_responses,
        )


rd_helper = RdHelper(decode_responses=True)
