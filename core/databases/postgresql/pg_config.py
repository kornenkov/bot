from core.configs.base_config import BaseConfig


class PostgreSQLConfig(BaseConfig):
    pg_user: str
    pg_password: str
    pg_host: str
    pg_port: int
    pg_name: str

    echo: bool = False

    def get_pg_url(self):
        return f"postgresql+asyncpg://{self.pg_user}:{self.pg_password}@{self.pg_host}/{self.pg_name}"
