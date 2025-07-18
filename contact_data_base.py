import sqlite3


def add(name, date):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO birthdays (name, date) VALUES(?, ?)", (name, date))


def read():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        rows = cur.execute("SELECT name, date FROM birthdays").fetchall()
        return rows
    
def remove(name):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM birthdays WHERE name = ?", (name,))

