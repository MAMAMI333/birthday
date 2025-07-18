import contact_data_base as db
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        db.add(name, date)
        return redirect("/")
    
    dates = db.read()
    return render_template("index.html", dates=dates)
    