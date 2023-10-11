class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        while i < n and j < n:
            if nums[i] != nums[j]:
                nums[i+1],nums[j] = nums[j], nums[i+1]
                i += 1
            j += 1
    
        return i+1
    
#  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/