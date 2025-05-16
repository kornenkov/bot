from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from core.configs.bot_config import bot_config


class PgHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


pg_helper = PgHelper(
    url=bot_config.pg.get_pg_url(),
    echo=bot_config.pg.echo,
)
