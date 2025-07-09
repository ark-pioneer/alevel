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
        self.front = 0
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
        
        
Array([1,2,"h",4])



# lists v Arrays

# Properties
# 1. Static or Dynamic
# Static - fixed size at runtime, size cannot be changed
# Dynamic - size can vary at runtime.

# arrays are static, lists are dynamic.

# 2. type of access.
# Direct access - O(1) - as long as you have the index, you can 'go' straight to the value you want.
# Sequential access - O(n) - you must traverse the sequence of items until you find the target
# Arrays are Direct Access, lists usually are sequential

# 3. Memory location type
# Contiguous - a fixed set of sequential memory blocks that are reserved for the Array.
# Non-contiguous - the memory blocks are not sequential - they can be anywhere.
# Arrays have contiguous memory locations, lists usually don't

# 4. data types
# Arrays must hold a unique data type - can be declared eg: as an array of strings or an array of ints
# lists can hold different data types












