class importMurderList:

    def murderList(self):
        import json

        with open('murderList.json') as mlists:
            murder_list = json.load(mlists)

        return murder_list
