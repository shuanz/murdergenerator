class GenerateAddres:

    def generator(self):
        from geopy.geocoders import Nominatim
        import random

        geolocator = Nominatim()

        lon =  "40.%s" % str((random.randint(498863, 914234)))
        lat =  "-73.%s" % str((random.randint(263688, 940643)))

        location = geolocator.reverse("%s, %s" % (lon, lat))
        return (location.address)
