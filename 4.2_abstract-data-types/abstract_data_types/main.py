class Array():
    def __init__(self, items):
        if len(set([type(item) for item in items])) > 1:
            raise TypeError
        self.__items = items

    def __str__(self):
        return str(self.__items)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, arg):
        return self.__items[arg]

    def __setitem__(self, arg, value):
        self.__items[arg] = value


class Queue():
    def __init__(self, size):
        self.items = Array([None]*size)
        self.front = None
        self.rear = 0


        

    def enqueue(self, value):
        if self.rear < len(self.items):
            self.items[self.rear] = value
            self.rear += 1
        else:
            print("no space")

    def dequeue(self):
        if self.front != self.rear:
            item = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            return item
        else:
            print("empty")

class CircularQueue(Queue):
    def enqueue(self, value):
        if self.rear == self.front:
            print("no space")
        else:
            if self.front is None:
                self.front = 0
            self.items[self.rear] = value
            self.rear = (self.rear + 1) % len(self.items)

    def dequeue(self):
        if self.front != self.rear:
            item = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % len(self.items)
            return item
        else:
            print("empty")

class PriorityQueue(Queue):
    def enqueue(self, item):
        if self.rear == self.front:
            print("no space")
        else:
            if self.front is None:
                self.front = 0
            i = self.front
            insertion_point = 0
            print(i, self.rear)
            while i < self.rear:
                qitem = self.items[i]
                if item["priority"] > qitem["priority"]:
                    insertion_point = i
                    break
                i = (i + 1) % len(self.items)
            j = insertion_point
            while j < self.rear:
                temp = self.items[j+1]
                print(j, self.items)
                self.items[j+1] = self.items[j]
                j = (j + 1) % len(self.items)
            self.items[j] = item
                    
            self.rear = (self.rear + 1) % len(self.items)

    def dequeue(self):
        if self.front != self.rear:
            item = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % len(self.items)
            return item
        else:
            print("empty")

class Stack():
    def __init__(self, size=10):
        self.items = Array([None]*size)
        self.top = 0
    
    def push(self, item):
        if self.top >= len(self.items):
            print("stack overflow")
        else:
            self.items[self.top] = item
            self.top += 1
        
    def pop(self):
        if self.top == 0:
            print("stack empty")
        else:
            item = self.items[self.top-1]
            self.items[self.top-1] = None
            self.top -= 1
            return item

    def peek(self):
        if self.top == 0:
            return "stack empty"
        return self.items[self.top-1]
        
        
# q = Queue(10)
# q.enqueue("Charlotte")
# q.enqueue("Joseph")
# q.enqueue("Ensar")
# q.enqueue("Marcel")
# print(q.items)
# print(q.front, q.rear)

# s = Stack()
# s.push("Charlotte")
# s.push("Marcel")
# s.push("Joseph")
# s.push("Ensar")
# print(s.items)
# print(s.peek())
# print(s.pop())
# print(s.items)

# cq = CircularQueue(5)
# cq.enqueue("Charlotte")
# cq.enqueue("Joseph")
# cq.enqueue("Ensar")
# cq.enqueue("Marcel")
# print(cq.items)
# print(cq.dequeue())
# print(cq.front, cq.rear)
# cq.encqueue("Edwin")
# print(cq.items)
# print(cq.front, cq.rear)
# cq.encqueue("Alaa")
# print(cq.items)
# print(cq.front, cq.rear)

pq = PriorityQueue(5)
pq.enqueue({ "value": "Charlotte", "priority": 1 })
pq.enqueue({ "value": "Ensar", "priority": 1 })
pq.enqueue({ "value": "Joseph", "priority": 2 })
# pq.enqueue({ "value": "Marcel", "priority": 1 })
print(pq.items)



The transmitting device checks for traffic (senses the carrier). If a signal is present, then transmitter waits a random time period before checking for traffic again. If no signal is present, the transmitter will send a request to send (RTS) signal. The wireless access point (WAP) responds with a clear to send (CTS) signal if it has not already received an RTS signal from a different device. If a CTS is not received, the transmitter waits a random period of time before restarting transmission process. When a CTS signal is received, the transmitter begins transmitting data. The receiver sends an acknowledgement (ACK) sign. If no ACK signal is received, then data is re-sent.
