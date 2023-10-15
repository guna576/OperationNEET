"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None 
        leftNode = root.left
        rightNode = root.right

        while leftNode and rightNode:
            leftNode.next = rightNode
            leftNode = leftNode.right
            rightNode = rightNode.left

        self.connect(root.left)
        self.connect(root.right)

        return root

        # if not root: return None
        # q = [root]
        # while q:
        #     n = len(q)
        #     for i in range(n):
        #         nd = q.pop(0)
        #         if i == n-1: nd.next = None
        #         else: nd.next = q[0]
        #         if nd.left: q += [nd.left]
        #         if nd.right: q += [nd.right]
        # return root

# BOth are fine , but you need to improve ra Guna in recursion
# In recursion, remember, you need to make a letter 'A'