from basket import Basket

print("Welcome to the Pioneer Shopping Experience")

basket = Basket(3)

while True:
    print("Options")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show Basket")
    print("4. Basket Summary")

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
    elif choice == "2":
        name = input("item name: ")
        quantity = int(input("item quantity: "))
        try: 
            basket.remove(name, quantity)
        except ValueError as e:
            print(e)
    elif choice == "3":
        print(basket.show())
    elif choice == "4":
        print(basket.summary())

print(f"Thank you for shopping. Your total is: {basket.total()}")