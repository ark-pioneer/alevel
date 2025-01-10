class Queue():
    def __init__(self, list, maxsize=10):
        self.list = list
        self.maxsize = maxsize

    def enqueue(self, value):
        if len(self.list) >= self.maxsize:
            print("no more space")
        else:
            self.list.append(value)
    
    def dequeue(self):
        if len(self.list) <= 0:
            print("queue empty")
        else:
            return self.list.pop(0)