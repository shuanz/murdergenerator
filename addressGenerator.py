from geopy.geocoders import Nominatim
from cordinatesGenerator import CordinatesGenerator

class AddressGenerator:

    def generate(self):

        geolocator = Nominatim()
        cordinates = CordinatesGenerator()

        lon, lat = cordinates.generate()

        location = geolocator.reverse("%s, %s" % (lon, lat))
        return (location.address, lat, lon)
