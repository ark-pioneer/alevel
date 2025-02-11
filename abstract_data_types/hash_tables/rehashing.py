class HashTable():
    def __init__(self):
        self.data = [None for _i in range(10)]
    
    def insert(self, key, value):
        index = self._hash(key)
        while True:
            item = self.data[index]
            if item is None:
                self.data[index] = [key, value]
                break
            else:
                print("collision! Rehashing...")
                index += 1
            
    def find_by(self, key):
        index = self._hash(key)
        while True:
            item = self.data[index]
            if item is None:
                print("no data found!")
                break
            elif item[0] is key:
                return item[1]
            else:
                index += 1

    def _hash(self, key):
        num = sum([ord(char) for char in key])
        return num % 10

ht = HashTable()
print(ht.data)
ht.insert("hello", "world")
ht.insert("olleh", "dlrow")

print(ht.data)
print(ht.find_by("hello"))