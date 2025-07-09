# object oriented programming (OOP)
# procedural programming
# next year -> functional programming (FP)

# OOP
# putting data and methods together in an object

# example requirement: write a program that adds two numbers
# and prints the result.

# approach 1
#print(3 + 9)
# approach 2
#num1 = int(input())
#num2 = int(input())
#print(num1 + num2)
# approach 3
#def add(num1, num2):
#    return num1 + num2 + 10000
#print(add(3, 9))

# OOP

#class Addition(): # class is a keyword that starts a class definition
#    def add(self, num1, num2): # def keyword starts a function definition
#        return num1 + num2

#class Addition2():
#    def add(self, num1, num2):
#        return num1 + num2 + 25

#addition = Addition() # creating an instance of the class
#print(addition.add(3, 9)) # using dot notation to access the instance method


# task: write a program that can handle the four main operations: add, subtract, multiply,  divide: only 2 numbers.

# calculator.add(5, 6)
# calculator.divide(9, 3)

# task: store a starting number. And then update this number with the result of the 4 main operations.

# eg: calculation = Calculation(100)
#     calculation.add(10)
#     calculation.divide(11)
#     calculation.subtract(6)

class Calculation():
    def __init__(self, starting_num):
        self.starting_num = starting_num
    def add(self, num):
        self.starting_num += num
        return self.starting_num
c = Calculation(100)
print(c.add(4))
print(c.add(4))

# Do Now
# Define a class called Person.
# It should have the following properties and methods
# Properties: name, age (set through the initializer)
# Methods: 
#   summary() => returns "My name is [name]. I am [age]yrs old"


class Person():
    def __init__(self, name, age):
        self # name
        self # age

    def summary(self):
        # return the string
        
p1 = Person("Joe", 15)
print(p1.summary())
# prints "My name is Joe. I am 15yrs old"




