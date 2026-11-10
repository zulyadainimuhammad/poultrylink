"""Typed application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PoultryLink API"
    app_env: str = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    secret_key: str = "development-only-change-this-secret"
    access_token_expire_minutes: int = 30
    database_url: str = (
        "postgresql+psycopg://poultrylink:local-dev-only-change-me@localhost:5432/poultrylink"
    )
    cors_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
