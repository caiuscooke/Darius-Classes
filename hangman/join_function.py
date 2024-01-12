# print("".join(gameboard))

# gameboard is a list of underscores
# if the word is something like tool then gameboard = ["_", "_", "_", "_"]
gameboard = ["_", "_", "_", "_"]
print(gameboard)
# method one is to convert it to a string
# print(str(gameboard)) # this is the wrong method for most applications

# method two is to use join
# "".join() # only works connected to a string
# "hello" # an instance of the string class
# the part that comes before join defines what is seperating each item in a list
# gameboard = ["_", "_", "_", "_"] we want to print it out with a space in between each item
" ".join(gameboard)
print("$".join(gameboard))
