# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def fun(root,k):
            if not root: return None 
            left = fun(root.left, k)
            if left: return left # can't undertand why this line
            k -= 1
            if k == 0: return root
            return fun(root.right,k)

        return fun(root,k).val
        # def find(root,ans):
        #     if not root: return 
        #     find(root.left,ans)
        #     ans += [root.val]
        #     find(root.right,ans)
        # ans = []
        # find(root,ans)
        # return ans[k-1]


### So Messy but idea is good