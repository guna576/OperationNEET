# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        l = []
        
        def dfs(node, vis, adj, l):
            l += [node]
            vis[node] += 1
            
            for edge in adj[node]:
                if vis[edge] == 0:
                    dfs(edge, vis, adj, l)
            return 
            
        vis = [0]*V
        for node in range(V):
            if not vis[node]:
                dfs(node, vis, adj, l)
        return l
        

# SC: O(N)nodes + O(N)vis + O(N)rec stack
# TC: O(N)ndoes + O(2E)all degress of nodes[2 times becauase it's undrected]