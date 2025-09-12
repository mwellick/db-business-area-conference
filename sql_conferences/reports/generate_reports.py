from sql_conferences.reports.reports import Report
from sql_conferences.scripts.init_db import init_db


def generate_reports():
    engine = init_db()
    report = Report(engine.connection, engine.cursor)
    report.create_views()

    conf_schedule = report.get_conference_schedule()
    conf_speaker = report.get_conference_speaker()
    conf_equipments = report.get_equipment_for_conf()

    print("*" * 100)
    print("CONFERENCE SCHEDULE:\n")
    for schedule in conf_schedule:
        print(f"{schedule}\n")

    print("*" * 100)
    print("\nCONFERENCE SPEAKER:\n")
    for speaker in conf_speaker:
        print(f"{speaker}\n")

    print("*" * 100)
    print("\nEQUIPMENT NEEDED:\n")
    for equipment in conf_equipments:
        print(f"{equipment}\n")


if __name__ == "__main__":
    generate_reports()
