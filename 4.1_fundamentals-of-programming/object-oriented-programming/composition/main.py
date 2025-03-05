# Composition
class Gear():
    def __init__(self):
        self.speed = 0

    def change(self):
        self.speed += 1

class Wheel():
    def __init__(self):
        self.diameter = 70

class Bike():
    def __init__(self):
        self.gear = Gear() # instance of gear is inside Bike
        self.wheel1 = Wheel()
        self.wheel2 = Wheel()

    def change_gear(self):
        self.gear.change()

class Car():
    def __init__(self):
        self.wheel = Wheel()


bike = Bike()
bike.change_gear()
print(bike.gear.speed)
bike.change_gear()
print(bike.gear.speed)
bike.change_gear()
print(bike.gear.speed)
