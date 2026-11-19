from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine

app = FastAPI(
    title="HALI Wellness API",
    description="Backend services for the HALI wellness platform",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to HALI Wellness Platform",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "HALI Backend",
    }


@app.get("/health/db")
def database_health_check():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT current_database(), current_user")
            )
            database, user = result.fetchone()

        return {
            "status": "connected",
            "database": database,
            "user": user,
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection unavailable",
        )
