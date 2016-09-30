import random
from faker import Faker

class NameGenerator:

    def generator(self):

        fake = Faker()

        gender_list = ["Man", "Woman"]

        gender = random.choice(gender_list)

        if gender == "Man":
            name = fake.name_male()
        else:
            name = fake.name_female()

        return name, gender
