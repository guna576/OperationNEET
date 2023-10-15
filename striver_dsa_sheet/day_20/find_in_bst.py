class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root: return None
        # elif root.val < val: return self.searchBST(root.right,val)
        # elif root.val > val: return self.searchBST(root.left,val)
        # else: return root

        curr = root
        while curr:
            if curr.val == val: return curr
            elif curr.val < val: curr = curr.right
            else: curr = curr.left

        return None