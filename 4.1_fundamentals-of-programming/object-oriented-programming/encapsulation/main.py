# Encapsulate the following functions using one class or more!

# Encapsulation (1 of 4 pillars of OOP) Abstraction, Inheritance, Polymorphism.
# - groups similar data and methods together (classes, files)
# - reduces the scope of data and methods

# Why are these ideas beneficial 
# Grouping similar data and methods together: it means programmers can more easily understand, and find things they need.
# Reducing the scope of data and methods: it means there is less chance of data being changed unexpectedly

# Demo, students redo, then independent work
class Calculation():
    def add(self, num1, num2):
        answer = num1 + num2
        result = self.format_answer(answer)
        return result
    def subtract(self, num1, num2):
        answer = num1 - num2
        result = self.format_answer(answer)
        return result
    def format_answer(answer):
        return f"the answer is: {answer}"
    
calculation = Calculation()
print(calculation.add(5, 9))
print(calculation.subtract(4, 1))


# def add(num1, num2):
#     answer = num1 + num2
#     result = format_answer(answer)
#     return result

# def subtract(num1, num2):
#     answer = num1 - num2
#     result = format_answer(answer)
#     return result

# def format_answer(answer):
#     return f"the answer is: {answer}"



