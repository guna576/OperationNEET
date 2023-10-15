'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here
        curr = root
        while curr:
            
            if curr.key > key:
                curr = curr.left
                pre = curr
            elif curr.key < key:
                curr = curr.right
                suc = curr

# You can also do inorder and find the index or key
# You can do inorder using recursiona and first eleent greateer than ky will be success

# present aproach is simple iteration with O(H) and O(1) space