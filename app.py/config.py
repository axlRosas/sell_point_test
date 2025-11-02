from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./sellpoint.db"
    app_title: str = "SellPoint"
    app_host: str = "0.0.0.0"
    app_port: int = 8000


class Config:
    env_file = ".env"


settings = Settings()