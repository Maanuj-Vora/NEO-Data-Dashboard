import json
from collections import namedtuple
import requests
from datetime import datetime
import os


def todayDate():
    return datetime.today().strftime("%Y-%m-%d")


def dumpJSONtest(data):
    json.dump(data, open("test.json", "w", encoding="utf-8"))

def dumpJSON(filename, data):
    f = open(os.path.join('tmp', f'{filename}.json'), "x", encoding="utf-8")

    json.dump(data, f)

def get(file):
    try:
        with open(file, encoding="utf8") as data:
            return json.load(
                data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values())
            )
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        # raise FileNotFoundError("JSON file wasn't found")
        return None


def getJSON(url):
    response = requests.get(url)
    return response.json()


def replaceAPI_KEY(placeholder):
    return placeholder.replace("{API_KEY}", os.environ.get("API_KEY"))


def replaceSTART_DATE(placeholder):
    return placeholder.replace("{START_DATE}", todayDate())


config = get("config.json")
