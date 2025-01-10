class Stack():
    def __init__(self, maxsize=10):
        self.list = ['_' for i in range(maxsize)]
        self.maxsize = maxsize
        self.size = 0
        self.front = 0
        self.back = 0
    
    def enqueue(self, item):
        if self.size >= self.maxsize:
            print("stack overflow")
        else:
            self.list[self.front] = item
            self.front += 1
            self.size += 1
        
    def dequeue(self):
        if self.size <= 0:
            print("stack empty")
        else:
            item = self.list[self.front-1]
            self.list[self.front-1] = "_"
            self.front -= 1
            self.size -= 1
            return item

