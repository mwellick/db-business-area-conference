import psycopg2
from psycopg2 import sql


class CreateDatabaseEngine:

    def __init__(self, user, db_name, password, host, port):
        self.user = user
        self.db_name = db_name
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def create_db(self):
        self.connect("postgres")
        try:
            self.cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.db_name)))
            print(f"Database created successfully")
        except psycopg2.Error as e:
            raise Exception(f"Error creating Database: {e} ")
        finally:
            self.close()

    def connect(self, db_name=None):
        db_to_connect = db_name or self.db_name
        try:
            self.connection = psycopg2.connect(
                dbname=db_to_connect,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print(f"Successfully connected to th db: {self.db_name}")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e} ")

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
