class Transaction:
    # date, time, $amount, category
    def __init__(self, date: str, time: str, amount: float, category: str) -> None:
        self.date = date
        self.time = time
        self.amount = amount
        self.category = category

    # saving the transaction to storage
    def save(self) -> None:
        # r is read
        # a is append
        # w is write
        # x is create
        with open("transactions.txt", "a") as file:
            file.write(
                f"\n{self.date} {self.time} {self.amount} {self.category}")

    def view() -> None:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    # delete a transaction from storage
        # 1. readlines() for the file
        # 2. get user input to select the transaction to delete
        # 3. go to that transaction in the list
        # 4. delete that entry from the list
        # 5. use that list to completely overwrite the file

    # create a function in this class that simply opens the file
    # and returns the file as a list of lines
