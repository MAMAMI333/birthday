import datetime
import json


def add(name, date):
    with open("dates.json", "r") as file:
        dates = json.load(file)

    id = 0
    for i in dates:
        id += 1

    new_person = {
        "id": id,
        "name": name,
        "date": date
    }

    dates.append(new_person)
    with open("dates.json", "w") as file:
        json.dump(dates, file, indent=2)


def reminder():
    today = datetime.date.today()
    
    with open("dates.json", "r") as file:
        people = json.load(file)
    # for i in people:
    #     bday = i.date
    birthday = "2005-06-30" 
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

    this_year_birthday = datetime.date(today.year, birthday.month, birthday.day)

    #check if birtday have passed
    if this_year_birthday == today:
        #It's today
        print("It's today!")
        #send email
    else:
      #No, it hasn’t happened yet this year
      print("No, it hasn’t happened yet this year.")
      #check if it is next week or in 3 days and if it is send an email

    print(today - birthday)

reminder()