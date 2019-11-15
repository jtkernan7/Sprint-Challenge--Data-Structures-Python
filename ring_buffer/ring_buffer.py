class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):

    if self.capacity == self.current:
        self.current = 1
    else:
        self.current += 1
    self.storage[current - 1] = item
        

  def get(self):
    if self.capacity = 0:
        print('[]')
    else:
        while x > self.capacity:
         print(self.storage[x])