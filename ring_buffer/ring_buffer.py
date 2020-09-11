class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.head = 0

    def append(self, item):
        # if storage is full 
        if self.size == self.capacity:
            # replaces whatever is in storage at the index of, self.head
            self.storage[self.head] = item
            # updates head to be oldest item in storage; when this leaves no remainders start back at 0
            self.head = (self.head + 1) % self.capacity
        # if storage is not full
        else:
            self.enqueue(item)

    def get(self):
        # if size is empty nothing to return
        if self.size == 0:
            return None
        # Otherwise return storage
        else:
            print(self.storage)
            return self.storage
    
    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
        
    def dequeue(self):
        # if not empty
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0) # removes the 1st index
        return None


# buffer = RingBuffer(5)
# buffer.append('a') # 1
# buffer.append('b') # 2
# buffer.append('c') # 3
# buffer.append('d') # 4
# buffer.append('e') # 5 
# buffer.append('f') # 6
# buffer.append('g') # 7
# buffer.append('h') # 8
# buffer.append('j') # 9
# buffer.append('k') # 10
# buffer.append('l') # 11
# buffer.get()