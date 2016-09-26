class GenerateJobs:

    def generator(self):
        from faker import Faker

        fake = Faker()

        job = fake.job()

        return job
