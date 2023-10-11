class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def fun(root):
            nonlocal d # Understand how this can be used and try without this
            if not root: return 0
            l = fun(root.left)
            r = fun(root.right)
            d = max(d,l+r)
            return 1 + max(l,r)
        d = 0
        fun(root)
        return d
    
# https://leetcode.com/problems/diameter-of-binary-tree/description/
