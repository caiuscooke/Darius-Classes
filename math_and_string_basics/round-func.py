# arguments are also known as parameters

# arguments is the data you put between the parantheses of a function
print("hello")  # this is a function with one argument
int("12")  # this is a function with one argument

# round function has two arguments
# round(item1, item2)  # arguments are separated by commas
# print(round(10.518237123, 4))

# method 1
total = 10.518237123
print(f"your total is:${round(total, 2)}")

# method 2
total = 10.518237123
total_rounded = round(total, 2)
total_sentence = f"your total is:${total_rounded}"
print(total_sentence)
