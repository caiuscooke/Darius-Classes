"""
If statements - conditions
! operator means NOT
== means equals
= is not allowed in a condition
"""


# CHALLENGE 1:

# Write a program that takes two inputs
# The first input is how much money the user has in their bank account
balance = float(input("How much money do you have in your bank account?"))

# The next input is how much money the thing is the user wants to purchase
cost = float(input("how much do the goods cost that you want to purchase?"))

# cost divided by balance
percentage = (cost / balance) * 100
rounded_percentage = round(percentage, 2)
# print out the percentage using an fstring
# phrase = f"the percentage is {percentage}"
# print(phrase)

# if the purchase is between 20% and 50% of the user's bank account balance, tell the user not to make the purchase
if percentage >= 20 and percentage <= 50:
    phrase = f"Don't buy that junk crazy because ${cost:.2f} is {rounded_percentage}% of your ${balance:.2f}"
    print(phrase)

# if the purchase is 50% or more than the user's bank account balance, tell the user to DEFINITELY not make the purchase and call them crazy
elif percentage > 50:
    phrase = f"DEFINITELY dont buy that because ${cost:.2f} is {rounded_percentage}% of your ${balance:.2f}"
    print(phrase)

# if the purchase is less than 20% of the user's bank account, give them the go ahead on making the purchase
else:
    phrase = f"Nah go ahead. Buy it because ${cost:.2f} is {rounded_percentage}% of your ${balance:.2f}"
    print(phrase)
