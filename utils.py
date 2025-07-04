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
