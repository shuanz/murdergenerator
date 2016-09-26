class VictimGenerator:

    def generator(self):
        from importMuderList import importMurderList
        from nameGen import NameGen
        from jobs import GenerateJobs

        murder_list = importMurderList()
        name_gen = NameGen()
        job_gen = GenerateJobs()

        name = name_gen.generator()
        job = job_gen.generator()
        height = murder_list.generate("heights")
        weight = murder_list.generate("weights")
        tone = murder_list.generate("tones")
        eyecolors = murder_list.generate("eyecolors")
        hairlengths = murder_list.generate("hairlengths")
        haircolors = murder_list.generate("haircolors")

        return [name, job, height, weight, tone, eyecolors,
                hairlengths, haircolors]
