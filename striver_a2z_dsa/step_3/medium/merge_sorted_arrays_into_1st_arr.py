# come from back ra using 2 pointers
# Filling first zeros happens instead of having from start and mess up things
class Solution:
    def merge(nums1,m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n - 1
        k = m+n-1

        while k > -1 and i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        while i > -1:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1

        
print(f"The combined sorted array in place 1st is {Solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)}")

# TC : O(m+n) and sc:O(1)