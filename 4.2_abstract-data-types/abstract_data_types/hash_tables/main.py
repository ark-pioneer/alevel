class HashTable():
    def __init__(self):
        self.data = [[] for _i in range(10)]
    
    def insert(self, value):
        index = self._hash(value)
        bucket = self.data[index]
        bucket.append(value)

    def find(self, value):
        index = self._hash(value)
        bucket = self.data[index]
        for item in bucket:
            if item is value:
                return value
            else:
                print("item not present")

    def _hash(self, value):
        return ord(value[0]) % 10

ht = HashTable()
print(ht.data)
ht.insert("abra")
ht.insert("alwyn")
ht.insert("moon")
print(ht.data)
print(ht.find("abra"))
print(ht.find("mew"))
