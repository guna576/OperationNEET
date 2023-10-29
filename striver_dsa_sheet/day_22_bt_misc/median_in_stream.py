class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        n1 = len(self.large)
        n2 = len(self.small)
        if n1 or n2:
            med = self.findMedian()
        # print(med)
        if n1 == n2:
            if n1 or n2:
                if num < med:
                    heappush(self.large, -1*num)
                else:
                    heappush(self.small, num)
            else:
                heappush(self.large,-1*num)

        elif n1 > n2:
            if num > med:
                heappush(self.small, num)
            else:
                val = -1*heappop(self.large)
                heappush(self.small, val)
                heappush(self.large, -1*num)
        else:
            if num < med:
                heappush(self.large, -1*num)
            else:
                val = heappop(self.large)
                heappush(self.large, -1*val)
                heappush(self.small, num)

    def findMedian(self) -> float:
        n1 = len(self.large)
        n2 = len(self.small)
        if n1 > n2:
            return self.large[0] * -1
        if n2 > n1:
            return self.small[0]
        else:
            if n1 == 0: return 0
            return (-1*self.large[0]+self.small[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# giving errorrrrrrrrrr

# # O(nlogn) and O(n)