
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right


def inOrder(root):
    if not root: return 
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)

def preOrder(root):
    if not root: return 
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if not root: return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")

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

print("Inorder of a Tree is :"),inOrder(root)
print("\nPreOrder of a Tree is:"),preOrder(root)
print("\nPostOrder of a Tree is:"),postOrder(root)
