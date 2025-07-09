account_balance = 0

def update_balance(value):
    global account_balance
    account_balance += value

def menu():
    return """
    1. debit
    2. credit
    3. print balance
    X. exit
    """

print("Welcome to Pioneer Bank")
while True:
    print(menu())
    data = input("enter choice: ").lower()
    if data == "x":
        break
    elif data == "1":
        amount = int(input("enter debit amount: "))
        update_balance(-amount)
    elif data == "2":
        amount = int(input("enter credit amount: "))
        update_balance(amount)
    elif data == "3":
        print(f"balance: {account_balance}")
print("Goodbye!")
