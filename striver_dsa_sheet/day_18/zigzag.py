# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = [[root.val]]
        q = [root]

        while q:
            n = len(q)
            for _ in range(n):
                nd = q.pop(0)
                if nd.left: q += [nd.left]
                if nd.right: q += [nd.right]
            if len(q): ans += [[x.val for x in q]]
        for x in range(len(ans)):
            if x&1:
                ans[x] = ans[x][::-1]
        return ans
## alternate levels follows alternate ways to see nodes like left to right and vice versa.

