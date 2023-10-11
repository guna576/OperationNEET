class Node:
  def __init__(self, val = 0,left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
def isLeaf(root):
  return root.left == None and root.right == None 


  
def findLeaf(root,ans):
  if not root: return 
  if isLeaf(root):
    ans += [root.val]
  findLeaf(root.left,ans)
  findLeaf(root.right,ans)

def leftNodes(root,ans):
  while not isLeaf(root):
    ans += [root.val]
    if not root.left and root.right:
      root = root.right 
    else:
      root = root.left
  return ans

def rightNodes(root,ans):
  while not isLeaf(root):
    ans += [root.val]
    if not root.right and root.left:
      root = root.left 
    else:
      root = root.right

  return ans[::-1]
  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)

leaf_nodes = []
left_nodes = []
right_nodes = []
findLeaf(root,leaf_nodes)
leftNodes(root,left_nodes)
rightNodes(root,right_nodes)
print(left_nodes,leaf_nodes,right_nodes[:0:-1])

# Big inside functions, take care of it

# traversal should happen in anti clock wise
