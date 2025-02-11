from linked_list import LinkedList

ll = LinkedList()
# ll.create_root(12)
# ll.insert(30, 1)
# ll.insert(6, 2)
# ll.insert(45, 1)
# ll.insert(50, 4)
# ll.insert(3, 0)

# 3, 12, 45, 30, 6, 50
# ll.print()

# 6
# print(len(ll))

# 50
# print(ll.get_tail().data)


# print(ll.remove(0)) # 3
# ll.print()
# print(ll.remove(2)) # 30
# ll.print()
# print(ll.pop()) # 12
# ll.print()
# print(len(ll))



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

q = Queue(ll)
    
q.enqueue("a")
q.enqueue("b")
q.enqueue("f")
q.enqueue("g")
q.enqueue("z")
q.list.print()
print(q.dequeue())
q.list.print()




