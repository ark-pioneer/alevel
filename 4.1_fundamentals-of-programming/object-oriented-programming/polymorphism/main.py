# 4 Pillars of Object-Oriented Programming
# - Why OOP? it uses classes, which groups together data and the actions that work on that data
# - organisation of code. To reduce complexity
# Encapsulation: reduces the scope of variables and subroutines/ limit access to identifiers
# grouping similar methods together.
# Inheritance: share data and behaviour from parent classes to child classes. (DRY)
# refactoring: reorganising code 

# Polymorphism
# Giving an action one name that is shared up and down a class hierarchy.
# Each class in the hierarchy implements the action in a way appropriate to itself.

# In context: 
# Polymorphism allows methods (or actions) to be called using the same name across different classes,
# with each class providing its own specific implementation.

class Animal():
    def eat(self):
        return 

class Dog(Animal):
    def eat(self):  # method overriding: intentionally defining the parent class method again
                    # because the child class has a different implementation
        print("I eat kibble")
    
class Cat(Animal):
    def eat(self):
        print("I am fussy and eat mice")

# Both classes implement the same interface.

pets = [Dog(), Cat(), Dog()]
for pet in pets:
    pet.eat() # this part here is the polymorphism: different classes, same behaviour


## Method qualifiers
# Abstract: means the method MUST be implemented by a child class
# Virtual: means the method SHOULD be implemented by a child class

## Access qualifiers
# public: anything qualified as public means it is accessible inside and outside of the class
# private: means it is accessible only inside of the class (weak privacy, _, __)
# protected: means is is accessible only inside the class and any child classes (within the class hierarchy)


