"""
If the user typed in anything other than a float or an integer, print an error message in the console.
"""


def multiply(num1, num2):
    accepted_types = [int, float]

    if type(num1) not in accepted_types or type(num2) not in accepted_types:
        return f"{num1} or {num2} is not the correct type. Make sure its an Int or Float."
    else:
        return num1 * num2


product = multiply(10.5, 10.5)
print(product)
