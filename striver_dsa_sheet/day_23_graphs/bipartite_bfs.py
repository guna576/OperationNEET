class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        # g = defaultdict(list)
        # for i,j in graph:
        #     g[i] += [j]

        def bi(i,n,col,g):
            q = [i]
            col[i] = -1
            while q:
                nd = q.pop(0)
                adj_col = col[nd] 
                for edg in g[nd]:
                    if col[edg] == 0:
                        col[edg] = adj_col*-1
                        q += [edg]
                    elif col[edg] == adj_col:
                        return False
                    
            return True

        n = len(g)
        col = [0] * n 
        for i in range(n):
            if col[i]==0:
                if not bi(i,n,col,g): return False

        return True
    
# https://leetcode.com/problems/is-graph-bipartite/submissions/
# We are finding the odd length cycle and it's persent we can't split garaph into 2 parts.
# we say if adjacent colors for nodes are differnt, then we can split graph into two groups and 
# definitely there is edge between every node of 2 groups 