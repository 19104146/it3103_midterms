from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)

    APP_NAME: str = "Product Microservice"
    APP_VERSION: str = "1.0.0-alpha"


settings = Settings()  # type: ignore
