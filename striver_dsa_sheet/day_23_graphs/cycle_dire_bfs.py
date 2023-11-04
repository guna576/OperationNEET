class Solution:
    def canFinish(self, n: int, l: List[List[int]]) -> bool:
        g = defaultdict(list)
        ind = [0]*n
        for i,j in l:
            g[i] += [j]
            ind[j] += 1 

        q = []
        for i in range(n):
            if ind[i] == 0:
                q += [i]

        cnt = 0
        while q:
            v = q.pop(0)
            cnt += 1
            for edge in g[v]:
                ind[edge] -= 1
                if ind[edge] == 0:
                    q += [edge]

        return cnt == n # means we can visit and decrese every indegree
    # else we may remain with some nodes who has more incoming than required ie cycle
        
# topological sort mowa