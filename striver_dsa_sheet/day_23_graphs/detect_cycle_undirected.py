class Solution:
    def canFinish(self, n: int, adj: List[List[int]]) -> bool:
        def isCycle(i,adj,vis, par):
            vis[i] = 1
            for ngbr in adj[i]:
                if vis[ngbr] == 0:
                    if isCycle(ngbr,adj,vis,i): return True
                elif ngbr != par:
                    return True
            return False

        def makeGraph(adj,n):
            l = [[] for _ in range(n)]
            for i,j in adj:
                l[i] += [j]
            return l
        
        adj = makeGraph(adj,n)
        vis = [0]*n
        for i in range(n):
            
            if vis[i]==0 and adj[i]:
                if isCycle(i, adj, vis, -1): return False
        return True

# O(N+2E) + O(N) where 2*E becoz of indegrees
# O(V) for vertices