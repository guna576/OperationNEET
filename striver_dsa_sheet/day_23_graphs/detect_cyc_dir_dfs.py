class Solution:
    def canFinish(self, n: int, l: List[List[int]]) -> bool:
        def dfs(i, vis, par, g):
            vis[i] = 1
            par[i] = 1
            for e in g[i]:
                if vis[e]==0:
                    if dfs(e, vis, par, g): return True
                elif par[e]:
                    return True

            par[i] = 0
            return False

        par = [0]*n
        vis = [0]*n

        g = defaultdict(list)
        for i,j in l:
            g[i] += [j]

        for i in range(n):
            if vis[i]==0:
                if dfs(i, vis, par, g): return False
        return True
    
# https://leetcode.com/problems/course-schedule/description/
