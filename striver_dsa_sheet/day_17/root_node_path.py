class Node:
  def __init__(self, val = 0,left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
def get(root,node,ans):
  if not root: return False 
  ans += [root.val]
  if node == root.val:
    return True
  if get(root.left,node,ans) or get(root.right,node,ans):
    return True 
  ans.pop()
  return False
  
  
def find(root,node):
  ans = []
  if get(root,node,ans):
    return ans
  else:
    return "Node is not present"

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)

print("The path is : ",find(root,6))

# TC and SC: O(N) and O(N)