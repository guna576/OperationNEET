class Solution:
    def kthElement(self,  l1, l2, n, m, k):
        if m > n: return self.kthElement(l2,l1,m,n,k)
        
        low = max(0,k-m)
        high = min(k,n)
        
        while low <= high:
            
            cut1 = (low+high) >> 1
            cut2 = k - cut1
            
            ll1= float('-inf') if cut1==0 else l1[cut1-1]
            ll2= float('-inf') if cut2==0 else l2[cut2-1]
            
            rr1= float('inf') if cut1==n else l1[cut1]
            rr2= float('inf') if cut2==m else l2[cut2]
    
            if ll1 <= rr2 and ll2 <= rr1: return max(ll1,ll2)
            elif ll1 > rr2: high = cut1 - 1
            else: low = cut1 + 1
        return -1
            
# TC: O(log(min(n,m)))

# same as median of sorted arrays 
# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1