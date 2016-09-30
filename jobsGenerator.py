from faker import Faker

class JobsGenerator:

    def generator(self):

        fake = Faker()

        job = fake.job()

        return job
