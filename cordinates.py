import random

class GenerateCordinates:

    lon = 0
    lat = 0

    def generator(self):

        lon = "40.%s" % str((random.randint(498863, 914234)))
        lat = "-73.%s" % str((random.randint(263688, 940643)))

        return lon, lat
