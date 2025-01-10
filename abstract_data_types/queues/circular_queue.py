class CQueue():
    def __init__(self, maxsize=10):
        self.list = ['_' for i in range(maxsize)]
        self.size = 0
        self.maxsize = maxsize
        self.front = 0
        self.back = 0

    def enqueue(self, item):
        if self.size >= self.maxsize:
            print("no more space")
        else:
            index = self.back % len(self.list)
            self.list[index] = item
            self.back += 1
            self.size += 1
    
    def dequeue(self):
        if self.size <= 0:
            print("queue empty")
        else:
            index = self.front % len(self.list)
            item = self.list[index]
            self.list[index] = '_'
            self.size -= 1
            self.front += 1
            return item