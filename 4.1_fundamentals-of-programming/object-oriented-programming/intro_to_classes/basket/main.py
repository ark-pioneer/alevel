from basket import Basket

print("Welcome to the Pioneer Shopping Experience")

basket = Basket(3)

while True: # condition controlled / indefinite v. definite or count-controlled
    print("Options")
    print("1. Add item")
    print("X. Quit")
    choice = input("> ").lower()
    
    if choice == "x":
        break
    elif choice == "1":
        name = input("item name: ")
        cost = int(input("item cost: "))
        try:
            basket.add({"name":  name, "cost": cost})
        except ValueError as e:
            print(e)

print(f"Thank you for shopping. Your total is: {basket.total()}")