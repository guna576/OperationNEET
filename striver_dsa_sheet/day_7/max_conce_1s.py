class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                i += 1 
            elif nums[x] == 0:
                ans = max(ans,i)
                i = 0
        return max(i,ans)
        