"""
Central registry for all SQLAlchemy models.

Import every model here so Alembic can discover
all database tables through Base.metadata.
"""

from app.db.base import Base

__all__ = ["Base"]
