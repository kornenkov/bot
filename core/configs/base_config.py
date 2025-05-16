from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file="/Users/danielkornenkov/PycharmProjects/dmallwww telegram bot/.env",
        extra="ignore",
    )
