# Composition
class Gear():
    def __init__(self):
        self.speed = 0

    def change(self):
        self.speed += 1

class Bike():
    def __init__(self):
        self.gear = Gear() # instance of gear is inside Bike
        self.wheel1 = Wheel()
        self.wheel2 = Wheel()

    def change_gear(self):
        self.gear.change()





class Person():
    def __init__(self, name):
        self.name = name

class Wheel():
    def __init__(self):
        self.diameter = 70


class Car():
    def __init__(self, driver):
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        self.driver = driver
    def test(self):
        def inner_method():
            print("hello!")
        inner_method()

person = Person("Mr Withers")
car = Car(person)
car.test() 

