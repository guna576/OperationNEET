
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cnt = 0
        tot = 0
        que = []
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    tot += 1
                if grid[i][j] == 2:
                    que += [(i,j)]
        
        ans = 0

        while que:
            n = len(que)
            cnt += n
            for _ in range(n):
                i,j = que.pop(0)
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx = i+x
                    ny = j+y
                    if nx > -1 and nx < r and ny > -1 and ny < c and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        que += [(nx,ny)]

            if len(que): ans += 1  # remember this 

        return ans if cnt==tot else -1

# O(N*N) x 4 and O(N*N)    

# we can use visited set and perform the same: Graph kind of BFS approach

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis = set()
        que = []
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    vis.add((i,j))
                elif grid[i][j] == 2:
                    que += [(i,j)]
        
        ans = 0

        while vis and que:
            for _ in range(len(que)):
                i,j = que.pop(0)
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if (i+x,y+j) in vis:
                        que += [(i+x,j+y)]
                        vis.remove((i+x,y+j))
            ans += 1  ## Here Vis will take care even though Que is non empty

        return ans if len(vis) == 0 else -1