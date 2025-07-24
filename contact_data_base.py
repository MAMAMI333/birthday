import sqlite3


def add_to_birthdays(name, date):
    """Add a new birthday to the database."""
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO birthdays (name, date) VALUES(?, ?)", (name, date))


def add_to_days_left(id, days_left):
    """Add or update the days left for a specific birthday."""
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT OR REPLACE INTO days_left (id, days_left) VALUES(?, ?)", (id, days_left))


def read(table_name):
    """Read data from the specified table."""
    if table_name in ("birthdays", "days_left"):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            query = f"SELECT * FROM {table_name}"
            rows = cur.execute(query).fetchall()
            return rows if rows else []
    else:
        return []
        
    
def remove(name):
    """Remove a birthday entry by name."""
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM birthdays WHERE name = ?", (name,))

