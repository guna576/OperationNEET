class Solution:
    # https://practice.geeksforgeeks.org/problems/topological-sort/1
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        def dfs(i, V, adj, st):
            vis[i] = 1
            for edg in adj[i]:
                if 0==vis[i]:
                    dfs(edg,V,adj,st)
            st += [i]
            
        vis = [0]*V
        st = []
        
        for i in range(V):
            if vis[i]==0: dfs(i, V, adj, st)

        return st[::-1]
    
# Dont knoe why it's not working 