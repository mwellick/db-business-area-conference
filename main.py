from sql_conferences.scripts.init_db import init_db, init_tables
from sql_conferences.scripts.run_seed import run_seed


def main():
    engine = init_db()
    init_tables(engine.connection, engine.cursor)

    # Check if everything works
    engine.cursor.execute("SELECT version();")
    version = engine.cursor.fetchone()
    print("PostgreSQL version:", version)

    # Check all tables in db
    engine.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = engine.cursor.fetchall()
    print("Tables in the database:", tables)

    # insert_data
    run_seed(engine.connection, engine.cursor)
    print("Seed data inserted successfully.")

    engine.close()


if __name__ == "__main__":
    main()