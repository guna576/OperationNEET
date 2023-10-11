class Solution:
    def threeSum(self, l: List[int]) -> List[List[int]]:
        l.sort()
        n = len(l)
        ans = []
        for i in range(n):
            if i > 0 and l[i] == l[i-1]: continue # you are missing this as well
            x = l[i]
            le = i+1
            ri = n-1
            while le < ri:
                y,z = l[le],l[ri]
                if x+y+z == 0:
                    ans += [[x,y,z]]
                    le += 1 
                    ri -= 1
                    while le < ri and l[le] == l[le-1]: le += 1 # you are doing mistake in these checks
                    while ri > le and l[ri] == l[ri+1]: ri -= 1 

                elif x + y + z < 0:
                    le += 1
                else:
                    ri -= 1
        return [x for x in ans]

# https://leetcode.com/problems/3sum/description/