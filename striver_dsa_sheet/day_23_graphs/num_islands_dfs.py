class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        r,c = len(grid), len(grid[0])
        cnt = 0
        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != "1":
                return 
            grid[i][j] = "2"
            for x,y in ((0,1),(1,0),(0,-1),(-1,0)):
                dfs(x+i, y+j)
            return 
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i,j)

        return cnt
    
# You can use the Vis[r][c] if initial array is not disturbed