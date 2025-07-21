import datetime
import contact_data_base as db


def days_until_birthday():
    """Calculate the number of days until the next birthday."""
    days_left_dict = {}
    today = datetime.date.today()
    for person in db.read():
        id = person[0]
        birthday = person[2]

        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

        this_year_birthday = datetime.date(today.year, birthday.month, birthday.day)

        if this_year_birthday < today:
            this_year_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
            days_left_dict[id] = (this_year_birthday - today).days
        else:
            days_left_dict[id] = (this_year_birthday - today).days
    
    return days_left_dict