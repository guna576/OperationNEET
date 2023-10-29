class Solution:
    def floodFill(self, l: List[List[int]], sr: int, sc: int, k: int) -> List[List[int]]:
        r = len(l)
        c = len(l[0])
        vis = set()
        def dfs(i,j,src_c,tar_c):
            if i < 0 or i >= r or j < 0 or j >=c or (i,j) in vis or l[i][j] != src_c: return 
            vis.add((i,j))
            l[i][j] = tar_c
            for x,y in ((1,0),(0,1),(-1,0),(0,-1)):
                dfs(x+i, y+j, src_c, tar_c)
        dfs(sr,sc,l[sr][sc],k)
        return l

        