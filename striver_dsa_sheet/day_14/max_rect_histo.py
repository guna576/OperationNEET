class Solution:
    def largestRectangleArea(self, l: List[int]) -> int:
        n = len(l)
        ll = [0]*n
        rr = [n-1]*n
        st1 = []
        st2 = []

        for i in range(n):
            while st1 and l[st1[-1]] >= l[i]:
                st1.pop()
            if st1:
                ll[i] = st1[-1] + 1
            st1 += [i]

        for i in range(n-1,-1,-1):
            while st2 and l[st2[-1]] >= l[i]:
                st2.pop()
            if st2:
                rr[i] = st2[-1] - 1
            st2 += [i]

        ans = 0
        for i in range(n):
            ans = max(ans, l[i]*(rr[i]-ll[i]+1))

        return ans
# O(N)+O(N) for first stack and O(N) + O(N) for second stack
# O(N)+O(N) space

# for every element you are finding right smaller element and left smaller element
# then you are computing the smaller sum after left smaller and before right smaller with current peak
# Use your trapping rain water knowledge with stack findinf left and right sum

## One ore Chuthiya SOluiton using only sinhle pass like suing stack order itself
# Unrealistic

class Solution:
    def largestRectangleArea(self, l: List[int]) -> int:
        n = len(l)
        s = []
        ans = 0

        for i in range(n+1):
            while s and i == n or l[s[-1]] >= l[i]:
                ele = l[s[-1]]
                s.pop()
                wid = 0
                if not s:
                    wid = i
                else:
                    wid = i - s[-1] + 1
                ans = max(ans,l[i]*wid)
            s += [i]
        return ans
                
        
       