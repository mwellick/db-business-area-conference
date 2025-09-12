from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class ConferenceReport:
    conference_name: str
    start_date: date
    end_date: date
    building: str
    section_name: str
    hall: str
    presentation_topic: str
    start_time: datetime
    duration_minutes: int
    speaker_name: str
    bio: str
    academic_degree: str


@dataclass
class ConferenceSpeakerReport:
    full_name: str
    workplace: str
    position: str


@dataclass
class ConferenceEquipmentReport:
    conference_name: str
    equipment_name: str
    section_hall: str
    start_time: datetime
