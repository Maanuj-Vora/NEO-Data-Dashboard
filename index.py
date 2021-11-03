from flask import Flask, request, render_template, jsonify, redirect, session
from flask.helpers import make_response
from scripts.NeoWs import data
import os

try:
    import test
except:
    pass

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

cached_asteriod_data = None


@app.route("/")
def home():
    global cached_asteriod_data
    cached_asteriod_data = data.todayAsteroids()
    session_cookies()
    response = make_response(
        render_template(
            "index.html",
            clean_words=clean_words,
            asteroid_data=cached_asteriod_data,
            current_id=cached_asteriod_data[0]["id"],
        )
    )
    return response


@app.route("/<string:asteroid_id>")
def different_asteroid(asteroid_id):
    global cached_asteriod_data

    response = make_response(
        render_template(
            "index.html",
            clean_words=clean_words,
            asteroid_data=cached_asteriod_data,
            current_id=asteroid_id,
        )
    )
    return response


@app.route("/update_units", methods=["POST"])
def update_units():
    session["estimated_diameter"] = request.form["estimated_diameter"]
    session["relative_velocity"] = request.form["relative_velocity"]
    session["miss_distance"] = request.form["miss_distance"]
    return redirect("/")


def session_cookies():
    if not session.get("estimated_diameter"):
        session["estimated_diameter"] = "kilometers"

    if not session.get("relative_velocity"):
        session["relative_velocity"] = "kilometers_per_second"

    if not session.get("miss_distance"):
        session["miss_distance"] = "astronomical"


def clean_words(word):
    return word.replace("_", " ").title()


@app.errorhandler(404)
def page_not_found(e):
    return home()


@app.errorhandler(500)
def internal_server_error(e):
    return home()
