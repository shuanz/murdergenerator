import random
import json
from addressGenerator import AddressGenerator

class CaseGenerator:

    def generator(self):

        with open('murderList.json') as mlists:
            murder_list = json.load(mlists)

        case = {}
        keys = ['how', 'why', 'where', 'address', 'lat', 'lon',
                'when', 'who']

        for key in keys:
            case.get(key)

        case['how'] = random.choice(murder_list["how"])
        case['why'] = random.choice(murder_list["why"])
        case['where'] = random.choice(murder_list["where"])
        case['address'], case['lat'], case['lon'] = AddressGenerator().generator()
        case['when'] = random.choice(murder_list["when"])
        case['who'] = random.choice(murder_list["who"])

        return case
