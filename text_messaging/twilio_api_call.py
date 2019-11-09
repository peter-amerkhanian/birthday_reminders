import os
import socket
from datetime import datetime

from twilio.rest import Client

socket.getaddrinfo('localhost', 8000)


class TextMessage:
    """
    A class that stores Twilio api info and is initialized for each person
    with a birthday the user wants to be reminded of.
    """
    account_sid: str = os.environ['TW_ACCOUNT']
    auth_token: str = os.environ['TW_KEY']

    def __init__(self, name: str, date: datetime) -> None:
        self.client: Client = Client(self.account_sid, self.auth_token)
        self.name: str = name
        self.date: datetime = date

    def __repr__(self) -> str:
        return "<TextMessage: {}'s birthday is on {}>".format(self.name, self.date.strftime("%m-%d-%Y"))

    def send_message(self) -> None:
        """
        Makes and sends a message using the Twilio client
        :return: None
        """
        body: str = "{}'s birthday is today ({}).".format(self.name, self.date.strftime("%m-%d-%Y"))
        # Send to Peter
        message = self.client.messages.create(
            body=body,
            from_=os.environ["TWILIO_PHONE"],
            to=os.environ["MY_PHONE"]
        )
        # Send to John
        self.client.messages.create(
            body=body,
            from_=os.environ["TWILIO_PHONE"],
            to=os.environ["JOHN_PHONE"]
        )
        print(message.sid, " - ", body)
