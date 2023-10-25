class Solution:
    def singleNonDuplicate(self, l: List[int]) -> int:
        n = len(l) - 1
        if n < 1: return l[0]
        if l[0] != l[1]: return l[0]
        if l[n] != l[n-1]: return l[n]

        i = 1
        j = n-1

        while i <= j:
            m = (i+j) >> 1

            if l[m] != l[m-1] and l[m] != l[m+1]: return l[m]
            elif m&1 and l[m] == l[m-1] or m%2==0 and l[m] == l[m+1]: i = m + 1 ## Use a testcase to understand it
            else: j = m-1 
        return l[m] 


# O(logN) and O(1)
# if mid if odd then even number of element till there and vice versa
# https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/