"""Distance Between Two Cities -
Calculates the distance between two cities and allows the user to specify a
unit of distance. This program may require finding coordinates for the cities
like latitude and longitude."""

from math import *
from decimal import *
from geopy.geocoders import Nominatim
geolocator = Nominatim()

R = {
    'mi': 3961,
    'km': 6373
}


city1 = {
    'name': raw_input("City 1: ")
}

city2 = {
    'name': raw_input("City 2: ")   
}

while True:
    unit = raw_input("Unit (km, mi): ")
    if (unit == "km" or unit == "mi"):
        break

city1["location"] = geolocator.geocode(city1.get('name'))
city2["location"] = geolocator.geocode(city2.get('name'))
city1["lat"] = city1.get('location').latitude
city1["long"] = city1.get('location').longitude
city2["lat"] = city2.get('location').latitude
city2["long"] = city2.get('location').longitude

dlon = radians(city2.get('long')) - radians(city1.get('long'))
dlat = radians(city2.get('lat')) - radians(city1.get('lat'))

a = (sin(dlat/2))**2 + cos(radians(city1.get('lat'))) * cos(radians(city2.get('lat'))) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R.get(unit) * c

print "%f %s between %s and %s" % (d, unit, city1.get('name'), city2.get('name'))
