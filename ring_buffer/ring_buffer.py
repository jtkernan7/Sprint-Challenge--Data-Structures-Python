class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = 0
        self.storage = [None]*capacity
        
    def get(self):
        return [x for x in self.storage if x != None]
    
        
    def append(self, item):
        if self.capacity > self.current:
            self.storage[self.current] = item
            self.current += 1
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1
    
#     def append(self, item):
#         if self.capacity + 1 == self.current:
#             self.current = 0
#         self.storage[self.current] = item
#         self.current += 1

        
    def append(self, item):
        if self.capacity > self.current:
            self.storage[self.current] = item
            self.current += 1
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1
            
            