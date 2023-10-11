# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float('-inf')
        def dfs(root):
            nonlocal mx
            if not root: return 0
            l = max(0,dfs(root.left))
            r = max(0,dfs(root.right))

            sm = root.val + l + r
            mx = max(mx,sm)
            return root.val + max(l,r)

        dfs(root)
        return mx
        

# Just like Diameter