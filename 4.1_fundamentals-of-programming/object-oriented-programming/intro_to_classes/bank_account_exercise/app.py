from account import Account
from statement import Statement

## this class can be broken into command pattern with user input parsing and validating
class App():
    def __init__(self, account_class=Account):
        self.account = account_class()
    
    def run(self):
        print("Welcome to Pioneer Bank")
        print("H for help")
        print("S for account statement")
        print("D [amount] to deposit amount")
        print("W [amount] to withdraw amount")

        while True:
            data = input("Enter instruction: ")
            if data[0] == "X":
                break
            elif data[0] == "S":
                print(Statement(self.account.transaction_list).create())
            elif data[0] == "D":
                [command, amount] = data.split(" ") 
                self.account.new_transaction({"type": "credit", "amount": float(amount)})
            elif data[0] == "W":
                [command, amount] = data.split(" ") 
                self.account.new_transaction({"type": "debit", "amount": float(amount)})

        print("Session ended")