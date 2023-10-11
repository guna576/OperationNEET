# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # if not more childs return 0 
        l = 1 + self.maxDepth(root.left)  # 1 is for calculating the current root level
        r = 1 + self.maxDepth(root.right)
        return max(l,r)
    

# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/