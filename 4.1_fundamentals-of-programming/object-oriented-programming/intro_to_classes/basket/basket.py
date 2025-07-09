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


        
