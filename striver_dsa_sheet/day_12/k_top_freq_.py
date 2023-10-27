from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = [] # O(n)
        d = Counter(nums) # O(n)

        for i,j in d.items():
            heappush(hp, (-1*j,i)) # O(nlogn)

        ans = []
        for _ in range(k):
            ans+= [heappop(hp)[1]] # O(nlogn)
        return ans

