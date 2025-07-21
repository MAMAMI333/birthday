import calc
import contact_data_base as db
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page of the application."""
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        db.add_to_birthdays(name, date) # Add new birthday to the database
        calc.days_until_birthday()  # Update days left before the next birthday
        return redirect("/")
    
    dates = db.read("birthdays")
    days_left = db.read("days_left")
    calc.days_until_birthday()  # Update days left before the next birthday
    return render_template("index.html", dates=dates, days_left=days_left)
    