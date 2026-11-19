from sqlalchemy import text

from app.db.session import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user, version()")
        )

        database, user, version = result.fetchone()

        print("DATABASE CONNECTION SUCCESSFUL")
        print(f"Database: {database}")
        print(f"User: {user}")
        print(f"PostgreSQL: {version.split(',')[0]}")

except Exception as error:
    print("DATABASE CONNECTION FAILED")
    print(f"Error: {error}")

finally:
    engine.dispose()
