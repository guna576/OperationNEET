class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        que = []

        for i in range(len(nums)):
            if que and i - que[0] >= k: que.pop(0)
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que += [i]
            if i+1 >= k: ans += [nums[que[0]]]
        return ans
    
# You are finding max element right within the window sizen using Queue becoz of sliding window
# https://leetcode.com/problems/sliding-window-maximum/description/

# O(N) + O(N) acual impl + Stack iteration and O(k) for stack storage