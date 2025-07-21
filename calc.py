import datetime
import contact_data_base as db


def days_until_birthday():
    """Calculate the number of days until the next birthday."""
    today = datetime.date.today()
    for person in db.read("birthdays"):
        id = person[0]
        birthday = person[2]

        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

        this_year_birthday = datetime.date(today.year, birthday.month, birthday.day)

        if this_year_birthday < today:
            this_year_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
            db.add_to_days_left(id, (this_year_birthday - today).days)
        else:
            db.add_to_days_left(id, (this_year_birthday - today).days)
