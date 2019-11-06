from datetime import datetime
from typing import Iterator, List, NamedTuple

from icalendar import Calendar, Event


class Birthday(NamedTuple):
    name: str
    date: datetime


def get_names() -> List[str]:
    with open('names.txt', 'r') as f_1:
        names_str: str = f_1.read()
        names: List[str] = names_str.split(',')
        return [name.strip().lower() for name in names]


def get_birthdays() -> Iterator[Birthday]:
    with open('Facebook_Calendar.ics', encoding="latin1") as f_2:
        file: str = f_2.read()
        birthdays: Calendar = Calendar.from_ical(file)
        event: Event
        for event in birthdays.walk():
            if event.name == "VEVENT":
                summary: str = str(event.get("SUMMARY"))
                date_str: str = event.get("DTSTART").to_ical().decode('utf-8')
                name: str = summary.replace("'s Birthday", "").strip().lower()
                date: datetime = datetime.strptime(date_str, "%Y%m%d")
                if name in get_names():
                    yield Birthday(name, date)