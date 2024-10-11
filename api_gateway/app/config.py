from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str = "API Gateway"
    APP_VERSION: str = "1.0.0-alpha"

    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY: int = 15
    JWT_SECRET: str

    PRODUCT_SERVICE_URL: str = "http://localhost:3001"
    USER_SERVICE_URL: str = "http://localhost:3002"
    ORDER_SERVICE_URL: str = "http://localhost:3003"

    REDIS_URL: str = "redis://localhost:6379"


config = Config()  # type: ignore
