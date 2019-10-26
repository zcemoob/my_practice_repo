import requests

quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",    # requestvariablename = (url link, paramters (e.g. as dict))
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

# to see a sub-section of the dataset use a parser
parsed_quakesdata = quakes.text[0:100]
print(parsed_quakesdata)

# rest of code...
