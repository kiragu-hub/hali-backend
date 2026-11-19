from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "hali_wellness"

    # FastAPI runtime credentials
    DB_USER: str = "hali_app"
    DB_PASSWORD: str

    # Alembic migration credentials
    MIGRATION_DB_USER: str = "hali_migrator"
    MIGRATION_DB_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
