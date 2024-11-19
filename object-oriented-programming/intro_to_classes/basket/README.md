### Basket Exercise

### Setup

1. Create your project folder following the same structure:
- create a folder called `basket`
- in this folder create two files: `basket.py` and `main.py`
2. Copy the code in each file and paste into the correct file on your computer.
3. Run the program to make sure it runs before extending it. You should see printed output of the cost for the first scenario, and then an error happening from the second scenario.
4. You can comment out the code in `main.py` before writing your own code.

### Instructions
Your job is to extend the class definition to satisfy the requirements in each of the tasks below. This will involve creating new functions.

For each task: 
- FIRST: write the interaction in the main.py file that you're trying to complete (see the current `main.py` for an example interaction)
- THEN: and then add code to the class definition in `basket.py` so that when you run the main file, it outputs as expected.

#### TASK 1
```
Basket#remove
- if the item by name exists and there are at least as many items by that name in the basket, remove them from the list of items.
- if the item does not exist by that name, raise a ValueError with message, item not in basket
- if the number of items to remove is greater than the number of items present, raise a Valueerror with message: there are only x items in basket

for example:
GIVEN: 
- a basket of capacity 5
    basket = Basket(5)
- add two items
    basket.add({"name": "bread", "cost": 5})
    basket.add({"name": "water", "cost": 3})
WHEN:
- calling basket remove method with correct values
    basket.remove("bread", 1)
THEN:
- each item should be removed

GIVEN:
- (same setup)
WHEN:
- calling basket remove method with item and too greater a quantity
    basket.remove("bread", 2)
THEN:
- error is raised
    ValueError: there is only 1 bread in basket

GIVEN:
- (same setup)
WHEN:
- calling basket remove method with different item
    basket.remove("pizza", 2)
THEN:
- error is raised
    ValueError: item not in basket
```

#### TASK 2
```
Basket#show
- for each item in the basket print the name and its cost.

for example:
GIVEN: 
- a basket of capacity 5
    basket = Basket(5)
- add two items
    basket.add({"name": "bread", "cost": 5})
    basket.add({"name": "water", "cost": 3})
WHEN:
- calling basket show method
    basket.show()
THEN:
- each item and its cost should be printed
    bread  5
    water  3
```

#### EXTENSION
```
Basket#summary
- group items by name and show the summary: item, quantity and subtotal
- show the grand total

for example:
GIVEN: 
- a basket of capacity 5
    basket = Basket(5)
- add three items
    basket.add({"name": "bread", "cost": 5})
    basket.add({"name": "bread", "cost": 5})
    basket.add({"name": "water", "cost": 3})
WHEN:
- calling basket show method
    basket.summary()
THEN:
- each basket should print a summary of the items in the basket
    bread  x2  10
    water  x1  3
    -------------
    total:     13
```