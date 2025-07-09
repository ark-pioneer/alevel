# why use Inheritance?
# Keep code DRY: easier to read, change, debug if in one place, not many
# Classes need only define new behaviour, not repeat all behaviour.
class Device():
    def name(self):
        return "I am a device!"

class Laptop(Device):
    def input_type(self):
        return "keys and mouse"

class Tablet(Device):
    def input_type(self):
        return "taps"

class PencilCase():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def name(self):
        return "I am not a device!"

# Instructions
# 1. identify the shared behaviour
# 2. encapsulate the shared behaviour in a base class
# 3. Inherit from the base class in the appropriate child classes. 

# No need to change the below.
# Once you're done, the program should still run without error:
l = Laptop()
t = Tablet()
p = PencilCase()

print("Laptop")
print(l.input_type())
print(l.name())

print("Tablet")
print(t.input_type())
print(t.name())

print("PencilCase")
print(p.name())
print(p.add("pen"))
