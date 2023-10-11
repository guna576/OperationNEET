# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = collections.defaultdict(list)
        q = [(root,0,0)]

        while q:
            n = len(q)
            for _ in range(n):
                node,lv,r = q.pop(0)
                d[lv] += [(r,node.val)]
                if node.left:
                    q += [(node.left,lv-1,r+1)]
                if node.right:
                    q += [(node.right,lv+1,r+1)]
        ans = []
        for ll in sorted(d.keys()):
            # print(d[ll])
            ans += [[x[1] for x in sorted(d[ll])]]
        return ans

# Row number also matters and print sorted list iff row number is same
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

