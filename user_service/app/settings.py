from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str = "User Microservice"
    APP_VERSION: str = "1.0.0-alpha"

    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY: int = 15
    JWT_SECRET: str


settings = Settings()  # type: ignore
