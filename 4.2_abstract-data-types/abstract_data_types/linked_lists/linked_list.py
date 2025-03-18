from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
    
    # This function is called automatically when len() is used with
    # an instance of LinkedList as an argument
    def __len__(self):
        length = 0
        current_node = self.head
        if current_node:
            length += 1
            while current_node.next != None:
                current_node = current_node.next
                length += 1
        return length
    
    def create_root(self, value):
        node = Node(value)
        self.head = node

    def insert(self, value, index):
      	# if the the list is empty, create the head node
        if self.head == None:
            self.create_root(value)
        # otherwise find out where in the list we need to insert
        else:
          	# track the list traversal with a counter
            position = 0
            # start at the head
            current_node = self.head
            # continue until we reach the target insertion point
            while position < index:
                previous_node = current_node
                current_node = current_node.next
                position += 1
            # if the insertion is at the end
            # append the value
            if current_node == None:
                self.append(value)
            # if the insertion is at the beginning
            # set new head and link to previous head
            elif index == 0:
                current_node = self.head
                self.head = Node(value)
                self.head.next = current_node
            # otherwise link new node to previous and next nodes.
            else:
                node = Node(value)
                node.next = current_node
                previous_node.next = node
    
    def remove(self, index):
        current_node = self.head
        previous_node = current_node
        
        if index == -1:
          while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
          
        position = 0
        while position < index:
            previous_node = current_node
            current_node = current_node.next
            position += 1

        if index == 0:
            self.head = current_node.next
        elif current_node.next == None:
            previous_node.next = None
        else:
            previous_node.next = current_node.next
        return current_node.data
    
    def append(self, value):
      	# if list empty, create head node
        if self.head == None:
            self.create_root(value)
        # otherwise get tail of list, set tail to link to new tail
        else:
            tail = self.get_tail()
            tail.next = Node(value)
    
    def get_tail(self):
      	# find last node in list: when node has no next node
        # start with head
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        return current_node
    
    def index_of(node):
      current_node = self.head
      index = 0
      while current_node != node:
        if current_node is None:
        	return "not in list"
        current_node = current_node.next
        index += 1
      return index
    
    # this method simply forwards to the remove method
    # supports no arguments - by default removes at the end.
    def pop(self, index=-1):
        return self.remove(index)

    def print(self):
        node = self.head
        while True:
          	if node == None:
                print("list empty")
                break
            elif node.next == None:
                print(node.data, "(-> None)")
                break
            else:
                print(node.data, "(->", str(node.next.data) + ")")
                node = node.next