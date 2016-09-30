from faker import Faker

class JobsGenerator:

    def generate(self):

        fake = Faker()

        job = fake.job()

        return job
