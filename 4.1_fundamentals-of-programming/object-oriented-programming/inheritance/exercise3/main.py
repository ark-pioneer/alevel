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
        