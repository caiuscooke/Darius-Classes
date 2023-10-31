class Person:
    # name
    # age
    # birthplace
    species = "Human"

    def __init__(self, name, age, birthplace):
        self.name = name
        self.age = age
        self.birthplace = birthplace

    def print_person_info(self):
        print(
            f'{self.name} is my name, {self.age} is my age, and Im from {self.birthplace}, Im a {self.species}')


john = Person("John", 32, "Raleigh")
john.print_person_info()
