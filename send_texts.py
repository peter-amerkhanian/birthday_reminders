from text_messaging.twilio_api_call import TextMessage
from text_messaging.parse_calendar import Birthday, get_birthdays
from datetime import datetime

if __name__ == "__main__":
    message_sent: bool = False
    today: str = datetime.today().strftime("%m-%d-%Y")
    birthday: Birthday
    for birthday in get_birthdays():
        if birthday.date.date() == today:
            messenger = TextMessage(birthday.name, birthday.date)
            messenger.send_message()
            message_sent = True
    if not message_sent:
        print("No birthdays today: {}".format(today))
