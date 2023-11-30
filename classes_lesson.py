# make a class for a person
# make the person have a name, age, and birthplace
class Person:  # Parent class
    def __init__(self, name: str, age: int, birthplace: str):
        self.name = name
        self.age = age
        self.birthplace = birthplace

    def print_info(self):
        print(
            f"Hi my name is {self.name}. I am {self.age} years old. I am from {self.birthplace}")


class AmericanPerson(Person):
    country = "America"

    def __init__(self, name, age, birthplace, state: str, city: str):
        self.state = state
        self.city = city
        super.__init__(name, age, birthplace)


john = Person("John", 34, "Durham")
caius = AmericanPerson("Caius", 23, "Raleigh", "North Carolina", "Raleigh")
john.print_info()
caius.print_info()
