class Skateboard():
    def move_skateboard(self):
        print("you skated 200m")

class Car():
    def move_car(self):
        print("you drove 2000m")

class Train():
    def move_train(self):
        print("you rode 20000m")

vehicles = [
    Skateboard(),
    Car(),
    Train(),
    Car()
]

for vehicle in vehicles:
    if isinstance(vehicle, Skateboard):
        vehicle.move_skateboard()
    elif isinstance(vehicle, Car):
        vehicle.move_car()
    elif isinstance(vehicle, Train):
        vehicle.move_train()
