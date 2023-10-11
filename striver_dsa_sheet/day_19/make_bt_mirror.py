class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        
        if not root: return None
        l = self.mirror(root.left)
        r = self.mirror(root.right)
        
        root.left = r
        root.right = l
        return root

# Just swap the links ra falthu Doctor