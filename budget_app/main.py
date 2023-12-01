from transaction import Transaction

# get the users input on which thing they'd like to do
# options are view, add, delete

view = 1
add = 2
edit = 3
delete = 4

print("Welcome to the budgeting app.")
option = int(
    input("Type 1 to view transactions, 2 to add, 3 to edit, and 4 to delete."))

if option == view:
    Transaction.view()
elif option == add:
    date = input("Date of transaction: ")
    time = input("Time of transaction: ")
    amount = float(input("Amount of transaction: "))
    category = input("Category of transaction: ")

    transaction = Transaction(date, time, amount, category)
    transaction.save()
