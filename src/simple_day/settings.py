from pydantic import (
    BaseSettings
)


class Settings(BaseSettings):
    DYNAMODB_URL: str = 'http://localhost:8000'