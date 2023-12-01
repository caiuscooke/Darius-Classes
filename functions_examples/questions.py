name = input("enter your name:")

# since input is always a string
# we want to make sure that its not a number
# if it is possible to type cast to either int or float
# ask the user to re-input


def MainProgram():
    try:
        name = int(name)
        print("That is not a name, that is a number.")
    except:
        CheckNameExists()


def CheckNameExists():
    if not name:  # checks if name has a value
        print("you did not enter your name")
    else:
        print(f"hello {name}. hows your day going")
        GetAge()


def GetAge():
    try:
        age = int(input(f"{name} what is your age?:"))
        print(f"{name} your age is {age} years old")
    except:
        print("That is not a number.")


MainProgram()
