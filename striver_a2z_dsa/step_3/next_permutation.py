class Solution:
    @staticmethod
    def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        i = n - 1
        while i > -1 and nums[i] >= nums[i+1]: i -= 1
        if i==-1: return nums.reverse()
        while i <=n and nums[i] >= nums[n]: n -= 1
        
        nums[i],nums[n] = nums[n],nums[i]
        
        l = i + 1 
        r = len(nums) - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1 
        return nums
    
print(f"The next bigger number than ours is {Solution.nextPermutation([2,4,1,7,5,0])}")