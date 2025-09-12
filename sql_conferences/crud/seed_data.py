from datetime import datetime, date
from sql_conferences.crud.insert_data import InsertData


def seed_data(connection, cursor):
    insert_data = InsertData(connection, cursor)

    # Add Conferences
    conferences = [
        (
            "Python main event 2025 Forum",
            date(2025, 9, 20),
            date(2025, 9, 21),
            "Tech building block A"
        ),
        (
            "Will AI substitute developers?",
            date(2025, 9, 22),
            date(2025, 9, 22),
            "Tech building block B"
        ),
        (
            "Best ways to get into Tech in 2025 Forum",
            date(2025, 10, 2),
            date(2025, 10, 4),
            "Tech building block C"
        )
    ]
    conf_ids = []
    for conf in conferences:
        conf_ids.append(insert_data.add_conference(*conf))

    # Add Sections
    sections = [
        ("Python development", 1, "Michael Ellipsis", "Hall 1", conf_ids[0]),
        ("Web Development", 2, "John Doe", "Hall 2", conf_ids[1]),
        ("IT", 3, "Alice Qwe", "Hall 3", conf_ids[2])
    ]
    section_ids = []
    for section in sections:
        section_ids.append(insert_data.add_section(*section))

    # Add Speakers
    speakers = [
        (
            "Bob Smith",
            "Python developer with over 20 years of experience",
            "Msc in Software Engineering",
            "Google",
            "Senior Developer"
        ),
        (
            "Chris Kyle",
            "Data Scientist and AI Developer",
            "Msc in Computer Science",
            "IBM",
            "Lead Data Scientist"
        ),
        (
            "Mark Carry",
            "Python & JavaScript developer",
            "MSc in Web Development",
            "Facebook",
            "Senior Full Stack Developer"
        ),
    ]
    speaker_ids = []
    for speaker in speakers:
        speaker_ids.append(insert_data.add_speaker(*speaker))

    # Add Presentations
    presentations = [
        (
            "The most popular Python frameworks in 2025",
            datetime(2025, 9, 20, 13, 0),
            120,
            section_ids[0],
            speaker_ids[0]
        ),
        (
            "How to develop easy maintainable backend systems with Python",
            datetime(2025, 9, 20, 16, 0),
            120,
            section_ids[0],
            speaker_ids[1]
        ),
        (
            "Make your development easier with  the most powerful AI tools",
            datetime(2025, 9, 22, 15, 0),
            90,
            section_ids[1],
            speaker_ids[1]
        ),
        (
            "From Zero to Hero in IT: Efficient Roadmap",
            datetime(2025, 10, 2, 16, 0),
            120,
            section_ids[2],
            speaker_ids[2]
        ),
    ]
    presentation_ids = []
    for presentation in presentations:
        presentation_ids.append(insert_data.add_presentation(*presentation))

    # Add Equipment
    equipments = [
        ("Microphone",),
        ("Projector",),
        ("Chair",),
        ("Large display",),
        ("Cable management system",),
    ]
    equipment_ids = []
    for equipment in equipments:
        equipment_ids.append(insert_data.add_equipment(*equipment))

    # Relate Equipment to Presentations
    equipment_relations = [
        # pres 1
        (presentation_ids[0], equipment_ids[0], 1),
        (presentation_ids[0], equipment_ids[1], 1),
        (presentation_ids[0], equipment_ids[2], 100),
        (presentation_ids[0], equipment_ids[4], 1),
        # pres 2
        (presentation_ids[1], equipment_ids[0], 1),
        (presentation_ids[1], equipment_ids[2], 70),
        (presentation_ids[1], equipment_ids[3], 1),
        (presentation_ids[1], equipment_ids[4], 2),
        # pres3
        (presentation_ids[2], equipment_ids[0], 1),
        (presentation_ids[2], equipment_ids[1], 3),
        (presentation_ids[2], equipment_ids[2], 100),
        (presentation_ids[2], equipment_ids[3], 1),
        (presentation_ids[2], equipment_ids[4], 2),
        # pres4
        (presentation_ids[3], equipment_ids[0], 2),
        (presentation_ids[3], equipment_ids[2], 80),
        (presentation_ids[3], equipment_ids[3], 1),
        (presentation_ids[3], equipment_ids[4], 2),

    ]
    for pres_id, equip_id, quantity in equipment_relations:
        insert_data.relate_equipment_to_presentation(
            quantity=quantity,
            presentation_id=pres_id,
            equipment_id=equip_id
        )
