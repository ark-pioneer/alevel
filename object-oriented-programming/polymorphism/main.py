# def make_quack(item):
#     item.quack()

# class Duck():
#     def quack(self):
#         print("QUACCCCCCKKKKKKKK")

# class Table():
#     def quack(self):
#         print("WAAAIT IM A TABLE")

# class Paper():
#     def bleep(self):
#         print("BLEEP BLEEP")

# duck = Duck()
# table = Table()
# paper = Paper()

# make_quack(duck)
# make_quack(table)
# make_quack(paper)

def move_skateboard():
    print("you skated 200m")

def move_car():
    print("you drove 2000m")

def move_train():
    print("you rode 20000m")

vehicles = [
    "Skateboard",
    "Car",
    "Train",
    "Car"
]

for vehicle in vehicles:
    if vehicle == "skateboard":
        move_skateboard()
    elif vehicle == "car":
        move_car()
    elif vehicle == "train":
        move_train()




# class Skateboard():
#     def move(self):
#         print("you skated 200m")
# # def move_skateboard():
# #     print("you skated 200m")

# class Car():
#     def move(self):
#         print("you drove 2000m")

# vehicles = [
#     Skateboard(),
#     Car()
# ]

# for vehicle in vehicles:
#     vehicle.move()