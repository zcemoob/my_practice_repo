# download data(set)
import requests

quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

# parse data as a JSON file
import json
requests_json = json.loads(quakes.text) # FXN??
print(type(requests_json))  # double checks data type (should be dict in this ex)

# navigate through the dictionary to see how the info is stored
requests_json.keys()  # should print out the dict keys
len(requests_json['features']) # should give the number of values under this key

requests_json['features'][0].keys() #FXN??
requests_json['features'][0]['properties'].keys()
requests_json['features'][0]['properties']['mag']
requests_json['features'][0]['geometry']

# try saving the data in a text file & opening it in an IDE/internet browser
# code goes here...

# finding the largest earthquake
quakes = requests_json['features']

largest_so_far = quakes[0]
for quake in quakes:
    if quake['properties']['mag'] > largest_so_far['properties']['mag']:
        largest_so_far = quake
largest_so_far['properties']['mag']

lat = largest_so_far['geometry']['coordinates'][1]
long = largest_so_far['geometry']['coordinates'][0]
print("Latitude: {} Longitude: {}".format(lat, long))

# mapping the data (point of the quake)
import requests

def request_map_at(lat, long, satellite=True,
                   zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size="{},{}".format(size[0], size[1]),
        ll="{},{}".format(long, lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)

map_png = request_map_at(lat, long, zoom=10, satellite=False) # is this command or result?

# displaying the map
from IPython.display import Image
Image(map_png.content)

