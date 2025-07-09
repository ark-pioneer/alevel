# basket.py
class Basket():
    def __init__(self, capacity):
        self.capacity = capacity
        self.products = []
    
    def add(self, item):
        if len(self.products) < self.capacity:
            self.products.append(item)
        else:
            raise ValueError("basket is full")
    
    def total(self):
        sum = 0
        for item in self.products:
            sum += item["cost"]
        return sum

    def remove(self, name, quantity):
        products = []
        # count all occurrences of the items to be removed
        count = 0
        for item in self.products:
            if item["name"] == name:
                count += 1
        # 1: does the item exist? => if not, error
        if count == 0:
            raise ValueError("Item does not exist")
        # 2: do we have enough to remove => if not, error
        elif quantity > count:
            raise ValueError("Basket does not have enough")

        # remove items up to quantity
        removed = 0
        for item in self.products:
            # if item is not item to be removed, add it new list
            # stop removing when quantity reached
            if item["name"] != name or removed == quantity:
                products.append(item)
            else:
            # if item is to be removed, count
                removed += 1
        # set products to be filtered products
        self.products = products
            
    def show(self):
        return "\n".join([
            f"{item["name"]} {item["cost"]}" for item in self.products
        ])

    def summary(self):
        basket_summary = {}
        for item in self.products:
            basket_summary.setdefault(item["name"], { "quantity": 0, "cost": item["cost"] })
            basket_summary[item["name"]]["quantity"] += 1
        summary = []
        total_cost = 0
        for name in basket_summary:
            data = basket_summary[name]
            cost = data["quantity"] * data["cost"]
            total_cost += cost
            summary.append(f"{name.ljust(15, " ")} x{str(data["quantity"]).ljust(5, " ")} {str(cost).rjust(5, " ")}")
        summary.append("-"*25)
        summary.append(f"total cost: {total_cost}".rjust(25, " "))
        return "\n".join(summary)
            
            