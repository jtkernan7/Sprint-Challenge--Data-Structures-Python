'''

class Node:
    def __init__(self, value=None, next_node=None):
    # the value at this linked list node
        self.value = value
    # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
    # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node
            
    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
                current = current.get_next()
        return False        
'''    


    

'''
    def reverse_list(self):
        stack = []
        curr = self.head
   #     while self.head != None and self.head.get_next != None:
        while curr != None:
            stack.append(curr.get_value())
            curr = curr.get_next()
            
        self.head = Node(stack.pop())
        rev = self.head
        while len(stack) != 0:
            rev.set_next(Node(stack.pop))
            rev = rev.get_next()
                
'''           
                
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    curr = self.head
    stack = []
    while curr:
      stack.append(curr.get_value())
      curr = curr.get_next()
    if len(stack) > 0:
      self.head = Node(stack.pop())
      curr = self.head
      #while len(stack) > 0:
      while stack:    
        curr.set_next(Node(stack.pop()))
        curr = curr.get_next()
'''
  def reverse_list(self):
        stack = []
        curr = self.head
   #     while self.head != None and self.head.get_next != None:
        while curr != None:
            stack.append(curr.get_value())
            curr = curr.get_next()
            
        self.head = Node(stack.pop())
        rev = self.head
        while len(stack) != 0:
            rev.set_next(Node(stack.pop))
            rev = rev.get_next()
            
            
'''
