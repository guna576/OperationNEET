
# This is the method using DLL and HashMap
class Node:
  def __init__(self,key = 0,val = 0, prev = None, next = None):
    self.key = key 
    self.val = val
    self.prev = prev 
    self.next = next 

class DLinkedinList:
  def __init__(self, cap = 0):
    self.head = None  
    self.cap = cap
    print(self.cap)
  def ini(self):
    start = Node(key=0, val=0)
    tail = Node(key=0, val=0)
    start.next = tail 
    tail.prev = start 
    self.head = start 
    return None 
    
  def addNode(self,node):
    node.next = self.head.next
    node.prev = self.head 
    self.head.next = node 
    node.next.prev = node
    
  def deleteNode(self,node):
    node.prev.next = node.next 
    node.next.prev = node.prev
    
  def get(self,key,d):
    if key in d:
      node = d[key]
      self.deleteNode(node)
      self.addNode(node)
      return d[key].val 
    else:
      return -1
    
  def put(self,key,val,d):
    if key in d:
      node = d[key]
      self.deleteNode(node)
      newNode = Node(key,val)
      self.addNode(newNode)
    else:
      if self.cap == len(d.keys()):
        curr = self.head
        while curr.next:
          curr = curr.next
        self.deleteNode(curr.prev)
        d.pop(curr.key)
        print("Yes",d)
      node = Node(key,val)
      d[key] = node 
      self.addNode(node)
      
    return None

l = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
m = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# [null, null, null, 1, null, -1, null, -1, 3, 4]

ans = []
d = dict()

for x in range(len(l)):
  if l[x] == "LRUCache":
    obj = DLinkedinList(cap=m[x][0])
    ans += [obj.ini()]
  elif l[x] == "put":
    ans += [obj.put(m[x][0],m[x][1],d)]
    
  elif l[x] == "get":
    ans += [obj.get(m[x][0],d)]
  print(d)

print(ans)
    
####### Has a BUG, work on it and also have the start and tail as class pointers 

#### This is using OrderedDict in Python
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v 
        return v
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            
            if self.size > 0:
                self.size -= 1 
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value