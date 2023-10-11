# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if not root: return 0
            l = fun(root.left)
            if l == -1: return l
            r = fun(root.right)
            if r == -1: return r
            if abs(l-r) > 1: return -1

            return 1+max(l,r)
        
        return -1 != fun(root)

## https://leetcode.com/problems/balanced-binary-tree/description/