class InsertData:

    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def add_conference(self, name, start_date, end_date, building):
        query = """
                INSERT INTO Conference(name, start_date, end_date, building)
                VALUES (%s, %s, %s, %s) 
                RETURNING id;
                """

        self.cursor.execute(query, (name, start_date, end_date, building))
        return self.cursor.fetchone()[0]

    def add_section(self, name, number, moderator, hall, conference_id):
        query = """
                INSERT INTO Section (name, number, moderator, hall, conference_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """
        self.cursor.execute(query, (name, number, moderator, hall, conference_id))
        return self.cursor.fetchone()[0]

    def add_speaker(self, full_name, bio, academic_degree, workplace, position):
        query = """
                INSERT INTO Speaker(full_name, bio, academic_degree, workplace, position)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """
        self.cursor.execute(query, (full_name, bio, academic_degree, workplace, position))
        return self.cursor.fetchone()[0]

    def add_presentation(self, topic, start_time, duration_minutes, section_id, speaker_id):
        query = """
                INSERT INTO Presentation(topic, start_time, duration_minutes, section_id, speaker_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """
        self.cursor.execute(query, (topic, start_time, duration_minutes, section_id, speaker_id))
        return self.cursor.fetchone()[0]

    def add_equipment(self, name):
        query = """
                INSERT INTO Equipment(name)
                VALUES (%s)
                RETURNING id;
                """
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()[0]

    def relate_equipment_to_presentation(self, quantity, presentation_id, equipment_id):
        query = """
                INSERT INTO PresentationEquipment(quantity, presentation_id, equipment_id)
                VALUES (%s, %s, %s)
                RETURNING id;
                """
        self.cursor.execute(query, (quantity, presentation_id, equipment_id))
