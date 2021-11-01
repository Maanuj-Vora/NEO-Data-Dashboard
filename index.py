from flask import Flask, request, render_template, jsonify, redirect
from scripts.NeoWs import data
import os

app = Flask(__name__)

cached_asteriod_data = None


@app.route("/")
def home():
    global cached_asteriod_data
    cached_asteriod_data = data.todayAsteroids()
    return render_template(
        "index.html",
        asteroid_data=cached_asteriod_data,
        current_id=cached_asteriod_data[0]["id"],
    )


@app.route("/<string:asteroid_id>")
def different_asteroid(asteroid_id):
    global cached_asteriod_data
    return render_template(
        "index.html", asteroid_data=cached_asteriod_data, current_id=asteroid_id
    )
