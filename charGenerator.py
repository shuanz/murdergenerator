from importMuderList import importMurderList
from nameGenerator import NameGenerator
from jobsGenerator import JobsGenerator

class CharGenerator:

    def generate(self):

        murder_list = importMurderList()
        name = NameGenerator()
        job = JobsGenerator()
        character = {}
        keys = ['name', 'gender', 'relation' 'job', 'height', 'weight', 'tone',
                'eyecolors', 'hairlengths', 'haircolors', 'hairtypes',
                'facehairs', 'clothings']

        for key in keys:
            character.get(key)

        character['name'], character['gender'] = name.generate()
        character['job'] = job.generate()
        character['relation'] = murder_list.generate("who")
        character['height'] = murder_list.generate("heights")
        character['weight'] = murder_list.generate("weights")
        character['tone'] = murder_list.generate("tones")
        character['eyecolors'] = murder_list.generate("eyecolors")
        character['hairlengths'] = murder_list.generate("hairlengths")
        character['haircolors'] = murder_list.generate("haircolors")
        character['hairtypes'] = murder_list.generate("hairtypes")
        character['clothings'] = murder_list.generate("clothings")

        if character['gender'] == "Man":
            character['facehairs'] = murder_list.generate("facehairs")
        else:
            character['facehairs'] = "none"

        return character
