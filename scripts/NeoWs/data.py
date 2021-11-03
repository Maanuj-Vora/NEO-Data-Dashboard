from utils import default
import os

config = default.get("config.json")


def todayAsteroids():
    data = default.get(f'{os.path.join("tmp", "todayAsteroids-" + default.todayDate())}.json')
    if data != None and type(data) == dict:
        return data
    else:
    # data = default.getJSON(
    #     default.replaceAPI_KEY(default.replaceSTART_DATE(config.NeoWs_date))
    # )
        data = default.getJSON(
            config.NeoWs_date.replace("{API_KEY}", os.environ.get("API_KEY")).replace(
                "{START_DATE}", default.todayDate()
            )
        )
        data = data.get("near_earth_objects").get(default.todayDate())

        default.dumpJSON('todayAsteroids-' + default.todayDate(), data)

        return data
