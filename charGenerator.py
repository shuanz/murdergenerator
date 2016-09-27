from importMuderList import importMurderList
from nameGen import NameGen
from jobs import GenerateJobs

class CharGenerator:

    def generator(self):

        murder_list = importMurderList()
        name_gen = NameGen()
        job_gen = GenerateJobs()

        name, gender = name_gen.generator()
        job = job_gen.generator()
        relation = murder_list.generate("who")
        height = murder_list.generate("heights")
        weight = murder_list.generate("weights")
        tone = murder_list.generate("tones")
        eyecolors = murder_list.generate("eyecolors")
        hairlengths = murder_list.generate("hairlengths")
        haircolors = murder_list.generate("haircolors")
        hairtypes = murder_list.generate("hairtypes")
        if gender == "Man":
            facehairs = murder_list.generate("facehairs")
        else:
            facehairs = "none"
        clothings = murder_list.generate("clothings")

        return [name, job, height, weight, tone, eyecolors,
                hairlengths, haircolors, hairtypes, facehairs,
                clothings, relation]
