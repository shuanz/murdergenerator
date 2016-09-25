class GenerateAddres:

    def generator(self):
        from geopy.geocoders import Nominatim
        from cordinates import GenerateCordinates

        geolocator = Nominatim()
        cordinates = GenerateCordinates()

        lon, lat = cordinates.generator()

        location = geolocator.reverse("%s, %s" % (lon, lat))
        return (location.address)
