# make a class for a person
# make the person have a name, age, and birthplace
class Person:
    def __init__(self, name, age, birthplace):
        self.name = name
        self.age = age
        self.birthplace = birthplace

    def print_info(self):
        print(
            f"Hi my name is {self.name}. I am {self.age} years old. I am from {self.birthplace}")


john = Person("John", 34, "Durham")
caius = Person("Caius", 23, "Raleigh")
john.print_info()
caius.print_info()
