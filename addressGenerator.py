from geopy.geocoders import Nominatim
from cordinatesGenerator import CordinatesGenerator

class AddressGenerator:

    def generator(self):

        geolocator = Nominatim()
        cordinates = CordinatesGenerator()

        lon, lat = cordinates.generator()

        location = geolocator.reverse("%s, %s" % (lon, lat))
        return (location.address, lat, lon)
