import json
import random

class importMurderList:

    def generate(self, json_item):

        with open('murderList.json') as mlists:
            murder_list = json.load(mlists)
            result = random.choice(murder_list[json_item])

        return result
