from basket import Basket

# Scenario: Adding items and then calculating total cost
basket1 = Basket(10)

basket1.add({"name": "bread", "cost": 5})
basket1.add({"name": "bread", "cost": 5})
basket1.add({"name": "water", "cost": 3})

# expected: printed output of 13
print(basket1.total())

# Scenario: adding items over capacity causes an error
basket2 = Basket(1)

basket2.add({"name": "bread", "cost": 5})
# expected: next line causes an error
basket2.add({"name": "bread", "cost": 5})
