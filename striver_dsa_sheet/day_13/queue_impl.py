##### We are implementing Queue with a single array wth start and end pointers



class Queue:
  def __init__(self, cap = 16):
    self.cap = cap
    self.start = -1
    self.end = -1
    self.queueSize = 0
    self.queue = [0] * self.cap 
    
  def push(self, val):
    if self.end == self.cap:
      return "The Queue is out of space"
    if self.end == -1:
      self.end = 0
      self.start = 0
    else:
      self.end = (self.end + 1) % self.cap 
    self.queue[self.end] = val
    print(f"The element pushed is {val}")
    self.queueSize += 1 
    
  def pop(self):
    if self.start == -1:
      return "The Queue is Empty"
    ele = self.queue[self.start]
    if self.queueSize == 1:
      self.start = -1 
      self.end = -1
    else:
      self.start = (self.start + 1) % self.cap 
    
    self.queueSize -= 1 
    return ele
    
    
  def topPointer(self):
    if self.start == -1:
      return "The Queue is empty"
    return self.queue[self.start]
    
  def size(self):
    return self.queueSize
    
    
obj = Queue()
obj.push(10)
obj.push(20)
print(f"The poped element is {obj.pop()}")
obj.push(30)
print(f"The top elemet is {obj.topPointer()}")
print(f"The size of our queue is {obj.size()}")
    
    
    
    
## Tricky, remember the consitions in pushing and popping doctor