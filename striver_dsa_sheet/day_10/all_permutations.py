class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(ans, nums, l, r):
            if l == r:
                ans += [nums.copy()]
            else:
                for k in range(l,r):
                    nums[l],nums[k] = nums[k], nums[l]
                    rec(ans, nums, l+1, r)
                    nums[l], nums[k] = nums[k], nums[l]
        
        
        rec(ans, nums, 0, len(nums))
        return ans

    # O(N! X N) and O(1)