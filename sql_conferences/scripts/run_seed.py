import os
from sql_conferences.core.engine import CreateDatabaseEngine
from sql_conferences.crud.seed_data import seed_data
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASS")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")


def run_seed():
    db_engine = CreateDatabaseEngine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        db_name=DB_NAME
    )

    db_engine.connect()
    seed_data(db_engine.connection, db_engine.cursor)
    db_engine.connection.commit()
    print(db_engine.connection.dsn)
    print("Seed data inserted successfully.")


if __name__ == "__main__":
    run_seed()
