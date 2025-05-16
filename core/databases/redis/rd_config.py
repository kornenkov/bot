from core.configs.base_config import BaseConfig


class RedisConfig(BaseConfig):
    rd_db: int
    rd_host: str
    rd_port: int
