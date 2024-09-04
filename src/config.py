from pydantic_settings import (
    BaseSettings, SettingsConfigDict,
)


class ModelConfig:
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


class AppSettings(BaseSettings):
    debug: bool = False
    host: str = 'asfmlmkadsmflkds'
    port: int = 5000

    model_config = ModelConfig(env_prefix="APP_")


app = AppSettings()
