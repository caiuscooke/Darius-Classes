"""
# # make sure that the input can NOT be casted to an int

# name = input("Enter your name: ")

# try:
#     name = int(name)
# except:
#     print(f"Welcome {name}")


# print("hello world!")
"""

x = 26

# try-except type 1
try:
    print(x + " hello!")
except:
    print("you can't add strings with ints")


# # try-except type 2
try:
    print(x + " hello!")
except TypeError:
    print("you can't add strings with ints")


# # try-except type 3
try:
    print(x + " hello!")
except TypeError as e:
    print(e)
    print("you can't add strings with ints")
