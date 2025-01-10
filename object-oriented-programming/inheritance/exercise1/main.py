import math

class Shape():
    def __init__(self, base, height, sides):
        self.base = base
        self.height = height
        self.sides = sides
    
    def perimeter(self):
        sum = 0
        for side in self.sides:
            sum += side
        return sum
    
    def area(self):
        return self.base * self.height

class Square(Shape):
    def area(self):
        return self.base * self.height
        
class Triangle(Shape):
    def area(self):
        return self.base * self.height * 0.5
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(0,0, [])

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return math.pi * self.radius * 2

    
# Below doesn't change
square = Square(5, 5, [5,5,5,5])
triangle = Triangle(3, 4, [3,4,5])
circle = Circle(10)

# print(square.area())
# print(square.perimeter())
# print(triangle.area())
# print(triangle.perimeter())
print(circle.area())
print(circle.circumference())
print(circle.perimeter())
