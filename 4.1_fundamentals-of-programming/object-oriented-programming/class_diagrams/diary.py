class Diary():
    def __init__(self):
        self.entries = []
        self.is_locked = False
    
    def add_entry(self, text):
        self.entries.append(text)

    def read(self):
        if not self.is_locked:
            for entry in self.entries:
                self.__print_entry(entry)

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    def __print_entry(self, entry):
        print("Entry: " + entry)

class Addition():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class AddCalc():
    def __init__(self, num1, num2, results):
        self.num1 = num1
        self.num2 = num2
        self.results = results
    
    def add_num(self):
        self.results = self.num1 + self.num2
        print("answer: " + str(self.results))


class Calc():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # public
    def add(self):
        self.__print_ans(self.num1 + self.num2)
    
    # private
    def __print_ans(self, value):
        print("Answer: " + str(value))




item1 = {
    "name": "curry",
    "base_cost": 10,
    "days_left": 2
}
item2 = {
    "name": "naan",
    "base_cost": 2,
    "days_left": 1
}

