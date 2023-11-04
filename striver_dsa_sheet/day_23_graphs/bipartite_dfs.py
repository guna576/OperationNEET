class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        # g = defaultdict(list)
        # for i,j in graph:
        #     g[i] += [j]

        def bi(i,n,col,g,tc):
            col[i] = tc

            for edg in g[i]:
                if col[edg] == 0:
                    if not bi(edg,n,col,g,col[i]*-1): return False
                elif col[edg] == col[i]:
                    return False
                    
            return True

        n = len(g)
        col = [0] * n 
        for i in range(n):
            if col[i]==0:
                if not bi(i,n,col,g,-1): return False

        return True
    
# https://leetcode.com/problems/is-graph-bipartite/submissions/
# O(n+e) and O(n)