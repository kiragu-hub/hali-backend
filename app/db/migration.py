from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from app.core.config import settings


MIGRATION_DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=settings.MIGRATION_DB_USER,
    password=settings.MIGRATION_DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


migration_engine = create_engine(
    MIGRATION_DATABASE_URL,
    pool_pre_ping=True,
)
