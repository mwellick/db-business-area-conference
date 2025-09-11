import psycopg2

class CreateTables:

    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def create_tables(self):
        try:
            queries = [
                """
                CREATE TABLE IF NOT EXISTS Conference (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    building VARCHAR(64) NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Section (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    number INT NOT NULL,
                    moderator VARCHAR(64) NOT NULL,
                    hall VARCHAR(64) NOT NULL,
                    conference_id INT REFERENCES Conference(id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Speaker (
                    id SERIAL PRIMARY KEY,
                    full_name VARCHAR(64) NOT NULL,
                    bio TEXT NOT NULL,
                    academic_degree VARCHAR(255) NOT NULL,
                    workplace VARCHAR(255) NOT NULL,
                    position VARCHAR(255) NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Presentation (
                    id SERIAL PRIMARY KEY,
                    topic VARCHAR(255) NOT NULL,
                    start_time TIMESTAMP NOT NULL,
                    duration_minutes INT NOT NULL,
                    section_id INT REFERENCES Section(id),
                    speaker_id INT REFERENCES Speaker(id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Equipment (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS PresentationEquipment (
                    presentation_id INT REFERENCES Presentation(id),
                    equipment_id INT REFERENCES Equipment(id),
                    quantity INT NOT NULL,
                    PRIMARY KEY (presentation_id, equipment_id)
                );
                """
            ]
            for query in queries:
                self.cursor.execute(query)

            self.connection.commit()
            print("Tables created successfully! ")
        except psycopg2.Error as e:
            print(f"Error occured during creating tables: {e}")
