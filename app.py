import calc
import contact_data_base as db
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page of the application."""
    dates = db.read("birthdays")
    days_left = db.read("days_left")
    calc.days_until_birthday()  # Update days left before the next birthday
    return render_template("index.html", dates=dates, days_left=days_left)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    date = request.form.get("date")
    db.add_to_birthdays(name, date) # Add new birthday to the database
    calc.days_until_birthday()  # Update days left before the next birthday
    return redirect("/")


@app.route("/remove", methods=["POST"])
def remove():
    id = request.form.get("id")
    db.remove_from_birthdays(id)  # Remove birthday from the database
    print(f"Removed birthday with ID: {id}")
    return redirect("/")


@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("register.html")


@app.route("/log_in", methods=["GET","POST"])
def log_in():
    return render_template("log_in.html")


if __name__ == "__main__":
    app.run(debug=True)
    