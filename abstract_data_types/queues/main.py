import sys

sys.path.append('../linked_lists')
from linked_lists.linked_list import LinkedList
from queue import Queue

# from priority_queue import PQueue
# from circular_queue import CQueue
# from queue_static import StaticQueue

# q = CQueue() # back [] front
# q.enqueue({"name": "Kalina", "priority": 5}) # back ["Kalina"] front
# q.enqueue({"name": "Emmanuella", "priority": 1}) # back [] front
# q.enqueue({"name": "Henry", "priority": 10}) # back [] front
# print(q.list) # back [] front
# pupil = q.dequeue() # 
# print(q.list) # back [] front
# print(pupil) # 
# q.enqueue({"name": "Dylan", "priority": 1}) # back [] front
# q.enqueue({"name": "Lydia", "priority": 5}) # back [] front
# q.enqueue({"name": "Max", "priority": 10}) # back [] front
# q.enqueue({"name": "Ariana", "priority": 1}) # back [] front
# q.enqueue({"name": "Val", "priority": 1}) # back [] front
# q.enqueue({"name": "Georgia", "priority": 5}) # back [] front
# q.enqueue({"name": "Alex", "priority": 10}) # back [] front
# q.enqueue({"name": "Kat", "priority": 1}) # back [] front


# print(q.list) # back [] front

# pupil = q.dequeue() # 
# print(q.list) # back [] front
# print(pupil) # 
ll = LinkedList()
q = Queue(ll)

q.enqueue("a")
q.enqueue("b")
q.enqueue("f")
q.enqueue("g")
q.enqueue("z")
print(q.list)
print(q.dequeue())
print(q.list)

