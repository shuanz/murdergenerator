class VictimGenerator:

    def generator(self):
        from nameGen import NameGen
        from importMuderList import importMurderList
        from nameGen import NameGen
        from jobs import GenerateJobs
        import random

        murder_list = importMurderList()
        name_gen = NameGen()
        job_gen = GenerateJobs()

        name = name_gen.generator()
        job = job_gen.generator()
        #height = random.choice(murder_list["heights"])

        return name, job
