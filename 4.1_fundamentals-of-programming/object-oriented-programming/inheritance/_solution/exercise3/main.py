class Item():
    def __init__(self, name, age, quality):
        self.name = name
        self.age = age
        self.quality = quality

    def summary(self):
        return f"{self.name}: age: {self.age}, quality: {self.quality}"

    def next_day(self):
        self.age += 1

class KitchenItem(Item):
    def next_day(self):
        super().next_day()
        self.quality -= 4
        
class BedroomItem(Item):
    def next_day(self):
        super().next_day()
        self.quality -= 2

class LivingRoomItem(Item):
    def next_day(self):
        super().next_day()
        self.quality -= 1


house_items = [
    KitchenItem("knife", 0, 50),
    BedroomItem("double bed", 1, 100),
    LivingRoomItem("4-seater sofa", 4, 300)
]

for day in range(10):
    print("----------------")
    print(f"Day {day}")
    for item in house_items:
        item.next_day()
        print(item.summary())
        