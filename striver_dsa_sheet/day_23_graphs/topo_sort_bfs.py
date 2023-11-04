class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        ind = [0]*V
        
        for i in range(V):
            for j in adj[i]:
                ind[j]+=1 
                
        q = []
        for i in range(V):
            if ind[i] == 0:
                q += [i]
                
        topo = []
        while q:
            nd = q.pop(0)
            topo += [nd]
            
            for edg in adj[nd]:
                ind[edg] -= 1
                if ind[edg] == 0:
                    q += [edg]
        return topo
    
# O(N+E) and O(N)+O(N)