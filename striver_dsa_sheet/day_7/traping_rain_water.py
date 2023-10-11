class Solution:
    def trap(self, h: List[int]) -> int:
        ans = 0
        le = h[0]
        ri = h[-1]
        i = 0
        j = len(h)-1

        while i <= j:

            if h[i] <= h[j]:
                ans += max(0,le-h[i])            
                le = max(le,h[i])
                i += 1
            else:
                ans += max(0,ri-h[j])          
                ri = max(ri,h[j])
                j -= 1
        return ans

    
# Checking left element as lesser than right, if yes then finding differce between left max and left element
# because there is definitely a max height which is greater than left height as wre are iterating
# constitions will be life either h[i] <= h[j] or le <= ri
