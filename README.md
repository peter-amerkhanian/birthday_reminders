## SMS Birthday Reminder
This app uses Twilio to send the user a text the morning
of a friend's birthday. This is meant to be used as
a chron job.
Note that the following environmental variables must be
set to run `send_texts.py` :
- `TW_ACCOUNT` - Your twilio account id
- `TW_KEY` - The key for your twilio account
- `MY_PHONE` - the phone # that will receive the reminders
- `TWILIO_PHONE` - your twilio phone #

Please note that for testing purposes, there is an
additional environmental variable, `JOHN_PHONE`, which can
either be set to a second number to receive the same birthday
reminders, or can be deleted by removing the following
portion of code from `twilio_api_call.py`:
```
38        # Send to John
39        self.client.messages.create(
40            body=body,
41            from_=os.environ["TWILIO_PHONE"],
42            to=os.environ["JOHN_PHONE"]
43        )
```

### Also,  
In the main directory, you must have a `Facebook_Calendar.ics`
file, which is an icalendar file that I used the excellent
[Scrap Facebook Birthdays](https://github.com/ani10030/scrap-facebook-birthdays)
command line app for. You also must have a `names.txt` file
that includes a comma (no space) separated list of the names
of the specific friends out of all of your facebook friends
that you want a birthday reminder for.
