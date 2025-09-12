from sql_conferences.crud.seed_data import seed_data
from sql_conferences.scripts.init_db import init_db, init_tables


def run_seed(connection, cursor):
    seed_data(connection, cursor)
    connection.commit()
    print("Seed data inserted successfully.")


# This logic is performed to init db,init tablse & insert_data into db separately
if __name__ == "__main__":
    engine = init_db()
    try:
        init_tables(engine.connection, engine.cursor)
        run_seed(engine.connection, engine.cursor)
    except Exception as e:
        raise f"Error occuered: {e}"
    finally:
        engine.close()
