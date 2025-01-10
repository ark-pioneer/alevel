class StaticQueue():
    def __init__(self, maxsize=10):
        self.list = ['_' for i in range(maxsize)]
        self.size = 0
        self.front = 0
        self.back = 0
        self.maxsize = maxsize

    def enqueue(self, value):
        if self.back >= self.maxsize:
            print("no more space")
        else:
            self.list[self.back] = value
            self.back += 1
            self.size += 1
    
    def dequeue(self):
        if self.size <= 0:
            print("queue empty")
        else:
            item = self.list[self.front]
            self.list[self.front] = "_"
            self.front += 1
            self.size -= 1
            return item