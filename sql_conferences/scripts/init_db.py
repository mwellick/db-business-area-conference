import os
from sql_conferences.core.engine import CreateDatabaseEngine
from sql_conferences.core.tables import CreateTables
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASS")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")


def init_db():
    db_engine = CreateDatabaseEngine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        db_name=DB_NAME
    )

    # Initialize db if it does not exist yet (If it's already exists - exception will be raised)
    db_engine.create_db()

    # Connection to db
    db_engine.connect()
    return db_engine


def init_tables(connection, cursor):
    tables = CreateTables(connection, cursor)
    tables.create_tables()


# This logic is performed to init db,init tablse separately
if __name__ == "__main__":
    engine = init_db()
    try:
        init_tables(engine.connection, engine.cursor)
    finally:
        engine.close()
