from pydantic import Field
from pydantic_settings import BaseSettings

from backend.constants import DEFAULT_PORT, DEFAULT_HOST


class Settings(BaseSettings):
    host: str = Field(DEFAULT_HOST)
    port: int = Field(DEFAULT_PORT)
