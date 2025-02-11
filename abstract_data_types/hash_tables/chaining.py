class HashTable():
    def __init__(self):
        self.data = [None for _i in range(10)]
    
    def insert(self, key, value):
        index = self._hash(key)
        item = self.data[index]
        if item is None:
            self.data[index] = [key, value]
        else:
            print("collision! Chaining...")
            if item[0] != type([]):
                self.data[index] = [item, [key, value]]
            else:
                self.data[index].append([key, value])
            
    def find_by(self, key):
        index = self._hash(key)
        item = self.data[index]
        if item is None:
            print("no data found!")
        else:
            if type(item[0]) != type([]):
                return item[1]
            else:
                for b in item:
                    if b[0] == key:
                        return b[1]
                print("no data found!")

    def _hash(self, key):
        num = sum([ord(char) for char in key])
        return num % 10

ht = HashTable()
print(ht.data)
ht.insert("hello", "world")
ht.insert("olleh", "dlrow")

print(ht.data)
print(ht.find_by("hello"))