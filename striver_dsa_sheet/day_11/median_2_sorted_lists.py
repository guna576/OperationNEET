class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2 = len(nums1), len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2,nums1)
        
        i = 0
        j = n1 # dont know why we took n1 insead of n1-1

        while i <= j:
            cnt1 = (i+j) >> 1
            cnt2 = ((n1+n2+1)//2) - cnt1   ##Cant understand why we computer that big equation

            l1 = float('-inf') if cnt1 == 0 else nums1[cnt1-1]  # dont know why -1 in indexing 
            l2 = float('-inf') if cnt2 == 0 else nums2[cnt2-1]

            r1 = float('inf') if cnt1 == n1 else nums1[cnt1-1]
            r2 = float('inf') if cnt2 == n2 else nums2[cnt2-1]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1 > r2:
                j = cnt1 - 1
            else:
                i = cnt1 + 1
        return 0.0



# Not sure why not working
# TC: O(log(min(n1,n2)) and SC: O(1)