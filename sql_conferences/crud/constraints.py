from datetime import timedelta


def speaker_can_perform(cursor, speaker_id, section_id, start_time) -> None:
    query = """
            SELECT COUNT(*)
            FROM Presentation
            WHERE speaker_id = %s
              AND section_id = %s
              AND DATE (start_time) = %s;
            """
    cursor.execute(query, (speaker_id, section_id, start_time))
    if cursor.fetchone()[0]:
        raise Exception("Speaker has already performed in this section today")


def hall_availability(cursor, section_id, start_time, duration_minutes) -> None:
    query = """
        SELECT COUNT(*)
        FROM Section AS s
        JOIN Presentation AS p ON s.id = p.section_id
        WHERE s.id=%s
        AND tsrange(p.start_time,p.start_time + (p.duration_minutes) * interval '1 minute')
        && tsrange(%s,%s);
        """
    end_time = start_time + timedelta(minutes=duration_minutes)
    cursor.execute(query,(section_id, start_time, end_time))
    if cursor.fetchone()[0]:
        raise Exception("This hall is already reserved, please choose another time")
