from stack import Stack

s = Stack()

s.enqueue('a')
s.enqueue('b')
s.enqueue('c')
print(s.dequeue())
s.enqueue('d')
print(s.dequeue())
print(s.list)



