"""
This program takes a word, and checks if there are two identical letters in a row in it.
For instance, if the word is "hello", it prints out TRUE because "l" is right next to "l".
But, if the word was "bad", it would print out false.
"""

word = "hello"  # try changing this word

# this allows us to check the first item in the word with the second when we start the loop below
empty_string = word[0]

"""
Since a for-loop can't go ahead of the current iteration in the loop, we have to use this kind of logic. 
For example, if we didn't use this we couldn't tell our for loop to check if the first letter "h" is the same as the NEXT letter, "e". 
The for-loop is only aware of the item it is currently at in its iteration. If letter is equal to "h", it doesn't know that the next item is "e".
Just like humans, computers can't tell the future.
"""

# By using string slicing with "word[:1]" we can tell a loop to start at a some other point than the very beginning. Usually, when we loop through a string like
# "hello", letter is first equal to "h" then "e" and so on. But, in this case we're telling letter to be equal to "e" first, then "l" and so on.
# Run the code to see how this logic works. The fstrings will help you understand how this loop is running.
for letter in word[1:]:
    print(f'Is {empty_string} the same as {letter}?')
    if letter == empty_string:
        print(f"{True}... {empty_string} is the same as {letter}")
        print("\n")
    else:
        print(f"{False}... {empty_string} is NOT the same as {letter}")
        print("\n")

    empty_string = letter
