import socket

from twilio.rest import Client
from datetime import datetime
import os

socket.getaddrinfo('localhost', 8000)


class TextMessage:
    account_sid: str = os.environ['TW_ACCOUNT']
    auth_token: str = os.environ['TW_KEY']

    def __init__(self, name: str, date: datetime):
        self.client: Client = Client(self.account_sid, self.auth_token)
        self.name: str = name
        self.date: datetime = date

    def __repr__(self):
        return "<TextMessage: {}'s birthday is on {}>".format(self.name, self.date.strftime("%m-%d-%Y"))

    def send_message(self) -> None:
        body: str = "{}'s birthday is today ({}).".format(self.name, self.date.strftime("%m-%d-%Y"))
        message = self.client.messages.create(
            body=body,
            from_=os.environ["TWILIO_PHONE"],
            to=os.environ["MY_PHONE"]
        )
        print(message.sid, " - ", body)
