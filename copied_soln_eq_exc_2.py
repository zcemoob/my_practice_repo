import requests
import urllib.request

quakes = requests.get(
    "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
    params={
        "starttime": "2000-01-01",
        "maxlatitude": "58.723",
        "minlatitude": "50.008",
        "maxlongitude": "1.67",
        "minlongitude": "-9.756",
        "minmagnitude": "1",
        "endtime": "2018-10-11",
        "orderby": "time-asc",
    },
)

q = quakes.json()
magnitude_list = []

for i in range(len(q["features"])):
    magnitude = q["features"][i]["properties"]["mag"]
    magnitude_list.append(magnitude)

index = magnitude_list.index(max(magnitude_list))
coor = q["features"][index]["geometry"]["coordinates"]

print("Largest magnitude is:", max(magnitude_list))
print("Country is:", q["features"][index]["properties"]["place"])
print("Coordinates are:", coor)


def request_map_at(lat, long, satellite=True, zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US",
    )

    return requests.get(base, params=params)


map_response = request_map_at(coor[1], coor[0])
url = map_response.url
urllib.request.urlretrieve(url, "location.png")
