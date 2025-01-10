class PQueue():
    def __init__(self, list, maxsize=10):
        self.list = list
        self.maxsize = maxsize

    def enqueue(self, item):
        if len(self.list) >= self.maxsize:
            print("no more space")
        else:
            index = 0
            while index < len(self.list): 
                if item["priority"] >= self.list[index]["priority"]:
                    break
                index += 1
            self.list.insert(index, item)
    
    def dequeue(self):
        if len(self.list) <= 0:
            print("queue empty")
        else:
            return self.list.pop()

