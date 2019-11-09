from flask import Blueprint, jsonify, request, Response
from . import db
from .models import Name
from flask_sqlalchemy import SQLAlchemy
from typing import List, Dict
from icalendar import Calendar, Event
import os

main: Blueprint = Blueprint('main', __name__)

@main.route('/add_name', methods=['POST'])
def add_name():
    name_data: dict = request.get_json()
    new_name: Name = Name(name=name_data['name'])
    db.session.add(new_name)
    db.session.commit()
    return 'Done', 201

@main.route('/names', methods=['GET'])
def names():
    names_list: SQLAlchemy.Query = Name.query.all()
    names: List[Dict[str, str]] = [{'name': name.name} for name in names_list]
    return jsonify({'names': names})

@main.route('/all_calendar_names', methods=['GET'])
def all_calendar_names():
    if os.getcwd().endswith("birthday_reminders"):
        path = os.path.join(os.getcwd(), "Facebook_Calendar.ics")
    else:
        path = os.path.join(os.getcwd(), "birthday_reminders", "Facebook_Calendar.ics")
    with open(path, encoding="latin1") as f:
        file: str = f.read()
        birthdays: Calendar = Calendar.from_ical(file)
        names: List[str] = []
        for event in birthdays.walk(): # event: Event
            if event.name == "VEVENT":
                summary: str = str(event.get("SUMMARY"))
                name: str = summary.replace("'s Birthday", "").strip().lower()
                names.append({'name': name})
    return jsonify({'names': names})