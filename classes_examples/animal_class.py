class Animal:
    animal = "Animal"

    def add(self):
        print(10*10)


class Cats(Animal):
    def __init__(self, subspecies_name):
        self.subspecies_name = subspecies_name


jaguar = Cats("jaguar")
print(jaguar.animal)
jaguar.add()
