

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right



def LeftView(root):
    if not root: return []
    ans = []
    que = [root]
    while que:
        n = len(que)
        flag = 1
        for _ in range(n):
            node = que.pop(0)
            if node.left: que += [node.left]
            if node.right: que += [node.right]
            if flag:
                ans += [node.data]
                flag = 0
    return ans

def rightView(root):
    if not root: return []
    ans = []
    que = [root]
    while que:
        n = len(que)  
        for x in range(n):
            node = que.pop(0)
            if node.left: que += [node.left]
            if node.right: que += [node.right]
            if x == n-1:
                ans += [node.data]
    return ans

def topView(root):
  if not root: return []
  q = [(root,0)]
  d = {0:root.data}
  while q:
    n= len(q)
    for _ in range(n):
      node,l = q.pop(0)
      if l not in d:
        d[l] = node.data
      if node.left:
        q += [(node.left,l-1)]
      if node.right:
        q += [(node.right,l+1)]
      
  return d

def bottomView(root):
    if not root: return []
    q = [(root,0)]
    d = {0:root.data}
    while q:
      n= len(q)
      for _ in range(n):
        node,l = q.pop(0)
        d[l] = node.data
        if node.left:
          q += [(node.left,l-1)]
        if node.right:
          q += [(node.right,l+1)]
        
    return d

#      1
#     /\
#    2  3
#   / \ / \
#  4  5 6  7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("The left view: ",LeftView(root))
print("The right view: ",rightView(root))
print("The top view: ",topView(root))
print("The bottom view: ",bottomView(root))

