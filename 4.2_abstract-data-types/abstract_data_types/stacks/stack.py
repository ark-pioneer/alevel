class Stack():
    def __init__(self, maxsize=10):
        self.list = ['_' for i in range(maxsize)]
        self.top = 0
    
    def push(self, item):
        if self.top >= self.maxsize:
            print("stack overflow")
        else:
            self.list[self.front] = item
            self.front += 1
            self.size += 1
        
    def pop(self):
        if self.size <= 0:
            print("stack empty")
        else:
            item = self.list[self.front-1]
            self.list[self.front-1] = "_"
            self.front -= 1
            self.size -= 1
            return item

