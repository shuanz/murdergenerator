class importMurderList:

    def generate(self, json_item):
        import json
        import random

        with open('murderList.json') as mlists:
            murder_list = json.load(mlists)
            result = random.choice(murder_list[json_item])

        return result
