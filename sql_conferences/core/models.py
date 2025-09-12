from dataclasses import dataclass
from datetime import date, datetime

"""

These dataclasses are almost  useless  & aren't used in this code yet
They are created for better db structure & self understanding and may be useful for future
scalability :)
 
"""


@dataclass
class Conference:
    id: int
    name: str
    start_date: date
    end_date: date
    building: str


@dataclass
class Section:
    id: int
    name: str
    number: int
    moderator: str
    hall: str
    conference_id: int


@dataclass
class Speaker:
    id: int
    full_name: str
    bio: str
    academic_degree: str
    workplace: str
    position: str


@dataclass
class Presentation:
    id: int
    topic: str
    start_time: datetime
    duration_minutes: int
    section_id: int
    speaker_id: int


@dataclass
class Equipment:
    id: int
    name: str


@dataclass
class PresentationEquipment:
    quantity: int
    presentation_id: int
    equipment_id: int
