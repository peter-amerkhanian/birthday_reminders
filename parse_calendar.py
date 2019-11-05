from datetime import date, datetime
from typing import Iterator, List, NamedTuple

from icalendar import Calendar, Event
from twilio_api_call import TextMessage


class Birthday(NamedTuple):
    name: str
    date: datetime


def get_names() -> List[str]:
    with open('names.txt', 'r') as f_1:
        names_str: str = f_1.read()
        names: list = names_str.split(',')
        return names


def get_birthdays() -> Iterator[Birthday]:
    with open('Facebook_Calendar.ics', encoding="latin1") as f_2:
        file: str = f_2.read()
        birthdays: Calendar = Calendar.from_ical(file)
        event: Event
        for event in birthdays.walk():
            if event.name == "VEVENT":
                summary: str = str(event.get("SUMMARY"))
                date_str: str = event.get("DTSTART").to_ical().decode('utf-8')
                name: str = summary.replace("'s Birthday", "")
                date: datetime = datetime.strptime(date_str, "%Y%m%d")
                if name in get_names():
                    yield Birthday(name, date)


if __name__ == "__main__":
    birthday: Birthday
    for birthday in get_birthdays():
        today: date = datetime.today().date()
        if birthday.date.date() == today:
            messenger = TextMessage(birthday.name, birthday.date)
            messenger.send_message()
