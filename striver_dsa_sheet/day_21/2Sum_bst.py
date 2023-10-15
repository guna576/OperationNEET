class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, seen):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)            
            return dfs(node.left, seen) or dfs(node.right, seen)
        
        return dfs(root, set())

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:return False
        visit=set()
        q=[root]
        for i in q:
            if (k-i.val) in visit:return True
            visit.add(i.val)
            if i.left:
                q.append((i.left))
            if i.right:
                q.append(i.right)
        return False
    
## Practice with BST iter question structrue