import random

class Person:
    def get_random_male_first_name(self):
        with open('assets/male_names.txt', 'r') as file:
            names = file.readlines()
        names = [name.strip() for name in names]
        random_male_name = random.choice(names)
        return random_male_name

    def get_random_female_first_name(self):
        with open('assets/female_names.txt', 'r') as file:
            names = file.readlines()
        names = [name.strip() for name in names]
        random_female_name = random.choice(names)
        return random_female_name

    def get_random_last_name(self):
        with open('assets/last_names.txt', 'r') as file:
            names = file.readlines()
        names = [name.strip() for name in names]
        random_last_name = random.choice(names)
        return random_last_name

    def create_full_name(self):
        gender = random.choice(['male', 'female'])
        if gender == 'male':
            first_name = self.get_random_male_first_name()
        else:
            first_name = self.get_random_female_first_name()

        last_name = self.get_random_last_name()
        full_name = f"{first_name} {last_name}"
        return full_name


        
# Example usage
#person = Person()
#print(person.create_full_name())
