def add_numb(num1: int, num2: int):
    return num1 + num2


def divide_numb(num1: int, num2: int):
    return num1 / num2


def sub_numb(num1: int, num2: int):
    return num1 - num2


def multiply_numb(num1: int, num2: int):
    return num1 * num2


def caculate(func, numb1: int, numb2: int):
    return func(numb1, numb2)


# cheese = caculate(add_numb, 7, 5)
# print(cheese)
# cheese = caculate(multiply_numb, 7, 5)
# print(cheese)

# cheese = caculate(divide_numb, 7, 5)
# print(cheese)
# cheese = caculate(sub_numb, 7, 5)
# print(cheese)
# print(multiply_numb)


def caculate(numb1: int, numb2: int):

    def add_numb(num1: int, num2: int):
        return num1 + num2

    def divide_numb(num1: int, num2: int):
        return num1 / num2

    def sub_numb(num1: int, num2: int):
        return num1 - num2

    def multiply_numb(num1: int, num2: int):
        return num1 * num2
    print(add_numb(numb1, numb2))
    print(divide_numb(numb1, numb2))
    print(sub_numb(numb1, numb2))
    print(multiply_numb(numb1, numb2))


caculate(7, 3)
