from faker import Faker

class GenerateJobs:

    def generator(self):

        fake = Faker()

        job = fake.job()

        return job
