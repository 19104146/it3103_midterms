from pydantic_settings import BaseSettings
from typing_extensions import List


class Settings(BaseSettings):
    CORS_ORIGINS: List[str] = ["http://order-service:3003"]


settings = Settings()
