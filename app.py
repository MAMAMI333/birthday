from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)


with open("dates.json", "r") as file:
    dates = json.load(file)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", dates=dates)
    else:
        return redirect("/")
    