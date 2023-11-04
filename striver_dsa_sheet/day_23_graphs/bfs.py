class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        que = [0]
        vis = [0]*V
        bfs = []
        vis[0] = 1
        while que:
            node = que.pop(0)
            bfs += [node]
            for x in adj[node]:
                if vis[x]==0:
                    vis[x] = 1 # You are marking these to vis right before pushing to que to make sure u dont push it again on evaluting the first pushed neighbors
                    que += [x]
        return bfs
    
# SC: O(V)
# Tc: O(N) + O(2E) (edges for undirected)