from importMuderList import importMurderList
from addressGenerator import AddressGenerator

class CaseGenerator:

    def generate(self):

        murder_list = importMurderList()

        case = {}
        keys = ['how', 'why', 'where', 'address', 'lat', 'lon',
                'when', 'who']

        for key in keys:
            case.get(key)

        case['how'] = murder_list.generate("how")
        case['why'] = murder_list.generate("why")
        case['address'], case['lat'], case['lon'] = AddressGenerator().generate()
        case['when'] = murder_list.generate("when")

        return case
