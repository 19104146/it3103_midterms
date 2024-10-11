from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str = "Order Microservice"
    APP_VERSION: str = "1.0.0-alpha"

    PRODUCT_SERVICE_URL: str = "http://localhost:3001"
    USER_SERVICE_URL: str = "http://localhost:3002"


settings = Settings()
