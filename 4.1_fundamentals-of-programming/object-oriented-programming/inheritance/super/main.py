class Animal():
    def __init__(self, country):
        print("in the parent class")
        self.country = country

class Dog(Animal):
    def __init__(self, country, breed):
        print("in the child class")
        super().__init__(country)
        self.breed = breed

dog = Dog("England", "German Shepherd")
dog2 = Dog("France", "German Shepherd")
print(dog.country)
print(dog.breed)
print(dog2.country)
print(dog2.breed)
