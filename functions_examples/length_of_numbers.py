"""
Write a function that;
1) Takes a number as an argument
2) Returns the length of that number

So if the number is 1000, the function returns 4.
"""


def num_length(num):
    num_string = str(num)
    num_string_length = len(num_string)
    return num_string_length


print(num_length(1000))
