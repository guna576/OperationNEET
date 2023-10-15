

class Stack:
  def __init__(self, cap = 100):
    self.cap = cap
    self.stack = [0] * self.cap
    self.top = -1
    
  def push(self, val):
    self.top += 1
    self.stack[self.top] = val
    
  def pop(self):
    if self.top > -1:
      popEle = self.stack[self.top]
      self.top -= 1
      return popEle
    else:
      return "The Stack is empty!!!"
      
  def topPointer(self):
    return self.stack[self.top]
    
  def isEmpty(self):
    return self.top == -1
    
  def size(self):
    return self.top + 1
    
  def printStack(self):
    return self.stack[:self.top+1]
    
stackObj = Stack(cap = 10)
stackObj.push(1)
stackObj.push(2)
stackObj.push(3)
stackObj.push(4)
stackObj.push(5)

print(stackObj.printStack())
print(stackObj.pop())
print(stackObj.printStack())
print(stackObj.topPointer())
print(stackObj.isEmpty())
print(stackObj.size())
print(stackObj.printStack())

# O(N) and O(N)