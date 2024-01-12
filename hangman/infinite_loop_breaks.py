some_boolean = True  # the light switch is ON

while some_boolean == True:  # checking if the light switch is turned on
    print("Hello")
    loop_breaker = input()

    if loop_breaker == "exit":
        some_boolean = False  # turns the light switch off AKA BREAKS THE LOOP

some_number = 0

while some_number != 10:
    some_number += 1  # when this line makes the variable some_number = 11 then the loop breaks
