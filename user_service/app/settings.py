from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)

    APP_NAME: str = "User Microservice"
    APP_VERSION: str = "1.0.0-alpha"

    JWT_SECRET: str


settings = Settings()  # type: ignore
