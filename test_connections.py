from sqlalchemy import text
from app.db.session import engine
from app.db.migration import migration_engine


def test_connection(name, db_engine):
    try:
        with db_engine.connect() as connection:
            result = connection.execute(
                text("SELECT current_database(), current_user")
            )
            database, user = result.fetchone()

        print(f"\n{name}: SUCCESS")
        print(f"Database: {database}")
        print(f"User: {user}")

    except Exception as error:
        print(f"\n{name}: FAILED")
        print(f"Error: {error}")


test_connection("FASTAPI CONNECTION", engine)
test_connection("ALEMBIC CONNECTION", migration_engine)

engine.dispose()
migration_engine.dispose()
