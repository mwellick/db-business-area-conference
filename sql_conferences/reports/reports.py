from sql_conferences.reports.models_report import (
    ConferenceReport,
    ConferenceSpeakerReport,
    ConferenceEquipmentReport
)


class Report:

    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def create_views(self):
        queries = [
            """
            CREATE
            OR REPLACE VIEW conference_schedule AS
            SELECT c.name       AS conference_name,
                   c.start_date,
                   c.end_date,
                   c.building,
                   s.name       AS section_name,
                   s.hall,
                   p.topic      AS presentation_topic,
                   p.start_time,
                   p.duration_minutes,
                   sp.full_name AS speaker_name,
                   sp.bio,
                   sp.academic_degree
            FROM Conference AS c
                     JOIN Section AS s ON s.conference_id = c.id
                     JOIN Presentation AS p ON p.section_id = s.id
                     JOIN Speaker AS sp ON sp.id = p.speaker_id;
            """,

            """
            CREATE
            OR REPLACE VIEW conference_speakers AS
            SELECT sp.full_name,
                   sp.workplace,
                   sp.position,
                   c.name AS conference_name
            FROM Speaker AS sp
                     JOIN Presentation AS p ON sp.id = p.speaker_id
                     JOIN Section AS s ON p.section_id = s.id
                     JOIN Conference AS c ON c.id = s.conference_id;
            """,

            """
            CREATE
            OR REPLACE VIEW equipment_needed AS
            SELECT e.name AS equipment_name,
                   s.hall AS section_hall,
                   p.start_time,
                c.name AS conference_name
            FROM PresentationEquipment AS pe
                     JOIN Presentation AS p ON pe.id = p.id
                     JOIN Section AS s ON p.section_id = s.id
                     JOIN Equipment AS e ON pe.equipment_id = e.id
                     JOIN Conference AS c ON c.id = s.cconference_id
            """
        ]

        for query in queries:
            self.cursor.execute(query)
        self.connection.commit()

    def get_conference_schedule(self):
        self.cursor.execute("SELECT * FROM conference_schedule;")
        rows = self.cursor.fetchall()
        return [ConferenceReport(*row) for row in rows]

    def get_conference_speaker(self):
        self.cursor.execute("SELECT * FROM conference_speakers;")
        rows = self.cursor.fetchall()
        return [ConferenceSpeakerReport(*row) for row in rows]

    def get_equipment_for_conf(self):
        self.cursor.execute("SELECT * FROM equipment_needed;")
        rows = self.cursor.fetchall()
        return [ConferenceEquipmentReport(*row) for row in rows]
