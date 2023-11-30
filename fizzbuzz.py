fizz = "fizz"
buzz = "buzz"
fizzbuzz = "fizzbuzz"
# I made this into variables to be consistent with coding conventions
# For instance, it's not a great idea to say print("fizz").
# In general, strings shouldn't be hardcoded like above, why do you think that is?


for num in range(1, 101):
    # pay attention to the range. Why did I say range(1, 101) and not range(1, 100)
    if num % 3 == 0 and num % 5 == 0:
        # why does this condition come first? do you think it matters?
        print(fizzbuzz)
    elif num % 3 == 0:
        print(fizz)
    elif num % 5 == 0:
        print(buzz)
    else:
        print(num)
