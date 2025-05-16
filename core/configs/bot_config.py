from core.configs.base_config import BaseConfig

from core.databases.postgresql.pg_config import PostgreSQLConfig
from core.databases.redis.rd_config import RedisConfig


class BotConfig(BaseConfig):
    bot_token: str

    pg: PostgreSQLConfig = PostgreSQLConfig()
    rd: RedisConfig = RedisConfig()


bot_config = BotConfig()
