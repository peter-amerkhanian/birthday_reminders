from datetime import datetime

from text_messaging.parse_calendar import Birthday, get_birthdays
from text_messaging.twilio_api_call import TextMessage


def main() -> None:
    """
    Sends an sms text to the user any day that is the birthday
    of a person in names.txt
    :return: None
    """
    message_sent: bool = False
    today: datetime = datetime.today()
    for birthday in get_birthdays(): # birthday: Birthday
        if birthday.date.date() == today.date():
            messenger: TextMessage = TextMessage(birthday.name, birthday.date)
            messenger.send_message()
            message_sent = True
    if not message_sent:
        print("No birthdays today: {}".format(today.strftime("%m-%d-%Y")))


if __name__ == "__main__":
    main()
