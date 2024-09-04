from pydantic_settings import (
    BaseSettings, SettingsConfigDict
)
from pydantic import computed_field


class _ModelConfig:
    """
    Позволяет иметь общий конфиг для всех моделей
    с возможностью переопределения ключей индивидуально
    """
    def __new__(cls, *args, **kwargs) -> SettingsConfigDict:
        config = SettingsConfigDict(
            validate_default=False,
            case_sensitive=False,
            env_ignore_empty=True,
            env_file_encoding='utf-8',
            env_file='.env',
            extra='ignore'
        )
        config.update(**kwargs)
        return config


class _AppSettings(BaseSettings):
    debug: bool = False
    host: str = 'asfmlmkadsmflkds'
    port: int = 5000

    model_config = _ModelConfig(env_prefix="APP_")


class _DatabaseSettings(BaseSettings):
    user: str = 'postgres'
    password: str = 'postgres'
    name: str = 'postgres'
    host: str = 'postgres'
    port: int = 5432

    @computed_field
    @property
    def postgres_dsn(self) -> str:
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'

    model_config = _ModelConfig(env_prefix="DB_")


app_settings = _AppSettings()
db_settings = _DatabaseSettings()
