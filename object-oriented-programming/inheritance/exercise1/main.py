class Square():
    def __init__(self, base, height, sides):
        self.base = base
        self.height = height
        self.sides = sides
    
    def area(self):
        return self.base * self.height
        
    def perimeter(self):
        sum = 0
        for side in self.sides:
            sum += side
        return sum
    
class Triangle():
    def __init__(self, base, height, sides):
        self.base = base
        self.height = height
        self.sides = sides
    
    def area(self):
        return self.base * self.height * 0.5
        
    def perimeter(self):
        sum = 0
        for side in self.sides:
            sum += side
        return sum
    
# Below doesn't change
square = Square(5, 5, [5,5,5,5])
triangle = Triangle(3, 4, [3,4,5])

print(square.area())
print(square.perimeter())
print(triangle.area())
print(triangle.perimeter())

