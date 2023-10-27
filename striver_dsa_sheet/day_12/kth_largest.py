class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        l =[]
        for x in nums:
            heapq.heappush(l,-x)
        for i in range(len(nums)):
            val = heapq.heappop(l)
            if i == k-1: return -val

# TC: O((n-k)logn + k)
# O(n) but striver says it's O(k) have to check