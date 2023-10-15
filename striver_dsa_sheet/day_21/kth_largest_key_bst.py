class Solution:
    def kthLargest(self,root, k):
        #your code here
        def find(root,ans):
            if not root: return 
            find(root.left,ans)
            ans += [root.data]
            find(root.right,ans)
        ans = []
        find(root,ans)
        return ans[-k]

# We can do this using level order traversal and sort the list and return the same 
# we have this recursion approach also but it's messy