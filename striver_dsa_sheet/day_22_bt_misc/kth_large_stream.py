class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        n = len(nums)
        heapify(nums)
        for _ in range(n-k):
            heappop(nums)
        self.l = nums

    def add(self, val: int) -> int:
        if len(self.l) < self.k:
            heappush(self.l,val)
        elif val > self.l[0]:
            heapreplace(self.l,val)
        return self.l[0]

