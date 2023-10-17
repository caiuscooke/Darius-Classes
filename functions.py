"""
Function Type 1
"""


def print_three_lines():  # Define the function 1st
    print("Line 1")
    print("Line 2")
    print("Line 3")


# Call the function 2nd
print_three_lines()


"""
Function Type 2
"""


# arguments make a function dynamic
def print_three_lines_with_arguments(argument):
    print(argument)


# have to pass the argument when you call it
print_three_lines_with_arguments("This is an argument")
print_three_lines_with_arguments("Different output")


"""
Function Type 3
"""


def multiply(number1, number2):  # define the function with arguments
    return number1 * number2  # returning a value


def subtract(number1, number2):  # define the function with arguments
    return number1 - number2  # returning a value


def add(number1, number2):  # define the function with arguments
    return number1 + number2  # returning a value


def divide(number1, number2):  # define the function with arguments
    print("hello")
    return number1 / number2  # returning a value


product = multiply(10, 5)  # a value is applied to this function when you call
sum = add(10, 5)
quotient = divide(10, 5)
differnce = subtract(10, 5)
print(product)
