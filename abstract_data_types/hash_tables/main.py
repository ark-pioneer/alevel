class HashTable():
    def __init__(self):
        self.data = [None for _i in range(10)]
    
    def insert(self, key, value):
        index = self._hash(key)
        item = self.data[index]
        if item is None:
            self.data[index] = [key, value]
        else:
            print("collision!")

    def find_by(self, key):
        index = self._hash(key)
        item = self.data[index]
        if item is None:
            print("no data found!")
        else:
            return item[1]

    def _hash(self, key):
        num = sum([ord(char) for char in key])
        return num % 10

ht = HashTable()
print(ht.data)
ht.insert("hello", "world")
print(ht.data)
print(ht.find_by("hello"))